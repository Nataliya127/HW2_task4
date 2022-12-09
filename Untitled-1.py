

# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2



with open('List.txt','r') as f:
    a = f.read().split('\n')
a = list(map(int, a))

n = int(input('Введите число: '))
gen = [i for i in range(-n, n+1)]
kn=1
for i in a:
#multi *= gen[pos]
#print(gen[pos-1])
    kn *= gen[i]
    print(kn)

print(a)
print(gen)
print(kn)