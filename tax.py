from xml.dom.minidom import TypeInfo


amount = 10
tax = .06

total =  amount + amount * tax

print(total)

amount = 100

total =  amount + amount * tax

print(total)

total = int(total)

print(total)

total =  float(total)

print(total)