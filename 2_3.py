n = int(input('Введите число от 1 до 9: '))
def switch_it_up(n):
    chislo = {1 :"один", 2 :"два", 3 :"три", 4 :"четыре", 5 :"пять", 6 :"шесть", 7 :"семь", 8 :"восемь", 9 :"девять"}
    return chislo.get(n)
print(switch_it_up(n))