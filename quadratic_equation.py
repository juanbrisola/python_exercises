from math import sqrt

print ("Calculating a quadratic equation")

#receiving values from user
a = float(input("enter the first value: "))
b = float(input("enter the second value: "))
c = float(input("enter the third value: "))

#calculating delta
delta = b**2 - 4*a*c

#calculating results from equation
x1 = (-b + sqrt(delta))/(2*a)
x2 = (-b - sqrt(delta))/(2*a)

print ("Here are your results!")
print ("x¹ = %f" %x1)
print ("x² = %f" %x2)