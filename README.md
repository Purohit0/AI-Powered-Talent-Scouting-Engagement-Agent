# AI-Powered-Talent-Scouting-Engagement-Agent

Recruiters spend hours sifting through profiles and chasing candidate interest. This AI agent takes a Job Description as input, discovers matching candidates, engages them conversationally to assess genuine interest, and outputs a ranked shortlist scored on two dimensions: Match Score and Interest Score.

---

##  Working Model

### Local Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Purohit0/AI-Powered-Talent-Scouting-Engagement-Agent
cd AI-Powered-Talent-Scouting-Engagement-Agent

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open **(https://ai-powered-talent-scouting-engagement-pzen.onrender.com)** in your browser.

---

## 📹 Demo Video

Watch a 3-5 minute walkthrough demonstrating:
- Pasting a job description
- Automatic JD parsing and skill extraction
- Candidate matching with explainability
- Conversational outreach simulation
- Final ranked shortlist generation

[Demo Video Link - Coming Soon]

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│ Job Description │────▶│   JD Parser     │────▶│  Extract:           │
│   (Input)       │     │   Module         │     │  - Skills           │
└─────────────────┘     └──────────────────┘     │  - Experience       │
                                                  │  - Education        │
                                                  │  - Location         │
                                                  └─────────────────────┘
                                                          │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  Ranked         │◀────│  Ranking Engine │◀────│  Engagement Agent   │
│  Shortlist      │     │  (60% Match +    │     │  (Simulated         │
│  (Output)       │     │   40% Interest)  │     │   Outreach)         │
└─────────────────┘     └──────────────────┘     └─────────────────────┘
                                                          │
                                                          ▼
                                                 ┌─────────────────────┐
                                                 │  Candidate Matcher  │
                                                 │  - Skill Score      │
                                                 │  - Experience Score │
                                                 │  - Location Score   │
                                                 └─────────────────────┘
                                                          │
                                                          ▼
                                                 ┌─────────────────────┐
                                                 │  Candidate Database │
                                                 │  (15 Candidates)    │
                                                 │                     │
                                                 └─────────────────────┘
```

### Scoring Logic

| Component | Weight | Description |
|-----------|--------|-------------|
| **Skill Match** | 50% | Percentage of required skills matched |
| **Experience Match** | 30% | Years of experience vs requirement |
| **Location Match** | 20% | Geographic preference alignment |
| **Interest Score** | 40% | Assessed from conversational response |

**Combined Score = (Match Score × 0.6) + (Interest Score × 0.4)**

---

## 📋 Sample Input

### Job Description
```
Senior Python Developer
Location: Bangalore
Experience: 4-6 years

Required Skills:
- Python, Django, Flask
- React, JavaScript
- AWS, Docker
- PostgreSQL, MongoDB
- Machine Learning basics

Responsibilities:
- Build scalable web applications
- Lead technical projects
- Mentor junior developers

Education: B.Tech or M.Tech
```

---

## 📊 Sample Output

### Ranked Candidate Shortlist

| Rank | Name | Match Score | Interest Score | Combined | Status |
|------|------|-------------|----------------|----------|--------|
| 1 | Arjun Sharma | 84.6% | 93% | 87.96% | 🔥 Hot |
| 2 | Sneha Krishnan | 72.1% | 88% | 78.44% | 🔥 Hot |
| 3 | Rahul Verma | 78.2% | 71% | 75.66% | 🔥 Hot |
| 4 | Priya Patel | 68.5% | 85% | 75.10% | 🔥 Hot |
| 5 | Vikram Singh | 65.3% | 82% | 72.18% | 🔥 Hot |
| 6 | Meera Joshi | 58.2% | 79% | 66.52% | 🟡 Warm |
| 7 | Karthik Nair | 45.8% | 88% | 62.68% | 🟡 Warm |
| 8 | Divya Menon | 52.1% | 75% | 61.26% | 🟡 Warm |
| 9 | Aisha Khan | 48.6% | 72% | 58.36% | 🟡 Warm |
| 10 | Nikhil Chandra | 55.2% | 65% | 59.12% | 🟡 Warm |

### Sample Match Explanation
```
✓ Matches 9 required skills: python, react, django, sql, postgresql, aws, docker, machine learning, go
⚠ Missing skills: java, javascript, flask, mongodb
✓ Experience matches requirement (5 years)
✓ Location: Bangalore
```

### Sample Conversation
```
Recruiter: "Hi Arjun, I saw your background in Python and think you'd be perfect 
for an opening we have. Would you like to learn more about this opportunity?"

Candidate: "Absolutely! I'm always open to exploring new opportunities. Can you 
tell me more about the position and the company culture?"

Assessment: High interest - Candidate eager to learn more and potentially pursue opportunity
```

---

##  Project Structure

```
AI-Powered-Talent-Scouting-Engagement-Agent/
├── app.py                 # Flask web application
├── jd_parser.py          # JD parsing module
├── candidate_matcher.py  # Candidate matching algorithm
├── engagement_agent.py   # Conversational outreach simulation
├── candidates.py         # 15 Indian candidates database
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── templates/
    └── index.html       # Frontend UI
```

---

## 🔧 Features

- **JD Parsing**: Automatically extracts key requirements, skills, experience, and qualifications
- **Candidate Discovery**: Matches candidates from a diverse pool with Indian names
- **Smart Matching**: Scores candidates on skill, experience, and location match with explainability
- **Conversational Outreach**: Simulates personalized candidate engagement
- **Ranked Shortlist**: Outputs candidates ranked by combined Match + Interest Score

---

## 📝 License

MIT License
