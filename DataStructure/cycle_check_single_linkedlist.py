from single_linkedlist import Node

def cycle_check(node):
    marker = node

    while True:
        if node.nextnode == None:
            return False

        else:
            if node.nextnode == marker:
                return True
            else:
                node =  node.nextnode
                continue


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print "ALL TEST CASES PASSED"


# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
