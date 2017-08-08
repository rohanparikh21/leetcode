class Node(object):

    def __init__(self, val):
        self._next = None
        self.val = val

    @property
    def Next(self):
        return self._next

    @Next.setter
    def Next(self, n):
        self._next = n


class LinkedList(object):

    def __init(self, head):
        self._head = head

    @property
    def head(self):
        return self._head


def find_kth_element_to_last_recursive(head, k, index=0):
    if head is None:
        return head, index
    else:
        n, index = find_kth_element_to_last_recursive(head.Next, k, index)
        index += 1
        if index == k:
            return head, index
        return n, index


def find_kth_element_to_last_iterative(head, k):
    k_start = head
    for i in range(k):
        k_start = k_start.Next

    curr = head
    while k_start is not None:
        k_start = k_start.Next
        curr = curr.Next

    return curr


def partition(head, x):
    curr = head
    prev_node_with_greater_than_x_val = head
    while curr:
        if curr.val < x:
            if prev_node_with_greater_than_x_val.val == curr.val:
                prev_node_with_greater_than_x_val = prev_node_with_greater_than_x_val.Next
            else:
                temp = prev_node_with_greater_than_x_val.val
                prev_node_with_greater_than_x_val.val = curr.val
                curr.val = temp
                prev_node_with_greater_than_x_val = prev_node_with_greater_than_x_val.Next
        curr = curr.Next
    return head


def pprint_ll(head):
    s = ''
    while head:
        s += 'Node:{v} -> '.format(v=head.val)
        head = head.Next

    s += 'None'
    return s


def reverse_sum(ll1, ll2):
    carry = 0
    curr = None
    head = None
    ll1_curr = ll1
    ll2_curr = ll2
    while ll1_curr is not None and ll2_curr is not None:
        carry, sum = (carry + ll1_curr.val + ll2_curr.val)/10, (carry + ll1_curr.val + ll2_curr.val)%10
        if not curr:
            curr = Node(sum)
            head = curr
        else:
            curr.Next = Node(sum)
            curr = curr.Next
        ll1_curr = ll1_curr.Next
        ll2_curr = ll2_curr.Next

    while ll1_curr:
        carry, sum = (carry + ll1_curr.val) / 10, (carry + ll1_curr.val) % 10
        curr.Next = Node(sum)
        curr = curr.Next
        ll1_curr = ll1_curr.Next

    while ll2_curr:
        carry, sum = (carry + ll2_curr.val) / 10, (carry + ll2_curr.val) % 10
        curr.Next = Node(sum)
        curr = curr.Next
        ll2_curr = ll2_curr.Next
    return head


def if_intersection(head1, head2):
    if head1 is None or head2 is None:
        return False

    curr1 = head1
    len1 = 0
    while curr1.Next:
        len1 += 1
        curr1 = curr1.Next

    curr2 = head2
    len2 = 0
    while curr2.Next:
        len2 += 1
        curr2 = curr2.Next

    if curr1 != curr2:
        return False

    diff_len = abs(len1-len2)
    list_to_chop = head1 if len1 >= len2 else head2
    other_list = head1 if list_to_chop == head2 else head2
    for i in range(diff_len):
        list_to_chop = list_to_chop.Next

    while list_to_chop != other_list:
        list_to_chop = list_to_chop.Next
        other_list = other_list.Next

    return list_to_chop


def is_circular(head):
    slow_p = head
    fast_p = head
    while True:
        slow_p = slow_p.Next
        fast_p = fast_p.Next
        fast_p = fast_p.Next
        if slow_p == fast_p:
            break

    slow_p = head
    while True:
        slow_p = slow_p.Next
        fast_p = fast_p.Next
        if slow_p == fast_p:
            return slow_p


def reverse(head):
    curr = head
    prev = None
    while curr:
        temp = curr
        curr = curr.Next
        temp.Next = prev
        prev = temp

    return prev

def length_of_ll(head):
    ctr = 0
    curr = head
    while curr:
        ctr += 1
        curr = curr.Next
    return ctr


def is_palindrome_helper(head, length):
    if length == 0:
        return head, True
    elif length == 1:
        return head.Next, True
    else:
        node_to_compare, is_p = is_palindrome_helper(head.Next, length-2)
        if not is_p:
            return node_to_compare, False
        if head.val == node_to_compare.val:
            return node_to_compare.Next, True
        else:
            return node_to_compare, False


def is_palindrome(head):
    length = length_of_ll(head)
    _, is_p = is_palindrome_helper(head, length)
    return is_p


if __name__ == '__main__':
    n1 = Node(7)
    n2 = Node(1)
    n3 = Node(1)
    n4 = Node(7)

    n1.Next = n2
    n2.Next = n3
    n3.Next = n4

    print is_palindrome(n1)



