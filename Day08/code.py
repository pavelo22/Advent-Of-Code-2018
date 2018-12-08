import time


class Node:
    def __init__(self):
        self.quantity_child_nodes = None
        self.quantity_metadata = None
        self.child_nodes = list()
        self.meta_data = list()
        self.size = None


def build_node(_data):
    _idx = 0
    node = Node()
    node.quantity_child_nodes = _data[_idx]
    node.quantity_metadata = _data[_idx + 1]

    if node.quantity_child_nodes == 0:
        node.meta_data = _data[_idx + 2:_idx + 2 + node.quantity_metadata]
        node.size = 2 + node.quantity_metadata
    else:
        internal_idx = 2
        for i in range(node.quantity_child_nodes):
            new_node = build_node(_data[internal_idx:])
            node.child_nodes.append(new_node)
            internal_idx += new_node.size

        node.meta_data = _data[_idx + internal_idx:_idx + node.quantity_metadata + internal_idx]
        node.size = internal_idx + node.quantity_metadata
    return node


def traverse_tree1(node):
    meta_data_sum = sum(node.meta_data)
    for _node in node.child_nodes:
        meta_data_sum += traverse_tree1(_node)
    return meta_data_sum


def traverse_tree2(node):
    if node.quantity_child_nodes == 0:
        return sum(node.meta_data)

    meta_data_sum = 0
    for child_idx in node.meta_data:
        if len(node.child_nodes) < child_idx:
            continue
        meta_data_sum += traverse_tree2(node.child_nodes[child_idx - 1])
    return meta_data_sum


with open('data') as file_in:
    data = file_in.read().split(' ')

start = time.time()
data = [int(i) for i in data]

root_node = build_node(data[0:])
print('Part1', traverse_tree1(root_node))
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))

start = time.time()
print('Part2', traverse_tree2(root_node))
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
