from single_linkedlist import Node

def reverse(node):

    current = node
    previous_node = None
    next_node = None

    while current:

        next_node = current.nextnode
        current.nextnode = previous_node

        previous_node = current
        current = next_node

    return previous_node


