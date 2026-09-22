# SPORTS MPS 투자제안서

GitHub 업로드용 발표 페이지입니다. 전체28장, A2Z와 Pretendard 두 글꼴 버전을 제공합니다.

- `index.html`: A2Z 버전
- `index_pretendard.html`: Pretendard 버전
- `site_assets/`: 화면에 필요한 이미지와 폰트. HTML과 함께 업로드해야 합니다.
- `build_deck.py`, `reference_24.py`, `revision_20260923.py`, `investor_story.py`: 장표 생성 및 편집 코드
- `verify_export.py`: 전체 장표 검증과 PDF/PPTX 내보내기

HTML은 이미지와 폰트를 상대경로로 참조합니다. 두 HTML과 site_assets를 같은 디렉터리 구조로 유지하면 로컬과 정적 웹사이트에서 작동합니다.

## 로컬 참고자료

참고자료와 생성 결과는 같은 상위 경로의 `../20260922mpssports_1/`에 보관합니다. GitHub에 함께 올릴 필요가 없습니다.

- `assets/`: 편집용 원본 이미지와 출처
- `근거자료/`: 원문 및 검토 자료
- `참고문서/`: 매출모델, 발표자 노트, 구성과 검증 기록
- `이전버전/`: 기존 버전
- `내보내기/`: 최신 PDF와 발표용 PPTX
- `preview/`, `preview_pretendard/`: 장표 이미지와 검증 결과
- `분리전_편집원본/`: 폴더 분리 전 코드와 독립형 HTML

## 재생성

현재 작업 환경에서 `python build_deck.py` 실행 후 `python verify_export.py` 및 `python verify_export.py --pretendard`로 출력합니다. PDF/PPTX와 미리보기는 `_1` 폴더에 저장됩니다. 편집 및 재생성에는 `_1` 원본자료와 기존20260919 사업제안서/20260920 투자제언서의 사진 및 폰트 경로가 필요합니다. 배포된 HTML 열람에는 이 참고자료가 필요하지 않습니다.

## Git 반영

이동된 파일은 Git에서 삭제로, `site_assets/`는 새 파일로 보입니다. 파일은 `_1`에 보존되어 있습니다. 이동과 경로 수정을 같은 커밋에 반영해야 합니다. 기존 커밋 이력과 원격 저장소는 이번 정리에서 변경하지 않았습니다.
