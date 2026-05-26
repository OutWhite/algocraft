class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        ptr_nums1: int = m - 1
        ptr_nums2: int = n - 1
        ptr_res: int = m + n - 1
        
        while ptr_nums1 >= 0 and ptr_nums2 >= 0:
            if nums1[ptr_nums1] > nums2[ptr_nums2]:
                nums1[ptr_res] = nums1[ptr_nums1]
                ptr_nums1 -= 1
            else:
                nums1[ptr_res] = nums2[ptr_nums2]
                ptr_nums2 -= 1
            ptr_res -= 1
        
        while ptr_nums2 >= 0:
            nums1[ptr_res] = nums2[ptr_nums2]
            ptr_nums2 -= 1
            ptr_res -= 1
