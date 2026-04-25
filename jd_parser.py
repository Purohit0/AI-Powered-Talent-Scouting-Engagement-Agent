"""
JD Parser Module
Extracts key requirements, skills, experience, and qualifications from job descriptions
"""

import re

class JDParser:
    def __init__(self):
        # Common tech skills keywords
        self.tech_skills = [
            'python', 'java', 'javascript', 'typescript', 'react', 'angular', 'vue',
            'node.js', 'nodejs', 'django', 'flask', 'spring', 'hibernate',
            'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch',
            'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git',
            'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'keras',
            'data science', 'data analysis', 'data engineering', 'etl', 'spark',
            'html', 'css', 'rest api', 'graphql', 'microservices', 'agile', 'scrum',
            'ci/cd', 'linux', 'shell scripting', 'networking', 'security',
            'c++', 'c#', 'ruby', 'go', 'rust', 'swift', 'kotlin', 'php',
            'tableau', 'power bi', 'excel', 'pandas', 'numpy', 'scikit-learn',
            'nlp', 'computer vision', 'ai', 'artificial intelligence',
            'communication', 'leadership', 'problem-solving', 'teamwork'
        ]
        
        # Experience level indicators
        self.experience_patterns = {
            'entry': r'(\d+[-–]?\d*\+?\s*(?:years?|yrs?)?\s*(?:of\s+)?(?:experience|exp)?)',
            'senior': r'senior|lead|principal|staff|architect',
            'manager': r'manager|director|head|vp|vice president'
        }
        
    def parse(self, jd_text):
        """Parse job description and extract key information"""
        
        # Extract skills
        skills = self._extract_skills(jd_text)
        
        # Extract experience required
        experience = self._extract_experience(jd_text)
        
        # Extract education
        education = self._extract_education(jd_text)
        
        # Extract job title
        title = self._extract_title(jd_text)
        
        # Extract key responsibilities
        responsibilities = self._extract_responsibilities(jd_text)
        
        # Extract location
        location = self._extract_location(jd_text)
        
        return {
            'title': title,
            'skills': skills,
            'experience_required': experience,
            'education': education,
            'responsibilities': responsibilities,
            'location': location,
            'raw_text': jd_text[:500]  # First 500 chars for reference
        }
    
    def _extract_skills(self, text):
        """Extract technical and soft skills from JD"""
        text_lower = text.lower()
        found_skills = []
        
        for skill in self.tech_skills:
            if skill in text_lower:
                found_skills.append(skill)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_skills = []
        for skill in found_skills:
            if skill not in seen:
                seen.add(skill)
                unique_skills.append(skill)
        
        return unique_skills
    
    def _extract_experience(self, text):
        """Extract required years of experience"""
        patterns = [
            r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)',
            r'(\d+[-–]\d+)\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)',
            r'minimum\s*(\d+)\s*(?:years?|yrs?)',
            r'(\d+)\s*-\s*(\d+)\s*years?'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return None
    
    def _extract_education(self, text):
        """Extract education requirements"""
        education_levels = []
        
        if re.search(r'ph\.?d|doctorate|doctoral', text, re.IGNORECASE):
            education_levels.append('PhD')
        if re.search(r'm\.?s\.?|master\'?s?|m\.?tech', text, re.IGNORECASE):
            education_levels.append("Master's")
        if re.search(r'b\.?s\.?|bachelor\'?s?|b\.?tech|b\.?e\.?', text, re.IGNORECASE):
            education_levels.append("Bachelor's")
        if re.search(r'diploma', text, re.IGNORECASE):
            education_levels.append('Diploma')
            
        return education_levels if education_levels else ['Not specified']
    
    def _extract_title(self, text):
        """Extract job title from JD"""
        lines = text.split('\n')
        for line in lines[:5]:  # Check first few lines
            line = line.strip()
            if len(line) > 5 and len(line) < 100:
                # Check if it looks like a title (no special chars, capitalized)
                if re.match(r'^[A-Z][a-zA-Z\s]+$', line):
                    return line
        return "Software Engineer"  # Default
    
    def _extract_responsibilities(self, text):
        """Extract key responsibilities"""
        responsibilities = []
        
        # Look for bullet points or numbered lists
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith(('- ', '• ', '* ', '1.', '2.', '3.')):
                resp = line.lstrip('-•*123456789. ')
                if len(resp) > 20 and len(resp) < 200:
                    responsibilities.append(resp)
        
        return responsibilities[:10]  # Return first 10
    
    def _extract_location(self, text):
        """Extract job location"""
        locations = ['Bangalore', 'Bengaluru', 'Hyderabad', 'Chennai', 'Mumbai', 
                    'Delhi', 'Pune', 'Gurgaon', 'Noida', 'Kolkata', 'Remote', 'WFH']
        
        text_upper = text.upper()
        for loc in locations:
            if loc.upper() in text_upper:
                return loc
        
        return "Not specified"