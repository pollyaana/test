# 1 вариант

f = {'x1': 6, 'x2': 7, 'x3': 3, 'x4': 6, 'x5': 3, 'x6': 7, 'value': 'max'}
u1 = {'x1': 3, 'x2': 2, 'x3': 1, 'x4': 5, 'x5': 0, 'x6': -1, 'sign': '<=', 'value': 8}
u2 = {'x1': 6, 'x2': 3, 'x3': 5, 'x4': 5, 'x5': 5, 'x6': -2, 'sign': '<=', 'value': 7}
u3 = {'x1': -1, 'x2': -1, 'x3': 0, 'x4': 0, 'x5': -2, 'x6': 5, 'sign': '<=', 'value': 4}


# 2 вариант
"""
f = {'x1': 4, 'x2': 5, 'x3': 4, 'x4': 2, 'x5': 3, 'x6': 4, 'value': 'max'}
u1 = {'x1': 2, 'x2': 3, 'x3': 5, 'x4': 2, 'x5': 5, 'x6': -1, 'sign': '<=', 'value': 8}
u2 = {'x1': 3, 'x2': 3, 'x3': 0, 'x4': 2, 'x5': 1, 'x6': 2, 'sign': '<=', 'value': 6}
u3 = {'x1': 0, 'x2': 2, 'x3': 5, 'x4': -1, 'x5': 0, 'x6': -2, 'sign': '<=', 'value': 6}
"""

# 3 вариант
"""
f = {'x1': 6, 'x2': 3, 'x3': 6, 'x4': 6, 'x5': 5, 'x6': 5, 'value': 'max'}
u1 = {'x1': 5, 'x2': 6, 'x3': 4, 'x4': 4, 'x5': 5, 'x6': 6, 'sign': '<=', 'value': 8}
u2 = {'x1': 1, 'x2': 3, 'x3': -2, 'x4': 3, 'x5': 2, 'x6': 0, 'sign': '<=', 'value': 7}
u3 = {'x1': 3, 'x2': -1, 'x3': 5, 'x4': 2, 'x5': -1, 'x6': 2, 'sign': '<=', 'value': 3}
"""

# 4 вариант
"""
f = {'x1': 5, 'x2': 3, 'x3': 8, 'x4': 3, 'x5': 5, 'x6': 6, 'value': 'max'}
u1 = {'x1': 5, 'x2': 3, 'x3': 5, 'x4': 3, 'x5': 0, 'x6': 4, 'sign': '<=', 'value': 4}
u2 = {'x1': -1, 'x2': 3, 'x3': 3, 'x4': 1, 'x5': 1, 'x6': -1, 'sign': '<=', 'value': 8}
u3 = {'x1': -1, 'x2': 4, 'x3': 3, 'x4': 2, 'x5': 3, 'x6': 0, 'sign': '<=', 'value': 8}
"""

def change_sign(dictionary):
    for k, v in dictionary.items():
        if k == 'sign':
            continue
        dictionary[k] = v * -1


''' выполняем правила приведения задачи к каноническому виду '''

# 1. если в исходной задаче требуется определить максимум линейной функции,
# то следует изменить знак и искать минимум этой функции

if f['value'] == 'max':
    change_sign(f)
    f['value'] = 'min'

# 2. если среди ограничений имеются неравенства, то путем введения дополнительных неотрицательных переменных
# они преобразуются в равенства

if u1['sign'] == '>=':
    u1['x7'] = -1
if u1['sign'] == '<=':
    u1['x7'] = 1
u1['x8'] = 0
u1['x9'] = 0
if u2['sign'] == '>=':
    u1['x8'] = -1
if u2['sign'] == '<=':
    u2['x8'] = 1
u2['x7'] = 0
u2['x9'] = 0
if u3['sign'] == '>=':
    u3['x9'] = -1
if u3['sign'] == '<=':
    u3['x9'] = 1
u3['x7'] = 0
u3['x8'] = 0
# 3. если в ограничениях правая часть отрицательна, то следует умножить это ограничение на -1
if u1['value'] < 0:
    change_sign(u1)
if u2['value'] < 0:
    change_sign(u2)
if u3['value'] < 0:
    change_sign(u3)

f['x7'] = 0
f['x8'] = 0
f['x9'] = 0
# формирование начального базиса - дополнительные переменные и есть базисные
basis = {'7': 0, '8': 0, '9': 0}
c = [f['x1'], f['x2'], f['x3'], f['x4'], f['x5'], f['x6'], f['x7'], f['x8'], f['x9']]
b = [u1['value'], u2['value'], u3['value']]
tb = [
    [u1['x1'], u2['x1'], u3['x1']],
    [u1['x2'], u2['x2'], u3['x2']],
    [u1['x3'], u2['x3'], u3['x3']],
    [u1['x4'], u2['x4'], u3['x4']],
    [u1['x5'], u2['x5'], u3['x5']],
    [u1['x6'], u2['x6'], u3['x6']],
    [u1['x7'], u1['x8'], u1['x9']],
    [u2['x7'], u2['x8'], u2['x9']],
    [u3['x7'], u3['x8'], u3['x9']]
]
while True:
    z = 0
    deltas = {}
    j = 0
    # главная дельта - z
    for bas in basis.values():
        z += bas * b[j]
        j += 1

    # дельты переменных
    for i in range(0, len(c)):
        k = 0
        t = 0
        for bas in basis.values():
            k += bas * tb[i][t]
            t += 1
        deltas['x' + str(i + 1)] = k - c[i]

    # План оптимален, если в таблице отсутствуют положительные дельты.
    deltas_cnt = 0
    for val in deltas.values():
        if val <= 0:
            deltas_cnt += 1
    # проверка условия выхода из цикла
    if deltas_cnt == len(c):
        z = abs(z)
        print('------------------------------------------------')
        print('Найдено оптимальное решение: Z = ' + str(round(z, 3)))
        h = 0
        for k, v in basis.items():
            if int(k) <= 6:
                print('x' + str(k) + ' : ' + str(round(b[h], 3)))
            h += 1
        print('Все остальные переменные имеют коэффициент 0')
        print('------------------------------------------------')
        exit()

    # ведущий столбец s
    s = 0
    max_val = 0
    for key, val in deltas.items():
        if max_val <= val:
            max_val = val
            s = int(key.strip('x'))

    # проверка условия выхода из цикла
    s_el = 0
    for i in range(0, len(tb[s - 1])):
        if tb[s - 1][i] <= 0:
            s_el += 1
    if s_el == 3:
        print('Целевая функция является неограниченной на области допустимых решений ЗЛП, т.е. ЗЛП не имеет решений')
        exit()

    # ведущая строка r
    list_s = {}
    for i in range(0, len(tb[s - 1])):
        if tb[s - 1][i] <= 0:
            continue
        q = b[i] / tb[s - 1][i]
        list_s[i] = q
    # r = 0
    r = min(list_s, key=list_s.get) + 1
    n = 1
    new_basis = {}
    for key, val in basis.items():
        if n != r:
            new_basis[key] = val
        else:
            new_basis[s] = c[s - 1]
        n += 1
    basis = new_basis

    tb.insert(0, b)
    new_tb = []
    for j in range(0, len(c) + 1):
        column = []
        for i in range(0, len(basis)):
            a = tb[j][i]
            bb = tb[s][r - 1]
            cc = tb[j][r - 1]
            dd = tb[s][i]
            if i == r - 1:
                column.append(tb[j][i] / tb[s][r - 1])
            else:
                column.append((tb[j][i] * tb[s][r - 1] - tb[j][r - 1] * tb[s][i]) / tb[s][r - 1])
        new_tb.append(column)
    tb = new_tb[1:]
    b = new_tb[0]
