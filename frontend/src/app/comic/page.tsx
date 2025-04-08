"use client"

import React, { useState } from 'react'

export default function ComicPage() {
  const [slang, setSlang] = useState("");
  const [imageUrls, setImageUrls] = useState<string[]>([]);

  const handleGenerate = async () => {
    const res = await fetch("http://localhost:8000/comic/generate", {
      method : "POST",
      headers : {"Content-type" : "application/json"},
      body: JSON.stringify({prompt: slang}),
    });
    const data = await res.json();
    console.log(data.image_urls); // 일단 콘솔에 이미지 base64 나오는 것 확인
    setImageUrls(data.image_urls);    
  };
  
  return (
    <div className='p-6'>
      <input type="text" className='border p-2 mr-2' placeholder='줄임말을 입력하세요' value={slang} onChange={(e) => setSlang(e.target.value)}/>
      <button className='bg-blue-500 text-white px-4 py-2 rounded' onClick={handleGenerate}>생성하기</button>
      {imageUrls.length > 0 && (
        <div className='grid grid-cols-2 gap-4 mt-6'>
          {imageUrls.map((url:string, idx:number) => (
            <div key={idx} className='border p-2 rounded shadow'>
              <img src={url} alt={`컷 ${idx + 1}`} className='w-full rounded' />
            </div>
          ))}
        </div>
      )}
    </div>

  )
}
