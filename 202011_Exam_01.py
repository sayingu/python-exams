# With python version 3.9.0

# 문제 1 시작
# 다음과 같은 기능을 가지는 Student라는 학생 클래스를 구현하여라.
# 이 학생은 국어, 수학, 과학 교과목에 대하여 시험을 치고 그 점수를 입력 받는다고 가정하자.
# 그리고 이 클래스를 이용하여 인스턴스를 생성하여라. 이 클래스는 다음과 같은 속성과 메소드를 가진다.

class Student:
    # 학생의 이름. 학번으로 초기화. 국어, 수학, 과학 점수는 디폴트로 0의 값을 가짐
    def __init__(self, name, student_id):
        # 인스턴스 변수
        # 학생의 이름이 문자열 형으로 저장
        self.__name = name

        # 학번과 같은 8자리 문자열 형으로 저장
        self.__student_id = student_id

        # 학생의 국어 퀴즈 점수로 정수형으로 저장
        self.__korean_quiz = 0

        # 학생의 수학 퀴즈 점수로 정수형으로 저장
        self.__math_quiz = 0

        # 학생의 과학 퀴즈 점수로 정수형으로 저장
        self.__science_quiz = 0

        # 학생의 퀴즈 점수의 합계
        self.__total_score = 0

    # 학생의 이름, 학번, 점수, 점수의 합, 평균을 문자열로 반환함
    def __str__(self):
        return "이름 : {}, 학번 : {}\n국어 성적 : {}, 수학 성적 : {}, 과학 성적 : {}\n합계 : {}, 평균 : {}".format(self.get_name(), self.get_student_id(), self.get_korean_quiz(), self.get_math_quiz(), self.get_science_quiz(), self.get_total_score(), self.get_avg_score())

    # 이름을 반환하는 메소드
    def get_name(self):
        return self.__name

    # 학생의 학번을 반환하는 메소드
    def get_student_id(self):
        return self.__student_id

    # 학생의 국어 시험 점수를 반환하는 메소드
    def get_korean_quiz(self):
        return self.__korean_quiz

    # 학생의 수학 시험 점수를 반환하는 메소드
    def get_math_quiz(self):
        return self.__math_quiz

    # 학생의 과학 시험 점수를 반환하는 메소드
    def get_science_quiz(self):
        return self.__science_quiz

    # 학생의 국어 시험 점수를 설정하는 메소드
    def set_korean_quiz(self, korean_quiz):
        self.__korean_quiz = int(korean_quiz)

    # 학생의 수학 시험 점수를 설정하는 메소드
    def set_math_quiz(self, math_quiz):
        self.__math_quiz = int(math_quiz)

    # 학생의 과학 시험 점수를 설정하는 메소드
    def set_science_quiz(self, science_quiz):
        self.__science_quiz = int(science_quiz)

    def get_score_list(self):
        return [self.get_korean_quiz(), self.get_math_quiz(), self.get_science_quiz()]

    # 학생의 전체 시험 점수를 반환하는 메소드
    def get_total_score(self):
        return sum(self.get_score_list())

    # 학생의 시험 점수의 평균을 반환하는 메소드
    def get_avg_score(self):
        return round(sum(self.get_score_list()) / len(self.get_score_list()), 1)


# Student라는 클래스를 만든 후 student이라는 학생 인스턴스를 생성하고 사용자로부터 이름, 학번을 입력 받은 후, 국어, 수학, 과학 점수를 입력 받아라.
print("------------------------------------------")
print("문제 1, 실행결과")
print("------------------------------------------")
name = input("학생의 이름을 입력하세요 : ")
student_id = input("학생의 학번을 입력하세요 : ")
student = Student(name, student_id)
student.set_korean_quiz(input("학생의 국어 성적을 입력하세요 : "))
student.set_math_quiz(input("학생의 수학 성적을 입력하세요 : "))
student.set_science_quiz(input("학생의 과학 성적을 입력하세요 : "))
print(student.__str__())

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

# 문제 3 시작
# 다음과 같은 기능을 가지는 은행계좌 클래스 BankAccount 클래스를 구현하여라.
# 그리고 이 클래스를 이용하여 인스턴스를 생성하여라.
# 이 클래스는 다음과 같은 속성과 메소드를 가진다.


class BankAccount:
    # 계좌 주인의 이름, 계좌번호, 최초 잔액으로 BankAccount를 초기화 함
    def __init__(self, name, account_num, balance):
        self.__name = name
        self.__account_num = account_num
        self.__balance = balance

    # 계좌 주인의 이름, 계좌번호, 잔액을 문자열로 반환함
    def __str__(self):
        return "{}님의 계좌 {}의 잔고는 {}원입니다.".format(self.get_name(), self.get_account_num(), self.get_balance())

    # 이름을 반환하는 메소드
    def get_name(self):
        return self.__name

    # 계좌번호를 반환하는 메소드
    def get_account_num(self):
        return self.__account_num

    # 계좌 잔액을 반환하는 메소드
    def get_balance(self):
        return self.__balance

    # amount 만큼의 돈을 balance에 추가함
    def deposit(self, money):
        self.__balance += money
        print("{}원이 입금되었습니다. 잔고는 {}원 입니다.".format(money, self.get_balance()))

    # amount 만큼의 돈이 balance에서 빠져나감. 만일 amount가 money보다 작으면 계좌 잔액과 인출 요구금액을 출력하고 출금이 되지 않음
    def withdraw(self, money):
        if (self.get_balance() < money):
            print("계좌 잔고는 {}원으로 인출 요구 금액 {}원보다 작습니다.".format(
                self.get_balance(), money))
        else:
            self.__balance -= money


# BankAccount라는 클래스를 만든 후 account1라는 계좌를 생성하고 2000원을 입금하여라.
# 이 계좌 정보를 출력한 후 500원을 출금한 후 계좌 정보를 출력하여라. 마지막으로 5000원을 출금하여라.
print("\n------------------------------------------")
print("문제 3, 실행결과")
print("------------------------------------------")
account1 = BankAccount("홍길동", "1234-0001", 0)
print(account1.__str__())
account1.deposit(2000)
print(account1.__str__())
account1.withdraw(500)
print(account1.__str__())
account1.withdraw(5000)
