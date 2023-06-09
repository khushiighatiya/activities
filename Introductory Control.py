"""Problem Statement- II
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2"""

Nint=28
Divisor=0
for Div in range(1,Nint):
    if Nint % Div==0:
        Divisor+=Div
if Divisor>Nint:
    print(Nint,"is_abundant")
elif Divisor<Nint:
    print(Nint,"is_deficient")
else:
    print(Nint,"is_perfect")
