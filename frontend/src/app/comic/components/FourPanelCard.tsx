"use client";

import React from "react";

interface FourPanelCardProps {
  panels: string[]; // 4개의 패널 텍스트를 받음
}

const FourPanelCard: React.FC<FourPanelCardProps> = ({ panels }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
      {panels.map((text, index) => (
        <div key={index} className="border rounded-2xl shadow-md p-6 bg-white flex flex-col justify-center items-center">
          <h2 className="text-lg font-bold mb-2">Panel {index + 1}</h2>
          <p className="text-center text-gray-700 whitespace-pre-line">{text}</p>
        </div>
      ))}
    </div>
  );
};

export default FourPanelCard;