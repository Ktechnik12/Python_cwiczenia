from queue import RandomQueue
rq = RandomQueue()

rq.insert(10)
rq.insert(20)
rq.insert(30)
rq.insert(40)
rq.insert(50)

print(rq.remove())
print(rq.remove())

print(rq.is_empty())
print(rq.is_full())
rq.clear()
print(rq.is_empty())
