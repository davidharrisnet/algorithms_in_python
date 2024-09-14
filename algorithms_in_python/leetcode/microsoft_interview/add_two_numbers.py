class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        l1str = ""
        l2str = ""
        l1curr = l1
        l2curr = l2
        while l1curr is not None:          
           l1str += str(l1curr.val)
           l1curr = l1curr.next           
           if l2curr:
               l2str += str(l2curr.val)
               l2curr = l2curr.next               
                                 
        l1str = l1str[::-1]  
        l2str = l2str[::-1]
        sum = int(l1str) + int(l2str)
        rsum = str(sum)[::-1]
        head = ListNode(list(rsum)[0])
        curr = head
        for i in list(rsum[1:]):
            curr.next = ListNode(i)
            curr = curr.next
        return head

        
           
if __name__ == "__main__":
    
    #l1 = [2,4,3]
    
    l1arr = [9,9,9,9,9,9,9]
    
    l1head = ListNode(l1arr[0])
    curr = l1head
    for i in l1arr[1:]:
        curr.next = ListNode(i)
        curr = curr.next
        
    l2arr = [9,9,9,9]
    l2head = ListNode(l2arr[0])
    curr = l2head
    for i in l2arr[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    
           
    res = addTwoNumbers(l1head,l2head)
    curr = res
    while curr is not None:
        print(curr.val)
        curr = curr.next

