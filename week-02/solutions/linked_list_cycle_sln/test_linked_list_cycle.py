import pytest
from solution import ListNode, hasCycle 
def test_empty_list():
    assert hasCycle(None) == False
 
 
def test_single_node_no_cycle():
    head = ListNode(1)
    assert hasCycle(head) == False
 
 
def test_single_node_self_cycle():
    head = ListNode(1)
    head.next = head
    assert hasCycle(head) == True
 
 
def test_two_node_cycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head  # cycle back to head
    assert hasCycle(head) == True
 
 
if __name__ == "__main__":
    test_has_cycle()
    test_empty_list()
    test_single_node_no_cycle()
    test_single_node_self_cycle()
    test_two_node_cycle()
    print("All tests passed!")
 