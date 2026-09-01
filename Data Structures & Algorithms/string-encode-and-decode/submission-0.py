class Solution:

    def encode(self, strs: List[str]) -> str:
        # get length of each string, append length and # to start of each string.
        encoded_string = ""

        for s in strs:
            length = len(s)
            encoded_string += str(length) + "#" + s

        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        j = 0
        start = 0
        forward = 0
        chunk_length = 0
        
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            chunk_length = int(s[i:j])

            start = j + 1
            end = start + chunk_length

            decoded_string.append(s[start:end])

            i = end

        return decoded_string
