from solution import Node, cloneGraph


def test_clone_graph():
    # Create graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    # Clone it
    cloned = cloneGraph(node1)

    # Check values
    assert cloned.val == 1
    assert cloned.neighbors[0].val == 2
    assert cloned.neighbors[1].val == 4

    # Verify deep copy
    assert cloned is not node1
    assert cloned.neighbors[0] is not node2
    assert cloned.neighbors[1] is not node4


def test_empty_graph():
    assert cloneGraph(None) is None


def test_single_node():
    node = Node(1)

    cloned = cloneGraph(node)

    assert cloned.val == 1
    assert cloned is not node
    assert cloned.neighbors == []


def test_circular_reference():
    node1 = Node(1)
    node2 = Node(2)

    node1.neighbors = [node2]
    node2.neighbors = [node1]

    cloned = cloneGraph(node1)

    assert cloned is not node1
    assert cloned.neighbors[0] is not node2
    assert cloned.neighbors[0].neighbors[0] is cloned