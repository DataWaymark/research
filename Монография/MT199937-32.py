#############################################################################################################################
# Този изходен код и файл са част от демонстрационните примерни към изследването:
# Бъдещето е неясно….и това е добре, Университетско издателство „Паисий Хилендарски", Пловдив, 2023, ISBN: 978-619-202-850-3
#
#
# Част от проект КП-06-ДК2/6, финансиран от Фонд Научни Изследвания (ФНИ).
#############################################################################################################################

# Input values for MT19937-32 (Начална стойност на параметрите на алгоритъма MT19937-32)
(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253


# State vector (Вектор на състоянието съдържащ n стойности/думи )
MT = [0 for i in range(n)]
index = n + 1
lower_mask = 0x7FFFFFFF # (1 << r) - 1 => In binary this is 1111....1 (total of r 1 bits)
upper_mask = 0x80000000 # lowest w bits (Младшите w бита)


# initialize the generator from a seed
def mt_seed(seed):
    # global index
    # index = n
    MT[0] = seed
    for i in range(1, n):
        temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
        MT[i] = temp & 0xffffffff


# Extract a tempered value based on MT[index]
# calling twist() every n numbers
def extract_number():
    global index
    if index >= n:
        twist()
        index = 0

    y = MT[index]
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> l)

    index += 1
    return y & 0xffffffff


# Generate the next n values from the series x_i
def twist():
    for i in range(0, n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if (x % 2) != 0:
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA


if __name__ == '__main__':
    # Seed of 0 (Начална стойност на състоянието 0)
    mt_seed(0)
    # Print 100 random numbers (Отпечатваме 100 случайни числа)
    for i in range(100):
        print(extract_number())