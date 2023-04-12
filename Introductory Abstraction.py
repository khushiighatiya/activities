#Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)

a=int(input())
b=int(input())
def add(a,b):
    k=a+b
    return k
print("Addition:",add(a,b))
.
.
#Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3)

n=float(input("celsius: "))
def fahreniet(n):
    convert=(n*9/5)+32
    return convert
print(fahreniet(n),"fahreniet")
.
.
#Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)

def Earthquake(range):
    if range<=0:
        print("No Earthquake")
    elif range>0 and range<3:
        print("Micro Earthquake")
    elif range>=3 and range<5:
        print("Minor Earthquake")
    elif range>=5 and range<7:
        print("Moderate Earthquake")
    elif range>=7 and range<8:
        print("Strong Earthquake")
    elif range>=8 and range<9:
        print("Major Earthquake")
    else:
        print("Great Earthquake")
print(Earthquake(5))
.
.
#Factor:  Calculate temperature that a person feels because of the wind (Python3)

air_temp=float(input('Air temperature in celsius: '))
v=float(input('wind speed in km/h: '))
def chill_wind(air_temp,v):
    Temperature=13.12 + 0.6215 * T_a * (0.3965 * T_a - 11.37) * (v**0.16)
    return Temperature
print(chill_wind(air_temp,v),"deg celsius")
