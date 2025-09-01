import React from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function ChartView({ progressData }) {
  if (!progressData.length) return null;

  const data = {
    labels: progressData.map((item) => item.skill),
    datasets: [
      {
        label: "Skill Level",
        data: progressData.map((item) => item.level),
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
    ],
  };

  return (
    <div className="chart-container">
      <h3>Your Progress</h3>
      <Bar data={data} />
    </div>
  );
}

export default ChartView;
