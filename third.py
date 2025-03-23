import re


def clean_sequence(sequence):
    return re.sub(r'[^ATCG]', '', sequence)


def find_specific_sequence(seq1, seq2):
    for i in range(1, len(seq1) + 1):
        for j in range(0, len(seq1) - i + 1):
            subsequence = seq1[j:j + i]
            if subsequence not in seq2:
                return subsequence
    return None


def find_common_sequence(seq1, seq2):
    max_len = 0
    common_subsequence = ''
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            k = 0
            while (i + k < len(seq1)) and (j + k < len(seq2)) and seq1[i + k] == seq2[j + k]:
                k += 1
            if k > max_len:
                max_len = k
                common_subsequence = seq1[i:i + k]
    return common_subsequence


def longest_common_subsequence(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))


covid_uhan_genome = """ATGCGTGAGAGTGGAGGACCTGCGTACAGGACTGGGAGGAGGCGTGAGGAGTGGAGGAC"""
h5n1_gripp_genome = """ATGCGTGGAGGAGGAGTGGAGGACTAGGTAGGAACCTGAGAGAGGGGAGAGAGGAG"""
covid_delta_genome = """ATGGGAGAGTGGAGGACTGAGGACAGGGGAGGGAGGAGGAGAGAGGAGAGGAGAG"""

clean_covid_uhan = clean_sequence(covid_uhan_genome)
clean_h5n1_gripp = clean_sequence(h5n1_gripp_genome)
clean_covid_delta = clean_sequence(covid_delta_genome)

specific_covid_uhan = find_specific_sequence(clean_covid_uhan, clean_h5n1_gripp)
print(f"Минимальная специфичная последовательность для COVID-Ухань: {specific_covid_uhan}")

specific_h5n1 = find_specific_sequence(clean_h5n1_gripp, clean_covid_uhan)
print(f"Минимальная специфичная последовательность для H5N1: {specific_h5n1}")

common_sequence = find_common_sequence(clean_covid_uhan, clean_h5n1_gripp)
print(f"Минимальная общая последовательность для COVID-Ухань и H5N1: {common_sequence}")

specific_covid_uhan_exclude_delta_h5n1 = find_specific_sequence(clean_covid_uhan, clean_covid_delta)
specific_covid_uhan_exclude_h5n1 = find_specific_sequence(specific_covid_uhan_exclude_delta_h5n1, clean_h5n1_gripp)
print(
    f"Минимальная специфичная последовательность для COVID-Ухань, отсутствующая в COVID-Дельта и H5N1: {specific_covid_uhan_exclude_h5n1}")

specific_covid_delta_exclude_h5n1_uhan = find_specific_sequence(clean_covid_delta, clean_h5n1_gripp)
specific_covid_delta_exclude_uhan = find_specific_sequence(specific_covid_delta_exclude_h5n1_uhan, clean_covid_uhan)
print(
    f"Минимальная специфичная последовательность для COVID-Дельта, отсутствующая в COVID-Ухань и H5N1: {specific_covid_delta_exclude_uhan}")

lcs_covid_uhan_delta = longest_common_subsequence(clean_covid_uhan, clean_covid_delta)
print(f"Максимальная общая подпоследовательность для COVID-Ухань и COVID-Дельта: {lcs_covid_uhan_delta}")
print(
    f"Длина максимальной общей подпоследовательности к длине генома: {len(lcs_covid_uhan_delta) / len(clean_covid_uhan)}")
