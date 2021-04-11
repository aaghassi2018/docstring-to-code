#hw8pr2
#Name: Ashkon Aghassi

def count_evens(nums):
  result = 0
  for i in nums:
    if i%2 == 0:
      result += 1
  
  return result

def big_diff(nums):
  large = nums[0]
  small = nums[0]
  for i in nums:
    if(i > large):
      large = i
    elif(i < small):
      small = i
  
  return large - small

def centered_average(nums):
  large = nums[0]
  small = nums[0]
  for i in nums:
    if(i > large):
      large = i
    elif(i < small):
      small = i
    
  nums.remove(small)
  nums.remove(large)
  
  result = 0
  for i in nums:
   result += i
  
  return result//len(nums)

def sum13(nums):
  result = 0
  i = 0
  while i < len(nums):
    if(nums[i] == 13):
      i += 2
    else:
      result += nums[i]
      i += 1

  return result

def sum67(nums):
  result = 0
  i = 0
  
  while(i < len(nums)):
    if(nums[i] == 6):
      i = i + nums[i:].index(7) + 1
    else:
      result += nums[i]
      i += 1
  
  return result

def has22(nums):
  i = 0
  while i < len(nums) - 1:
    if(nums[i] == 2 and nums[i+1] == 2):
      return True
    else:
      i += 1
  return False

def double_char(str):
  new  = ''
  for i in str:
    new += i*2
  
  return new

def count_hi(str):
  result  = 0
  i = 0
  
  while(i < len(str)-1):
    if(str[i] == 'h' and str[i+1] == 'i'):
      result += 1
      i += 2
    else:
      i += 1
  
  return result

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'dog':
      dog += 1
    elif str[i:i+3] == 'cat':
      cat += 1
   
  return cat == dog

def count_code(str):
  result = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      result += 1
  return result

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  if(b[0:len(a)] == a or b[len(b)-len(a): len(b)] == a or a[0:len(b)] == b or a[len(a)-len(b):len(a)] == b):
    return True
  else:
    return False

def xyz_there(str):
  i = 0
  
  while i < len(str) - 2:
    if str[i] == '.':
      i += 2
    elif str[i:i+3] == 'xyz':
      return True
    else:
      i += 1
  
  return False