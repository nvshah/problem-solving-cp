from collections import deque
from typing import List, Optional, Tuple, Set, Dict


# ---------- 1. Tree / Level-order (no visited set needed) ----------
def bfs_tree(root: Optional["TreeNode"]) -> List[List[int]]:
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):  # fixed length for current level
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


# ---------- 2. Graph (adjacency list) – single source ----------
def bfs_graph(adj: Dict[int, List[int]], start: int) -> Dict[int, int]:
    """returns shortest distance from start to every reachable node"""
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:  # not visited
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


# ---------- 3. Grid / Matrix – multi-source or single ----------
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_grid(
    grid: List[List[int]], start: List[Tuple[int, int]]
) -> Dict[Tuple[int, int], int]:
    """start can be a single (r,c) or list of cells; returns shortest dist"""
    m, n = len(grid), len(grid[0])
    q = deque(start)
    seen = set(start)
    dist = {cell: 0 for cell in start}
    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < m
                and 0 <= nc < n
                and (nr, nc) not in seen
                and grid[nr][nc] != 1
            ):  # 1 == wall
                seen.add((nr, nc))
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))
    return dist


# ---------- 4. Generic skeleton you can copy-paste ----------
def bfs_generic(start) -> int:
    q = deque([start])
    seen = {start}
    steps = 0
    while q:
        for _ in range(len(q)):  # level-by-level
            node = q.popleft()
            if is_target(node):
                return steps
            for neighbor in expand(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)
        steps += 1
    return -1  # or whatever “not found” means
