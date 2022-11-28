def sorting(string_to_sort):
    text = ''
    while len(string_to_sort) > 0:
        text += min(string_to_sort)
        string_to_sort = string_to_sort.replace(min(string_to_sort), '', 1)
    return text.lower()


def is_anagram(first_string, second_string):
    first_string_sorted = sorting(first_string)
    second_string_sorted = sorting(second_string)
    if not first_string_sorted or not second_string_sorted:
        return (first_string_sorted, second_string_sorted, False)

    if len(first_string_sorted) != len(second_string_sorted):
        return (first_string_sorted, second_string_sorted, False)

    else:
        return (first_string_sorted, second_string_sorted, True)
