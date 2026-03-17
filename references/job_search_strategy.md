# Job Search Strategy for Boss 直聘

## Overview

This guide provides best practices for searching and collecting job postings from Boss 直聘 (https://www.zhipin.com).

## Search URL Construction

Boss 直聘 uses URL parameters for filtering. The basic search URL structure is:

```
https://www.zhipin.com/web/geek/job?query={job_title}&city={city_code}&salary={salary_code}&experience={experience_code}
```

### Parameter Mapping

**City Codes:**
- 101280600 = Shenzhen (深圳)
- 101010100 = Beijing (北京)
- 101020100 = Shanghai (上海)
- 101280100 = Guangzhou (广州)
- 101190400 = Hangzhou (杭州)

**Salary Codes (Approximate):**
- 15 = 15K
- 21 = 20K+
- 30 = 30K+
- 50 = 50K+

**Experience Codes:**
- 104 = 1-3 years
- 105 = 3-5 years
- 106 = 5-10 years
- 107 = 10+ years

### Example Search URL

For "AI Product Manager" in Shenzhen, 3-5 years experience, 20K+ salary:

```
https://www.zhipin.com/web/geek/job?query=AI产品经理&city=101280600&salary=21&experience=105
```

## Data Collection Process

### Step 1: Initial Search

1. Construct the search URL with appropriate parameters
2. Navigate to the URL in the browser
3. Wait for results to load
4. Check the total number of results

### Step 2: Pagination and Collection

1. Extract job listings from the current page
2. For each job, collect:
   - Job title
   - Company name
   - Company size/type (look for indicators like "融资阶段" for funding stage)
   - Salary range
   - Work location
   - Job description (may need to click into each job)
   - Required qualifications
   - Key responsibilities

### Step 3: Company Type Classification

Classify each company as either "large_corporation" or "startup" based on:

**Large Corporation Indicators:**
- Company size: 1000+ employees
- Established companies (founded 10+ years ago)
- Well-known brands
- Multiple office locations

**Startup Indicators:**
- Company size: <500 employees
- Recent funding rounds (Series A, B, C)
- Founded within last 10 years
- Single or few office locations
- Growth-stage companies

### Step 4: Handling Incomplete Data

If a job description is truncated:
- Click into the job posting to view full details
- Copy the complete description
- Note any special requirements or benefits

## Data Quality Checks

Before proceeding to analysis, verify:

1. **Minimum 20 Jobs**: Ensure you have at least 20 job postings
2. **Diverse Company Types**: Aim for at least 5 large corporations and 15 startups
3. **Complete Descriptions**: All jobs should have full descriptions (not truncated)
4. **Accurate Salary**: Salary ranges should be within the specified range
5. **Relevant Positions**: All jobs should match the target job title (allow for slight variations)

## Common Challenges and Solutions

### Challenge: Fewer than 20 Results

**Solution:** Broaden the search parameters:
- Increase salary range (e.g., from 20K+ to 15K+)
- Expand experience range (e.g., from 3-5 years to 2-6 years)
- Include related job titles (e.g., "产品经理" + "产品负责人")

### Challenge: Duplicate or Similar Jobs

**Solution:** Remove near-duplicates:
- Same company posting the same job multiple times
- Same job title at the same company with slightly different descriptions
- Keep only the most recent posting

### Challenge: Irrelevant Results

**Solution:** Filter out non-matching jobs:
- Jobs with significantly different titles
- Jobs at wrong salary level
- Jobs requiring different experience levels

## Data Storage Format

Store collected jobs in JSON format:

```json
{
  "job_title": "AI Product Manager",
  "city": "Shenzhen",
  "experience_level": "3-5 years",
  "min_salary": "20K",
  "total_jobs": 20,
  "jobs": [
    {
      "id": 1,
      "company": "ByteDance",
      "position": "AI Product Manager - Creative",
      "salary_range": "30-60K",
      "type": "large_corporation",
      "company_size": "1000+",
      "location": "Shenzhen",
      "description": "Full job description text...",
      "responsibilities": ["Responsibility 1", "Responsibility 2"],
      "requirements": ["Requirement 1", "Requirement 2"],
      "url": "https://..."
    }
  ]
}
```

## Tips for Efficiency

1. **Use Browser Dev Tools**: Open DevTools to inspect and copy job data in bulk
2. **Save Snapshots**: Periodically save your collected data to prevent loss
3. **Organize by Company**: Group jobs by company to identify patterns
4. **Note Variations**: Record job title variations (e.g., "产品经理" vs "产品负责人")
5. **Timestamp Data**: Record when data was collected (job market changes rapidly)

## Ethical Considerations

- Respect Boss 直聘's terms of service
- Don't scrape data at excessive rates
- Use the data for legitimate research purposes
- Don't republish raw job postings without permission
- Aggregate and anonymize data when sharing results
