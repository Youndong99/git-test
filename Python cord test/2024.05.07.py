
# (A+B)%C는 ((A%C)+(B%C))%C 와 같을까?
# (A*B)%C는 ((A%C)*(B%C))%C 와 같을까?
# 세 수 A,B,C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오
# 첫째 줄에 A,B,C가 순서대로 주어진다. (2<=A,B,C<=10000)

A=int(input('2<=A<=10000'))
B=int(input('2<=B<=10000'))
C=int(input('2<=C<=10000'))

print((A+B)%C)
print((A%C)+(B%C)%C)
print((A*B)%C)
print((A%C)*(B%C)%C)


if A,B,C=int(input('2<=A,B,C<=10000')):
             print(((A%C)+(B%C)%C)=((A%C)*(B%C)%C))
            
A, B, C = map(int, input("Enter three integers A, B, C where 2 <= A, B, C <= 10000: ").split())

# Check if the equation is true
if ((A % C) + (B % C)) % C == ((A % C) * (B % C)) % C:
    print("True")
else:
    
    print("False")
