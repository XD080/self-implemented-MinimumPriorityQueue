class MinimumPriorityQueue:
    class LinkedMinHeap:
        class Node:
            def __init__(self, item):
                self.item = item
                self.parent = None
                self.left = None
                self.right = None

        class Item:
            def __init__(self, priority, value=None):
                self.priority = priority
                self.value = value

            def __lt__(self, other):
                return self.priority < other.priority

        def __init__(self):
            self.root = None
            self.size = 0

        def __len__(self):
            return self.size

        def is_empty(self):
            return self.size == 0

        def min(self):
            if self.is_empty():
                raise Exception("Heap is empty")
            return self.root.item.priority, self.root.item.value

        def insert(self, pri, val):
            Node = MinimumPriorityQueue.LinkedMinHeap.Node(MinimumPriorityQueue.LinkedMinHeap.Item(pri, val))

            if self.size == 0:
                self.root = Node
                self.size += 1
                return
            cur = self.root
            binary = '{0:b}'.format(self.size + 1)[1:-1]
            for i in range(len(binary)):
                if int(binary[i]) == 0:
                    cur = cur.left
                else:
                    cur = cur.right
            if cur.right is None:
                cur.right = Node
            else:
                cur.left = Node

            Node.parent = cur

            self.size += 1

            while Node.parent and Node.item.priority < Node.parent.item.priority:
                Node.item, Node.parent.item = Node.parent.item, Node.item
                Node = Node.parent

        def delete_min(self):

            if self.is_empty():
                raise Exception("Heap is empty")

            if self.size == 1:
                data = self.root.item
                self.root = None
                self.size -= 1
                return data.priority, data.value

            binary = '{0:b}'.format(self.size)[1:]
            cur = self.root
            for i in binary:
                if i == '0':
                    cur = cur.left
                else:
                    cur = cur.right

            lastNode = cur
            result = self.root.item
            self.size -= 1

            if binary[-1] == '0':
                lastNode.parent.left = None
            else:
                lastNode.parent.right = None

            self.root.item = lastNode.item
            cur = self.root
            keepgoing = False
            while ((keepgoing == True) and (cur.left is not None)):
                if (cur.right is not None):
                    if (cur.left.priority< cur.right.priority):
                        small_child = cur.left
                    else:
                        small_child = cur.right
                else:
                    cur = cur.left
                    small_child = cur

                if (small_child.priority < cur.priority):
                    cur.priority,small_child.priority = small_child.priority,cur.priority
                    cur = small_child
                else:
                    keepgoing = False


            return result.priority, result.value

    def __init__(self):
        self.data = MinimumPriorityQueue.LinkedMinHeap()

    def __len__(self):
        return self.data.size

    def is_empty(self):
        return len(self) == 0

    def insert(self, pri, val):
        self.data.insert(pri, val)

    def delete_min(self):
        return self.data.delete_min()

    def min(self):
        return self.data.min()
