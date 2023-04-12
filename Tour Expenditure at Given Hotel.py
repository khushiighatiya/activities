def trip(Delux_Room,days,amount_food):
    if Delux_Room == True:
        room_t=7500*days
        tax=0.18*amount_food
    elif Delux_Room==False:
        room_t=4500*days
        tax=0.05*amount_food
    tip=0.1*amount_food
    cgst=tax/2
    sgst=tax/2
    total=room_t+tax+amount_food+tip
    print("room_t: INR",round(room_t,2))
    print("GST-CGST=INR",round(cgst,2),"SGST=INR",round(sgst,2))
    print("Tip: INR",round(tip,2))
    print("Grand Total: INR",round(total,2))
    
A=trip(True,6,15000)
