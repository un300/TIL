

class PrintHello:
    def say_hello(self):
        print('반갑습니다! 모듈을 연습 중 이에요!')


class MakeSquared:
    def __init__(self, num):
        self.num = num

    def squared(self):
        return self.num**2
