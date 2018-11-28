'''
Author: Nicole Torres
CS2302: Lab 5A
EXTRA CREDIT
'''
import heapq


# 1. Kth Largest element in an Array
class Solution:
    def sift(self, nums, low, high):
        i, j = low, 2 * low
        tmp = nums[i]
        while j <= high:
            if j < high and nums[j] < nums[j + 1]:
                j += 1
            if tmp < nums[j]:
                nums[i] = nums[j]
                i = j
                j = 2 * i
            else:
                break
        nums[i] = tmp

    def findKthLargest(self, nums, k):
        n = len(nums)
        for i in range(n // 2, -1, -1):
            self.sift(nums, i, n - 1)
        for i in range(n - 1, n - 1 - k, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.sift(nums, 0, i - 1)
        return nums[i]


# 2. Super ugly numbers are positive numbers whose all prime
# factors are in the given prime list primes of size k.
class Solution2:
        def nthSuperUglyNumber(self, n, primes):
            """
            :type n: int
            :type primes: List[int]
            :rtype: int
            """
            ans = [1] * n
            q = [[prime, 0, prime] for prime in primes]
            heapq.heapify(q)

            for i in range(1, n):
                cur = heapq.heappop(q)
                ans[i] = cur[0]

                while q and q[0][0] == ans[i]:
                    t = heapq.heappop(q)
                    t[1] += 1
                    t[0] = ans[t[1]] * t[2]
                    heapq.heappush(q, t)
                cur[1] += 1
                cur[0] = ans[cur[1]] * cur[2]
                heapq.heappush(q, cur)

            return ans[n - 1]


# 3. Write a program to find the n-th ugly number. Ugly numbers
# are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note that 1 is typically treated as an ugly number.
class Solution3:
    pool = set()
    seq = []
    hpq = [1]

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        while len(self.seq) < n:
            i = heapq.heappop(self.hpq)
            self.seq.append(i)
            for j in (i * 2, i * 3, i * 5):
                if j not in self.pool:
                    self.pool.add(j)
                    heapq.heappush(self.hpq, j)
        else:
            return self.seq[n-1]


if __name__ == '__main__':

    # 1.
    nums, k = [3, 2, 1, 5, 6, 4], 2
    solu = Solution()
    print(solu.findKthLargest(nums, k))

    # 2.
    n = 12
    ints = [2, 7, 13, 19]
    solu2 = Solution2()
    print(solu2.nthSuperUglyNumber(n, ints))

    # 3.
    f = 10
    solu3 = Solution3()
    print(solu3.nthUglyNumber(f))
