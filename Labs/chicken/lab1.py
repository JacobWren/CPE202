def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   
   if int_list == []:
      return None
   if int_list == None:
      raise ValueError
   l = len(int_list)
   if l == 1:
      return int_list[0]
   for i in range(l - 1):
      if i == 0: # Find initial max between first 2 nums in list
         if int_list[i + 1] > int_list[i]:
            max = int_list[i + 1]
         else:
            max = int_list[i]
      if i != 0:
         if int_list[i + 1] > max:
            max = int_list[i + 1]
   return max

#print(max_list_iter([]))


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   length = len(int_list)
   if length == 0 or length == 1:
      return int_list
   return [int_list.pop()] + reverse_rec(int_list[0:length - 1])

#print(reverse_rec([2, 1, 5, 4]))


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   
   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   if low == high:
      if target == int_list[low]:
         return low
      else:
         return None # No match
   mid = int((low + high) / 2)
   if target == int_list[mid]:
      return mid
   if target > int_list[mid]:
      y = mid + 1
      low = min(y, high)
   else:
      x = mid - 1
      high = max(x, low)
   return bin_search(target, low, high, int_list)

#print(bin_search(6, 0, 4, [1, 2, 4, 6, 7]))
#print(bin_search(3, 0, 4, [1, 2, 4, 6, 7]))
#print(bin_search(1, 0, 0, None))

#x = list(range(2, 50000, 2))
#for i in range(1, 50000, 2):
   #self.assertEqual(lab1.bin_search(i, 0, 25000, x), None)
#try:
   #for i in range(1, 50000, 2):
      #bin_search(i, 0, 2498, x)
#except RecursionError:
  # print(i)
#print(bin_search(13, 0, 23, x))
