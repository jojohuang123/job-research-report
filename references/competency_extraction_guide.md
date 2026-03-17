# Competency Extraction Guide

## Overview

This guide explains how to identify, extract, and categorize core competencies from job descriptions.

## Competency Definition

A competency is a skill, knowledge area, or capability that a job requires. It can be:

- **Technical Skills**: Programming languages, tools, frameworks (Python, React, SQL)
- **Domain Knowledge**: Industry expertise, product knowledge (e-commerce, fintech, AI/ML)
- **Soft Skills**: Communication, leadership, problem-solving
- **Process Skills**: Project management, data analysis, user research
- **Emerging Skills**: AI/ML, blockchain, cloud computing

## Extraction Method

### Step 1: Read the Entire Description

Before extracting competencies, read the full job description to understand context.

### Step 2: Identify Key Phrases

Look for phrases that indicate required skills:

**Verb Patterns:**
- "Responsible for..." → indicates core responsibility
- "Required to..." → indicates required skill
- "Experience with..." → indicates required experience
- "Proficient in..." → indicates required proficiency
- "Understanding of..." → indicates required knowledge

**Noun Patterns:**
- "Strong [skill]" → indicates important skill
- "[Skill] experience" → indicates required experience
- "Knowledge of [domain]" → indicates required knowledge

### Step 3: Normalize Competencies

Group similar competencies under common names:

**Example Groupings:**
- "Communication", "Cross-team communication", "Stakeholder management" → **Communication & Collaboration**
- "Data analysis", "Analytics", "Metrics" → **Data-Driven Decision Making**
- "Product roadmap", "Product strategy", "Vision" → **Product Strategy**
- "From 0 to 1", "Product launch", "Go-to-market" → **Launch & Execution**

### Step 4: Frequency Counting

Count how many jobs mention each competency. This indicates importance.

## Common Competencies by Job Type

### Product Manager

1. **Product Strategy** - Defining vision, roadmap, and direction
2. **Cross-team Collaboration** - Working with engineering, design, marketing
3. **User Research** - Understanding user needs and pain points
4. **Data-Driven Decision Making** - Using metrics to guide decisions
5. **Project Management** - Managing timelines and deliverables
6. **Market Analysis** - Understanding competitive landscape
7. **Communication** - Presenting ideas and influencing stakeholders
8. **Technical Understanding** - Grasping technical feasibility
9. **Problem Solving** - Breaking down complex problems
10. **Agile/Scrum** - Working in iterative cycles

### AI Product Manager (Additional)

1. **AI/ML Knowledge** - Understanding large models, algorithms, capabilities
2. **Prompt Engineering** - Crafting effective prompts for AI systems
3. **Agent/Autonomous Systems** - Understanding agent architectures
4. **From 0 to 1** - Launching new AI-powered products
5. **Scenario Discovery** - Identifying best use cases for AI
6. **Model Evaluation** - Assessing model performance and limitations

### Data Analyst

1. **SQL/Database** - Querying and managing data
2. **Data Visualization** - Creating dashboards and reports
3. **Statistical Analysis** - Analyzing trends and patterns
4. **Business Acumen** - Understanding business metrics
5. **Communication** - Presenting findings to stakeholders
6. **Problem Solving** - Asking the right questions
7. **Tools Proficiency** - Excel, Tableau, Python, R
8. **Data Cleaning** - Preparing data for analysis

## Extraction Examples

### Example 1: Product Manager Job Description

**Text:**
"We're looking for an experienced Product Manager to lead our mobile app. You'll be responsible for defining product strategy, collaborating with engineering and design teams, and using data to drive decisions. Required: 5+ years of experience, strong communication skills, and understanding of mobile technologies."

**Extracted Competencies:**
1. Product Strategy (defining product strategy)
2. Cross-team Collaboration (collaborating with teams)
3. Data-Driven Decision Making (using data to drive decisions)
4. Communication (strong communication skills)
5. Technical Understanding (understanding of mobile technologies)

### Example 2: AI Product Manager Job Description

**Text:**
"Join our AI team as an AI Product Manager. You'll lead the development of AI-powered features, from 0 to 1. Responsibilities include: discovering use cases for our large language models, working with ML engineers to evaluate model performance, and crafting effective prompts. Required: understanding of LLMs, ability to work cross-functionally, and experience launching AI products."

**Extracted Competencies:**
1. From 0 to 1 (lead from 0 to 1)
2. Scenario Discovery (discovering use cases)
3. Cross-team Collaboration (work cross-functionally)
4. AI/ML Knowledge (understanding of LLMs)
5. Prompt Engineering (crafting effective prompts)
6. Model Evaluation (evaluate model performance)

## Competency Ranking

Rank competencies by frequency:

```
Rank 1: Product Strategy (18/20 jobs = 90%)
Rank 2: Cross-team Collaboration (17/20 jobs = 85%)
Rank 3: Data-Driven Decision Making (15/20 jobs = 75%)
Rank 4: Communication (14/20 jobs = 70%)
Rank 5: User Research (12/20 jobs = 60%)
...
```

## Company Type Analysis

For each competency, analyze differences between company types:

**Example:**
- **"From 0 to 1" Launch Experience**
  - Large Corporations: 2/5 (40%)
  - Startups: 14/15 (93%)
  - **Insight**: Startups emphasize launch experience much more

- **Project Management**
  - Large Corporations: 5/5 (100%)
  - Startups: 8/15 (53%)
  - **Insight**: Large corporations emphasize process and structure more

## Quality Checks

Before finalizing competency extraction:

1. **Relevance**: Are all extracted competencies relevant to the job?
2. **Completeness**: Did you capture all major competencies?
3. **Accuracy**: Are competency descriptions accurate?
4. **Consistency**: Are similar competencies grouped together?
5. **Frequency**: Do frequency counts match the actual data?

## Output Format

Store extracted competencies in JSON:

```json
{
  "competencies": [
    {
      "rank": 1,
      "name": "Product Strategy",
      "frequency": 18,
      "percentage": 90,
      "description": "Ability to define product vision, roadmap, and strategic direction",
      "jobs_mentioning": ["Company A", "Company B", ...],
      "large_corp_frequency": 5,
      "large_corp_percentage": 100,
      "startup_frequency": 13,
      "startup_percentage": 87,
      "key_phrases": [
        "产品规划",
        "产品策略",
        "产品路线图",
        "vision"
      ]
    }
  ]
}
```

## Tips for Accuracy

1. **Read Carefully**: Don't skim; read each job description thoroughly
2. **Context Matters**: Understand why a skill is mentioned
3. **Normalize Terms**: Use consistent terminology across jobs
4. **Double-Check**: Verify frequency counts by spot-checking
5. **Ask Questions**: If unsure about a competency, ask: "Is this a core skill or nice-to-have?"

## Handling Ambiguity

**Ambiguous Phrase**: "Strong problem-solving skills"

**Analysis:**
- This is too generic; look for specific problem types
- In context of product management: "breaking down complex product challenges"
- Classification: **Problem Solving** (general) or **Product Strategy** (specific)
- Decision: Include as **Problem Solving** if mentioned in multiple jobs

**Ambiguous Phrase**: "5+ years of experience"

**Analysis:**
- This indicates seniority level, not a specific competency
- Note the experience requirement separately
- Don't count as a competency unless paired with specific skills
