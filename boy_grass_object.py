import random
from pico2d import *

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599  
        self.fall_speed = random.randint(5, 15)
        self.image_size = random.choice([21, 41])
        if self.image_size == 21:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):

        if self.y - self.image_size // 2 > 30:
            self.y -= self.fall_speed
        else:
            self.y = 30 + self.image_size // 2

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    for o in world:
        o.update()
    grass.update()
    for boy in team:
        boy.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

def reset_world():  # 초기화하는 함수
    global running
    global grass
    global team
    global world

    running = True
    world = [Ball() for _ in range(20)]
    grass = Grass()
    world.append(grass)
    team = [Boy() for _ in range(11)]
    world += team

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code
close_canvas()
