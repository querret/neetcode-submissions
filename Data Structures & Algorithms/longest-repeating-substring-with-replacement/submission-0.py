class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = dict()
        back = 0
        front = 0
        max_length = 0

        while front < len(s):
            if s[front] not in counts:
                counts[s[front]] = 1
            else:
                counts[s[front]] += 1
            
            while (front - back + 1) - max(counts.values()) > k:
                counts[s[back]] -= 1
                back += 1

            current_window_size = front - back + 1
            max_length = max(max_length, current_window_size)
        
            front += 1
        return max_length
