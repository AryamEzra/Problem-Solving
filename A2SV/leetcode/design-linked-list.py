class Node:
    def __init__ (self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        #these two are dummy nodes the real action is what goes on lft. next and right.prev, it is the thing in between that counts 
        #connect the left and right nodes by making the left and right connected to one another ina double linked list fashion
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode, next, prev = Node(val), self.left.next, self.left
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev


    def addAtTail(self, val: int) -> None:
        newNode, next, prev = Node(val), self.right, self.right.prev
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        #insert before the index as long as it doesn't go above the dummy node on  either the left and the right
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            newNode, next, prev = Node(val), cur, cur.prev
            prev.next = newNode
            next.prev = newNode
            newNode.next = next
            newNode.prev = prev    
            

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)