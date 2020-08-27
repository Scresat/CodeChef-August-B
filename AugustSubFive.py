def power(a_, b_, mod) : 
    answer_ = 1     
    a_ = a_ % mod  
    if (a_ == 0) : 
        return 0
  
    while b_ > 0:
        if b_ & 1 == 1: 
            answer_ = (answer_ * a_) % mod 
        b_ = b_ >> 1 
        a_ = (a_ * a_) % mod 
          
    return answer_  
  
def program():
    n = int(input())
    z = input()
    for i in range(n-1, 0, -1):
        print(str(power(2, i, 1000000007)), end = ' ') 
    print(1)

 
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()