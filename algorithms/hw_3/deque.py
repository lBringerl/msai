class Node:
    def __init__(self, value, next_, prev):
        self.value = value
        self.next_ = next_
        self.prev = prev


class NoInsertDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_back(self, v):
        new_node = Node(v, None, None)
        if self.tail:
            new_node.prev = self.tail
            self.tail.next_ = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.length += 1
        return new_node
    
    def push_front(self, v):
        new_node = Node(v, None, None)
        if self.head:
            new_node.next_ = self.head
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.length += 1
        return new_node

    def __len__(self):
        return self.length

    def pop_back(self):
        if self.length == 0:
            return None
        if self.length == 1:
            result = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return result
        result = self.tail
        self.tail.prev.next_ = None
        self.tail = self.tail.prev
        self.length -= 1
        return result

    def pop_front(self):
        if self.length == 0:
            return None
        if self.length == 1:
            result = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return result
        result = self.head
        self.head.next_.prev = None
        self.head = self.head.next_
        self.length -= 1
        return result


if __name__ == '__main__':
    deque = NoInsertDoubleLinkedList()
    while 1:
        request = map(int, input().split())
        _type = next(request)
        if _type == 0:
            v = next(request)
            deque.push_back(v)
        elif _type == 1:
            v = next(request)
            deque.push_front(v)
        elif _type == 2:
            print(len(deque))
        elif _type == 3:
            node = deque.pop_back()
            if node is None:
                print('Error!')
            else:
                print(node.value)
        elif _type == 4:
            node = deque.pop_front()
            if node is None:
                print('Error!')
            else:
                print(node.value)
        elif _type == -1:
            break
