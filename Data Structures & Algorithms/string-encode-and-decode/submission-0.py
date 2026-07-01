class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
            res = []
            i = 0
            
            while i < len(s):
                j = i
                # Find the delimiter to isolate the length number
                while s[j] != "#":
                    j += 1
                    
                # Extract the length as an integer
                length = int(s[i:j])
                
                # The string starts right after '#' and ends after 'length' characters
                start_of_string = j + 1
                end_of_string = start_of_string + length
                
                # Slice the exact string and add it to our result
                res.append(s[start_of_string : end_of_string])
                
                # Move our main pointer 'i' to the start of the next encoded string
                i = end_of_string
                
            return res
