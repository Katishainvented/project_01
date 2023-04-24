
arr = input('Введите список целых чисел через пробел: ').split()
p=[]
for element in arr:
    p.append(int(element))


print(p)
a = sorted(p)
print(a)
def minimum(arr):
    x = a[0]
    return x

def maximum(arr):
    y = a[-1]
    return y

print(minimum(arr), maximum(arr))
