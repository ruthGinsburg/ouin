import pyglet
from physicalobject import PhysicalObject
from pyglet.graphics import Batch
win_width,win_height = 800,600
window = pyglet.window.Window(win_width,win_height)
school_img = pyglet.resource.image('school-clip-art-2.png')
penis_image = pyglet.resource.image('mrpenis.png')
penis_image.width,penis_image.height = 100,100
penis_image.anchor_x,penis_image.anchor_y = penis_image.width//2,penis_image.height//2
school_img.width,school_img.height = win_width//4,win_height//4
school_img.anchor_x,school_img.anchor_y = school_img.width//2,school_img.height//2
batch = Batch()
school = PhysicalObject(school_img,x=window.width//2,y=window.height//2,batch=batch)
text = ""
label = pyglet.text.Label(text=text,x=10,y=window.height-10,batch=batch)
cock_txt = pyglet.text.Label("",x=window.width//2,y=window.height-30,batch=batch,anchor_x='center',font_size=30)
player = PhysicalObject(penis_image,x=penis_image.width//2,y=penis_image.height//2,batch=batch)
swift_img = pyglet.resource.image('swift-head.png')
swift_img.width,swift_img.height = 100,100
taylor = pyglet.sprite.Sprite(swift_img,x=0,y=window.height - swift_img.height,batch=batch)
cosby_img = pyglet.resource.image('coshead.png')
cosby_img.width,cosby_img.height = 100,100
def school_chk():

    if school.x - school.width//2 < player.x < school.x + school.width//2:
        cock_txt.text = 'The penis in in front of the school.'
        return True
    else:
        cock_txt.text = ""
        return False

@window.event
def on_key_press(symbol,modifiers):
    if taylor.image == cosby_img:
        taylor.image = swift_img
    if symbol == pyglet.window.key.LEFT:
        player.x -= 10
        school_chk()
    if symbol == pyglet.window.key.RIGHT:

        player.x += 10
        school_chk()
    if symbol == pyglet.window.key.ENTER:
        if school_chk():
            cock_txt.text = 'The children see the penis.'
            taylor.image = cosby_img

from pyglet.window import mouse
@window.event
def on_mouse_press(x,y,button,modifier):
    if button == mouse.LEFT:
        label.text = f'x: {x} y:{y}'
        label.x, label.y = x, y
        print(school.x,school.y)
    if button == mouse.RIGHT:
        player.x = x
        school_chk()



@window.event
def on_draw():
    window.clear()

    batch.draw()


pyglet.app.run()