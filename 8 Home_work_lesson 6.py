#Assertive Lists: The Art of Coding Confidence

# 1. Write a Python program to compute the difference between two lists. Don`t use sets here
#     Sample data: ['a', 'b', 'c', 'd'], ['c', 'd', 'e']
#     Expected Output:
#     first-second: ['a', 'b']
#     second-first: ['e']
#     ```python
#     def compute_difference(first: list, second: list) -> tuple:
#         # write your code here
#         pass

sample_data_1 = ['a', 'b', 'c', 'd']
sample_data_2 = ['c', 'd', 'e']

def compute_difference (sample_data_1,sample_data_2):

    diff_1minus2 = []
    for i in sample_data_1:
        if i not in sample_data_2:
            diff_1minus2.append(i)
 #   print(diff_1minus2)
    
    diff_2minus1 = []
    for j in sample_data_2:
        if j not in sample_data_1:
            diff_2minus1.append(j)
  #  print(diff_2minus1)
    return diff_1minus2, diff_2minus1

result = compute_difference(sample_data_1,sample_data_2)
print (result)

def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])
    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])
    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])
    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])


# 2. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
#     **Example 1:**
#     Input: nums = [2,7,11,15], target = 9
#     Output: [0,1]
#     Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#     **Example 2:**
#     Input: nums = [3,2,4], target = 6
#     Output: [1,2]
#     **Example 3:**
#     Input: nums = [3,3], target = 6
#     Output: [0,1]
#     ```python
#     def sum_of_two(nums: list, target: int) -> list:
#         # write your code here
#         pass

Input_nums1 = [[2,7,11,15],9]
# Input_nums1 = [[3,2,4],6]
# Input_nums1 = [[3,3],6]

nums1 = Input_nums1[0]
target1 = Input_nums1[1]

def sum_of_two(nums1, target1):
    index_counter1 = 1
    for i1 in range(len(nums1)):
        for j1 in range(len(nums1[index_counter1:])):
            if nums1[i1] + nums1[j1 + index_counter1] == target1:
                return [i1, j1 + index_counter1]
        index_counter1 += 1

result1=sum_of_two(nums1, target1)
print(result1)


def test_sum_of_two():
    result1 = sum_of_two([2,7,11,15], 9)
    assert result1 == [0, 1]
    result2 = sum_of_two([3,2,4], 6)
    assert result2 == [1, 2]
    result3 = sum_of_two([3,3], 6)
    assert result3 == [0, 1]

test_sum_of_two()


# 3. Write a program that takes a list of integers as input and returns a new list that contains only the elements that are unique 
#(i.e., that appear only once in the list). For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output list should be [1, 3, 4]. 
#     ```python
#     def unique_elements(arr: list) -> list:
#         # write your code here
#         pass

input_list = input('Enter figures with comma and a space as a separator: ').split(', ')
input_list = [int(x) for x in input_list]

def unique_elements(array: list):
    res = []
    for number in array:
        if array.count(number) == 1:
            res.append(number)
    return res

result_unique = unique_elements(input_list)
print(result_unique)

def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []


# 4. Write a program that takes a list of integers as input and returns a new list
# that contains only the elements that appear an odd number of times in the list. 
# For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output list should be [1, 3, 4].
#     ```python
#     def odd_elements(arr: list) -> list:
#         # write your code here
#         pass
#     def test_odd_elements():
#         result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
#         assert result1 == [1, 3, 4]
#         result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
#         assert result1 == [1, 3, 4, 6]

input_list_odd = input('Enter figures with comma and a space as a separators: ').split(', ')
input_list_odd = [int(x) for x in input_list_odd]

def unique_elements(arr: list):
    return [number for number in arr if arr.count(number) % 2 != 0]

result_odd_input = unique_elements(input_list_odd)
print(result_odd_input)


# 5. Write a program that takes a list of integers as input and returns the second-largest element in the list. 
# If the list has fewer than two elements, the program should return None. 
# For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the program should return 5. Don`t use the sort method.
#     ```python
#     def second_largest_element(arr: list) -> int:
#         # write your code here
#         pass
    
input_list_top_2nd = input('Enter figures with comma and a space as a separator: ').split(',')
input_list_top_2nd = [int(x) for x in input_list_top_2nd]

def second_largest_element(arr: list) -> int | None:
    if len(arr) < 2:
        return None
    max_el = max(arr)
    arr = [x for x in arr if x != max_el]
    return max(arr)

print(second_largest_element(input_list_top_2nd))

def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5
    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4
    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None


# 6. Sort the following list by population. Calculate average and total population for cities from this list:
Population = [
('New York City', 8550405),
('Los Angeles', 3792621),
('Chicago', 2695598),
('Houston', 2100263),
('Philadelphia', 1526006),
('Phoenix', 1445632),
('San Antonio', 1327407),
('San Diego', 1307402),
('Dallas', 1197816),
('San Jose', 945942),
]

def my_soring(row):
    return row[1]

values = sorted([(r[0], r[1]) for r in Population], reverse=True, key=my_soring)

for i in Population:
    print(i)
values = [x[1] for x in Population]
print('Average:', sum(values)/len(values))
print('Total Sum:', sum(values))