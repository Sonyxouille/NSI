from turtle import * # type: ignore
from random import * # type: ignore

setup(1920,1080,0,0)

colors=['blue','red','green']
rez_de_chaussee = ['window','door','window']

def rez_chaussee(x,y):
    x_base = x
    y_base = y
    color_rez_chaussee = choice(colors)
    fillcolor(color_rez_chaussee)
    begin_fill()
    pencolor('black')
    goto(x,y+60)
    pencolor('black')
    goto(x+140,y+60)
    pencolor('black')
    goto(x+140,y)
    pencolor('black')
    goto(x,y)
    end_fill()
    up()
    x += 12.5
    goto(x,y)
    down()
    shuffle(rez_de_chaussee)
    for element in rez_de_chaussee:
        if element == 'window':
            window(x,y)
            x += 42.5
            goto(x,y)
        elif element == 'door':
            door(x,y,color_rez_chaussee)
            x += 42.5
            goto(x,y)
    up()
    goto(x_base,y_base)
    x,y = x_base,y_base
    return x,y,color_rez_chaussee

def etage(x,y,color_rez_chaussee):
    x,y = x,y+60
    x_base = x
    y_base = y
    goto(x,y)
    fillcolor(color_rez_chaussee)
    begin_fill()
    pencolor('black')
    goto(x,y+60)
    pencolor('black')
    goto(x+140,y+60)
    pencolor('black')
    goto(x+140,y)
    pencolor('black')
    goto(x,y)
    end_fill()
    up()
    x += 12.5
    goto(x,y)
    down()
    for i in range(3):
        if randint(0,2) == 1:
            window_with_barrier(x,y)
        else:
            window(x,y)
        x += 42.5
        goto(x,y)
    up()
    x,y = x_base,y_base
    return x,y,color_rez_chaussee

def door(x,y,color_rez_chaussee):
    colors_door = []
    for color in colors:
        if color != color_rez_chaussee:
            colors_door.append(color)
    fillcolor(choice(colors_door))
    begin_fill()
    pencolor('black')
    goto(x,y+50)
    pencolor('black')
    goto(x+30,y+50)
    pencolor('black')
    goto(x+30,y)
    pencolor('black')
    goto(x,y)
    x,y = x,y
    end_fill()
    return x,y

def window(x,y):
    up()
    goto(x,y+20)
    down()
    fillcolor('lightblue')
    begin_fill()
    pencolor('black')
    goto(x,y+50)
    pencolor('black')
    goto(x+30,y+50)
    pencolor('black')
    goto(x+30,y+20)
    pencolor('black')
    goto(x,y+20)
    end_fill()
    up()
    x,y = x,y
    return x,y

def window_with_barrier(x,y):
    up()
    goto(x,y)
    down()

    #window
    fillcolor('lightblue')
    begin_fill()
    pencolor('black')
    goto(x,y+50)
    pencolor('black')
    goto(x+30,y+50)
    pencolor('black')
    goto(x+30,y)
    pencolor('black')
    goto(x,y)
    end_fill()
    up()

    #barrier
    x -= 5
    goto(x,y)
    down()

    fillcolor('brown')
    begin_fill()
    goto(x,y+20)
    goto(x+40,y+20)
    goto(x+40,y)
    goto(x,y)
    end_fill()


    #bars
    marge = 3
    x_bars = x + 4
    for i in range(6):
        up()
        goto(x_bars, y+marge)
        down()
        pensize(2)
        pencolor('gray')
        goto(x_bars, y+20-marge)
        pensize(1)
        pencolor('black')
        x_bars += 6.5
    up()
    x,y = x,y
    return x,y

def roof(x,y):
    up()
    x,y = x,y+60
    goto(x,y)
    down()
    fillcolor('brown')
    begin_fill()
    goto(x-10,y)
    goto(x+(140/2),y+30)
    goto(x+150,y)
    goto(x,y)
    end_fill()
    return x,y

def immeuble(x,y):
    x,y,color_rez_chaussee = rez_chaussee(x,y)
    for i in range(randint(1,4)):
        x,y,color_rez_chaussee = etage(x,y,color_rez_chaussee)
    roof(x,y)
    return x,y

def quartier(x,y):
    up()
    goto(x,y)
    down()
    for i in range(randint(1,5)):
        immeuble(x,y)
        up()
        x += 160
        y = 0
        goto(x,y)
        down()

down()
quartier(-300,0)
done()


