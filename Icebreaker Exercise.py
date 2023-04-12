"""Icebreaker Exercise

Problem -I 
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum."""

n=int(input("enter range: "))
if n>=380 and n<450:
    print("VIOLET")
elif n>=450 and n<495:
    print("BLUE")
elif n>=495 and n<570:
    print("GREEN")
elif n>=570 and n<590:
    print("YELLOW")
elif n>=590 and n<620:
    print("ORANGE")
elif n>=620 and n<750:
    print("RED")
else:
    print("invaild")
 .
 .
 .
 .
 
"""Problem -II
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more

Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message."""

n=int(input("frequency: "))
if n<3000000000:
    print("RADIO WAVES")
elif n>=3000000000 and n<3000000000000:
    print("MICROWAVES")
elif n>=3000000000000 and n<430000000000000:
    print("INFRARED LIGHT")
elif n>=430000000000000 and n<750000000000000:
    print("VISIBLE LIGHT")
elif n>=750000000000000 and n<300000000000000000:
    print("ULTRANIOLET LIGHT")
elif n>=300000000000000000 and n<30000000000000000000:
    print("X-RAYS")
elif n>=30000000000000000000:
    print("GAMMA RAYS")
else:
    print("INVALID")
 
