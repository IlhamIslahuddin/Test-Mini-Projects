linked_list_values = [10,15,16,72,84]
linked_list_pointers = [2,4,3,1,None]

# linked_list_pointers.pop()

node0 = (linked_list_values[0],linked_list_pointers[0])
print (f"Node0 value: {node0[0]}, next node index: {node0[1]}")

def next_node(tuple):
    next_index = tuple[1]
    next_node = (linked_list_values[next_index],linked_list_pointers[next_index])
    return next_node

new = next_node(node0)
print (f"Node that node0 points to: {new}")
