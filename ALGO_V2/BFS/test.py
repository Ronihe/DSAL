n = len(str)
longest_sub = ""

for i in range(1, n + 1):
    sub_str = str[:i]


def if_substring(str, sub_string):
    str_len = len(str)
    substr_len = len(sub_string)

    if str_len % sub_string != 0:
        return False

    longeste_sub = [[0 for x in range(n + 1)] for y in range(n + 1)]

    result = ""
    result_len = 0
    idx = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            if (str[i - 1] == str[j - 1]) and longeste_sub[i - 1][j - 1] < (j - i):
                longeste_sub[i][j] = longeste_sub[i - 1][j - 1]

                if (longeste_sub[i][j] > result_len):
                    result_len = longeste_sub[i][j]
                    idx = max(i, idx)

            else:
                longeste_sub[i][j] = 0

    if result_len > 0:
        for i in range(idx - result_len + 1, idx + 1):
            result_len = result_len + str[i - 1]

    if not result_len:
        return -1
    else:
        return result_len


ave the function ShortestPath(strArr) take strArr which will be an array of strings which models a non-looping Graph. The structure of the array will be as follows: The first element in the array will be the number of nodes N (points) in the array as a string. The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes. They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all.

An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. Your program should return the shortest path from the first Node to the last Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array. If no path between the first and last node exists, return -1. The array will at minimum have two nodes. Also, the connection A-B for example, means that A can get to B and B can get to A.
Examples
Input: ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]
Output: A-C-D-F
Input: ["4","X","Y","Z","W","X-Y","Y-Z","X-W"]
Output: X-W