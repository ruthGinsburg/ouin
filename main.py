import pyglet
from pyglet.window import key
from pyglet.window import mouse
from numpy import random
window = pyglet.window.Window(width=800,height=600)
image = pyglet.resource.animation('dog.gif')
penis_image = pyglet.resource.image('mrpenis.png')

penis_image.height = 100
penis_image.width = 100
penis = pyglet.sprite.Sprite(penis_image)
dog = pyglet.sprite.Sprite(image, x=0, y=0)
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')
score = 0
score_label = pyglet.text.Label(f'score {score}',x=0,y=window.height - 20)
words = ["Hello","Vagina","Penis","Balls","Horse cock"]
@window.event
def on_mouse_press(x, y, button, modifiers):
    global score
    global score_label
    if button == mouse.LEFT:
        penis.update(x,y)
        dog.update(random.randint(0, window.width - 20), random.randint(0, window.height - 20))
    if button == mouse.RIGHT:
        label.text = random.choice(words)
        score += 1
        score_label.text = f'score {score}'



@window.event
def on_key_press(symbol,modifiers):
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




@window.event
def on_draw():
    window.clear()
    score_label.draw()
    label.draw()
    penis.draw()
    dog.draw()


pyglet.app.run()
