# With python version 3.9.0

# 문제 2 시작
# 다음과 같은 기능을 가지는 TV 클래스를 구현하여라. 그리고 이클래스를 이용하여 인스턴스를 생성하여라.
# 이 클래스는 다음과 같은 속성과 메소드를 가진다.


class TV:
    # 클래스 변수
    MIN_VOLUME = 0
    MAX_VOLUME = 20
    MIN_CHANNEL = 0
    MAX_CHANNEL = 200

    # 디폴트 볼륨 값은 5, 디폴트 채널 값은 0 값을 가지면 꺼짐 상태가 기본 상태
    def __init__(self):
        # 인스턴스 변수
        self.__volume = 5
        self.__channel = 0
        self.__is_on = False

    # 볼륨, 채널 상태를 문자열로 반환, TV가 꺼짐 상태일 경우 "TV가 꺼짐 상태입니다"를 반환
    def __str__(self):
        return ("TV가 꺼짐 상태입니다\n" if not self.__is_on else "") + "볼륨 : {}, 채널 = {}".format(self.get_volume(), self.get_channel())

    # TV가 켜짐 상태이면 꺼짐 상태로, 꺼짐 상태이면 켜짐 상태로 변환하는 기능
    def toggle_power(self):
        self.__is_on = not self.__is_on

    # 채널 값을 반환하는 메소드
    def get_channel(self):
        return self.__channel

    # 채널 값을 choice 값으로 설정하는 메소드
    # 이 때, choice 값이 0에서 201사이의 값이 아닐 경우, "채널 오류"를 출력함
    def set_channel(self, choice):
        if choice < TV.MIN_CHANNEL or choice > TV.MAX_CHANNEL:
            return print("채널 오류")

        self.__channel = choice

    # 볼륨 값을 반환하는 메소드
    def get_volume(self):
        return self.__volume

    # 볼륨 값을 choice 값으로 설정하는 메소드
    # 이 때, choice 값이 0에서 21사이의 값이 아닐 경우, "볼륨 오류"를 출력함
    def set_volume(self, choice):
        if choice < TV.MIN_VOLUME or choice > TV.MAX_VOLUME:
            return print("볼륨 오류")

        self.__volume = choice

    # 볼륨 값을 1 증가시키는 메소드로 최댓값은 MAX_VOLUME
    def volume_up(self):
        if (self.get_volume() < TV.MAX_VOLUME):
            self.set_volume(self.get_volume() + 1)

    # 볼륨 값을 1 감소시키는 메소드로 최솟값은 MIN_VOLUME
    def volume_down(self):
        if (self.get_volume() > TV.MIN_VOLUME):
            self.set_volume(self.get_volume() - 1)

    # 채널 값을 1 증가시키는 메소드로 201 이상이 될 경우 MIN_CHANNEL(0)이 됨
    def channel_up(self):
        if (self.get_channel() < TV.MAX_CHANNEL):
            self.set_channel(self.get_channel() + 1)
        else:
            self.set_channel(TV.MIN_CHANNEL)

    # 채널 값을 1 감소시키는 메소드로 0 이하가 될 경우 MAX_CHANNEL(200)이 됨
    def channel_down(self):
        if (self.get_channel() > TV.MIN_CHANNEL):
            self.set_channel(self.get_channel() - 1)
        else:
            self.set_channel(TV.MAX_CHANNEL)


# TV라는 클래스를 만든 후 my_tv라는 인스턴스를 생성하고 메소드 호출과 출력을 통해 다음과 같은 실행 결과를 출력하라.
# 호출 메소드 : toggle_power(), set_channel(), volume_up(), channel_up()
print("\n------------------------------------------")
print("문제 2, 실행결과")
print("------------------------------------------")
my_tv = TV()
print(my_tv.__str__())
my_tv.toggle_power()
my_tv.set_channel(45)
print(my_tv.__str__())
my_tv.volume_up()
my_tv.channel_up()
print(my_tv.__str__())
