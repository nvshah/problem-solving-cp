# https://leetcode.com/problems/max-dot-product-of-two-subsequences


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        rows, cols = len(nums1), len(nums2)
        # add 1 extra for boundary lookups
        table = [[float("-inf")] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                r, c = i + 1, j + 1  # effective row column in table

                # Choices
                # 1. current pair as scalar (ie dot product of 2 scalars)
                # 2. current pair + prev-dimensions
                # 3. exclude one of dimension of current pair
                #    a. from nums1 or from nums2

                scalar = nums1[i] * nums2[j]  # 1 dimension dot product
                vector = scalar + table[r - 1][c - 1]
                best = max(scalar, vector, table[r - 1][c], table[r][c - 1])
                table[r][c] = best

        return table[-1][-1]  # bottom right cell
