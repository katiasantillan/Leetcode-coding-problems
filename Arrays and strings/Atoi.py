class Solution:
    def myAtoi(self, str: str) -> int:

        number = []
        flag = 0
        signo = 0
        for i in str:
            if (i == ' ' and flag == 0):
                continue
            elif((i == '-' and signo == 0) or (i == '+' and signo == 0) or i.isnumeric()):
                flag = 1
                signo+=1  
                number.append(i)
            else:
                break
    
        if(number):
            try:
                n = int(('').join(number))

                if(abs(n) <= (2**31) -1):
                    return(n)
                else:
                    if(n<0):
                        return(-2**31)
                    else:
                        return(2**31-1)
            except:
                return 0
        else:
            return 0
