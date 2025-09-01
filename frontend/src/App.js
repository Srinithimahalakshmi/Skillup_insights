import React, { useState } from "react";
import Navbar from "./components/Navbar";
import SkillForm from "./components/SkillForm";
import Recommendation from "./components/Recommendation";
import ChartView from "./components/ChartView";
import "./Styles/App.css";

function App() 
{

  const [recommendations, setRecommendations] = useState([]);
  const [progressData, setProgressData] = useState([]);

  return (
    <div className="App">
      <Navbar />
      <div className="container">
        <SkillForm
          setRecommendations={setRecommendations}
          setProgressData={setProgressData}
        />
        <Recommendation recommendations={recommendations} />
        <ChartView progressData={progressData} />
      </div>
    </div>
  );
}

export default App;
