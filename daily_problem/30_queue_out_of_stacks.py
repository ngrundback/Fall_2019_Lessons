'''
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out)
data structure with the following methods: enqueue, which inserts an element into the queue,
and dequeue, which removes it.
'''


class Queue():
  def __init__(self):
    self.s1 = []
    self.s2 = []

  def enqueue(self, data):
    self.s1.append(data)

  def dequeue(self):
    if self.s2:
      return s2.pop()
    if self.s1:
      while self.s1:
        self.s2.append(self.s1.pop())
      return self.s2.pop()
    return None




if __name__ == '__main__':

  bork = Queue()

  for x in range(5):
    bork.enqueue(x)

  print(bork.s1)
  print(bork.dequeue())

  # print(bork.s2)
  # print(bork.s1)
