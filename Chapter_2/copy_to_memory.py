first = [1,2,3,4,5,6]
print(f"first : {first}")

#any changes made to the second is done to the first also
second = first
second.extend([7,8])
print(f"second : {second}")
print(f"again first : {first}")

# if we run on copy of second, it doesn't modify the second.
third = second.copy()
third.extend([9,10])
print(f"third : {third}")
print(f"again second : {second}")