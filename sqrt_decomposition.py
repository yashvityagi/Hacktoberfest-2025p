from typing import List

class SqrtDecomposition:
    def __init__(self, arr: List[int]) -> None:
        self.n: int = len(arr)
        self.block_size: int = int(self.n ** 0.5) + 1
        self.arr: List[int] = arr.copy()
        self.blocks: List[int] = [0] * self.block_size
        for i in range(self.n):
            self.blocks[i // self.block_size] += self.arr[i]

    def query(self, l: int, r: int) -> int:
        ans = 0
        while l < r:
            if l % self.block_size == 0 and l + self.block_size <= r:
                ans += self.blocks[l // self.block_size]
                l += self.block_size
            else:
                ans += self.arr[l]
                l += 1
        return ans

    def update(self, idx: int, val: int) -> None:
        block = idx // self.block_size
        self.blocks[block] += val - self.arr[idx]
        self.arr[idx] = val

# Usage: SqrtDecomposition for fast interval queries and updates
