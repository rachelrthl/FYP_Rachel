# services/newsapi_service.py - NewsAPI.ai service for article fetching

import requests
import time
from typing import List, Dict, Optional, Tuple
from datetime import datetime

from config import Config
from models import Article
from utils import IntelligenceAPIError, ErrorHandler, get_logger


class NewsAPIService:
    """
    Service for fetching news articles from NewsAPI.ai (EventRegistry)
    
    Handles article retrieval, parsing, and error handling with proper timeouts.
    """
    
    def __init__(self):
        """Initialize NewsAPIService with configuration"""
        self.api_key = Config.NEWSAPI_AI_KEY
        self.base_url = Config.NEWSAPI_AI_BASE_URL
        self.timeout = Config.NEWSAPI_TIMEOUT
        self.logger = get_logger()
    
    def fetch_articles_with_query(self, query_body: Dict) -> Tuple[List[Article], Dict]:
        """
        Fetch articles using the built query body.
        
        Args:
            query_body: The request body to send to NewsAPI
            
        Returns:
            Tuple of (List of Article objects, processing_info dict)
            
        Raises:
            IntelligenceAPIError: For external API errors with proper fallback
        """
        start_time = time.time()
        
        try:
            # Make external API call to NewsAPI
            response = requests.post(
                url=self.base_url,
                json=query_body,
                timeout=self.timeout,
                headers={'Content-Type': 'application/json'}
            )
            
            # Handle HTTP errors using unified error handler
            if response.status_code >= 400:
                http_error = requests.exceptions.HTTPError(response=response)
                raise ErrorHandler.handle_external_api_error(http_error, "NewsAPI")
            
            duration = time.time() - start_time
            
            # Parse JSON response
            try:
                data = response.json()
            except ValueError as e:
                get_logger().log_external_api_call(
                    service="NewsAPI",
                    operation="search_articles",
                    duration=duration,
                    status_code=response.status_code,
                    error="Invalid JSON response"
                )
                raise IntelligenceAPIError.news_api_error(
                    "Invalid JSON response from NewsAPI.ai",
                    "NEWS_API_RESPONSE_ERROR",
                    502,
                    str(e)
                )
            
            # Extract language from request body and parse articles
            language = self._extract_language_from_request_body(query_body)
            articles = self._parse_articles_response(data, language)
            
            # Log successful API call
            get_logger().log_external_api_call(
                service="NewsAPI",
                operation="search_articles",
                duration=duration,
                status_code=response.status_code
            )
            
            processing_info = {
                "external_apis_used": ["newsapi"],
                "fallback_used": False,
                "fallback_reason": None
            }
            
            return articles, processing_info
            
        except requests.exceptions.Timeout as e:
            duration = time.time() - start_time
            get_logger().log_external_api_call(
                service="NewsAPI",
                operation="search_articles",
                duration=duration,
                error=f"Timeout after {self.timeout}s"
            )
            raise IntelligenceAPIError.timeout_error("NewsAPI", self.timeout, "search_articles")
            
        except requests.exceptions.ConnectionError as e:
            duration = time.time() - start_time
            get_logger().log_external_api_call(
                service="NewsAPI",
                operation="search_articles",
                duration=duration,
                error="Connection error"
            )
            raise IntelligenceAPIError.news_api_error(
                "Failed to connect to NewsAPI.ai service",
                "NEWS_API_CONNECTION_ERROR",
                503,
                str(e)
            )
            
        except requests.exceptions.RequestException as e:
            duration = time.time() - start_time
            get_logger().log_external_api_call(
                service="NewsAPI",
                operation="search_articles",
                duration=duration,
                error=f"Request error: {str(e)}"
            )
            raise IntelligenceAPIError.news_api_error(
                f"NewsAPI.ai request failed: {str(e)}",
                "NEWS_API_ERROR",
                503,
                str(e)
            )
            
        except IntelligenceAPIError:
            # Re-raise IntelligenceAPIError as-is
            raise
            
        except Exception as e:
            duration = time.time() - start_time
            get_logger().log_external_api_call(
                service="NewsAPI",
                operation="search_articles",
                duration=duration,
                error=f"Unexpected error: {str(e)}"
            )
            raise ErrorHandler.handle_unexpected_error(e, {
                'operation': 'fetch_articles_with_query',
                'query_body': query_body
            })
    
    def _extract_language_from_request_body(self, request_body: Dict) -> str:
        """Extract language code from request body"""
        try:
            query = request_body.get('query', {})
            query_obj = query.get('$query', {})
            lang = query_obj.get('lang')
            
            if isinstance(lang, str):
                return lang
            elif isinstance(lang, dict) and '$or' in lang:
                lang_list = lang.get('$or', [])
                if isinstance(lang_list, list) and len(lang_list) > 0:
                    return lang_list[0]
            elif isinstance(lang, list) and len(lang) > 0:
                return lang[0]
            
            return 'eng'
        except Exception:
            return 'eng'
    
    def _parse_articles_response(self, data: Dict, language: str) -> List[Article]:
        """Parse EventRegistry response and extract articles"""
        articles = []
        
        if not isinstance(data, dict):
            return articles
        
        articles_data = data.get('articles', {}).get('results', [])
        
        if not isinstance(articles_data, list):
            return articles
        
        for article_data in articles_data:
            try:
                article = self._parse_single_article(article_data, language)
                if article:
                    articles.append(article)
            except Exception:
                continue
        
        return articles
    
    def _parse_single_article(self, article_data: Dict, language: str) -> Optional[Article]:
        """Parse a single article from EventRegistry response"""
        try:
            uri = article_data.get('uri', '')
            title = article_data.get('title', '')
            body = article_data.get('body', '')
            url = article_data.get('url', '')
            
            source_data = article_data.get('source', {})
            source = source_data.get('title', '') if isinstance(source_data, dict) else str(source_data)
            
            date_time_str = article_data.get('dateTime', '')
            publication_date = self._parse_datetime(date_time_str)
            
            image_url = article_data.get('image')
            if not image_url or not isinstance(image_url, str) or not image_url.strip():
                image_url = Config.DEFAULT_IMAGE_PLACEHOLDER
            
            sentiment = article_data.get('sentiment')
            relevance = article_data.get('relevance')
            
            if not all([uri, title, url, source]):
                return None
            
            content_preview = self._create_content_preview(body)
            
            return Article(
                uri=uri,
                title=title,
                content_preview=content_preview,
                source=source,
                publication_date=publication_date,
                url=url,
                image_url=image_url,
                sentiment=sentiment,
                language=language,
                relevance=relevance
            )
        except Exception:
            return None
    
    def _parse_datetime(self, date_time_str: str) -> datetime:
        """Parse datetime string from EventRegistry"""
        try:
            formats = [
                '%Y-%m-%dT%H:%M:%SZ',
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%dT%H:%M:%S',
                '%Y-%m-%d'
            ]
            
            for fmt in formats:
                try:
                    return datetime.strptime(date_time_str, fmt)
                except ValueError:
                    continue
            
            return datetime.fromisoformat(date_time_str.replace('Z', '+00:00'))
        except Exception:
            return datetime.utcnow()
    
    def _create_content_preview(self, body: str) -> str:
        """Create content preview by truncating body text"""
        if not body or not isinstance(body, str):
            return ""
        
        cleaned_body = ' '.join(body.strip().split())
        
        if len(cleaned_body) <= Config.CONTENT_PREVIEW_LENGTH:
            return cleaned_body
        
        truncated = cleaned_body[:Config.CONTENT_PREVIEW_LENGTH].strip()
        
        last_space = truncated.rfind(' ')
        if last_space > Config.CONTENT_PREVIEW_LENGTH * 0.8:
            truncated = truncated[:last_space]
        
        return truncated + "..."
