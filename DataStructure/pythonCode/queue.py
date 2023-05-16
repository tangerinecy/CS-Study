#!/usr/bin/env python3

# Uses deque
# Pushes(Enqueues) to front, Pops(Dequeues) from back

from collections import deque

queue = deque([])
queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)
print("queue: ", queue)
print("pop: ", queue.pop())
print("pop: ", queue.pop())
print("queue: ", queue)
