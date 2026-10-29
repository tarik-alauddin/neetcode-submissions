class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        heap = []

        for key in m.keys():
            heapq.heappush(heap, [m[key], key])

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res