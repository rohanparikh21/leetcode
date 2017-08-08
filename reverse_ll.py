class Node(object):

    def __init__(self, v, next):
        self.val = v
        self.nxt = next

    def __str__(self):
        return str(self.val)


class LinkedList(object):

    def __init__(self, head):
        self.head = head

    def reverse(self):
        if self.head.nxt is None:
            return
        else:
            prev = None
            curr = self.head
            nxt = self.head.nxt
            while nxt:
                curr.nxt = prev
                prev = curr
                curr = nxt
                nxt = curr.nxt
            curr.nxt = prev
            self.head = curr

    def __str__(self):
        s = ''
        curr = self.head
        nxt = curr.nxt
        while nxt:
            s += '{v}->'.format(v=curr.val)
            curr = nxt
            nxt = nxt.nxt

        s += '{v}->'.format(v=curr.val)
        s += 'None'
        return s


if __name__ == '__main__':
    n4 = Node(4, None)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    ll = LinkedList(n1)
    print ll
    ll.reverse()
    print ll

