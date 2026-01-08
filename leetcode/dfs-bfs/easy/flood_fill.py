# https://leetcode.com/problems/flood-fill


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start = (sr, sc)  # start position
        target = image[sr][sc]
        q = deque([start])
        seen = set(start)
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # directions (adjacent)
        while q:
            r, c = q.popleft()
            image[r][c] = color  # 3. process
            for dr, dc in DIRS:
                nr, nc = pos = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and target == image[nr][nc]
                    and pos not in seen
                ):
                    seen.add(pos)  # 1. registration
                    q.append(pos)  # 2. add in que for processing
        return image
