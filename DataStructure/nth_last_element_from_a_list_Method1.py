from single_linkedlist import Node


def nth_to_last_node(n, value):
    marker1 = value
    marker2 = value

    while marker2.nextnode != None:
        marker2 = marker1
        for i in range(n):
            marker2 = marker2.nextnode

        marker1 = value.nextnode
        value = value.nextnode

    return marker1


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = nth_to_last_node(1, a)
print target_node.value