a = input()
b=[]
sum_ = 0
for i in a:
    sum_+= int(i)
    b.append(i)
print(f"Sum: {sum_}")
print(f"Max: {max(b)}")
print(f"Min: {min(b)}")