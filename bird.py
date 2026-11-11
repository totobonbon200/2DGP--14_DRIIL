import game_framework
import random
from pico2d import get_canvas_height, get_canvas_width, load_image


FRAME_DURATION = 0.082
MOVE_PER_FRAME = 5.0
FLY_SPEED_PPS = MOVE_PER_FRAME / FRAME_DURATION
FRAME_COUNT = 14
DRAW_SCALE = 0.3


class Bird:
    image = None

    def __init__(self, boy_y, x=None, y=None, direction=None):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.cell_width = self.image.w // 5
        self.cell_height = self.image.h // 3
        self.draw_width = self.cell_width * DRAW_SCALE
        self.draw_height = self.cell_height * DRAW_SCALE
        self.frame = 0
        self.left = self.draw_width / 2
        self.right = get_canvas_width() - self.draw_width / 2
        if x is None:
            x = random.uniform(self.left, self.right)
        if y is None:
            y = random.uniform(max(boy_y + 100, self.draw_height / 2),
                               get_canvas_height() - self.draw_height / 2)
        if direction is None:
            direction = random.choice((-1, 1))
        self.initial_x = x
        self.x, self.y = x, y
        self.direction = direction
        self.initial_direction = direction
        self.elapsed_time = 0.0
        self.distance = 0.0

    def update(self):
        self.elapsed_time += game_framework.frame_time
        self.frame = int(self.elapsed_time / FRAME_DURATION) % FRAME_COUNT
        # 거리(픽셀) = 경과시간(초) * 속도(픽셀/초)
        self.distance = self.elapsed_time * FLY_SPEED_PPS
        # 위치 = 초기위치 + 방향을 적용한 거리
        self.x = self.initial_x + self.initial_direction * self.distance
        # 왕복 구간 두 개를 한 주기로 접어 경계를 넘은 거리도 보존한다.
        span = self.right - self.left
        phase = (self.x - self.left) % (2 * span)
        self.x = self.left + (phase if phase <= span else 2 * span - phase)
        if phase == 0:
            self.direction = 1
        elif phase == span:
            self.direction = -1
        else:
            self.direction = self.initial_direction * (1 if phase < span else -1)

    def draw(self):
        clip_x = (self.frame % 5) * self.cell_width
        clip_y = (2 - self.frame // 5) * self.cell_height
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            clip_x, clip_y, self.cell_width, self.cell_height,
            0, flip, self.x, self.y, self.draw_width, self.draw_height
        )
