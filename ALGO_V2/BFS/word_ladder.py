# https://www.lintcode.com/problem/word-ladder/description?_from=ladder&&fromId=1
import collections


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here

        # 1. find out all the words one distance away from the start
        # 2. if found return the distance
        # 3. if not, append the new data in the queue
        dict.add(end)
        q = collections.deque([start])
        visited = set([start])
        distance = 0

        while q:
            distance += 1
            # iterate through all the words one distance away

            for _ in range(len(q)):
                word = q.popleft()
                if word == end:
                    return distance

                for next_word in self.one_distance_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    q.append(next_word)
                    visited.add(next_word)

        return 0

    # O(26 * L^2) L is the length of the word
    def one_distance_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words






