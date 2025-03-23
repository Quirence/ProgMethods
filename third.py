import re


def read_file(path):
    """Чтение файла и удаление цифр и пробелов"""
    with open(path, 'r') as file:
        content = file.read()
    # Убираем все символы, кроме A, T, C, G
    return re.sub(r'[^ATCG]', '', content)


def get_substrings(sequence, min_len=2, max_len=6):
    """Получение всех подстрок заданной длины от min_len до max_len"""
    substrings = set()
    for length in range(min_len, max_len + 1):
        for i in range(len(sequence) - length + 1):
            substrings.add(sequence[i:i + length])
    return substrings


def find_min_unique(substrings1, substrings2):
    """Нахождение минимальной подстроки из substrings1, которой нет в substrings2"""
    unique_substrings = substrings1 - substrings2
    if unique_substrings:
        return min(unique_substrings, key=len)
    return None


def find_max_common(s1, s2):
    """Нахождение максимальной общей подпоследовательности для s1 и s2"""
    max_common = ""
    for i in range(len(s1)):
        for j in range(i + len(max_common), len(s1)):
            sub = s1[i:j]
            if sub in s2:
                max_common = sub
            else:
                break
    return max_common


def main():
    # Чтение файлов и очистка данных
    dna1 = read_file('covid_uhan.txt')
    dna2 = read_file('h5n1.txt')
    dna3 = read_file('covid_delta.txt')

    # Получаем подстроки длиной от 2 до 6 для каждого вируса
    substrings1 = get_substrings(dna1)
    substrings2 = get_substrings(dna2)
    substrings3 = get_substrings(dna3)

    # Нахождение минимальной специфичной последовательности
    min_unique_1_2 = find_min_unique(substrings1, substrings2)
    min_unique_2_1 = find_min_unique(substrings2, substrings1)
    min_common_1_2 = find_min_unique(substrings1, substrings2)

    min_unique_1_2_3 = find_min_unique(substrings1, substrings2.union(substrings3))
    min_unique_3_1_2 = find_min_unique(substrings3, substrings1.union(substrings2))

    # Нахождение максимальной общей подпоследовательности для COVID-Ухань и COVID-Дельта
    max_common_1_3 = find_max_common(dna1, dna3)
    ratio = len(max_common_1_3) / len(dna1) if len(dna1) > 0 else 0

    # Вывод результатов
    print(f"Минимальная специфичная последовательность для COVID-Ухань, отсутствующая в H5N1: {min_unique_1_2}")
    print(f"Минимальная специфичная последовательность для H5N1, отсутствующая в COVID-Ухань: {min_unique_2_1}")
    print(f"Минимальная общая последовательность для COVID-Ухань и H5N1: {min_common_1_2}")
    print(
        f"Минимальная специфичная последовательность для COVID-Ухань, отсутствующая в COVID-Дельта и H5N1: {min_unique_1_2_3}")
    print(
        f"Минимальная специфичная последовательность для COVID-Дельта, отсутствующая в COVID-Ухань и H5N1: {min_unique_3_1_2}")
    print(f"Максимальная общая подпоследовательность для COVID-Ухань и COVID-Дельта: {max_common_1_3}")
    print(f"Соотношение длины общей подпоследовательности к длине генома COVID-Ухань: {ratio}")


if __name__ == "__main__":
    main()
