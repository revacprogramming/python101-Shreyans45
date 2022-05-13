hrs = float(input("Enter Hours:"))
a=float(40)
diff=hrs-a
if (hrs > a):
    grass=40*10.5+(diff*10.5)*1.5
    print(grass)
else :
    grass=(hrs)*1.5
    print(grass)
