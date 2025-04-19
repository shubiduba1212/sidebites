"use client"

import React, { useState } from 'react'
// import FourPanelCard from './components/FourPanelCard';
// import { text } from 'stream/consumers';

export default function ComicPage() {
  const [slang, setSlang] = useState("");
  const [panelTexts, setPanelTexts] = useState<string[]>([]);
  const [imageUrls, setImageUrls] = useState<string[]>([]);

  const handleGenerate = async () => {
    const response = await fetch('http://localhost:8000/comic/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt : slang }),
    });

    if (response.ok) {
      const data = await response.json();
      console.log("[백엔드 응답 데이터]", data);
      setPanelTexts(data.panel_texts);
      setImageUrls(data.image_urls);      

    } else {
      console.error('Failed to generate comic:', response.statusText);
    }
  }

  return (
    <div className='p-6'>
      <div className='flex gap-2 mb-6'>
        <input 
          type="text" 
          className='border p-2 flex-1 rounded'
          placeholder='줄임말을 입력하세요'
          value={slang}
          onChange={(e) => setSlang(e.target.value)}
        />
        <button className='bg-blue-500 text-white px-4 py-2 rounded' onClick={handleGenerate}>
          생성하기
        </button>
      </div>

      {panelTexts.length > 0 && (
        <div className='grid grid-cols-2 gap-4 mt-6'>
          {panelTexts.map((text, idx) => (
            <div key={idx} className='border p-4 rounded shadow flex flex-col items-center'>
              <img src={imageUrls[idx]} alt={`Panel ${idx + 1}`} className='mb-4 w-full h-auto object-cover rounded' />
              {/* <img src={imageUrls[idx]} alt={`Panel ${idx + 1}`} className='mb-2 w-full h-auto rounded' /> */}
              <h2 className='text-lg font-bold mb-2'>Panel {idx + 1}</h2>
              <p className='text-gray-700 whitespace-pre-wrap'>{text}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}



// if (data.panel_texts && data.panel_texts.length > 0){
      //   const splitPanels = 
      //   typeof data.panel_texts[0] === 'string'
      //     ? data.panel_texts[0].split(/Panel \d+:/g).map(text => text.trim()).filter(text => text.length > 0)
      //     : [];
      //   console.log("[분리된 텍스트]",splitPanels);
      //   setPanels(splitPanels);
      // }

      // if (data.image_urls){
      //   setImageUrls(data.image_urls);
      // }

// const samplePanels = [
//   "Friends laughing loudly, enjoying their time together.",
//   "One friend leans forward with a mischievous grin, preparing to tell a joke.",
//   "The heavy joke lands, freezing everyone mid-laughter.",
//   "An awkward silence spreads across the once lively room, tension thick in the air."
// ];

// return (
//   <main className="min-h-screen p-8">
//     <h1 className="text-3xl font-bold mb-6 text-center">4-Panel Comic Test</h1>
//     <FourPanelCard panels={samplePanels} />
//   </main>
// );
