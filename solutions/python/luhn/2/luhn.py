class Luhn:
    def __init__(self, card_num):
        # remove spaces 
        self.card_num = card_num.split(" ")
        self.card_num = "".join(self.card_num)
        # reverse the number
        self.reverse_num = self.card_num[::-1]
        # get the length
        self.length = len(self.reverse_num)
        # add a list of digits to check for validity of card_num later
        self.digits = [str(ii) for ii in range(10)]

    def valid_prelim(self):
        if len(self.card_num) <= 1:
            return False
        for part in self.card_num:
            if part not in self.digits:
                return False 
        return True

    def valid(self):
        if self.valid_prelim():
            result = []
            for ii in range(self.length):
                part = int(self.reverse_num[ii])
                if ii % 2 != 0:
                    part *= 2
                    if part > 9:
                        part -= 9
                result.append(part)
            return (sum(result) % 10 == 0)
        else:
            return False
