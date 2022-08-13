# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = str(l1)
        l2 = str(l2)
        l1 = l1[::-1]
        l2 = l2[::-1]
        l1 = int(l1)
        l2 = int(l2)
        l3 = l1 + l2
        l3 = str(l3)
        l3 = l3[::-1]
        l3 = int(l3)
        return l3

