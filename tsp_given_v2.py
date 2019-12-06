
import turtle
import requests
import json
import time, threading
import math, random

# class ID constants
SWP01, SWP02 = 'swp01', 'swp02'

################################################################################
# IMPORTANT: replace all with your information
# you can set CLASS_ID as 
#     SWP01 (Tuesday 5,6)
#     SWP02 (Tuesday 7,8)
################################################################################
STUDENT_ID = '215545554' # Edit this
STUDENT_NAME = '김연세' # Edit this
STUDENT_NICKNAME = '김연세' # Edit this
CLASS_ID = SWP02 # Edit this
AUTH_TOKEN = '0000000000'
################################################################################

TSP_URL = 'https://chw4ei9oh7.execute-api.ap-northeast-2.amazonaws.com/live/update-tsp-path'

class TSP:

    def __init__(self, sid, sname, snickname, cid, auth):

        # validate student id
        if STUDENT_ID == '2018123456':
            print('\n\nInvalid STUDENT_ID!')

        # student info
        self.sid = sid
        self.sname = sname
        self.snickname = snickname
        self.cid = cid
        self.auth = auth

        # screen dimension
        self.swidth = 1000
        self.sheight = 500
        self.margin = 100

        # init turtle module
        self.screen = turtle.Screen()
        turtle.setup( self.swidth + self.margin*2, self.sheight + self.margin*2 )
        turtle.tracer(0, 0)

        # a tutle for drawing nodes
        self.turtle_node = turtle.Turtle()
        self.turtle_node.shape('circle')
        self.turtle_node.color('navy')
        self.turtle_node.shapesize(0.4)
        self.turtle_node.penup()
        self.turtle_node.ht()

        # a tutle for drawing paths
        self.turtle_path = turtle.Turtle()
        self.turtle_path.color('green')
        self.turtle_path.ht()

        # a tutle for drawing texts
        self.turtle_text = turtle.Turtle()
        self.turtle_text.ht()
        self.turtle_text.penup()

        # texts
        self.title_text = 'Traveling Salesman Problem'
        self.name_text = '{} {} ({})'.format(self.sid, self.sname, self.snickname)
        self.status_text = ''
        self.menu_text = 'Key: (1) Random (2) Greedy (3) 2-Opt (Q) QUIT'

        # init path
        self.path = []
        self.path_length = 0
        self.path_to_be_uploaded = None
        
        # draw timer
        self.upload_timer = 0
        self.draw_timer = 0

        # initialize nodes
        self.download_from_server()

        # initial drawing
        self.draw()
        self.write_texts()


    # Random Algorithm
    def make_random_path(self):
        
        # 모든 도시의 인덱스를 가지고 있는 임시 경로(result)를 생성
        # 모든 도시의 갯수: len(self.nodes)
        result = [node[0] for node in self.nodes] # EDIT THIS

        # 경로를 뒤섞음 (shuffle)
        random.shuffle(result) # EDIT THIS

        # 첫 도시 인덱스를 경로의 맨 뒤에 추가하여 경로를 닫음
        result.append( result[0] )

        # 완성된 임시 경로를 현재 경로로 저장
        self.set_new_path( result, 'Random Algorithm' )


    # Greedy Algorithm
    def make_greedy_path(self):

        # 모든 도시의 인덱스를 가지고 있는 pool 리스트 생성
        pool = list(range(len(self.nodes)))

        # 비어있는 임시 경로(result) 준비
        result = []
        
        # pool에서 꺼낸 도시 인덱스 하나를 result에 추가
        # EDIT THIS
        result.append(pool.pop(0))

        # 남아있는 도시가 하나라도 있다면 계속 반복
        while len( pool ) > 0:

            # min_dist 와 min_index 초기화
            min_dist = None
            min_index = None

            # 현재 남아있는 pool안의 모든 도시에 대하여...
            # (도시의 인덱스는 pool[i]로 가져올 수 있음)
            for i in range(len(pool)):
                
                # result에서 가장 최근 추가된 도시의 인덱스를 n1로 가져옴
                n1 = result[len(result) - 1] # EDIT THIS

                # pool 안에 남아있는 도시의 중 하나를 가져옴
                n2 = pool[i] # EDIT THIS

                # self.calc_dist() 를 이용하여 거리를 계산 
                dist = self.calc_dist(n1, n2)

                # 만약 dist가 min_dist보다 작다면 
                # EDIT THIS
                    # min_dist 와 min_index를 갱신
                    # EDIT THIS
                    # EDIT THIS
                if min_dist is None or dist < min_dist:
                    min_dist = dist
                    min_index = i

            # 이제 min_index를 발견했으므로
            # pool의 min_index 를 꺼내서 result에 추가
            result.append(pool.pop(min_index)) # EDIT THIS


        # append the first node index to the last
        result.append( result[0] )

        # update with a new path
        self.set_new_path( result, 'Greedy Algorithm' )


    # 2-Opt Algorithm
    def make_2opt_path(self):

        # 무작위 경로 하나를 완성
        # self.make_random_path()
        self.make_greedy_path()

        # 100 번 반복
        for i in range(500):
            
            # 경로의 두 지점을 무작위로 선택 (슬라이드 참고)
            i = 0 # EDIT THIS
            k = 0 # EDIT THIS
            j = random.randint(1, len(self.path)-2)
            k = random.randint(j, len(self.path)-2)

            # 3개의 세그먼트로 분할 (path1, path2, path3)
            # 현재 경로에서 슬라이스를 얻는 방법: self.path[x:y]
            path1 = []  # EDIT THIS
            path2 = []  # EDIT THIS
            path3 = []  # EDIT THIS
            path1 = self.path[:j]
            path2 = self.path[j:k]
            path3 = self.path[k:]

            # path2만 뒤집은 채 다시 결합 ( path1 + path2* + path3 )
            result = []  # EDIT THIS
            path2.reverse()
            result = path1 + path2 + path3

            # 만약 변경된 경로(result)가 기존(self.path)보다 줄어들었다면,
            if False:  # EDIT THIS
                # 변경된 경로를 현재 경로로 저장
                self.set_new_path( result, '2-Opt Algorithm' )
            pathLenth = self.calc_path_length(self.path)
            if pathLenth > self.calc_path_length(result):
                self.set_new_path( result, '2-Opt Algorithm' )


    # Draw nodes and the path
    def draw(self):
        
        # clear drawings
        self.turtle_node.clear()
        self.turtle_path.clear()

        # draw nodes
        for node in self.nodes:
            self.turtle_node.setposition( node[1], node[2] )
            self.turtle_node.color('black')
            self.turtle_node.stamp()
            self.turtle_node.color('blue')

        # draw the path
        is_first = True
        for index in self.path:
            node = self.nodes[index]

            if is_first:
                self.turtle_path.penup()
                is_first = False
            else:
                self.turtle_path.pendown()

            self.turtle_path.setposition( node[1], node[2] )


    # Draw status text
    def write_texts(self):

        # clear drawings
        self.turtle_text.clear()

        # title text
        self.turtle_text.color('gray')
        self.turtle_text.setposition( 0, self.sheight/2 + 60)
        self.turtle_text.write( '{}'.format(self.title_text) , align='center', font=('Helvetica', 22, 'bold') )
        # name text
        self.turtle_text.color('gray')
        self.turtle_text.setposition( self.swidth/2, self.sheight/2 + 30)
        self.turtle_text.write( '{}'.format(self.name_text) , align='right', font=('Helvetica', 16, 'bold') )
        # path status text
        self.turtle_text.color('green')
        self.turtle_text.setposition( 0, self.sheight/2 + 40)
        self.turtle_text.write( '{}'.format(self.status_text) , align='center', font=('Helvetica', 16, 'bold') )
        # menu text
        self.turtle_text.color('gray')
        self.turtle_text.setposition( self.swidth/2, -self.sheight/2 - 60 )
        self.turtle_text.write( '{}'.format(self.menu_text) , align='right', font=('Helvetica', 16, 'bold') )

    # Main update loop (dt - delta time)
    def update(self, dt):

        # main drawing
        if self.draw_timer >= 0.3:
            self.draw()
            turtle.update()
            self.draw_timer -= 0.3

        self.draw_timer += dt
        self.upload_timer += dt

        # uploading
        self.upload_to_server()

    # return a distance between nodes
    def calc_dist(self, i1, i2):
        node1 = self.nodes[i1]
        node2 = self.nodes[i2]
        return math.sqrt( (node1[1] - node2[1]) **2 + (node1[2] - node2[2]) **2 )

    # return a total travel length of the path
    def calc_path_length(self, path1):
        plen = 0
        for i in range(len(path1)):
            if i > 0:
                plen += self.calc_dist( path1[i-1], path1[i] )

        return plen

    # update with a new path
    def set_new_path(self, path, method_text='UNNAMED'):

        # self.path = path.copy()
        self.path = path[:]
        self.path_length = self.calc_path_length(self.path)
        # self.path_to_be_uploaded = self.path.copy()
        self.path_to_be_uploaded = self.path[:]

        self.method_text = method_text
        self.status_text = '{} - travel length = {:.2f}m'.format(self.method_text, self.path_length)        
        self.write_texts()

    # download from the TSP server - DO NOT MODIFY
    def download_from_server(self):

        params = {'get_nodes': 1}
        r = requests.get(TSP_URL, params)

        try:

            raw_nodes = json.loads( r.text )

            self.nodes = []

            for node in raw_nodes:
                node[1] = node[1] - self.swidth/2
                node[2] = node[2] - self.sheight/2
                self.nodes.append(node)

            if r.status_code == 200:
                print('{} nodes downloaded'.format(len(self.nodes)))
                print('self.nodes = ', self.nodes)
            else:
                print('ERROR({}): Could not download from the TSP server'.format(r.status_code))
                quit()
        except:
            pass

    # upload to the TSP server - DO NOT MODIFY
    def upload_to_server(self):

        if self.path_to_be_uploaded:

            if self.upload_timer < 1:
                return

            params = {'update_path': 1, 'sid': self.sid, 'name': self.sname, 'nickname': self.snickname, 'cid': self.cid, 'auth': self.auth, 'path': json.dumps(self.path) }

            r = requests.get(TSP_URL, params)

            try:
                result = json.loads( r.text )

                if r.status_code == 200:
                    print('You uploaded a new path ({} - travel length {:.2f}):\n  🏁 {} 🏁'.format( self.method_text, result.get('dist'), self.path ) )
                else:
                    print('ERROR({}): Could not update the path'.format(r.status_code))
            except:
                pass


            self.upload_timer = 0
            self.path_to_be_uploaded = None



# start time - global variable
st = 0

# key down evnet functions
def key_down_1():
    tsp.make_random_path()

def key_down_2():
    tsp.make_greedy_path()

def key_down_3():
    tsp.make_2opt_path()

def key_down_q():
    exit()

# main timer event function
def on_timer_event():
    global st

    et = time.time()
    dt = et - st
    tsp.update(dt)
    tsp.screen.ontimer( on_timer_event, 50 )

    st = et

# instantiate a TSP object
tsp = TSP(STUDENT_ID, STUDENT_NAME, STUDENT_NICKNAME, CLASS_ID, AUTH_TOKEN)

# register event functions
tsp.screen.onkey( key_down_1, '1' )
tsp.screen.onkey( key_down_2, '2' )
tsp.screen.onkey( key_down_3, '3' )
tsp.screen.onkey( key_down_q, 'q' )
tsp.screen.ontimer( on_timer_event, 50 )
tsp.screen.listen()

turtle.done()

