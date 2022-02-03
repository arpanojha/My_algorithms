class sliding_window:
  def __init__(self,k,arr):
    self.array = arr
    self.k = k
  def calculate_max(self):
    """
    input: array, window size k
    output:
    max value according to window size. 
    """
    m = []
    j=a[0]
    for i in range(self.k):
      if self.array[i]>j:
        j=self.array[i]
      m.append(j)
    for i in range(self.k,len(self.array)):
      if self.array[i]>m[-1]:
        m.append(self.array[i])
      else:
        m.append(m[len(m)-1])
    return m
