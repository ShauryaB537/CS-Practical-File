def hcf(a,b):
    n=min(a,b)
    i=1
    while i<=n:
        if a%i==0 and b%i==0:
            k=i
        else:
            pass
        i=i+1
    return(k)

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

print(f"\nThe HCF of {n1} & {n2} is: {hcf(n1,n2)}")
