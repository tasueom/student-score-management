def calculate(kor, eng, math):
    total = kor + eng + math
    average = total / 3
    grade = 'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'D' if average >= 60 else 'F'
    return total, average, grade

def format_chart_data(subject_averages):
    """과목별 평균 튜플을 Chart.js 바 차트용 데이터 형식으로 변환합니다.
    
    Args:
        subject_averages: (국어평균, 영어평균, 수학평균) 튜플
    
    Returns:
        dict: Chart.js 바 차트 설정 딕셔너리
    """
    avg_kor, avg_eng, avg_math = subject_averages
    
    return {
        'labels': ['국어', '영어', '수학'],
        'datasets': [{
            'label': '과목별 평균 점수',
            'data': [avg_kor, avg_eng, avg_math],
            'backgroundColor': ['rgba(54, 162, 235, 0.6)', 'rgba(255, 99, 132, 0.6)', 'rgba(75, 192, 192, 0.6)'],
            'borderColor': ['rgba(54, 162, 235, 1)', 'rgba(255, 99, 132, 1)', 'rgba(75, 192, 192, 1)'],
            'borderWidth': 1
        }]
    }