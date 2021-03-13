'''
@Author: rishi
https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
'''

from QuickDS import create_linked_list


def count(head):
    c = 0
    while head is not None:
        c += 1
        head = head.get_next()
    return c


def intersect_point(head1, head2):
    c1 = count(head1)
    c2 = count(head2)

    excess = abs(c1 - c2)
    while excess > 0:
        if c1 > c2:
            head1 = head1.get_next()
        else:
            head2 = head2.get_next()
        excess -= 1

    while head1 and head2:
        if head1.get_val() == head2.get_val():
            return head1.get_val()
        head1 = head1.get_next()
        head2 = head2.get_next()
    return -1


head1 = create_linked_list([4, 1, 8, 5, 2, 4, 5])
head2 = create_linked_list([5, 6, 1, 4, 5])

print(intersect_point(head1, head2))
