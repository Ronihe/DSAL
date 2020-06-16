class Anagram:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value' here
        for word in line.split():
            print(word)
            yield "".join(sorted(list(word))), word

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        print(key, values)
        yield key, list(values)

a = Anagram()
a.mapper("hi", "hi hello you")
print(a.)