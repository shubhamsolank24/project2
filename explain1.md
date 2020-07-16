Problem 1 explaination:
In the first task of this project i have to make a data structure for a Least Recently Used (LRU) cache with O(1) operations. so  have used dictionary in python which has constant time access of values with particular key. To keep track of the order of the values I have created a queue with the help of python deque, which allows constant time popleft().

Get Time complexity: O(1) 
Set Time complexity: O(1)

Space complexity of the LRU will be : O(capacity)


Problem 2 explaination:
I have written a recursive function for this task which takes input of the suffix, path and the list of required files which are found till now. Each time I find a file ending with .c it will be appended to this file.

Run time complexitywill be : O(depth X Avg. number of directory in each level)

Space complexity will be: O(depth)



Problem 3 explaination: 
I have implemented huffman encoding technique here with following steps:

i) Calculate the occurences of each characters in a string. ii) Character with highest occurence is encoded with minimum code length i.e. 1 then next Character as 01 and then 001 and so on.

Time complexity is : O(n) Space complexity: O(distinct_characters)


Problem 4 explaination:
Active Directory This problem in this task is being resolved using recurssion, starting from the root, checking if user is present for each group visited, if the user matches then it returns.

The worst case is if the user is not present on any group and the group structure has the same subgroups on each, taking O(n!) worst case, since a stack if used for recurssion the space complexity would be O(n)


Problem 5 explaination:
Blockchain A linked list is used in htis task since is easier to keep track of previous item on the blockchain, retrieval for the last block is O(1) and the first one O(n).

Hash Function: the hash function is calculated ciphering the data with sha256 using utf-8 encode, then with the encoded data as hex string we add another encode that is the timestamp ciphering the data twice.

Hash function and inserting a block are O(1), printing the whole blockchain is O(n).


Pronlem 6 explaination:
