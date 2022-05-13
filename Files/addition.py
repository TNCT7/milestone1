class NumberError(Exception):
    pass


class Addition:

    def add(self,num1):
        num11 = 0
        for i in range(len(num1)):
            j = int(num1[i])
            num11 = num11 + j
        return  num11

    def sub(self,num1,num2):
        if num1 < 0:
            raise NumberError(f"{num1} is a negative number")
        elif num2 < 0:
            raise NumberError(f"{num2} is a negative number")
        else:
            return num1 - num2

    def mul(self, num1,num2):
        return num1 * num2

    def div(self,num1,num2):
        if num2 ==0:
            raise NumberError(f"{num2} cannot be 0")
        else:
            return num1/num2
