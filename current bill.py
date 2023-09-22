units=int(input("please enter number of units you consumed:"))
if(units<50):
    amount=units*2.60
    subcharge=25
elif(units<=100):
    amount=130+(units-50)*3.25
    subcharge=35
elif(units<=200):
    amount=130+50*3.25+(units-100)*5.26
    subcharge=45
else:
    amount=130+50*3.25+100*5.26+(units-200)*8.45
    subcharge=75
total=amount+subcharge
print("\n electricity bill =",total)
