#Muhammad Furqan Elahi
#PY-108
print("Marksheet")
a=int(input("Marks in Robotics              : "))
b=int(input("Marks in Embedded Systems      : "))
c=int(input("Marks in Wireless Communication: "))
d=int(input("Marks in Industrial Electronics: "))
per=100*(a+b+c+d)//400
print(per)
if per <95 and per>= 90:
    print("A one Grade")
elif per<90 and per >= 85:
    print("A Grade")
elif per<85 and per>= 80:
    print("B Grade")
elif per <80 and per>= 70:
    print("C Grade")
else :
    print("Sorry You're Fail.")
    