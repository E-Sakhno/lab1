x=int(input("Input the first value: "))
y=int(input("Input the second value: "))
addit=x+y
subst=x-y
multi=x*y
try:
    divis=x/y
except:
    divis='cannot be divided by zero'
print(addit, subst)
print(multi, divis)
