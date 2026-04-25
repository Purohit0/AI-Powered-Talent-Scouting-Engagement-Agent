"""
Candidate Matcher Module
Matches candidates against parsed job descriptions with explainability
"""

class CandidateMatcher:
    def __init__(self):
        self.skill_weight = 0.5
        self.experience_weight = 0.3
        self.location_weight = 0.2
        
    def match(self, candidates, parsed_jd):
        """Match candidates against parsed JD and return scored results"""
        
        required_skills = parsed_jd.get('skills', [])
        exp_required = parsed_jd.get('experience_required')
        location = parsed_jd.get('location', '')
        
        results = []
        
        for candidate in candidates:
            # Calculate skill match score
            skill_score, matched_skills, missing_skills = self._calculate_skill_match(
                candidate.get('skills', []), 
                required_skills
            )
            
            # Calculate experience match score
            exp_score = self._calculate_experience_match(
                candidate.get('experience_years'),
                exp_required
            )
            
            # Calculate location match score
            loc_score = self._calculate_location_match(
                candidate.get('location'),
                location
            )
            
            # Calculate overall match score
            match_score = (
                skill_score * self.skill_weight +
                exp_score * self.experience_weight +
                loc_score * self.location_weight
            )
            
            # Generate explanation
            explanation = self._generate_explanation(
                candidate,
                matched_skills,
                missing_skills,
                skill_score,
                exp_score,
                loc_score
            )
            
            results.append({
                'id': candidate.get('id'),
                'name': candidate.get('name'),
                'email': candidate.get('email'),
                'phone': candidate.get('phone'),
                'location': candidate.get('location'),
                'experience_years': candidate.get('experience_years'),
                'current_role': candidate.get('current_role'),
                'company': candidate.get('company'),
                'skills': candidate.get('skills'),
                'education': candidate.get('education'),
                'current_salary': candidate.get('current_salary'),
                'notice_period': candidate.get('notice_period'),
                'bio': candidate.get('bio'),
                'match_score': round(match_score * 100, 1),
                'skill_score': round(skill_score * 100, 1),
                'experience_score': round(exp_score * 100, 1),
                'location_score': round(loc_score * 100, 1),
                'matched_skills': matched_skills,
                'missing_skills': missing_skills,
                'explanation': explanation
            })
        
        # Sort by match score descending
        results.sort(key=lambda x: x['match_score'], reverse=True)
        
        return results
    
    def _calculate_skill_match(self, candidate_skills, required_skills):
        """Calculate skill match score"""
        if not required_skills:
            return 1.0, [], []
        
        # Normalize skills to lowercase
        candidate_skills_lower = [s.lower() for s in candidate_skills]
        required_skills_lower = [s.lower() for s in required_skills]
        
        # Find matched and missing skills
        matched = []
        missing = []
        
        for req_skill in required_skills_lower:
            if any(req_skill in cskill or cskill in req_skill for cskill in candidate_skills_lower):
                matched.append(req_skill)
            else:
                missing.append(req_skill)
        
        # Calculate score
        if len(required_skills_lower) > 0:
            score = len(matched) / len(required_skills_lower)
        else:
            score = 1.0
            
        return score, matched, missing
    
    def _calculate_experience_match(self, candidate_exp, required_exp):
        """Calculate experience match score"""
        if not required_exp:
            return 1.0  # No experience requirement specified
            
        try:
            required = int(required_exp)
            if candidate_exp >= required:
                return 1.0
            elif candidate_exp >= required * 0.7:
                return 0.7
            elif candidate_exp >= required * 0.5:
                return 0.5
            else:
                return 0.3
        except:
            return 0.5
    
    def _calculate_location_match(self, candidate_location, required_location):
        """Calculate location match score"""
        if not required_location or required_location == 'Not specified':
            return 1.0
            
        # Check for remote work flexibility
        if required_location.lower() in ['remote', 'wfh', 'work from home']:
            return 1.0
            
        # Exact match
        if candidate_location.lower() == required_location.lower():
            return 1.0
            
        # Same city variations
        bangalore_synonyms = ['bangalore', 'bengaluru', 'blr']
        if candidate_location.lower() in bangalore_synonyms and required_location.lower() in bangalore_synonyms:
            return 1.0
            
        # Different city - still can relocate
        return 0.6
    
    def _generate_explanation(self, candidate, matched_skills, missing_skills, skill_score, exp_score, loc_score):
        """Generate human-readable explanation for the match"""
        
        explanations = []
        
        # Skill explanation
        if matched_skills:
            explanations.append(f"✓ Matches {len(matched_skills)} required skills: {', '.join(matched_skills[:5])}")
        if missing_skills:
            explanations.append(f"⚠ Missing skills: {', '.join(missing_skills[:3])}")
            
        # Experience explanation
        if exp_score >= 0.8:
            explanations.append(f"✓ Experience matches requirement ({candidate.get('experience_years')} years)")
        elif exp_score >= 0.5:
            explanations.append(f"⚠ Partial experience match ({candidate.get('experience_years')} years)")
        else:
            explanations.append(f"✗ Experience below requirement ({candidate.get('experience_years')} years)")
            
        # Location explanation
        if loc_score >= 0.8:
            explanations.append(f"✓ Location: {candidate.get('location')}")
        else:
            explanations.append(f"⚠ Location: {candidate.get('location')} (may require relocation)")
        
        return " | ".join(explanations)