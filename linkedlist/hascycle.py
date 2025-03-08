class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head #um ponteiro para andar lento
        fast = head #um ponteiro para andar rapido
        while fast and fast.next: #enquanto fast ter um valor e houver outro nodo alem de fast
            slow = slow.next #o ponteiro slow anda 1a casa
            fast = fast.next.next #e o ponteiro fast duas
            if fast == slow: #se os dois forem iguais
                return True #achamos o ciclo e retornamos true
        return False    #caso nao, não há ciclo
        
