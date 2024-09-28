import pygame
import sys

# Pygame 초기화
pygame.init()

# 게임 화면 크기 설정
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 색상 정의
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# 프레임 속도 설정
FPS = 60
clock = pygame.time.Clock()

# 스네이크 초기 설정
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# 스네이크 속도 및 시간 관리
snake_speed = 10
move_delay = 300  # 0.3초 = 300ms
last_move_time = pygame.time.get_ticks()  # 마지막 이동 시간

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                change_to = 'RIGHT'

    # 방향 업데이트
    snake_direction = change_to

    # 0.3초가 경과했을 때 스네이크 이동
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= move_delay:
        if snake_direction == 'UP':
            snake_pos[1] -= snake_speed
        if snake_direction == 'DOWN':
            snake_pos[1] += snake_speed
        if snake_direction == 'LEFT':
            snake_pos[0] -= snake_speed
        if snake_direction == 'RIGHT':
            snake_pos[0] += snake_speed

        # 스네이크 몸 업데이트
        snake_body.insert(0, list(snake_pos))
        snake_body.pop()  # 꼬리 제거 (길이 고정)

        # 마지막 이동 시간 갱신
        last_move_time = current_time

    # 화면 업데이트
    screen.fill(BLACK)

    # 스네이크 그리기
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # 화면 갱신
    pygame.display.update()

    # FPS 유지
    clock.tick(FPS)
