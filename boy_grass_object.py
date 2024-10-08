from pico2d import *

# Game object class here
class Grass:
    # 생성자를 이용해서 객체의 초기 상태를 정의상태 정의
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)

    pass
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    grass.update()

def render_world():
    clear_canvas()
    grass.draw()
    update_canvas()

def reset_world(): #초기화하는 함수
    global running
    global grass

    running = True
    grass = Grass() #Grass 클래스를 이용해서 grass객체를 생성

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
