# student-score-report-lab

Flask 기반 학생 성적 관리 웹 애플리케이션으로, MySQL에 데이터를 저장하고 Chart.js로 시각화하며 엑셀/PDF 성적표를 자동 생성합니다.

## 주요 기능

### ✅ 구현 완료

- **성적 입력**: 학생 이름과 국어, 영어, 수학 점수를 입력하여 성적을 저장
- **성적 조회**: 저장된 모든 성적을 테이블 형태로 조회
- **시각화**: Chart.js를 사용한 과목별 평균 점수 바 차트
- **데이터 검증**: 프론트엔드에서 점수 유효성 검사 (0-100 정수)
- **환경 변수 관리**: `.env` 파일을 통한 민감 정보 관리
- **반응형 디자인**: 모바일과 데스크톱 환경 모두 지원

### 🚧 개발 예정

- **엑셀 내보내기**: 성적 데이터를 엑셀 파일로 다운로드
- **PDF 내보내기**: ReportLab을 사용한 PDF 성적표 자동 생성

## 기술 스택

- **Backend**: Flask 3.0.0
- **Database**: MySQL (mysql-connector-python)
- **Frontend**: HTML, CSS, JavaScript
- **차트 라이브러리**: Chart.js
- **아이콘**: Font Awesome
- **마크다운 렌더링**: marked.js
- **환경 변수**: python-dotenv

## 프로젝트 구조

```
student-score-report-lab/
├── app/
│   ├── __init__.py          # Flask 앱 초기화
│   ├── routes.py            # 라우트 정의
│   ├── db.py                # 데이터베이스 연결 및 쿼리
│   ├── service.py           # 비즈니스 로직
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # 스타일시트
│   │   └── js/
│   │       ├── chart.js     # 차트 렌더링
│   │       └── check.js    # 폼 검증
│   └── templates/
│       ├── layout.html       # 기본 레이아웃
│       ├── index.html       # 홈페이지
│       ├── input.html       # 성적 입력 페이지
│       └── view.html        # 성적 조회 페이지
├── app.py                   # 애플리케이션 실행 파일
├── init_db.py              # 데이터베이스 초기화 스크립트
├── requirements.txt         # Python 패키지 의존성
├── .env                     # 환경 변수 (gitignore에 포함)
└── README.md               # 프로젝트 문서
```

## 설치 및 실행

### 1. 저장소 클론

```bash
git clone <repository-url>
cd student-score-report-lab
```

### 2. 가상 환경 생성 및 활성화

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 내용을 입력하세요:

```env
# Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=scoredb

# Flask Configuration
SECRET_KEY=your-secret-key-here
```

### 5. 데이터베이스 초기화

```bash
python init_db.py
```

이 스크립트는 다음을 수행합니다:
- `scoredb` 데이터베이스 생성
- `scores` 테이블 생성

### 6. 애플리케이션 실행

```bash
python app.py
```

브라우저에서 `http://localhost:5000`으로 접속하세요.

## 사용 방법

### 성적 입력

1. 네비게이션에서 "성적 입력" 클릭
2. 학생 이름과 국어, 영어, 수학 점수 입력 (0-100 정수)
3. "입력" 버튼 클릭

### 성적 조회

1. 네비게이션에서 "성적 조회" 클릭
2. 저장된 모든 성적을 테이블로 확인
3. 오른쪽에 과목별 평균 점수 바 차트 확인

### 데이터 내보내기 (준비중)

- **엑셀 다운로드**: 성적 조회 페이지의 엑셀 아이콘 클릭
- **PDF 다운로드**: 성적 조회 페이지의 PDF 아이콘 클릭

## 데이터베이스 스키마

### scores 테이블

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| id | INT | 기본 키 (자동 증가) |
| name | VARCHAR(50) | 학생 이름 |
| kor | INT | 국어 점수 |
| eng | INT | 영어 점수 |
| math | INT | 수학 점수 |
| total | INT | 총점 |
| average | DECIMAL(5,2) | 평균 |
| grade | CHAR(1) | 등급 (A-F) |

## 등급 기준

- **A**: 평균 90점 이상
- **B**: 평균 80점 이상
- **C**: 평균 70점 이상
- **D**: 평균 60점 이상
- **F**: 평균 60점 미만

## 개발 특징

- **역할 분리**: routes, service, db 모듈로 명확한 책임 분리
- **환경 변수 관리**: 하드코딩 없이 `.env` 파일로 설정 관리
- **에러 처리**: 데이터베이스 연결 및 쿼리 예외 처리
- **프론트엔드 검증**: JavaScript를 통한 실시간 입력 검증
- **반응형 디자인**: 모바일과 데스크톱 환경 모두 지원

## 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.
