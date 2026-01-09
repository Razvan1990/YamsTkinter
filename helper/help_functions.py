class Helper:

    def __init__(self):
        self.threshold = 63
        self.threshold_plus_10 = 123
        self.line_ok = 50

    def calculate_totals(self, row_number, *args) -> int:
        '''

        :param row_number: if servita -> need to double
        :param args: will be in fact the values of each entry
        :return: the result based on the yams calculation
        '''
        result = 0
        calculation = 0
        for arg in args:
            calculation+=arg
        if row_number == 5 or row_number == 10:
            if calculation < self.threshold:
                result = calculation * 2
            else:
                result = calculation + self.line_ok
                if result >= self.threshold_plus_10:
                    result = (calculation + self.line_ok + 10) * 2
                else:
                    result = (calculation + self.line_ok) * 2
        else:
            if calculation < self.threshold:
                result = calculation
            else:
                result = (calculation + self.line_ok)
                if result >= self.threshold_plus_10:
                    result = (result + 10)
        return result

    def calculate_totals_bs(self, row_number, big, small) -> int:
        result = 0
        if row_number == 5 or row_number == 10:
            result = (big -small) * 2
        else:
            result = big - small
        return result

    def calculate_full(self, dice1, dice2) -> tuple[int, int, int]:
        '''
        :param dice1: dice which appears 3 times
        :param dice2: dice which appears 2 times
        :return: full calculation normal, full calculation+10, full calculation served
        '''
        result_normal = (3 * int(dice1) + 2 * int(dice2)) + 10
        result_extra_10 = (3 * int(dice1) + 2 * int(dice2)) + 20
        result_served = ((3 * int(dice1) + 2 * int(dice2)) + 10) * 2
        return result_normal, result_extra_10, result_served

    def calculate_4_of_a_kind(self, dice1) -> tuple[int, int, int]:
        '''
        :param dice1: dice which appears 4 times
        :return: careu calculation normal, careu calculation+10, careu calculation served
        '''
        result_normal = (4 * int(dice1)) + 20
        result_extra_10 = (4 * int(dice1)) + 30
        result_served = ((4 * int(dice1)) + 20) * 2
        return result_normal, result_extra_10, result_served

    def calculate_yams(self, dice1) ->tuple[int, int, int]:
        '''
        :param dice1: dice which appears 5 times
        :return: yams calculation normal, yams calculation+10, yams calculation served
        '''
        result_normal = (5 * int(dice1)) + 70
        result_extra_10 = (5 * int(dice1)) + 80
        result_served = ((5 * int(dice1)) + 70) * 2
        return result_normal, result_extra_10, result_served
