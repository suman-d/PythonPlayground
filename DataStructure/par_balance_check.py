from mystack import MyStack


def balance_check(s):

    open_par = "([{"
    close_par = ")]}"

    test_stack = MyStack()

    for p in s:

        if p in open_par or test_stack.isEmpty():
            test_stack.push(p)
            print test_stack.peek()

        else:
            if open_par.index(test_stack.peek()) == close_par.index(p):
                test_stack.pop()
            else:
                return False

    if test_stack.items:
        return False
    else:
        return True


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestBalanceCheck(object):
    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print 'ALL TEST CASES PASSED'


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)