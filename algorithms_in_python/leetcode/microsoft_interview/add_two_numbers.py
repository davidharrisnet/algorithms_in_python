class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        h1 = l1
        h2 = l2
        head = None
        sumList1 = sumList2 = ""
        
        while h1 and h2:
            c1 = l1
            n1 = l1.next

            c2 = l2
            n2 = l2.next
                        
            while n1 is not None:
                sumList1 += str(c1.val)
                c1 = n1                
                n1 = n1.next
                sumList2 += str(c2.val)
                c2 = n2                
                n2 = n2.next
                                                            
           
            """
            if head is None:
                head = sumNode
            else:
                curr = head
                next = head.next
                while next is not None:
                    curr = next
                    next = next.next
                curr.next = sumNode
            """
        return head
        

if __name__ == "__main__":
    
    #l1 = [2,4,3]
 
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    
    #l2 = [5,6,4]
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    res = addTwoNumbers(l1,l2)
    print(res)

