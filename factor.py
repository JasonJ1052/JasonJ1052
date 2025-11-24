def gcd(m,n):
    i=0
    print(f"{'i':>3}|{'q':>4}{'m':>4}{'n':>4}{'r':>4}")
    print("-"*25)
    while n:
        q=m//n
        r=m%n
        print(f"{i:>3}|{q:>4}{m:>4}{n:>4}{r:>4}")
        m=n
        n=r
        i+=1
    print(f"{i:>3}|{'':>4}{m:>4}{n:>4}{'STOP':>4}")
    return m


a=int(input("Enter a number:"))
b=int(input("Enter a second number:"))
print(gcd(a,b))
print("#######")
print(gcd(4,7))

x=0
while True:
    x+=1
    if x%2==0:
        if x%3==0:
            if x%4==0:
                if x%5==0:
                    if x%6==0:
                        if x%7==0:
                            if x%8==0:
                                if x%9==0:
                                    if x%10==0:
                                        if x% 11==0:
                                            if x%12==0:
                                                print(x)
                                                break