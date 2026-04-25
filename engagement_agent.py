"""
Engagement Agent Module
Simulates conversational outreach to assess candidate interest
"""

import random

class EngagementAgent:
    def __init__(self):
        # Outreach templates
        self.outreach_templates = [
            "Hi {name}! I came across your profile and I'm impressed with your experience in {skills}. We're looking for someone with your background for an exciting opportunity. Would you be interested in exploring this?",
            "Hello {name}, I noticed your expertise in {skills} and thought you'd be a great fit for a role we're recruiting for. Are you open to new opportunities?",
            "Hey {name}! Your profile caught our attention - especially your work with {skills}. We'd love to discuss a position that matches your skills. Are you available for a quick chat?",
            "Hi {name}, I saw your background in {skills} and think you'd be perfect for an opening we have. Would you like to learn more about this opportunity?",
            "Hello {name}, your experience with {skills} aligns well with what we're looking for. Are you interested in hearing about this role?"
        ]
        
        # Interest assessment questions
        self.assessment_questions = [
            "What are you looking for in your next role?",
            "What type of projects are you most interested in working on?",
            "What's your ideal work environment like?",
            "What are your career goals for the next few years?",
            "What technologies would you like to work with?",
            "Are you open to remote work or relocation?",
            "What's important to you in a company culture?",
            "What motivates you in your work?"
        ]
        
        # Response patterns for interest scoring
        self.high_interest_indicators = [
            'interested', 'excited', 'definitely', 'absolutely', 'yes', 'sounds great',
            'love to', 'eager', 'keen', 'curious', 'more details', 'tell me more',
            'when can', 'how soon', 'available'
        ]
        
        self.medium_interest_indicators = [
            'maybe', 'perhaps', 'could be', 'depends', 'considering', 'might',
            'need to', 'let me', 'think about', 'not sure', 'somewhat'
        ]
        
        self.low_interest_indicators = [
            'not interested', 'no thanks', 'not looking', 'happy', 'satisfied',
            'currently', 'busy', 'later', 'maybe later', 'not now'
        ]
    
    def engage(self, candidates):
        """Engage candidates conversationally and assess interest"""
        
        engaged_candidates = []
        
        for candidate in candidates:
            # Generate personalized outreach message
            outreach = self._generate_outreach(candidate)
            
            # Simulate candidate response
            response = self._simulate_response(candidate)
            
            # Assess interest based on response
            interest_score = self._assess_interest(response)
            
            # Generate conversation summary
            conversation = self._generate_conversation(candidate, outreach, response)
            
            engaged_candidates.append({
                **candidate,
                'outreach_message': outreach,
                'candidate_response': response,
                'interest_score': interest_score,
                'conversation': conversation,
                'engagement_status': self._get_status(interest_score)
            })
        
        # Sort by interest score descending
        engaged_candidates.sort(key=lambda x: x['interest_score'], reverse=True)
        
        return engaged_candidates
    
    def _generate_outreach(self, candidate):
        """Generate personalized outreach message"""
        template = random.choice(self.outreach_templates)
        
        # Get top skill for personalization
        skills = candidate.get('skills', [])
        top_skill = skills[0].title() if skills else 'technology'
        
        return template.format(
            name=candidate.get('name', 'there').split()[0],
            skills=top_skill
        )
    
    def _simulate_response(self, candidate):
        """Simulate candidate response based on their profile"""
        
        # Use candidate ID to seed random responses for consistency
        random.seed(candidate.get('id', 0))
        
        # Get match score to influence response
        match_score = candidate.get('match_score', 50)
        
        # High match candidates more likely to show interest
        if match_score >= 80:
            responses = [
                "That sounds interesting! I'd love to learn more about the role and the team. What are the main responsibilities?",
                "Absolutely! I'm always open to exploring new opportunities. Can you tell me more about the position and the company culture?",
                "Yes, definitely! I've been looking for a change and this sounds like a great fit. When can we discuss further?",
                "I'm excited to hear more! What technologies will I be working with? What's the team structure like?",
                "That sounds great! I'd love to explore this opportunity. What are the next steps?"
            ]
        elif match_score >= 60:
            responses = [
                "Thanks for reaching out! Could you tell me more about the role and compensation?",
                "I'm interested but would like to know more about the projects and growth opportunities.",
                "Maybe. What are the key responsibilities and what's the team like?",
                "Could you share more details about the position and the company?",
                "I'm considering it. What technologies are involved and what's the work-life balance like?"
            ]
        else:
            responses = [
                "Thanks for reaching out, but I'm not currently looking for a change.",
                "I'm happy in my current role, but I appreciate you reaching out.",
                "Not sure right now. Maybe later when I'm ready to make a move.",
                "I'm currently focused on my present role. Perhaps another time.",
                "Thanks, but I'm not interested in exploring new opportunities at the moment."
            ]
        
        return random.choice(responses)
    
    def _assess_interest(self, response):
        """Assess candidate interest from their response"""
        response_lower = response.lower()
        
        # Check for high interest indicators
        high_count = sum(1 for indicator in self.high_interest_indicators if indicator in response_lower)
        
        # Check for medium interest indicators
        medium_count = sum(1 for indicator in self.medium_interest_indicators if indicator in response_lower)
        
        # Check for low interest indicators
        low_count = sum(1 for indicator in self.low_interest_indicators if indicator in response_lower)
        
        # Calculate score
        if low_count > high_count:
            base_score = random.randint(20, 40)
        elif high_count > medium_count:
            base_score = random.randint(75, 95)
        else:
            base_score = random.randint(50, 70)
        
        return base_score
    
    def _generate_conversation(self, candidate, outreach, response):
        """Generate conversation summary"""
        
        return {
            'initial_message': outreach,
            'candidate_reply': response,
            'assessment': self._get_assessment_summary(candidate, response)
        }
    
    def _get_assessment_summary(self, candidate, response):
        """Generate assessment summary"""
        response_lower = response.lower()
        
        if any(ind in response_lower for ind in self.high_interest_indicators):
            return "High interest - Candidate eager to learn more and potentially pursue opportunity"
        elif any(ind in response_lower for ind in self.low_interest_indicators):
            return "Low interest - Candidate not actively looking or satisfied with current role"
        else:
            return "Medium interest - Candidate open to discussion but needs more information"
    
    def _get_status(self, interest_score):
        """Get engagement status based on interest score"""
        if interest_score >= 75:
            return "Hot"
        elif interest_score >= 50:
            return "Warm"
        else:
            return "Cold"