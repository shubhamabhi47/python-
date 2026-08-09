def prime(n , i):
    if i==1:
        return 1
    if n%i==0:
        return 0
    else:
        return prime(n,i-1)
            

   
n = int(input("Enter a number to check prime:"))   
rs = prime(n , n-1)

if rs==1:
    print(f"{n} is prime number.")
if rs==0:
    print(f"{n} is not a prime number.")
    
    