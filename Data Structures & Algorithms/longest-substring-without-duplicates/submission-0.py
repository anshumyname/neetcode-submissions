class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
        store = {}
        l = 0
        maxlen = 0
        for i in range(len(S)):
            store[S[i]] = store.get(S[i], 0) + 1
            if store.get(S[i],0) > 0:
                while store.get(S[i],0)>1:
                    store[S[l]]-=1
                    l+=1
                    
            
            maxlen = max(maxlen, i-l+1)
                
        return maxlen