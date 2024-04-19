from collections import deque

class MovingAverage:

  def __init__(self, window_size):
    self.queue = deque()
    self.window_size = window_size
    self.total = 0

  def next(self, val):
    if self.window_size < 1: return None

    self.queue.append(val)

    if len(self.queue) > self.window_size:
      self.total -= self.queue.popleft()

    self.total += val

    return round(self.total / len(self.queue), 2)

def main():
  ma2 = MovingAverage(2)
  print('Test 1:',
        [ma2.next(4), ma2.next(6)] == 
        [4.0, 5.0])

  ma2 = MovingAverage(2)
  print('Test 1:',
        [ma2.next(4), ma2.next(6), ma2.next(14)] == 
        [4.0, 5.0, 10.0])

  ma1 = MovingAverage(1)
  print('Test 2:', 
        [ma1.next(1), ma1.next(0), ma1.next(1), ma1.next(0), ma1.next(1)] == 
        [1.0, 0.0, 1.0, 0.0, 1.0])

  ma0 = MovingAverage(0)
  print('Test 3:', 
        [ma0.next(5), ma0.next(8), ma0.next(3)] == 
        [None, None, None])

  ma3 = MovingAverage(3)  
  print('Test 4:', 
        [ma3.next(1), ma3.next(10), ma3.next(3), ma3.next(5)] == 
        [1.0, 5.5, 4.67, 6.0])

main()