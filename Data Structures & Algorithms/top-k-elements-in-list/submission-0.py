class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        # build hashmap of num : count
        for num in nums:
            count[num] += 1

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        # now we have a heap of size K
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
