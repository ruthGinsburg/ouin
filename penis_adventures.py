import pyglet
from numpy import random as rd
from pyglet.window import key

pic = pyglet.image.load('mrpenis.png')
dog_image = pyglet.image.load_animation('dog.gif')
dog = pyglet.sprite.Sprite(dog_image, x=150, y=50)

test_window = pyglet.window.Window(caption='Penis Adventures')
start_label = pyglet.text.Label("Penis adventures", font_name='Times New Roman', font_size=36, x=test_window.width // 2,
                                y=test_window.height // 2, anchor_x='center', anchor_y='center')
penis = pyglet.sprite.Sprite(pic, x=rd.randint(10,500), y=rd.randint(10,500))
penis.update(scale_x=.25, scale_y=.25)


def callback(dt):
    words = ['Adventures for your penis', 'Can you fill the hole?', 'Bone up on fun!', 'use arrow keys to move']
    start_label.text = rd.choice(words)


@test_window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        penis.x -= 10
    if symbol == key.RIGHT:
        penis.x += 10
    if symbol == key.UP:
        penis.y += 10
    if symbol == key.DOWN:
        penis.y -= 10
    if symbol == key.R:
        penis.rotation += 10


pyglet.clock.schedule_interval(callback, 2)


@test_window.event
def on_draw():
    test_window.clear()
    start_label.draw()
    dog.draw()
    penis.draw()


pyglet.app.run()
