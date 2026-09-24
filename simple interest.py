#simple interest problem
pa=int(input())
ri=int(input())
y=int(input())

si=(pa*ri*y)//100
a=pa+si
di=si*(2/100)
fa=a-di

print(f"{si:.2f}")
print(f"{a:.2f}")
print(f"{di:.2f}")
print(f"{fa:.2f}")
