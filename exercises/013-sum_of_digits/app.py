# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
    n = str(num)
    sum = 0
    for d in n:
      sum += int(d)  
    return sum


# Invoke the function with any three-digit number
print(digits_sum(123))
