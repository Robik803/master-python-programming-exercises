# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  return int(str(num)[::-1])
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
