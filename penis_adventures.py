import pyglet
from numpy import random as rd
from pyglet.window import key

cosby_img = pyglet.image.load('coshead.png')
cosby = pyglet.sprite.Sprite(cosby_img,x=0,y=0)
pic = pyglet.image.load('mrpenis.png')
dog_image = pyglet.image.load_animation('dog.gif')
dog = pyglet.sprite.Sprite(dog_image, x=150, y=50)
bagkground = pyglet.image.load('catfunsmall.png')
test_window = pyglet.window.Window(841,847,caption='Penis Adventures')
start_label = pyglet.text.Label("Penis adventures", font_name='Times New Roman', font_size=46, x=test_window.width // 2,
                                y=test_window.height // 2, anchor_x='center', anchor_y='center',color=(255,255,0,255))
penis = pyglet.sprite.Sprite(pic, x=rd.randint(10,500), y=rd.randint(10,500))
penis.update(scale_x=.25, scale_y=.25)

def cos_move(dt):
    cosby.x = rd.randint(0,test_window.width - cosby.width)
    cosby.y = rd.randint(0,test_window.height - cosby.height)


def callback(dt):
    words = ['Adventures for your penis', 'Can you fill the hole?', 'Bone up on fun!', 'use arrow keys to move','use c key to chang Cosby']
    start_label.text = rd.choice(words)

cos = True
@test_window.event
def on_key_press(symbol, modifiers):
    global cos
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
    if symbol == key.C:

        if cos:
            cos = False
            cosby.image = dog_image
        else:
            cos = True
            cosby.image = cosby_img

pyglet.clock.schedule_interval(callback, 2)
pyglet.clock.schedule_interval(cos_move,3)

@test_window.event
def on_draw():
    test_window.clear()
    bagkground.blit(0,0)
    cosby.draw()
    start_label.draw()
    dog.draw()
    penis.draw()



pyglet.app.run()
