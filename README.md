# SkillUp Insights

## Overview
SkillUp Insights is a personalized learning tracker and career recommender built with FastAPI and React. Users log their skills, monitor progress, and receive tailored career suggestions powered by a lightweight ML model.

---

## Table of Contents
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Features](#features)  
- [Future Enhancements](#future-enhancements)  
- [Contributing](#contributing)  
- [Contact](#contact)  
- [License](#license)  

---

## Installation

```bash
git clone https://github.com/Srinithimahalakshmi/Skillup_insights.git
cd Skillup_insights

# Backend
cd backend
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python setup_db.py           # Initializes SQLite database
python train_model.py        # Trains and saves model.pkl
python app.py                # Start FastAPI backend (default port: 8000)

# Frontend
cd ../frontend
npm install
npm run dev                  # Starts React app (default port: 5173)
