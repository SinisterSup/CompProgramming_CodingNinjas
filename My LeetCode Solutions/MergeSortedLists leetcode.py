#Best Solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, curr = m - 1, n - 1, (m + n) - 1

        while p2 >= 0 and p1 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[curr] = nums2[p2]
                p2 -= 1
            else:
                nums1[curr] = nums1[p1]
                p1 -= 1
            curr -= 1

        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1

#My Solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        j = m - 1
        k = -n

        if m + n == n:
            while k < 0:
                nums1[k] = nums2[k]
                k += 1

        for i in range(n - 1, -1, -1):

            while j >= 0:
                if j == 0 and nums2[i] < nums1[j]:
                    nums1.insert(j, nums2[i])
                    break
                if nums2[i] >= nums1[j]:
                    nums1.insert(j + 1, nums2[i])
                    break
                j -= 1

            if m + n != n:
                nums1.pop()

        return nums1