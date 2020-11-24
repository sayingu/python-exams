# With python version 3.9.0

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
