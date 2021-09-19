class RomanNumerals:
    @staticmethod
    def to_roman(numeral):
        roman = ''
        digits = str(numeral)
        if len(digits) == 4:
            # position 1
            roman += ''.join('M' * (numeral // 1000))
            # position 2
            # if digit is between 5 and 9
            if '5' <= digits[2] <= '9':

            # or digit between 0 and 4



        print(roman)

    @staticmethod
    def from_roman(numeral):
        pass


RomanNumerals.to_roman(1990)
