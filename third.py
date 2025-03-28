import re


def get_substrings(text, min_len=2, max_len=6):
    """Получение всех подстрок заданной длины от min_len до max_len"""
    result = []
    for length in range(min_len, max_len + 1):
        for i in range(len(text) - length + 1):
            result.append(text[i:i + length])
    return result


def read_file(path):
    """Чтение файла и удаление цифр и пробелов"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return re.sub(r'[\d\s]', '', file.read())
    except FileNotFoundError:
        print(f"Ошибка: файл {path} не найден.")
        return ""
    except Exception as e:
        print(f"Ошибка при чтении файла {path}: {e}")
        return ""


def find_min(substrings):
    """Нахождение минимальной по длине подстроки в множестве"""
    return min(substrings, key=len) if substrings else None


def find_max_common(s1, s2):
    """Нахождение максимальной общей подпоследовательности для s1 и s2"""
    max_common = ""
    for i in range(len(s1)):
        for j in range(i + len(max_common) + 1, len(s1) + 1):
            sub = s1[i:j]
            if sub in s2:
                max_common = sub
            else:
                break
    return max_common


def find_unique_in_first(subs1, subs2):
    """Поиск уникальных подстрок в первой строке, отсутствующих во второй"""
    return set(subs1) - set(subs2)


def find_common(subs1, subs2):
    """Поиск общих подстрок между двумя списками"""
    return set(subs1) & set(subs2)


def find_missing_in_second_and_third(subs1, subs2, subs3):
    """Поиск подстрок в первой строке, отсутствующих во второй и третьей"""
    return set(subs1) - (set(subs2) | set(subs3))


def main():
    # Чтение содержимого файлов в строки
    dna1 = read_file("example1.txt")
    dna2 = read_file("example2.txt")
    dna3 = read_file("example3.txt")

    if not dna1 or not dna2 or not dna3:
        print("Ошибка: один из файлов пуст или не найден.")
        return

    # Получение подстрок
    subs1 = get_substrings(dna1)
    subs2 = get_substrings(dna2)
    subs3 = get_substrings(dna3)

    # Поиск уникальных и общих подстрок
    unique1 = find_unique_in_first(subs1, subs2)
    unique2 = find_unique_in_first(subs2, subs1)
    common12 = find_common(subs1, subs2)
    unique3 = find_unique_in_first(subs3, subs1)
    unique3 -= set(subs2)  # Убираем подстроки, которые есть в dna2
    missing_in_23 = find_missing_in_second_and_third(subs1, subs2, subs3)

    # Нахождение минимальной по длине подстроки
    min_unique1 = find_min(unique1)
    min_unique2 = find_min(unique2)
    min_common12 = find_min(common12)
    min_missing23 = find_min(missing_in_23)
    min_unique3 = find_min(unique3)

    # Нахождение максимальной общей подпоследовательности для dna1 и dna3
    max_common13 = find_max_common(dna1, dna3)
    ratio = len(max_common13) / len(dna1) if dna1 else 0

    # Вывод результатов
    print("Мин. уникальная для 1, отсутствующая в 2:", min_unique1)
    print("Мин. уникальная для 2, отсутствующая в 1:", min_unique2)
    print("Мин. общая для 1 и 2:", min_common12)
    print("Мин. уникальная для 1, отсутствующая в 2 и 3:", min_missing23)
    print("Мин. уникальная для 3, отсутствующая в 1 и 2:", min_unique3)
    print("Макс. общая подпоследовательность для 1 и 3:", max_common13)
    print("Соотношение длины общей подпоследовательности к длине 1:", ratio)

def test():
    """Тестирование функций на искусственных данных"""
    dna1 = "ATCGAT"
    dna2 = "GATCGA"
    dna3 = "TCGATC"

    subs1 = get_substrings(dna1)
    subs2 = get_substrings(dna2)
    subs3 = get_substrings(dna3)

    expected_unique_1_2 = {'TCGAT', 'ATCGAT', 'CGAT'}
    expected_unique_2_1 = {'GATC', 'GATCG', 'GATCGA'}
    expected_common_1_2 = {'CGA', 'TC', 'AT', 'GAT', 'ATCGA', 'ATCG', 'GA', 'TCG', 'TCGA', 'CG', 'ATC'}
    expected_missing_1_23 = {'ATCGAT'}
    expected_unique_3_12 = {'TCGATC', 'CGATC'}
    expected_max_common_1_3 = "TCGAT"
    expected_ratio = len(expected_max_common_1_3) / len(dna1)

    assert find_unique_in_first(subs1, subs2) == expected_unique_1_2, f"Ошибка в уникальных подстроках 1: {find_unique_in_first(subs1, subs2)}"
    assert find_unique_in_first(subs2, subs1) == expected_unique_2_1, f"Ошибка в уникальных подстроках 2: {find_unique_in_first(subs2, subs1)}"
    assert find_common(subs1, subs2) == expected_common_1_2, f"Ошибка в общих подстроках 1 и 2: {find_common(subs1, subs2)}"
    assert find_missing_in_second_and_third(subs1, subs2, subs3) == expected_missing_1_23, f"Ошибка в отсутствующих подстроках 1: {find_missing_in_second_and_third(subs1, subs2, subs3)}"
    assert find_unique_in_first(subs3, subs1) - set(subs2) == expected_unique_3_12, f"Ошибка в уникальных подстроках 3: {find_unique_in_first(subs3, subs1) - set(subs2)}"
    assert find_max_common(dna1, dna3) == expected_max_common_1_3, f"Ошибка в максимальной общей подпоследовательности: {find_max_common(dna1, dna3)}"
    assert abs((len(find_max_common(dna1, dna3)) / len(dna1)) - expected_ratio) < 1e-6, f"Ошибка в вычислении соотношения: {len(find_max_common(dna1, dna3)) / len(dna1)}"

    print("Все тесты пройдены!")


if __name__ == "__main__":
    test()
