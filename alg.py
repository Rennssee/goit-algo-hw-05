import timeit


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return []

    last_occurrence = {pattern[i]: i for i in range(m - 1)}
    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return [i]  # Знайдено збіг

            i -= 1
            j -= 1
        else:
            last_occ = last_occurrence.get(text[i], -1)
            i = i + m - min(j, 1 + last_occ)
            j = m - 1

    return []


def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return []

    pi = compute_prefix_function(pattern)
    q = 0
    occurrences = []

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]

        if pattern[q] == text[i]:
            q += 1

        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]

    return occurrences


def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]

        if pattern[k] == pattern[q]:
            k += 1

        pi[q] = k

    return pi


def rabin_karp_search(text, pattern):
    d = 256  # Розмір алфавіту (ASCII)
    q = 101  # Просте число
    m = len(pattern)
    n = len(text)
    h = pow(d, m - 1, q)  # d^(m-1) % q

    p = 0  # Хеш для шаблону
    t = 0  # Хеш для поточного вікна тексту

    occurrences = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t and pattern == text[s : s + m]:
            occurrences.append(s)

        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            t = (t + q) % q  # Впевненість, що t не від'ємне

    return occurrences


def measure_time(search_func, text, pattern):
    start_time = timeit.default_timer()
    search_func(text, pattern)
    return timeit.default_timer() - start_time


def compare_algorithms_markdown_to_file(
    filename, article_name, text, real_pattern, fake_pattern
):
    with open(filename, "a", encoding="utf-8") as markdown_file:
        markdown_file.write(f"\n## Результати для статті '{article_name}'\n\n")

        markdown_file.write(f"### Порівняння для реального підрядка:\n")

        bm_time_real = measure_time(boyer_moore_search, text, real_pattern)
        kmp_time_real = measure_time(kmp_search, text, real_pattern)
        rk_time_real = measure_time(rabin_karp_search, text, real_pattern)

        markdown_file.write(f"**Алгоритм Боєра-Мура:** {bm_time_real} секунд\n")
        markdown_file.write(
            f"**Алгоритм Кнута-Морріса-Пратта:** {kmp_time_real} секунд\n"
        )
        markdown_file.write(f"**Алгоритм Рабіна-Карпа:** {rk_time_real} секунд\n")

        markdown_file.write(f"\n### Порівняння для вигаданого підрядка:\n")

        bm_time_fake = measure_time(boyer_moore_search, text, fake_pattern)
        kmp_time_fake = measure_time(kmp_search, text, fake_pattern)
        rk_time_fake = measure_time(rabin_karp_search, text, fake_pattern)

        markdown_file.write(f"**Алгоритм Боєра-Мура:** {bm_time_fake} секунд\n")
        markdown_file.write(
            f"**Алгоритм Кнута-Морріса-Пратта:** {kmp_time_fake} секунд\n"
        )
        markdown_file.write(f"**Алгоритм Рабіна-Карпа:** {rk_time_fake} секунд\n")


# Зчитування текстових файлів
with open("стаття1.txt", "r", encoding="cp1251") as file:
    text_article1 = file.read()
with open("стаття2.txt", "r", encoding="cp1251") as file:
    text_article2 = file.read()

# Задання реальних і вигаданих підрядків для кожної статті окремо
real_pattern_article1 = (
    "логарифмічний пошук часто використовується через швидкий час пошуку"
)
fake_pattern_article1 = "мила мама рибу 8765"

real_pattern_article2 = "Предметом дослідження є методи та структури даних для"
fake_pattern_article2 = "колись були козаки які били турків"


output_filename = "results_all_articles.md"

# Видалення попереднього вмісту файлу (якщо файл існує)
with open(output_filename, "w", encoding="utf-8") as clear_file:
    pass

# Порівняння алгоритмів для статті 1 та запис результатів у файл
compare_algorithms_markdown_to_file(
    output_filename,
    "Стаття 1",
    text_article1,
    real_pattern_article1,
    fake_pattern_article1,
)

# Порівняння алгоритмів для статті 2 та запис результатів у файл
compare_algorithms_markdown_to_file(
    output_filename,
    "Стаття 2",
    text_article2,
    real_pattern_article2,
    fake_pattern_article2,
)

print(f"Результати порівнянь збережено у файлі: {output_filename}")
