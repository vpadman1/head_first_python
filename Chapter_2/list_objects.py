# list methods

# creating a new list 
nums = [12,3,4,5,6,7,8]

# remove - remove is only used if we know the value in the list that needs to be removed. 
nums.remove(7)
print(nums)

# pop - takes the index as an input argument, if the index is not provided it will remove the last value by default.
nums.pop(0)
print(nums)

# Extend - this helps in extending the list - it takes a list as an input unlike an append where it takes a single object as an argument
nums.extend([55,20])
print(nums)

# Insert - this method takes in two arguments, one is index and another is value.
nums.insert(0,15)
print(nums)