# Python3 code to demonstrate working of 
# Test if list is Palindrome
# Using list slicing
  
# initializing list
test_list = [1, 4, 5, 4, 1]
  
# printing original list
print("The original list is :"+ str(test_list))
  
# Reversing the list
reverse = test_list[::-1]
  
# checking if palindrome
res = test_list == reverse
  # zr
# printing result 
print("Is list Palindrome :"+ str(res))