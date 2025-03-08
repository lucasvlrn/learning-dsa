class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        

def reverseLinkedList(head: Optional[ListNode]) -> ListNode:
    new_list = None #uma nova lista apontando pro nada
    while head: #enquanto head existir
        next_node = head.next #ponteiro no nodo na frente do head
        head.next = new_list #viramos o ponteiro linkado para frente, para tras 
        new_list = head #new_list é igual ao head da linked list
        head = next_node #passamos o head para frente e reinicia o processo
        #passa tudo que esta () -> () para () <- () até o head apontar pro nada
    return new_list