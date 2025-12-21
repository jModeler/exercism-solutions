from string import punctuation, whitespace, ascii_letters
class PhoneNumber:
    def __init__(self, number):
        self.raw_number = number
        self.clean_number()
        self.get_area_code()
    
    def clean_number(self):
        self.number = self.raw_number.translate(str.maketrans('', '', '()-.+' + whitespace))
        # sense check block
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(self.number) == 11 and self.number[0] != "1":
            raise ValueError("11 digits must start with 1")
        else:
            # check for letters               
            self.check_characters(0)
            # check for punctuation
            self.check_characters(1)
        # legit number check block
        # remove the country code
        if len(self.number) == 11:
                self.number = self.number[1:]
        if int(self.number[0]) < 2:
            if int(self.number[0]) == 0:
                raise ValueError("area code cannot start with zero")
            else: 
                raise ValueError("area code cannot start with one")
        else:
            # do the remaining checks
            if int(self.number[3]) < 2:
                if int(self.number[3]) == 0:
                    raise ValueError("exchange code cannot start with zero")
                else: 
                    raise ValueError("exchange code cannot start with one")


    def check_characters(self, character_flag = 0):
        # 0 checks for letters, any other value for punctuations
        for char in self.number:
            if character_flag == 0:
                if char in ascii_letters:
                    raise ValueError("letters not permitted")
            else:
                if char in punctuation:
                    raise ValueError("punctuations not permitted")               
            
    def get_area_code(self):
        self.area_code = self.number[0:3]
    
    def pretty(self):
        result = ""
        # add area code
        result = "".join(["(", self.area_code, ")"])
        # add the rest
        result = "-".join([result, self.number[3:6], self.number[6:]])
        return result