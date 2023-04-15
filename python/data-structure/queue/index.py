class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self):
        if not self.head:
            return
        else:
            r = self.head
            self.head = self.head.next
            r.next = None

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)

q.dequeue()

q.print()
