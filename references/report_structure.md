# Report Structure Guide

## Overview

This guide describes the structure and content of the interactive research report.

## Report Architecture

The report consists of 3 main pages:

1. **Home Page** (`/`) - Overview and key metrics
2. **Keyword Mapping Page** (`/keyword-mapping`) - Detailed competency analysis
3. **Company Comparison Page** (`/company-comparison`) - Large corp vs. startup comparison

## Page 1: Home Page

### Purpose
Provide an overview of the job market research with key metrics and visualizations.

### Sections

#### 1.1 Hero Section
- **Title**: "{Job Title} Market Research Report - {City}"
- **Subtitle**: "Based on 20 job postings analysis | {Date}"
- **Background**: Professional gradient or image
- **CTA Buttons**: "View Keyword Analysis", "Download Report"

#### 1.2 Key Metrics Dashboard
Display 4 key metrics in cards:

| Metric | Value | Icon |
|--------|-------|------|
| Total Jobs Analyzed | 20 | 📊 |
| Average Salary | 32.2K | 💰 |
| Large Corporation % | 25% | 🏢 |
| Startup % | 75% | ⚡ |

**Design**: Gradient background cards, hover effects, smooth animations

#### 1.3 Salary Distribution Section
- **Title**: "Salary Distribution"
- **Subtitle**: "Market salary ranges and distribution"
- **Visualization**: Bar chart showing salary ranges (20-30K, 30-40K, 40K+)
- **Data**: Count and percentage for each range
- **Table**: Detailed breakdown with progress bars

**Example Data**:
```
20-30K: 8 jobs (40%)
30-40K: 7 jobs (35%)
40K+: 5 jobs (25%)
```

#### 1.4 Company Type Distribution Section
- **Title**: "Company Type Distribution"
- **Subtitle**: "Large corporations vs. startups"
- **Visualization**: Pie chart showing split
- **Cards**: Side-by-side comparison of company types

**Large Corporation Card**:
- Count: 5 jobs
- Characteristics: Formal processes, established brand, structured teams
- Pros: Stability, resources, clear career path
- Cons: Slower decision-making, rigid processes

**Startup Card**:
- Count: 15 jobs
- Characteristics: Fast-paced, innovative, flat hierarchy
- Pros: Growth opportunities, autonomy, impact
- Cons: Uncertainty, resource constraints, high pressure

#### 1.5 Core Competencies Section
- **Title**: "10 Core Competencies"
- **Subtitle**: "Most frequently required skills across all jobs"
- **Layout**: Grid of 10 competency cards

**Each Card Contains**:
- Rank (1-10)
- Competency name
- Frequency (e.g., "14 jobs")
- Brief description
- Icon representing the skill
- Hover effect showing more details

**Example Card**:
```
🚀 From 0 to 1 Launch
Rank: 1
Frequency: 14 jobs (70%)
Description: Ability to independently lead product from concept to launch
```

#### 1.6 Typical Job Profiles Section
- **Title**: "Typical Job Profiles"
- **Subtitle**: "4 representative positions showing role diversity"
- **Layout**: Tabbed interface with 4 jobs

**Each Job Profile**:
- Company name and type badge
- Job title
- Salary range
- Key responsibilities (3-4 bullet points)
- Required qualifications

**Example**:
```
Company: ByteDance (Large Corporation)
Position: AI Product Manager - Creative
Salary: 30-60K

Responsibilities:
- Lead product strategy for AI creative tools
- Collaborate with ML engineers on model evaluation
- Define product roadmap for next quarter

Qualifications:
- 3-5 years PM experience
- Understanding of LLMs
- Strong cross-team communication
```

#### 1.7 Industry Insights Section
- **Title**: "Industry Insights & Trends"
- **Content**: 3 key insights from the data

**Example Insights**:
1. **Growth Opportunity**: 75% of positions are at startups, indicating rapid market expansion
2. **Technical Depth Required**: AI/ML knowledge is essential (mentioned in 85% of jobs)
3. **Salary Competitiveness**: Average salary of 32.2K reflects high demand and competitive market

#### 1.8 Navigation to Other Pages
- Button to "View Keyword Matching Analysis"
- Button to "Compare Company Types"

## Page 2: Keyword Mapping Page

### Purpose
Show detailed analysis of each competency with specific job examples.

### Sections

#### 2.1 Header
- **Title**: "Keyword Matching Analysis"
- **Subtitle**: "How core competencies appear in actual job descriptions"
- **Background**: Subtle pattern or gradient

#### 2.2 Usage Instructions
- Explain how to use the page
- Show that competencies are clickable/expandable
- Highlight that job descriptions are color-coded

#### 2.3 Competency List
For each competency (10 total):

**Collapsed View**:
- Competency name
- Frequency badge (e.g., "14 jobs")
- Brief description
- Expand arrow

**Expanded View**:
- Full description
- List of jobs mentioning this competency
- For each job:
  - Company name
  - Job title
  - Highlighted excerpt from job description
  - Specific requirement or responsibility

**Example Expanded View**:
```
🚀 From 0 to 1 Launch Experience
Frequency: 14 jobs (70%)
Description: Ability to independently lead product from concept to launch

Appears in:
1. ByteDance - AI Product Manager
   "负责AI能力的产品路线图规划和落地"
   
2. MiniMax - AI Product Manager
   "从0到1的产品落地经验"
   
3. Startup X - Product Manager
   "独立负责产品从概念到上线的全流程"
```

#### 2.4 Navigation
- Link back to Home
- Link to Company Comparison page

## Page 3: Company Comparison Page

### Purpose
Compare how large corporations and startups differ in their competency requirements.

### Sections

#### 3.1 Header
- **Title**: "Large Corporation vs. Startup Comparison"
- **Subtitle**: "How competency requirements differ by company type"

#### 3.2 Overview Chart
- **Visualization**: Bar chart comparing competency frequency
- **X-axis**: Competencies
- **Y-axis**: Frequency percentage
- **Bars**: Two bars per competency (large corp vs. startup)
- **Colors**: Different colors for each company type

#### 3.3 Detailed Comparison Table
For each competency, show:

| Competency | Large Corp | Startup | Difference | Insight |
|------------|-----------|---------|-----------|---------|
| From 0 to 1 | 40% | 93% | +53% | Startups prioritize launch experience |
| Project Management | 100% | 53% | -47% | Large corps emphasize process |
| AI/ML Knowledge | 80% | 87% | +7% | Both value technical depth |

#### 3.4 Company Type Profiles
Two side-by-side cards:

**Large Corporation Profile**:
- **Strengths**: Project management, cross-team collaboration, data-driven
- **Focus**: Process, structure, scalability
- **Growth Path**: Clear career progression, mentorship
- **Best For**: Those who value stability and structured growth

**Startup Profile**:
- **Strengths**: From 0 to 1 execution, innovation, ownership
- **Focus**: Speed, impact, learning
- **Growth Path**: Rapid skill development, equity upside
- **Best For**: Those who value autonomy and growth potential

#### 3.5 Job Search Recommendations
Provide actionable advice based on the analysis:

**For Large Corporation Seekers**:
- Focus on: Project management, cross-team collaboration, data analysis
- Prepare: Examples of managing complex projects, stakeholder management
- Highlight: Experience with formal processes and large-scale initiatives

**For Startup Seekers**:
- Focus on: From 0 to 1 experience, rapid iteration, ownership
- Prepare: Examples of launching new products, wearing multiple hats
- Highlight: Ability to work in ambiguous environments, self-motivation

#### 3.6 Key Insights
- Summarize the most important differences
- Provide strategic guidance for job seekers

## Data Visualization Guidelines

### Chart Types

1. **Bar Chart** (Salary Distribution)
   - Show counts and percentages
   - Use gradient fill
   - Include data labels

2. **Pie Chart** (Company Type)
   - Show proportions clearly
   - Use distinct colors
   - Include legend

3. **Horizontal Bar Chart** (Company Comparison)
   - Compare two groups side-by-side
   - Use contrasting colors
   - Sort by difference

### Color Scheme

- **Primary**: Blue (#3b82f6)
- **Secondary**: Cyan (#06b6d4)
- **Accent**: Indigo (#4f46e5)
- **Neutral**: Gray (#6b7280)
- **Success**: Green (#10b981)
- **Warning**: Orange (#f59e0b)

### Animation & Interaction

- **Page Load**: Fade-in animation for cards
- **Hover**: Slight scale-up and shadow enhancement
- **Chart Load**: Bars animate from bottom-up
- **Expand/Collapse**: Smooth height transition

## Responsive Design

### Mobile (< 640px)
- Single column layout
- Smaller cards
- Simplified charts (remove some labels)
- Stacked comparison tables

### Tablet (640px - 1024px)
- Two column layout where appropriate
- Medium-sized cards
- Full charts with labels

### Desktop (> 1024px)
- Multi-column layouts
- Large cards with detailed information
- Full interactive features

## Content Guidelines

### Tone
- Professional but approachable
- Data-driven and objective
- Actionable and practical

### Language
- Use clear, simple language
- Avoid jargon where possible
- Explain technical terms when necessary
- Support both English and Chinese

### Accuracy
- All data should be accurate and current
- Cite sources for statistics
- Update data regularly (monthly recommended)

## Export Options

Provide users with export capabilities:

1. **PDF Report**: Full report as downloadable PDF
2. **CSV Data**: Raw data for further analysis
3. **JSON Export**: Structured data for integration
4. **Share Link**: Generate shareable report URL
