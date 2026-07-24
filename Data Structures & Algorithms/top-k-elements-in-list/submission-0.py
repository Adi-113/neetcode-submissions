class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Build the frequency map (your logic, slightly simplified)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
                
        # 2. Sort the keys based on their values (frequencies) in descending order
        sorted_keys = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        
        # 3. Return the top k elements
        return sorted_keys[:k]
