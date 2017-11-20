#Clay Kynor
#11/20/17
#antsDemo.py- How to use lists with graphics

from ggame import *
from random import randint

WIDTH = 1000
HEIGHT = 500

def step():
    for ant in data['antList']:
        dx = randint(-4,3)
        dy = randint(-4,3)
        if ant.x + dx > 0 and ant.x + dx < WIDTH:
            ant.x += dx
        if ant.y + dy > 0 and ant.y + dy < HEIGHT:
            ant.y += dy
    

if __name__ == '__main__':
    
    pink = Color(0xFF00CB,1)
    ant = CircleAsset(8,LineStyle(1,pink),pink)
    
    data = {}
    data['antList'] = []
    
    for i in range(50):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))

    App().run(step)