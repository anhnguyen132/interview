"""
Implement a function to increment an arbitrary precision integer represented in the form of an array, where each element in the array corresponds to a digit.

Examples:

Input: [1,2,3]
Output: [1,2,4]
Explanation: 123 + 1 = 124

Input: [5,8,9]
Output: [5,9,0]
Explanation: 589 + 1 = 590
"""
def increment(digits):
    i = len(digits) - 1
    output = []
    remember = 0
    while (i >= 0):
        if i == len(digits) - 1:
            sum = digits[i] + 1
            output.append(sum % 10)
            if sum // 10 > 0:
                remember = 1
        else:
            if remember == 1:
                sum = digits[i] + 1
                output.append(sum % 10)
                if sum // 10 > 0:
                    remember = 1
                else:
                    remember = 0
            else:
                output.append(digits[i])
            
        i -= 1

    if remember == 1:
        output.append(1)
    
    # print(output)
    output.reverse()
    return output

print(increment([1,2,3]) == [1,2,4])
print(increment([5,8,9]) == [5,9,0])
print(increment([9]) == [1,0])
