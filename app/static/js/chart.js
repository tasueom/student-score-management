/**
 * 과목별 평균 점수 바 차트를 그리는 함수
 * @param {Object} chartData - Chart.js 형식의 차트 데이터
 */
function initSubjectChart(chartData) {
    const ctx = document.getElementById('subjectChart');
    
    if (!ctx) {
        console.error('Canvas element not found');
        return;
    }
    
    new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        stepSize: 10
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                },
                title: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed.y;
                            return label + ' 평균 점수: ' + value + '점';
                        }
                    }
                }
            }
        }
    });
}

