def merge(nums1, m, nums2, n):
    i ,j , k = m -1 , n - 1 , m + n -1

    for _ in range(m+n):
        if i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -=1
            else:
                nums1[k] = nums2[j]
                j -=1
        elif i >=0:
            nums1[k] = nums1[i]
            i -=1
        else:
            nums1[k] = nums2[j]
            j -=1
        k -=1
