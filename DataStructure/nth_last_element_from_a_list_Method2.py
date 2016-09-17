from single_linkedlist import Node
from reverse_list import reverse


def nth_to_last_node(n, value):
    value = reverse(value)

    for i in range(n):
        tmp = value.nextnode

    return tmp

