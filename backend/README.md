## 🔧 진행 상황

- [x] 줄임말 → 시나리오 변환
- [x] 프롬프트 변환 (한국어 → 스타일+영어)
- [x] 4컷 이미지 생성 (Colab 연동)
- [x] FastAPI 서버에서 Colab Flask 서버로 요청 전송
- [ ] 이미지 생성 결과 다운로드 및 병합
- [ ] Hugging Face Spaces 배포 준비

## 📡 API 정리

### POST /comic/generate
- 설명: 줄임말 기반 4컷 만화 생성 요청
- Body: 
  ```json
  {
    "slang": "혼코노"
  }
