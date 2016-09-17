
class Node():

    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prenode = None

a = Node(10)
b = Node(20)
c = Node(30)

a.nextnode = b
b.nextnode = c
b.prenode = a
c.prenode = b

print a.nextnode.value
print b.nextnode.value
print c.prenode.value
print b.prenode.value
