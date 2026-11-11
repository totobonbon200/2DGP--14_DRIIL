import game_framework


FRAME_DURATION = 0.082
MOVE_PER_FRAME = 5.0
FLY_SPEED_PPS = MOVE_PER_FRAME / FRAME_DURATION


class Bird:
    def __init__(self, x=400, y=190, direction=1):
        self.initial_x = x
        self.x, self.y = x, y
        self.direction = direction
        self.elapsed_time = 0.0
        self.distance = 0.0

    def update(self):
        self.elapsed_time += game_framework.frame_time
        # 거리(픽셀) = 경과시간(초) * 속도(픽셀/초)
        self.distance = self.elapsed_time * FLY_SPEED_PPS
        # 위치 = 초기위치 + 방향을 적용한 거리
        self.x = self.initial_x + self.direction * self.distance
