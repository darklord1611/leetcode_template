class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        if k > n:
            return -1

        white_block_count = 0
        min_count = n
        left = 0
        for right in range(n):
            if blocks[right] == "W":
                white_block_count += 1

            if right >= k - 1:
                min_count = min(min_count, white_block_count)
                if blocks[left] == "W":
                    white_block_count -= 1
                left += 1

        # time complexity: O(n)
        # space complexity: O(1)

        return min_count
