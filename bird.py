import game_framework


FRAME_DURATION = 0.082
MOVE_PER_FRAME = 5.0
FLY_SPEED_PPS = MOVE_PER_FRAME / FRAME_DURATION


class Bird:
    def __init__(self):
        self.elapsed_time = 0.0
        self.distance = 0.0

    def update(self):
        self.elapsed_time += game_framework.frame_time
        # 거리(픽셀) = 경과시간(초) * 속도(픽셀/초)
        self.distance = self.elapsed_time * FLY_SPEED_PPS
