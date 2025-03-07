def enqueue(queue,name):
    print (f"Before enqueue: {queue}")
    queue.append(name)
    print (f"Enqueued: {name}")
    print (f"After enqueue: {queue}")
def dequeue(queue):
    print (f"Before dequeue: {queue}")
    if len(queue) == 0:
        print ("Queue is empty, Failed to dequeue.")
    else:
        popped = queue.pop(0)
        print (f"Dequeued: {popped}")
        print (f"After dequeue: {queue}")

if __name__ == "__main__":
    queue_list = ["Alice","Bob","Carlos","Dante"]
    enqueue(queue_list,"Ethan")
    dequeue(queue_list)
    dequeue(queue_list)
