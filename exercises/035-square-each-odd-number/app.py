def square_odd_numbers(seq):
    return [num for num in [int(x)**2  for x in seq.split(',')] if num%2==1]

print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))