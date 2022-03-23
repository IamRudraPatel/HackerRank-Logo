n = int(input("Enter The ThickNess: "))
C = "H"
temp = (n-1)//2
# TOP PRYAMID
j = 1
for i in range (n-1,-1,-1):
    print((i*" ")+(j*C))
    j=j+2
# Upper Part Of H
for i in range(n+1):
    noOfH = C*n
    print((noOfH.rjust((n+temp),' '))+(noOfH.rjust(len(noOfH)+n*3," ")))
# Middle Part Of H
noOfIteration = n-temp
for i in range(noOfIteration):
    numberofH = C*(n*5)
    print(numberofH.rjust(len(numberofH)+temp," "))
# Lower Part Of H
for i in range(n+1):
    noOfH = C*n
    print((noOfH.rjust((n+temp),' '))+(noOfH.rjust(len(noOfH)+n*3," ")))
# BOTTOM PRYAMID
frontspace = n*4
temp1 = n-1
for i in range(n):
    temp2 = (n+temp1)*C
    print(temp2.rjust(len(temp2)+frontspace," "))
    n-=2
    frontspace+=1