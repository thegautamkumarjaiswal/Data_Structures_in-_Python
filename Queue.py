# create a queue class #
class Queue:
    # define the function #
    def __init__(self, c):
        self.queue = []
        self.front = self. rear = 0
        self.size = c

    # insertion in queue #
    def enqueue(self, data):
        if self.size == self.rear:
            print("\nQueue is full.")

        else:
            self.queue.append(data)
            self.rear += 1
    # deletion in queue #
    def dequeue(self,):
        if self.front == self.rear:
            print("Queue is empty.")

        else:
            x = self.queue.pop(0)
            self.rear -= 1

    # display the elements in queue #
    def queue_diplay(self):
        if self.front == self.rear:
            print("\nQueue is empty.")

        for i in self.queue:
            print(i, " ", end=" ")

    # front of queue after insertion or deletion #
    def queue_front(self):
        if self.front == self.rear:
            print("\nQueue is empty.")
        print("\n front Empty is:", self.queue[self.front])

# main function #
if __name__ == '__main__':
    q = Queue(4)
    q.queue_diplay()

    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.queue_diplay()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print("\n\n after two node deletion")

    q.queue_diplay()

    print("\n\n add a new node")
    q.enqueue(60)
    q.enqueue(70)

    q.queue_diplay()

    print("\n")
    q.queue_front()

