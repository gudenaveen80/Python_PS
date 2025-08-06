# Testcase1 : Wonder  
# Output : nd  
# Explanation : The middle characters in the given word Wonder is nd.  
# Testcase1 : World  
# Output : r  
# Explanation : The middle character in the given word World is r.  Test Case 1 : 6969  
# Output : 96  
# Explanation : The middle character in the given number 6969 is 96. 


def middle_characters(input_str):
    length = len(input_str)
    if length % 2 == 1:
       
        middle = length // 2
        print(input_str[middle])
    else:
        middle_1 = length // 2 - 1
        middle = length // 2
        print(input_str[middle_1] + input_str[middle])

input_str = input("Enter a string or number: ")
middle_characters(input_str)

#  Write a program to check whether the sum of digits in the number except  
# first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal  
# Testcase1 : 75547  
# Output : equal  
# Explanation : In the given number 7557, first digit and last digit sum  that is sum(7,7)=14 is equal to sum of remaining numbers that is  sum(5,5,4) = 14. So both sums are equal.  
# Testcase1 : 765  
# Output : not equal  
# Explanation : Sum(7,5)=12 and Sum(6)=6, both sums are not equal.  

def check_sum_of_digits(number):
    # Convert the number to string for easy manipulation
    num_str = str(number)
    sum_middle = 0 
    
    # If the number has less than 3 digits, we cannot have middle digits to compare
    if len(num_str) < 3:
        print("not equal")
        return
    
    # Get the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    
    # Get the sum of the first and last digits
    sum_first_last = first_digit + last_digit
    
    # Get the sum of the middle digits
    middle_digits = num_str[1:-1]
    for digit in middle_digits:
      sum_middle += int(digit)
    
    # Compare the sums and print the result
    if sum_first_last == sum_middle:
        print("equal")
    else:
        print("not equal")

# Test the function
check_sum_of_digits(5266)  # Output: equal
check_sum_of_digits(2467)    # Output: not equal
