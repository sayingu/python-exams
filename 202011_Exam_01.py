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
