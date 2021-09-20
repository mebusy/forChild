#!python3

import turtle as tt
import math

def mx( d ):
    tt.up()
    x,y = tt.pos()
    tt.goto( x+d, y )
    tt.down()

def my( d ):
    tt.up()
    x,y = tt.pos()
    tt.goto( x, y+d )
    tt.down()

def mov(x,y):
    tt.up()
    tt.goto( x, y )
    tt.down()


col = tt.color

def cc( radius ): # cc = circle
    tt.up()
    tt.fd(radius)
    tt.left(90)
    tt.down()

    tt.begin_fill()
    tt.circle(radius)
    tt.end_fill()

    tt.up()
    tt.right(90)
    tt.bk(radius)
    tt.down()

def moon( radius ):
    x,y = tt.pos()
    tt.seth(0)

    tt.up()
    tt.bk(radius)
    tt.down()

    start_pos = tt.pos()

    tt.color('brown', '#fbbf4b' )  # '#C08040')
    tt.begin_fill()

    angle_left_turn = 170
    tt.right( (180-angle_left_turn)/2 )

    i = 0
    while True:
        tt.fd(radius*2)
        tt.left( angle_left_turn)
        # print(i,  tt.pos(), abs(tt.pos()) )
        i+=1
        if abs(tt.pos()- start_pos) < 1 :
            break

    tt.end_fill() 

    tt.color( 'black', 'white' )
    mov(x,y)
    tt.seth(0)

def pt(r, n):
    tt.penup()
    tt.goto(0, -r)
    tt.seth(0)
    tt.pendown()
    tt.color( '#C08040' ) # '#fbbf4b' )
    small_r = math.sin( math.pi/n) * r
    
    for i in range(n):
        tt.penup()
        tt.home()
        tt.seth((360/n)*i)
        tt.fd(r)
        tt.left((360/n)*0.5)
        tt.pendown()
        tt.begin_fill()
        tt.circle(small_r,180)
        tt.end_fill()

    mov(0,0)
    tt.seth(0)
    tt.color( 'black' )

def test():
    col( '#f5cf9c' )
    cc(300)
    petal(300,20)
    patt(300)


if __name__ == '__main__':
    tt.speed(10)

    # test()

    col( '#f5cf9c' )

    import code
    code.interact(local=locals())
