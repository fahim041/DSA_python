class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addLast(self, val):
        node = Node(val)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addFirst(self, val):
        node = Node(val)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def indexOf(self, val):
        index = 0
        cur = self.head
        while (cur != None):
            if cur.value == val:
                return index
            cur = cur.next
            index += 1
        return -1

    def contains(self, val):
        return self.indexOf(val) != -1

    def removeFirst(self):
        if self.head == None:
            return False

        if self.head == self.tail:
            self.head = self.tail = None
            return True

        else:
            second = self.head.next
            self.head.next = None
            self.head = second
            return True

    def removeLast(self):
        cur = self.head
        while (cur != None):
            if cur.next.next == None:
                break
            cur = cur.next
        cur.next = None
        self.tail = cur
        return True

    def size(self):
        size = 0
        if self.head == None:
            return 0
        else:
            cur = self.head
            while (cur != None):
                cur = cur.next
                size += 1
        return size

    def toArray(self):
        arr = []
        cur = self.head
        while (cur != None):
            arr.append(cur.value)
            cur = cur.next
        return arr

    def reverse(self):
        prev, curr = None, self.head
        self.tail = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def kth(self, k):
        curr, temp = self.head, self.head
        while k > 0 and temp:
            print('loop', k)
            temp = temp.next
            k -= 1

        while temp != None:
            temp = temp.next
            curr = curr.next
        return curr

    def removeKth(self, k):
        curr, temp = self.head, self.head
        while k >= 0 and temp:
            temp = temp.next
            k -= 1
        while temp:
            temp = temp.next
            curr = curr.next

        curr.next = curr.next.next

    def findMidNode(self):
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def print(self):
        cur = self.head
        while (cur != None):
            print(cur.value)
            cur = cur.next


l = LinkedList()
l.addLast(10)
l.addLast(20)
l.addLast(30)
l.addLast(40)
l.addLast(50)
l.addLast(60)
# l.addLast(70)
l.print()

print("mid node", l.findMidNode().value)
