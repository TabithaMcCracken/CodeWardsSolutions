"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the 
3missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
line = '123456789'
n = 2

char_list = [line[i:i+n] for i in range(0, len(line), n)]

if len(char_list[-1]) == 1:
    char_list[-1] += '_'

value = 

print(char_list)