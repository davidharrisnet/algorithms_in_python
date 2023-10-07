from algorithms_in_python.data_structures.linked_list import linked_list, single_linked_list_extra

from algorithms_in_python.data_structures.linked_list.single_linked_list_extra import SingleLinkedList
from algorithms_in_python.data_structures.linked_list.node import SingleNode


def find_middle(ll: SingleLinkedList):

    index = 0
    curr = ll.head
    while curr:
        curr = curr.next
        index += 1
    print(index)
    if index %2 == 0: # even
        middle2 = index // 2
        middle1 = middle2 - 1
        index = 0
        curr = ll.head
        while(index < middle1):
            curr = curr.next
            index += 1
        return (curr.data, curr.next.data)
    else:
        middle = index // 2
        index = 0
        curr = ll.head
        while(index < middle):
            curr = curr.next
            index += 1
        return (curr.data)



if __name__ == "__main__":

    nodes = [ SingleNode(i) for i in list(range(0,4))]
    l = SingleLinkedList();
    for n in nodes:
        l.add_head(n)

    r = find_middle(l)
    print(r)


    nodes = [ SingleNode(i) for i in list(range(0,5))]
    l = SingleLinkedList();
    for n in nodes:
        l.add_head(n)

    r = find_middle(l)
    print(r)