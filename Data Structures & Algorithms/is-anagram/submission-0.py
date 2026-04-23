class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        dictionary2 = {}
        if len(s) == len(t):
            dictionary1.setdefault(0)
            dictionary2.setdefault(0)
            for loop in list(s):
                dictionary1[loop] =  dictionary1.get(loop, 0)+1
            
            for loop in list(t):
                dictionary2[loop] = dictionary2.get(loop, 0)+1
            return dictionary1 == dictionary2
        
        else:
            return False
      





# Input  : string
# output : boolean
# Pattern: HashMap / HashSet
