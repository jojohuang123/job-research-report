#!/usr/bin/env python3
"""
Extract competencies from job descriptions.

This script analyzes job descriptions to identify and rank core competencies.
It uses keyword matching and frequency analysis to determine the most important skills.
"""

import json
import re
from collections import Counter
from typing import List, Dict, Tuple

# Common competency keywords and their categories
COMPETENCY_KEYWORDS = {
    "Product Strategy": ["产品规划", "产品策略", "产品路线图", "roadmap", "vision", "战略"],
    "Cross-team Collaboration": ["跨团队", "协作", "沟通", "collaboration", "communication", "coordination"],
    "Data-Driven": ["数据驱动", "数据分析", "metrics", "analytics", "指标体系", "数据"],
    "Technical Understanding": ["技术理解", "技术原理", "算法", "架构", "technical", "algorithm"],
    "User Research": ["用户研究", "用户需求", "用户洞察", "user research", "user insight"],
    "Project Management": ["项目管理", "进度管理", "timeline", "project management", "schedule"],
    "From 0 to 1": ["从0到1", "从零到一", "产品落地", "launch", "go-to-market"],
    "AI/ML Knowledge": ["AI", "机器学习", "大模型", "LLM", "深度学习", "neural"],
    "Agile/Scrum": ["敏捷", "scrum", "sprint", "迭代", "agile"],
    "Market Analysis": ["市场分析", "竞争分析", "market research", "competitive"],
}

def extract_competencies_from_text(text: str) -> List[str]:
    """
    Extract competencies from a job description text.
    
    Args:
        text: Job description text
        
    Returns:
        List of identified competencies
    """
    text_lower = text.lower()
    found_competencies = []
    
    for competency, keywords in COMPETENCY_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                found_competencies.append(competency)
                break
    
    return found_competencies

def analyze_job_descriptions(jobs: List[Dict]) -> Dict:
    """
    Analyze a list of job descriptions to extract and rank competencies.
    
    Args:
        jobs: List of job dictionaries with 'description' field
        
    Returns:
        Dictionary with competency analysis results
    """
    all_competencies = []
    competency_jobs = {}  # Track which jobs mention each competency
    
    for job in jobs:
        description = job.get('description', '') + ' ' + job.get('responsibilities', '')
        competencies = extract_competencies_from_text(description)
        
        for comp in competencies:
            all_competencies.append(comp)
            if comp not in competency_jobs:
                competency_jobs[comp] = []
            competency_jobs[comp].append(job.get('company', 'Unknown'))
    
    # Count frequencies
    competency_counts = Counter(all_competencies)
    
    # Create ranked list
    ranked_competencies = []
    for rank, (competency, count) in enumerate(competency_counts.most_common(10), 1):
        ranked_competencies.append({
            'rank': rank,
            'name': competency,
            'frequency': count,
            'jobs': competency_jobs[competency],
            'percentage': round(count / len(jobs) * 100, 1)
        })
    
    return {
        'total_jobs': len(jobs),
        'competencies': ranked_competencies,
        'total_unique_competencies': len(competency_counts)
    }

def categorize_by_company_type(jobs: List[Dict], competencies: List[Dict]) -> Dict:
    """
    Categorize competency requirements by company type.
    
    Args:
        jobs: List of job dictionaries with 'type' field
        competencies: List of competency dictionaries
        
    Returns:
        Dictionary with company type analysis
    """
    large_corp_jobs = [j for j in jobs if j.get('type') == 'large_corporation']
    startup_jobs = [j for j in jobs if j.get('type') == 'startup']
    
    comparison = []
    for comp in competencies:
        comp_name = comp['name']
        
        # Count mentions in each company type
        large_corp_count = sum(1 for j in large_corp_jobs if comp_name in extract_competencies_from_text(j.get('description', '')))
        startup_count = sum(1 for j in startup_jobs if comp_name in extract_competencies_from_text(j.get('description', '')))
        
        large_corp_pct = round(large_corp_count / len(large_corp_jobs) * 100, 1) if large_corp_jobs else 0
        startup_pct = round(startup_count / len(startup_jobs) * 100, 1) if startup_jobs else 0
        
        comparison.append({
            'competency': comp_name,
            'large_corp_frequency': large_corp_count,
            'large_corp_percentage': large_corp_pct,
            'startup_frequency': startup_count,
            'startup_percentage': startup_pct,
            'difference': startup_pct - large_corp_pct
        })
    
    return {
        'large_corp_count': len(large_corp_jobs),
        'startup_count': len(startup_jobs),
        'comparison': comparison
    }

if __name__ == '__main__':
    # Example usage
    sample_jobs = [
        {
            'company': 'ByteDance',
            'type': 'large_corporation',
            'description': '产品规划和策略制定，跨团队协作，数据驱动决策',
            'responsibilities': '负责产品路线图规划，与技术团队协调'
        },
        {
            'company': 'Startup X',
            'type': 'startup',
            'description': '从0到1的产品落地经验，AI/ML理解，用户研究',
            'responsibilities': '独立负责产品从概念到上线'
        }
    ]
    
    analysis = analyze_job_descriptions(sample_jobs)
    print(json.dumps(analysis, indent=2, ensure_ascii=False))
