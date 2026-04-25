"""
AI-Powered Talent Scouting Engagement Agent
Main Flask Application
"""

from flask import Flask, render_template, request, jsonify
import json
from jd_parser import JDParser
from candidate_matcher import CandidateMatcher
from engagement_agent import EngagementAgent
from candidates import get_candidates

app = Flask(__name__)

# Initialize components
jd_parser = JDParser()
candidate_matcher = CandidateMatcher()
engagement_agent = EngagementAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/parse-jd', methods=['POST'])
def parse_jd():
    """Parse job description and extract key requirements"""
    data = request.get_json()
    jd_text = data.get('jd_text', '')
    
    parsed = jd_parser.parse(jd_text)
    return jsonify(parsed)

@app.route('/api/match-candidates', methods=['POST'])
def match_candidates():
    """Match candidates against parsed JD"""
    data = request.get_json()
    parsed_jd = data.get('parsed_jd', {})
    
    candidates = get_candidates()
    matches = candidate_matcher.match(candidates, parsed_jd)
    
    return jsonify(matches)

@app.route('/api/engage-candidates', methods=['POST'])
def engage_candidates():
    """Engage candidates conversationally"""
    data = request.get_json()
    candidates = data.get('candidates', [])
    
    engaged = engagement_agent.engage(candidates)
    
    return jsonify(engaged)

@app.route('/api/final-rankings', methods=['POST'])
def final_rankings():
    """Generate final ranked shortlist"""
    data = request.get_json()
    candidates = data.get('candidates', [])
    
    # Sort by combined score (60% match, 40% interest)
    ranked = []
    for c in candidates:
        combined_score = (c.get('match_score', 0) * 0.6) + (c.get('interest_score', 0) * 0.4)
        c['combined_score'] = round(combined_score, 2)
        ranked.append(c)
    
    # Sort by combined score descending
    ranked.sort(key=lambda x: x['combined_score'], reverse=True)
    
    return jsonify(ranked)

@app.route('/api/full-process', methods=['POST'])
def full_process():
    """Run the complete talent scouting pipeline"""
    data = request.get_json()
    jd_text = data.get('jd_text', '')
    
    # Step 1: Parse JD
    parsed_jd = jd_parser.parse(jd_text)
    
    # Step 2: Get candidates and match
    candidates = get_candidates()
    matches = candidate_matcher.match(candidates, parsed_jd)
    
    # Step 3: Engage candidates
    engaged = engagement_agent.engage(matches)
    
    # Step 4: Generate final rankings
    ranked = []
    for c in engaged:
        combined_score = (c.get('match_score', 0) * 0.6) + (c.get('interest_score', 0) * 0.4)
        c['combined_score'] = round(combined_score, 2)
        ranked.append(c)
    
    ranked.sort(key=lambda x: x['combined_score'], reverse=True)
    
    return jsonify({
        'parsed_jd': parsed_jd,
        'ranked_candidates': ranked
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)