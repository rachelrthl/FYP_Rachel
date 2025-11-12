// Interactive FYP Report JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Generate Table of Contents
    function generateTOC() {
        const toc = document.getElementById('toc');
        if (!toc) return;
        
        // Only get headings that are NOT inside details elements (appendices)
        const allHeadings = document.querySelectorAll('h1, h2, h3');
        const mainHeadings = Array.from(allHeadings).filter(heading => {
            // Check if heading is inside a details element
            return !heading.closest('details');
        });
        
        if (mainHeadings.length === 0) return;
        
        let tocHTML = '<h4>Contents</h4><ul>';
        
        mainHeadings.forEach((heading, index) => {
            const id = heading.id || `heading-${index}`;
            heading.id = id;
            
            const level = heading.tagName.toLowerCase();
            const text = heading.textContent;
            const indent = level === 'h3' ? 'style="margin-left: 20px;"' : '';
            
            tocHTML += `<li ${indent}><a href="#${id}" class="toc-link">${text}</a></li>`;
        });
        
        tocHTML += '</ul>';
        toc.innerHTML = tocHTML;
        
        // Smooth scrolling for TOC links
        document.querySelectorAll('.toc-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    }
    
    // Highlight active section in TOC
    function highlightActiveTOC() {
        const allHeadings = document.querySelectorAll('h1, h2, h3');
        const mainHeadings = Array.from(allHeadings).filter(heading => {
            return !heading.closest('details');
        });
        const tocLinks = document.querySelectorAll('.toc-link');
        
        window.addEventListener('scroll', function() {
            let current = '';
            
            mainHeadings.forEach(heading => {
                const rect = heading.getBoundingClientRect();
                if (rect.top <= 100) {
                    current = heading.id;
                }
            });
            
            tocLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        });
    }
    
    // Image zoom functionality
    function setupImageZoom() {
        const images = document.querySelectorAll('.zoomable');
        
        images.forEach(img => {
            img.addEventListener('click', function() {
                this.classList.toggle('zoomed');
            });
        });
    }
    
    // Initialize all features
    generateTOC();
    highlightActiveTOC();
    setupImageZoom();
});
