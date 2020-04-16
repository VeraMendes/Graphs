'''
Given two words (begin_word and end_word), and a dictionary's word list,
 return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that
begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
'''

# def words_are_neighbors(w1, w2):
#     if len(w1) != len(w2):
#         return False
#     for i in range (len(w1)):
#         if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
#             return True
#         return False

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
      word_set.add(word.lower())

def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    # print(string_word)
    for i in range(len(string_word)):
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)



def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue( [begin_word] )
    while q.size() > 0:
        # print(q.queue)
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)


# print(get_neighbors('sail'))
# print(word_set)
# print(find_word_ladder("sail", "boat"))