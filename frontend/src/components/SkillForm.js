import React, { useState } from "react";
import api from "../utils/api";

function SkillForm({ setRecommendations, setProgressData }) {
  const [skills, setSkills] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Call backend API
      const response = await api.post("/predict", { skills: skills.split(",") });
      setRecommendations(response.data.recommendations);
      setProgressData(response.data.progress);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <form className="skill-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter your skills (comma separated)"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />
      <button type="submit">Get Recommendations</button>
    </form>
  );
}

export default SkillForm;
