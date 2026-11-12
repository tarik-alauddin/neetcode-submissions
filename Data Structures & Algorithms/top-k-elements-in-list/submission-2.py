class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        for num in m:
            heapq.heappush(heap, (m[num], num))

        while len(heap) > k:
            heapq.heappop(heap)

        res = []
        while len(heap) > 0:
            count, num = heapq.heappop(heap)
            res.append(num)

        return res