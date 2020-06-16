class RoniHeap:
    def heapify(self, A):
        # sift up
        for i in range(len(A)):
            self.sift_up(A, i)

        # sift down
        for i in range(len(A) // 2, -1 - 1):
            self.sift_down(A, i)

    def sift_up(self, A, k):
        while k != 0:
            parent = (k - 1) // 2
            if A[k] > A[parent]:
                break
            A[k], A[parent] = A[parent], A[k]
            k = parent

    def sift_down(self, A, k):
        n = len(A)
        while k < n:
            left = k * 2
            right = k * 2 + 1
            minIdx = k

            if left < n and A[left] < A[minIdx]:
                minIdx = left
            if right < n and A[right] < A[minIdx]:
                minIdx = right
            if minIdx == k:
                break
            A[minIdx], A[k] = A[k], A[minIdx]
            k = minIdx
