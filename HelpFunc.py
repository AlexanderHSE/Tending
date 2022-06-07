class HelpFunc:
    @staticmethod
    def Input_number(min, max):
        while True:
            try:
                num = int(input())
                if (num >= min) and num <= max:
                    return num
            except ValueError:
                pass
