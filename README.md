# nado_memoryGame
나도코딩 기억력 테스트 게임

## 개발전략 
1. 5rows, 9columns의 Grid 구성
2. 게임 시작을 위한 버튼을 좌측 하단에 배치
   1. 클릭을 하면 레벨 설명
3. 게임을 시작하면 격자 내의 숫자가 랜덤하게 배치됨
4. 숫자를 보여줬다가 숨기기
   1. 시작 버튼을 누르면 - 몇 초동안 보여주다가 시간제한을 초과하면 숫자를 숨김
   2. [1] 숫자 버튼을 누르면 나머지 숫자를 숨김
5. 바로 옆 격자에 숫자가 배치되면 겹쳐 보이므로 숨기는 숫자 배경을 격자에 안쪽 여백을 줌
6. 순서대로 숫자를 맞추면 - 다음 레벨로 이동
7. 잘못된 숫자를 누르면 - 게임 오버