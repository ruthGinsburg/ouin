import pyglet
from physicalobject import PhysicalObject
from numpy.random import choice
from pyglet.graphics import Batch
window = pyglet.window.Window()
batch = Batch()
gold = 100
swift_img = pyglet.resource.image('swift-head.png')
swift_img.width,swift_img.height = 100,100
penis_img = pyglet.resource.image('mrpenis.png')
penis_img.width,penis_img.height = 100,100
swift = PhysicalObject(swift_img,x=window.width//2,y=window.height//2,batch=batch)
girls_on_film = [swift,PhysicalObject(penis_img,x=0,y=0,batch=batch)]
swift_talk = 'lick my vagina!'
swift_text = pyglet.text.Label(swift_talk,font_size=22,x=swift.x - 200,y=swift.y + 50,batch=batch)
def swift_say(dt):
    global gold
    swift_text.text = choice(['I love penis','Feed me poop','My vulva is large.',f'The jew has {gold} gold'])
def jewgold(dt):
    global gold
    if gold > 0:
        gold -= 5

pyglet.clock.schedule_interval(jewgold,5)
pyglet.clock.schedule_interval(swift_say,2)
@window.event
def on_draw():
    window.clear()
    batch.draw()




pyglet.app.run()
