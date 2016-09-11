import string


def sub_string(st):
    first_letter_index = string.lowercase.index(st[0])
    first_letter_end_list = string.lowercase[first_letter_index::]
    result = {st: 0}
    for i in st:
        if i == first_letter_end_list[0]:
            result[st] = result[st] + 1

        elif i in first_letter_end_list:
            result[st] = result[st] + 1
            first_letter_end_list = "".join((list(first_letter_end_list)[first_letter_end_list.index(i)::]))
        else:
            break

    return result[st]


def check_for_longest_substring(test_string):

    max = 0
    index = 0
    for i, j in enumerate(list(test_string)):
        result = sub_string("".join(list(test_string)[i:]))

        if result == max and j <= test_string[index]:
            max = result
            index = i
        elif result > max:
            max = result
            index = i

    return "".join(list(test_string)[index:(index+max):])



print check_for_longest_substring("xxxiiiiiiiiiiaaabb")