def sort_string(string_to_sort):
    text = ''
    while len(string_to_sort) > 0:
        text += min(string_to_sort)
        string_to_sort = string_to_sort.replace(min(string_to_sort), '', 1)
    return text


def is_anagram(first_string, second_string):
    if not first_string or not first_string:
        return False

    if len(first_string) != len(second_string):
        return False

    first_string_sorted = sort_string(first_string)
    second_string_sorted = sort_string(second_string)

    index = 0

    while index < len(first_string_sorted):
        if first_string_sorted[index] != second_string_sorted[index]:
            return False
        index += 1
    return True
