# Example Interactive Elements

Here's how to use the interactive features in your report:

## 1. Glossary Terms with Tooltips
Use this format for technical terms:

<span class="tooltip">DGR<span class="tooltiptext">Demand Generation Representative - outbound sales role focused on creating new pipeline</span></span> manages a portfolio of 1,200 accounts.

The <span class="tooltip">API-first architecture<span class="tooltiptext">System design that prioritizes Application Programming Interface access over web scraping for data retrieval</span></span> achieved 96% success rate.

## 2. Footnotes with Hover
Add footnotes like this:

Sarah's performance depends on <span class="footnote" data-note="Sales-Qualified Meetings are meetings that meet specific criteria for passing to Account Executives, typically involving qualified decision-makers and confirmed budget/timeline">SQMs</span><sup>1</sup> she creates weekly.

## 3. Expandable Appendices
Replace your current appendices with:

<details>
<summary>Appendix A: Semi-Structured Interview Findings</summary>

**Purpose:** To understand how Demand Generation Representatives currently prioritize accounts...

[Your full appendix content here]

</details>

<details>
<summary>Appendix B: Technical Architecture</summary>

**System Architecture Diagram:**
[Your technical content here]

</details>

## 4. Zoomable Images
Add the `zoomable` class to images:

![Dashboard Interface](images/Dashboard-v1.png){: .zoomable}

## 5. Videos
Add videos like this:

<video controls width="800">
  <source src="videos/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 6. Table of Contents
The TOC is automatically generated from your headings and appears as a floating panel on the right side.

---

**Instructions:**
1. Copy these patterns into your main `index.md`
2. Replace glossary terms with tooltip versions
3. Convert appendices to expandable sections
4. Add `{: .zoomable}` to images you want to be clickable
5. The TOC will automatically generate from your existing headings
