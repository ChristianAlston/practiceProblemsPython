# // Remove duplicates from this array [1,5,7,8,4,3,1,6,9,8,14] 


def fixed(list_here):
    return set(list_here)
print(fixed([1,5,7,8,4,3,1,6,9,8,14] ))

# // Check to see if a word is a palindrome (if you reverse a word and it is the same word (mom, dad, bob, racecar, etc)

def reverse_this(word):
    if word == word[::-1]:
        return 'your word is a word lol'

print(reverse_this('bob'))

# // How can you find the minimum and maximum numbers in an array?

def findMax(list_of):
    return max(list_of)
print(findMax([1,2,3,4,5]))


def findMin(list_of):
    return min(list_of)
print(findMin([1,2,3,4,5]))

# // Return the length of the longest word in this sentence: “Those who can imagine anything, can create the impossible.”

def findLongest(phrase):
    new_imporved = phrase.split(' ')
    longest_so_far = ' '
    for word in new_imporved:
        if len(word) > len(longest_so_far):
            longest_so_far = word
            print(len(word)) 
print(findLongest('hello therewoo nope ue'))

# // (quote from Alan Turing)
