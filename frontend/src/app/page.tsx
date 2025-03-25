'use client'

import { useState } from 'react'

export default function Home() {
  const [query, setQuery] = useState('')
  const [result, setResult] = useState<any>(null)
  const [error, setError] = useState('')

  const handleSearch = async () => {
    if (!query) return

    try {
      const res = await fetch(`http://localhost:8000/slang?query=${encodeURIComponent(query)}`)
      const data = await res.json()
      if (data.error) {
        setResult(null)
        setError(data.error)
      } else {
        setResult(data)
        setError('')
      }
    } catch (err) {
      setError('서버 요청 중 오류가 발생했어요!')
    }
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-pink-100 to-blue-100 p-8 flex flex-col items-center">
      <h1 className="text-3xl font-bold mb-8 text-gray-800">✨ 줄마르: 줄임말을 번역해드립니다 ✨</h1>

      <div className="flex gap-4 mb-6">
        <input
          type="text"
          placeholder="예: 스불재, 혼코노"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="px-4 py-2 rounded-xl border border-gray-300 focus:outline-none shadow-sm"
        />
        <button
          onClick={handleSearch}
          className="bg-indigo-500 text-white px-6 py-2 rounded-xl shadow-md hover:bg-indigo-600"
        >
          검색
        </button>
      </div>

      {error && <p className="text-red-500 font-semibold mb-4">{error}</p>}

      {result && (
        <div className="bg-white rounded-2xl shadow-lg p-6 w-full max-w-md text-gray-800">
          <h2 className="text-xl font-bold mb-2">🧩 {result.kr_slang}</h2>
          <p className="mb-2">💬 <strong>의미:</strong> {result.meaning}</p>
          <div>
            🌍 <strong>영어 표현:</strong>
            <ul className="list-disc list-inside mt-1 text-sm">
              {result.eng_equivalent.map((item: string, idx: number) => (
                <li key={idx}>{item}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </main>
  )
}
