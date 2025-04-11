![status](https://img.shields.io/badge/status-in%20progress-yellow)  

## 🔧 진행 상황

- [x] 줄임말 → 시나리오 변환
- [x] 프롬프트 변환 (한국어 → 스타일+영어)
- [x] 4컷 이미지 생성 (Colab 연동)
- [x] FastAPI 서버에서 Colab Flask 서버로 요청 전송
- [ ] 이미지 생성 결과 다운로드 및 병합
- [ ] Hugging Face Spaces 배포 준비

---

## 📡 API 정리

### POST /comic/generate
- 설명: 줄임말 기반 4컷 만화 생성 요청
- Body:
```json
{
  "slang": "혼코노"
}


# Backend 구조 및 연동 흐름

## 주요 구성
- FastAPI: 메인 백엔드 서버
- Colab: Stable Diffusion 기반 이미지 생성 Flask 서버
- OpenAI: 시나리오 생성, 프롬프트 변환

## 흐름 요약
1. 사용자가 `/comic/generate`에 줄임말(prompt)을 POST 요청
2. 시나리오 4줄 생성 → 영어 스타일 변환
3. Colab Flask 서버에 프롬프트 4개 요청 → 이미지 4장 생성
4. 이미지 Base64 인코딩 후 JSON 응답

## 환경 변수
- `.env` 파일에 `OPENAI_API_KEY` 저장

