Problem 1:
In the first task of this project i have to make a data structure for a Least Recently Used (LRU) cache with O(1) operations. so  have used dictionary in python which has constant time access of values with particular key. To keep track of the order of the values I have created a queue with the help of python deque, which allows constant time popleft().

Get Time complexity: O(1) 
Set Time complexity: O(1)

Space complexity of the LRU will be : O(capacity)


Problem2:
I have written a recursive function for this task which takes input of the suffix, path and the list of required files which are found till now. Each time I find a file ending with .c it will be appended to this file.

Run time complexitywill be : O(depth X Avg. number of directory in each level)

Space complexity will be: O(depth)




