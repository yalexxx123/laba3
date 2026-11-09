from math import atan

print('введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg = '))
xe = float(input('Xend = '))
dx = float(input('Dx   = '))
eps = float(input('Eps  = '))

# проверка области допустимых значений
if abs(xb) > 1 or abs(xe) > 1:
    print('ряд сходится только при |x| <= 1')

# шапка таблицы
print("+---------+---------+-----+---------+")
print("I    X    I    Y    I  N  I  atan   I")
print("+---------+---------+-----+---------+")

x = xb
while x <= xe + 1e-12:          # +1e-12 — защита от накопления погрешности
    # инициализация суммы
    n = 0
    a = x                       # первый член ряда: a_0 = x
    S = a

    # суммируем, пока |a| >= eps
    while abs(a) >= eps:
        k = -x * x * (2 * n + 1) / (2 * n + 3)   # рекуррентный множитель
        a = a * k
        S = S + a
        n = n + 1

    # вывод строки таблицы (для сверки — встроенный atan)
    print("I{0: 8.4f} I{1: 8.4f} I{2: 3d}  I{3: 8.4f} I"
          .format(x, S, n, atan(x)))

    x = x + dx

print("+---------+---------+-----+---------+")