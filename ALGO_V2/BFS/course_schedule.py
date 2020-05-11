# https://www.lintcode.com/problem/course-schedule/description?_from=ladder&&fromId=1
from collections import deque


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish_v1(self, numCourses, prerequisites):
        # write your code here
        # create a mapping to match the course name and prerequisites{0: [1, 2], }
        # find the course prerequisites is 0
        # iterate through all the courses and remove the course from prerequisites
        # until the mapping is empty=
        prerequisites_set = prerequisites

        mapping = {c: [0, set()] for c in range(numCourses)}

        for pair in prerequisites_set:
            mapping[pair[0]][0] += 1
            mapping[pair[0]][1].add(pair[1])

        # find the set is empty
        # keep pusing all the courses with 0 prerequisite
        q = deque()
        next_courses = self.find_course(mapping)
        print(next_courses)

        if not next_courses:
            return not mapping
        q = deque(next_courses)
        while q:
            next_courses = self.find_course(mapping)
            for course in next_courses:
                q.append(course)
                del mapping[course]
                for c in mapping:
                    if c in mapping[c][1]:
                        mapping[c][0] -= 1

        print("mm", q, mapping)
        return not mapping

    def find_course(self, mapping):
        return [c for c in mapping if not mapping[c][0]]

    # 建图并记录所有节点的入度。
    # 将所有入度为0的节点加入队列。
    # 取出队首的元素now，将其加入拓扑序列。
    # 访问所有now的邻接点nxt，将nxt的入度减1，当减到0后，将nxt加入队列。
    # 重复步骤3、4，直到队列为空。
    # 如果拓扑序列个数等于节点数，代表该有向图无环，且存在拓扑序。

    # 时间复杂度O(V + E)
    # 建图，扫描一遍所有的边O(E)。
    # 每个节点最多入队出队1次，复杂度O(V)。
    # 邻接表最终会被遍历1遍，复杂度O(E)。
    # 综上，总复杂度为O(E + V)。
    # 空间复杂度O(E + V)
    # 邻接表占用O(E + V)的空间。
    # 队列最劣情况写占用O(V)的空间。
    # 综上，总复杂度为O(V + E)。
    def CanFinish_v2(self, numCourses, prerequisites):
        #         to decide if it is a toplogical sorted, also need to check the list and prerequisites and total number of prequsites
        mapping = {c: set() for c in range(numCourses)}
        degree = [0 for c in range(numCourses)]
        taken = 0
        q = deque()

        for c, p in prerequisites:
            mapping[c].add(p)
        for c in mapping:
            degree[c] = len(mapping[c])

        for i in range(coursenum):
            if degree[i] == 0:
                q.append(i)
        print(mapping, degree)
        while q:
            print(degree, mapping, q)
            next_course = q.popleft()
            taken += 1

            for course in mapping:
                if next_course in mapping[course]:
                    degree[course] -= 1
                    if degree[course] == 0:
                        q.append(course)
        print(taken)
        return taken == numCourses

    def CanFinish(self, numCourses, prerequisites):
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        print(edges, degrees)

        queue, count = deque([]), 0

        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count += 1

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return count == numCourses

    def findOrder(self, numCourses, prerequisites):
        # write your code here
        # find the corse x has no prerequisite,
        # remove the relation of the courses with x
        # loop until there is no courses left

        # relation mapiing, for n courses
        edge = {c: [] for c in range(numCourses)}
        # keep track of the number of courses depends on it
        degrees = {c: 0 for c in range(numCourses)}

        q = deque()
        order = []

        for c, p in prerequisites:
            edge[p].append(c)
            degrees[c] += 1
        for c in degrees:
            if degrees[c] == 0:
                q.append(c)

        while q:
            course2take = q.popleft()
            order.append(course2take)

            for p in edge[course2take]:
                degrees[p] -= 1
                if degrees[p] == 0:
                    q.append(p)

        return order if (len(order) == numCourses) else []


s = Solution()
coursenum = 10
prerequisites = [[5, 8], [3, 5], [8, 1], [4, 5], [0, 2], [1, 9], [7, 8], [4, 9]]

r = s.CanFinish(coursenum, prerequisites)

print(r)

# https://www.jiuzhang.com/solution/course-schedule-ii/#tag-highlight-lang-python