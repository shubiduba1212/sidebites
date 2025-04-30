import { create } from "zustand"

type ComicState = {
  slang: string
  scenario: string[]
  panelTexts: string[]
  imageUrls: string[]
  isLoading: boolean
  setSlang: (slang: string) => void
  fetchComic: (slang: string) => Promise<void>
}

export const useComicStore = create<ComicState>((set) => ({
  slang: '',
  scenario: [],
  panelTexts: [],
  imageUrls: [],
  isLoading: false,
  setSlang: (slang) => set({ slang }),
  fetchComic: async (slang) => {
    set({ isLoading: true })
    try {
      const response = await fetch('api/comic/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt : slang }),
      })
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      set({
        scenario: data.scenario,
        panelTexts: data.panelText,
        imageUrls: data.imageUrls,
        isLoading: false,
      })
    } catch (error) {
      console.error('[useComicStore] 만화 생성 실패:', error)
    } finally {
      set({ isLoading: false })
    }
  },
}))