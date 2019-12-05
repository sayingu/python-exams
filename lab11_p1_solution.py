import turtle, random, math

# <위치 pos와 터틀 t 사이의 거리>
# pos는 튜플 형태 (x, y)로 주어지며 t는 Turtle 객체 
def calc_dist(pos, t):
    return math.sqrt( (pos[0] - t.xcor())**2 + (pos[1] - t.ycor())**2 )

# 마우스 클릭할 때 호출되는 함수
def on_click(x, y):
    global tlist

    min_dist = None
    min_turtle = None

    # tlist 안의 turtle 중에서 가장 가까운 turtle의 color를 'red'로 변경
    for t in tlist:
        t.color('black')
        
        dist = calc_dist( (x, y), t )

        if min_dist == None:
            min_dist = dist
            min_turtle = t
        elif min_dist > dist:
            min_dist = dist
            min_turtle = t

        print(t.position()) # 모든 터틀의 위치를 프린트

    if min_turtle:
        min_turtle.color('red')

    # 마지막에 update 필요
    turtle.update()


turtle.setup(700, 700)
turtle.tracer(0, 0)
screen = turtle.Screen()

tlist = []

for i in range(10):
    t = turtle.Turtle()
    t.penup()
    t.shape('circle')
    t.setposition( random.random()*600 -300, random.random()*600 -300 )
    tlist.append(t)

turtle.update()
screen.onclick(on_click)
turtle.listen()
turtle.done()


