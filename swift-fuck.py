import pyglet
from pyglet import shapes
from pyglet.window import key

swift_img = pyglet.resource.image('swift-head.png')
penis_img = pyglet.resource.image('mrpenis.png')
window = pyglet.window.Window()
swift_img.width, penis_img.width = 100, 100
swift_img.height, penis_img.height = 150, 100
bg = shapes.Rectangle(0, 0, window.width, window.height, (255, 255, 255))
penis = pyglet.sprite.Sprite(penis_img, x=100, y=0)
swift = pyglet.sprite.Sprite(swift_img, 201, y=600 - swift_img.height *2)
swift_words = ['Lick my vagina']
penis.vx = 0
@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.LEFT:
        penis.vx -= 1
    if symbol == key.RIGHT:
        penis.vx += 1


def penis_move(dt):
    penis.y += 100 * dt
    penis.x += penis.vx
    if penis.y >= 600:
        penis.y = 0


swift.speed = 150


def swift_move(dt):
    swift.x += swift.speed * dt
    if swift.x >= 400:
        swift.speed = -swift.speed
    elif swift.x <= 200:
        swift.speed = -swift.speed


pyglet.clock.schedule_interval(penis_move, 1 / 120.0)
pyglet.clock.schedule_interval(swift_move, 1 / 120.0)


@window.event
def on_draw():
    window.clear()
    bg.draw()
    swift.draw()
    penis.draw()


pyglet.app.run()
