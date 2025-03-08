class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_front(self,value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
    
    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
    
    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value
    
    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail= self.tail.prev
        if self.tail:
            self.tail.prev = None
        else:
            self.head = None
        return removed_value
    

linked_list = DoublyLinkedList()

# Adicionando elementos ao início
linked_list.add_to_front(10)
linked_list.add_to_front(20)
linked_list.add_to_front(30)

# Adicionando elementos ao final
linked_list.add_to_end(40)
linked_list.add_to_end(50)

removed_from_front = linked_list.remove_from_front()
print(f"Removido do início: {removed_from_front}")

# Removendo do final
removed_from_end = linked_list.remove_from_end()
print(f"Removido do final: {removed_from_end}")

current = linked_list.head
print("Lista após remoções do início ao fim:")
while current:
    print(current.value, end=" ")
    current = current.next
print()

# Imprimindo a lista do fim ao início
current = linked_list.tail
print("Lista após remoções do fim ao início:")
while current:
    print(current.value, end=" ")
    current = current.prev
print()