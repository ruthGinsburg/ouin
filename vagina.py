import numpy as np
import numpy.random.mtrand

import pyglet
from physicalobject import PhysicalObject
from pyglet.window import key

bg = pyglet.image.load('catfunsmall.png')
game_window = pyglet.window.Window(800, 600)
dog_image = pyglet.image.load_animation('dog.gif')
penis_image = pyglet.resource.image('mrpenis.png')
cosby_image = pyglet.image.load('coshead.png')
penis_image.height, penis_image.width = 100, 100
dog = PhysicalObject(penis_image, x=0, y=0)
cosby = PhysicalObject(cosby_image, x=game_window.width // 2, y=game_window.height // 2)


def dog_update(dt):
    dog.update(dt)
    dog.check_bounds()


def cosby_change(dt):
    cosby.velocity_x = -dog.velocity_x
    cosby.velocity_y = -dog.velocity_y


def cosby_update(dt):
    cosby.update(dt)
    cosby.check_bounds()


pyglet.clock.schedule_interval(cosby_change, 1)
pyglet.clock.schedule_interval(dog_update, 1 / 120.0)
pyglet.clock.schedule_interval(cosby_update, 1 / 120.0)


@game_window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        if dog.velocity_x > 0:
            dog.velocity_x = 0
        else:
            dog.velocity_x -= 5

    elif symbol == key.RIGHT:
        if dog.velocity_x < 0:
            dog.velocity_x = 0
        else:
            dog.velocity_x += 5

    elif symbol == key.UP:
        if dog.velocity_y < 0:
            dog.velocity_y = 0
        else:
            dog.velocity_y += 5

    elif symbol == key.DOWN:
        if dog.velocity_y > 0:
            dog.velocity_y = 0
        else:
            dog.velocity_y -= 5
    elif symbol == key.SPACE:
        dog.velocity_x, dog.velocity_y = 0, 0


@game_window.event
def on_draw():
    game_window.clear()
    bg.blit(0, 0)
    cosby.draw()
    dog.draw()


pyglet.app.run()
