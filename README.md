
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
````

---

## Usage

1. Open your browser and go to **[http://localhost:5173/](http://localhost:5173/)**
2. Register and log in (dummy auth or your own logic)
3. Input skills (0–5 rating or text form)
4. View personalized career recommendations and track progress

---

## Project Structure

```
SkillUp_Insights/
│
├── backend/
│   ├── app.py             # FastAPI backend + ML inference
│   ├── train_model.py     # Train and export ML model
│   ├── setup_db.py        # Initialize SQLite database
│   ├── model.pkl          # Saved ML model
│   ├── database.db        # SQLite database
│   ├── requirements.txt   # Python dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.jsx
│   │   ├── api.js
│   │   ├── components/     # Login, SkillForm, Recommendation
│   │   └── pages/          # Dashboard.jsx
│   ├── package.json       # Node dependencies & scripts
│   └── tailwind.config.js # (if Tailwind used)
│
├── .gitignore             # Ignore build, env, dependencies
└── README.md              # This overview
```

---

## Features

* Skill logging and progress tracking
* Career recommendation via ML
* Interactive frontend using React (Vite + optional styling)
* Simple backend API with FastAPI
* SQLite for simple user management
* Lightweight architecture—easy to extend

---

## Future Enhancements

* Integrate real-world datasets & a richer ML model
* Enhance UI/UX with Tailwind CSS or charts
* Add user profile persistence and history
* Deploy backend and frontend via Docker/CI/CD
* Expand with gamification, LinkedIn integration, and mobile app

---

## Contributing

Your contributions are welcome!
To contribute:

1. Fork the repo
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit: `git commit -m "Add new feature"`
4. Push: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## Contact

**Maintainer**: Srinithi Mahalakshmi
**Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
**GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

