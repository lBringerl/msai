import sys


class Node:
    def __init__(self, value, next_, prev):
        self.value = value
        self.next_ = next_
        self.prev = prev


class TestLinkedList():
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.middle = self.head
        self.head.next_ = self.tail
        self.tail.prev = self.head
        self.length = 0

    def insert(self, prev_node: Node, val):
        new_node = Node(val, prev_node.next_, prev_node)
        prev_node.next_.prev = new_node
        prev_node.next_ = new_node
        if len(self) % 2 == 0:
            self.middle = self.middle.next_
        self.length += 1
        return new_node

    def remove(self, node: Node):
        node.prev.next_ = node.next_
        node.next_.prev = node.prev
        if len(self) == 1:
            self.middle = self.head
        elif len(self) % 2 == 0:
            self.middle = self.middle.next_
        self.length -= 1
        return node

    def push_back(self, val):
        return self.insert(self.tail.prev, val)

    def pop_front(self):
        return self.remove(self.head.next_)

    def insert_middle(self, val):
        return self.insert(self.middle, val)

    def __len__(self):
        return self.length


if __name__ == '__main__':
    N = int(input())
    shops = [TestLinkedList() for _ in range(N)]
    for line in sys.stdin:
        cmd = line.split()
        c_i = cmd[0]
        q_i = int(cmd[1]) if len(cmd) > 1 else None
        id_i = int(cmd[2]) if len(cmd) > 2 else None
        if c_i == '#':
            break
        shop = shops[q_i]
        if c_i == '+':
            shop.push_back(id_i)
        elif c_i == '!':
            shop.insert_middle(id_i)
        elif c_i == '-':
            res = shop.pop_front()
            print(res.value)
        elif c_i == '?':
            print(len(shop))
