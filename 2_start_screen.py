import pygame

def display_start_screen():
    # 시작 버튼을 원으로 그림
    # 흰색으로 원을 그리는데 중심좌표는 start_button의 중심좌표를 따라감
    # 반지름은 60, 선 두께는 5
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 초기화
pygame.init()
#   게임 화면 크기
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
#   게임 화면 크기 넣기(고정하기 위해 (튜플) 사용)
screen = pygame.display.set_mode((screen_width,screen_height))
#   게임 제목
pygame.display.set_caption("Memory Game")


# 시작 버튼
# 가로세로 사각형 120, 화면에서 왼쪽으로 120, 아래에서 120 여백
# 화면 좌하단의 시작버튼 크기(위치좌표이동 0, 가로세로 120)
start_button = pygame.Rect(0, 0, 120, 120) # (0.0) 이 좌하단
# x값: 좌하단에서 왼쪽으로 120, y값: 화면 높이에서 120을 뺀 값 720-120 = 위에서 600만큼 내려와라는 뜻
start_button.center = (120, screen_height-120)


# 색깔
# RGB 값. w3school RGB document 참조
BLACK = (0,0,0)
WHITE = (255,255,255)


# 게임 루프
#   while문을 돌면서 키보드, 마우스 입력 체크하다가 게임을 종료하면 루프 탈출
running = True  # 게임이 실행중인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 게임 화면을 닫는 이벤트인가?
            running = False # 게임이 더 이상 실행 중이 아님

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()