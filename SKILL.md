---
name: job-research-report-generator
description: "Automated job market research report generator. Analyzes job requirements and trends for any position in any city, extracts core competencies from job descriptions, creates interactive research reports with data visualization, and compares job requirements across company types. Requires target job title, city, years of experience, and minimum salary."
---

# Job Research Report Generator

## Overview

This skill automates the entire job market research workflow. Given a job title, city, experience level, and salary range, it:

1. Searches for 20 relevant job postings on Boss 直聘 (or similar job boards)
2. Analyzes job descriptions to extract core competencies and requirements
3. Generates a comprehensive research report with:
   - Interactive data visualizations (salary distribution, company types, skill frequency)
   - Keyword matching analysis (showing which skills appear in which jobs)
   - Company type comparison (large corporations vs. startups)
   - Typical job profiles with detailed responsibilities

The output is a static HTML report that can be viewed, shared, or published.

## Workflow

### Phase 1: Gather User Requirements

Ask the user for the following information (one question at a time):

1. **Target Job Title**: "What job position are you researching?" (e.g., "Product Manager", "AI Product Manager", "Data Analyst")
2. **Target City**: "Which city are you targeting?" (e.g., "Shenzhen", "Beijing", "Shanghai")
3. **Years of Experience**: "How many years of experience are you targeting?" (e.g., "3-5 years", "5-10 years", "1-3 years")
4. **Minimum Salary**: "What is your target minimum salary?" (e.g., "20K", "30K", "50K")

Store these parameters for the next phase.

### Phase 2: Research Job Market

**Data Collection:**
- Search Boss 直聘 (https://www.zhipin.com) for job postings matching the criteria
- Collect at least 20 job postings with:
  - Company name and type (large corporation vs. startup)
  - Job title
  - Salary range
  - Work location
  - Full job description
  - Key responsibilities
  - Required qualifications

**Filtering Strategy:**
- Filter by: job title, city, experience level, salary range
- Prioritize: diverse company types (mix of large corporations and startups)
- Ensure: at least 5 from large corporations, 15 from startups/mid-size companies

### Phase 3: Analyze Job Requirements

**Extract Core Competencies:**
- Scan all 20 job descriptions for recurring skills and requirements
- Identify the top 10 most frequently mentioned competencies
- For each competency, record:
  - Frequency (how many jobs mention it)
  - Description (what it means in context)
  - Which jobs mention it (with specific highlights)

**Categorize by Company Type:**
- For each competency, track:
  - Frequency in large corporations
  - Frequency in startups
  - Percentage difference

**Create Typical Job Profiles:**
- Select 4 representative jobs (2 from large corps, 2 from startups)
- Document their complete requirements and responsibilities

### Phase 4: Generate Interactive Report

**Create Static Web Project:**
- Use the webdev_init_project tool to create a new static web project
- Project name: `{job-title}-research-report` (e.g., `product-manager-research-report`)

**Report Structure:**

1. **Hero Section**
   - Title: "{Job Title} Market Research Report - {City}"
   - Subtitle: "Based on 20 job postings analysis"

2. **Key Metrics Dashboard**
   - Total jobs analyzed: 20
   - Average salary
   - Large corporation percentage
   - Startup percentage

3. **Salary Distribution**
   - Bar chart showing salary ranges
   - Breakdown by count and percentage

4. **Company Type Distribution**
   - Pie chart showing large corps vs. startups
   - Brief description of each category

5. **Core Competencies Section**
   - Display top 10 competencies
   - Show frequency for each
   - Clickable cards with detailed information

6. **Keyword Matching Analysis Page** (/keyword-mapping)
   - Interactive view of each competency
   - Show which jobs mention each skill
   - Highlight specific text from job descriptions

7. **Company Type Comparison Page** (/company-comparison)
   - Side-by-side comparison of competency requirements
   - Large corporations vs. startups
   - Show percentage differences
   - Provide job-seeking advice based on company type

8. **Typical Job Profiles**
   - 4 representative job cards
   - Complete descriptions
   - Key responsibilities
   - Salary and company info

**Design Principles:**
- Modern, professional, data-driven aesthetic
- Blue-cyan color scheme (or user preference)
- Clear typography and hierarchy
- Responsive design (mobile, tablet, desktop)
- Interactive elements (tabs, expandable sections, hover effects)

### Phase 5: Deliver Report

**Output:**
- Generate the complete web project
- Save a checkpoint
- Provide the project URL to the user
- Include summary statistics and key insights

**Optional Enhancements:**
- Export to PDF
- Generate downloadable data (CSV/JSON)
- Create shareable summary

## Implementation Notes

### Data Collection Strategy

When searching Boss 直聘:
- Use the search filters: job title, city, experience level, salary range
- If fewer than 20 results, broaden the salary range slightly
- Prioritize recent postings (within last 30 days)
- Capture complete job descriptions (may need to click into each job)

### Competency Extraction

**Common Competency Categories:**
- Technical skills (programming languages, tools, frameworks)
- Domain knowledge (industry expertise, product knowledge)
- Soft skills (communication, leadership, collaboration)
- Process skills (project management, data analysis, problem-solving)
- Emerging skills (AI/ML, blockchain, cloud computing)

**Extraction Method:**
- Use keyword matching and pattern recognition
- Look for verbs and nouns that indicate skills
- Group similar competencies (e.g., "communication", "cross-team collaboration" → "Communication & Collaboration")
- Rank by frequency

### Report Generation

**Technology Stack:**
- React + Tailwind CSS + shadcn/ui (for consistency)
- Recharts for data visualization
- Static deployment (no backend required)

**Data Structure:**
```json
{
  "jobTitle": "Product Manager",
  "city": "Shenzhen",
  "experience": "3-5 years",
  "minSalary": "20K",
  "totalJobs": 20,
  "averageSalary": "32.2K",
  "largeCorpPercentage": 25,
  "startupPercentage": 75,
  "competencies": [
    {
      "rank": 1,
      "name": "Product Strategy",
      "frequency": 18,
      "description": "Ability to define product vision and roadmap",
      "largeCorpFrequency": 5,
      "startupFrequency": 13,
      "jobs": [...]
    }
  ],
  "jobs": [...]
}
```

## Workflow Decision Tree

**User Request:** "I want to research job market for [position] in [city]"

→ **Gather Requirements** (Phase 1)
  - Ask for job title
  - Ask for city
  - Ask for experience level
  - Ask for salary range

→ **Research & Analyze** (Phases 2-3)
  - Search Boss 直聘
  - Extract competencies
  - Categorize by company type

→ **Generate Report** (Phase 4)
  - Create web project
  - Build interactive pages
  - Add visualizations

→ **Deliver** (Phase 5)
  - Save checkpoint
  - Provide URL
  - Share insights

## Resources

### scripts/
Contains Python scripts for data processing:
- `extract_competencies.py` - Analyzes job descriptions to extract skills
- `analyze_salary_distribution.py` - Processes salary data
- `generate_report_data.json` - Creates structured data for the report

### references/
Documentation for implementation:
- `job_search_strategy.md` - Best practices for searching job boards
- `competency_extraction_guide.md` - How to identify and categorize skills
- `report_structure.md` - Detailed layout and content guidelines

### templates/
Boilerplate for the web project:
- React component templates for report pages
- CSS/Tailwind utilities for consistent styling
- Sample data structures and JSON files

## Tips for Success

1. **Data Quality**: Ensure job descriptions are complete and recent
2. **Competency Accuracy**: Review extracted competencies for relevance
3. **Company Classification**: Verify company types (use company size/funding as indicator)
4. **Report Clarity**: Test all interactive elements before delivering
5. **User Customization**: Allow users to modify colors, add custom sections, or export data

## Example Usage

**User Input:**
- Job Title: "AI Product Manager"
- City: "Shenzhen"
- Experience: "3-5 years"
- Salary: "20K+"

**Output:**
- 20 job postings analyzed
- 10 core competencies identified
- Interactive report with 3 pages
- Average salary: 32.2K
- 25% large corporations, 75% startups
- Key insight: "From 0 to 1" product launch experience is most critical at startups
