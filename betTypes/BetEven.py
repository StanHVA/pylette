from BetType import BetType


class BetEven(BetType):
    def multiplier(self):
        return 2

    def bet_success(self, number):
        if number == '0' or number == '00':
            return False
        return int(number) % 2 == 0

    def description(self):
        return 'The even numbers'
