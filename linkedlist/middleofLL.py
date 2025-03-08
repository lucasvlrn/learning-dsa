class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:       
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head #definimos um ponteiro no inicio da LL
        while ahead and ahead.next: #enquanto houver valor no ahead e um valor depois de ahead
            ahead = ahead.next.next #ahead anda duas casas
            head = head.next #head anda apenas uma
        return head #retorna head
    
    #toda vez que ahead chegar no fim da lista, head estará no meio