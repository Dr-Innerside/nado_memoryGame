import pygame
from random import *

### 레벨에 맞게 설정
def setup(level):
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5         # 레벨로 3으로 나눈 몫에 5 더하기
    number_count = min(number_count, 20)    # 레벨이 높아도 최대 수를 20으로 제한

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)


### 숫자 섞기 (이 프로젝트에서 가장 중요!!!)
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 # 각 Grid cell 별 가로, 세로 크기
    button_size = 110 # Grid cell 내에 실제로 그려질 버튼 크기
    screen_left_margin = 55 # 전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백

    # [0,0,0,0,0,0,0,0,0] 앞 부분 for
    # [[0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0]] 뒷 부분 for
    grid = [[0 for col in range(columns)] for row in range(rows)]

    # 시작 숫자 1부터 number_count, 만약 5라면 5까지 숫자를 랜덤으로 배치
    number = 1

    # 레벨에서 주어지는 넘버 카운트 만큼 리스트 안에 숫자를 넣고 초과하면 루프 탈출
    while number <= number_count:
        # y좌표: 0, 1, 2, 3, 4 중에서 랜덤으로 뽑기
        row_index = randrange(0,rows)
        # x좌표: 0, 1, 2, 3, 4, 5, 6, 7, 8 중에서 랜덤으로 뽑기
        col_index = randrange(0,columns)

        # 리스트에 접근했는데 비어있는 값이라면
        if grid[row_index][col_index] == 0:
            grid[row_index][col_index] = number # 숫자 지정
            number += 1

            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_index * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_index * cell_size) + (cell_size / 2)

            # 숫자 버튼 만들기
            # 실제 여백이 들어간 버튼 크기로 설정
            button = pygame.Rect(0,0,button_size,button_size)
            # 버튼 위치 잡아주기
            button.center = (center_x,center_y)
            # 버튼 넣어주기
            number_buttons.append(button)

    # 배치된 랜덤함수 확인
    # for grid_pix in grid:
    #     print(grid_pix)

### 게임 시작 버튼 보여주기
# 함수 선언을 위해 상단 배치
def display_start_screen():
    # 시작 버튼을 원으로 그림
    # 흰색으로 원을 그리는데 중심좌표는 start_button의 중심좌표를 따라감
    # 반지름은 60, 선 두께는 5
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


### 게임 화면 보여주기
def display_game_screen():
    # 버튼 값을 반복을 돌면서 보여줘야 함
    for idx, rect in enumerate(number_buttons, start=1):
        # 화면에, 회색에 해당하는, rect형 이미지를 그려줌
        pygame.draw.rect(screen, GRAY, rect)


### pos에 해당하는 버튼 확인
def check_buttons(pos):
    # 함수 밖에 위치한 변수를 쓰는 것은 상관 없지만
    # 변수 값을 바꿔주기 위해서는 전역변수 설정을 해줘야함
    global start

    # 사용자가 클릭한 위치가 스타트 버튼 내부에 포함된다면
    if start_button.collidepoint(pos):
        # 게임 스타트 분기 변경
        start = True

### 초기화
pygame.init()
#   게임 화면 크기
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
#   게임 화면 크기 넣기(고정하기 위해 (튜플) 사용)
screen = pygame.display.set_mode((screen_width,screen_height))
#   게임 제목
pygame.display.set_caption("Memory Game")


### 시작 버튼
# 가로세로 사각형 120, 화면에서 왼쪽으로 120, 아래에서 120 여백
# 화면 좌하단의 시작버튼 크기(위치좌표이동 0, 가로세로 120)
start_button = pygame.Rect(0, 0, 120, 120) # (0.0) 이 좌상단
# x값: 좌하단에서 왼쪽으로 120, y값: 화면 높이에서 120을 뺀 값 720-120 = 위에서 600만큼 내려와라는 뜻
start_button.center = (120, screen_height-120)


### 색깔
# RGB 값. w3school RGB document 참조
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (50,50,50)

### 플레이어가 눌러야 하는 버튼들
number_buttons = []

### 게임 시작 여부
start = False

### 게임 시작 전에 게임 설정 함수 수행
setup(1)

### 게임 루프
#   while문을 돌면서 키보드, 마우스 입력 체크하다가 게임을 종료하면 루프 탈출
running = True  # 게임이 실행중인가?
while running:
    # 마우스 클릭 포지션 값을 받기 위한 변수 선언
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 게임 화면을 닫는 이벤트인가?
            running = False # 게임이 더 이상 실행 중이 아님
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을 때
            click_pos = pygame.mouse.get_pos()  # get_pos()으로 클릭한 위치 값 받아오기
            print(click_pos)

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    # 분기설정 : 게임이 시작됐다면,
    if start:
        display_game_screen() # 게임 화면 표시
    # 분기설정 : 게임이 시작되지 않았다면,
    else:
        display_start_screen() # 시작 화면 표시

    # 사용자가 클릭한 좌표 값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()


### 게임 종료
pygame.quit()