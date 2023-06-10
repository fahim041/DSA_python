class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def checkHead(self, newNode):
        self.head = self.tail = newNode
        newNode.next = None
        newNode.prev = None

    def insetFront(self, val):
        newNode = ListNode(val)
        if not self.head:
            self.checkHead(newNode)
        else:
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None
            self.head = newNode

    def insertLast(self, val):
        newNode = ListNode(val)
        if not self.head:
            self.checkHead(newNode)
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = None
            self.tail = newNode

    def removeLast(self):
        if not self.head:
            return
        else:
            r = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            r.prev = None

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


d = DoublyLinkedList()
d.insetFront(11)
d.insetFront(22)
d.insertLast(33)
d.insertLast(44)
d.removeLast()
d.print()
