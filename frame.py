import pygame

# 초기화
pygame.init()
#   게임 화면 크기
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
#   게임 화면 크기 넣기(고정하기 위해 (튜플) 사용)
screen = pygame.display.set_mode((screen_width,screen_height))
#   게임 제목
pygame.display.set_caption("Memory Game")

# 게임 루프
#   while문을 돌면서 키보드, 마우스 입력 체크하다가 게임을 종료하면 루프 탈출
running = True  # 게임이 실행중인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 게임 화면을 닫는 이벤트인가?
            running = False # 게임이 더 이상 실행 중이 아님
# 게임 종료
pygame.quit()