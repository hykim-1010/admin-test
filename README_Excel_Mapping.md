# HTML ID 매핑 관리 시스템

## 개요
HTML 요소의 id와 매핑되는 텍스트를 관리하기 위한 시스템입니다.

## 파일 구조
- `HTML_ID_Mapping.csv`: HTML 요소 id와 매핑 텍스트를 관리하는 CSV 파일
- `admin-template-v1.1.html`: 템플릿 파일 (id가 부여된 HTML 요소들 포함)

## CSV 파일 구조
CSV 파일은 다음 4개 컬럼으로 구성됩니다:

| 컬럼명 | 설명 | 예시 |
|--------|------|------|
| element_id | HTML 요소의 id 값 | meta-title, post-label-title |
| mapped_text | 사람이 관리할 텍스트 | 관리자 페이지 제목, 제목 |
| description | 요소에 대한 설명 | 페이지 상단 제목, 제목 입력 라벨 |
| category | 요소의 카테고리 | meta, form, button, filter |

## 사용 방법

### 1. Excel에서 편집
1. `HTML_ID_Mapping.csv` 파일을 Excel에서 열기
2. `mapped_text` 컬럼에서 원하는 텍스트로 수정
3. 새로운 id 추가 시 `element_id`와 `mapped_text` 입력
4. Excel 파일로 저장 (`.xlsx` 형식 권장)

### 2. 관리자 화면 생성 시 활용
```javascript
// CSV 파일을 읽어서 매핑 리스트 생성
function loadIdMapping() {
  // CSV 파일을 읽어서 JSON 객체로 변환
  // element_id를 키로, mapped_text를 값으로 하는 매핑 객체 생성
}

// HTML 요소에 매핑된 텍스트 적용
function applyMappedText(elementId, mappedText) {
  const element = document.getElementById(elementId);
  if (element) {
    element.textContent = mappedText;
  }
}
```

## 주요 ID 목록

### Meta Card 관련
- `meta-title`: 관리자 페이지 제목
- `meta-path`: Path
- `meta-writer`: Writer
- `meta-date`: Date / Version
- `meta-page`: page

### Section Title 관련
- `section-title-list`: 섹션 > 하위섹션 > 목록
- `section-title-post`: 섹션 > 하위섹션 > 등록
- `section-title-detail`: 섹션 > 하위섹션 > 수정/상세

### 폼 관련
- `post-label-lang`: 언어
- `post-label-type`: 유형
- `post-label-title`: 제목
- `post-label-image`: 이미지
- `post-label-attachment`: 첨부파일
- `post-label-link`: 링크 URL
- `post-label-daterange`: 노출기간
- `post-label-visible`: 노출여부

### 버튼 관련
- `btn-register`: 등록
- `post-btn-submit`: 등록
- `post-btn-list`: 목록
- `detail-btn-modify`: 수정하기
- `detail-btn-delete`: 삭제하기
- `detail-btn-list`: 목록으로

### 필터 관련
- `filter-start-date`: 시작일
- `filter-end-date`: 종료일
- `filter-cond`: 검색 조건
- `filter-keyword`: 검색
- `filter-submit`: 검색

## 확장 방법
1. 새로운 HTML 요소에 id 추가
2. CSV 파일에 해당 id와 매핑 텍스트 추가
3. 관리자 화면 생성 시 자동으로 매핑 적용

## 주의사항
- `element_id`는 HTML에서 실제로 사용되는 id와 정확히 일치해야 함
- `mapped_text`는 사용자에게 표시될 텍스트
- CSV 파일 편집 시 UTF-8 인코딩 사용 권장

