##for i in range(input()):
n=input()
ten=n/10
#print 'ten',ten
ten_rem=n%10
five= ten_rem/5
#print 'five',five
five_rem=ten_rem%5
one= five_rem/1
#print 'one',one
print sum((ten,five,one))
