def  is_palindrome ( num ):
    temp = num
    total =  0 
    while temp >  0 :
        total = total *  10  + temp %  10 
        temp //=  10 
    return total == num

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        else:
            return True



if __name__ == '__main__':
    num =  int ( input ( '請輸入正整數: ' ))
    if is_palindrome(num) and is_prime(num):
        print("%d是回文質數"% num)
    else:
        print("什麼都不是")


