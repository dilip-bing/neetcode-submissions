class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}

        if len(s) == len(t):
            for loop in list(s):
                dictionary1[loop] =  dictionary1.get(loop,0)+1
            
            for loop in list(t):
                dictionary1[loop] =    dictionary1.get(loop,0)-1
            
            return all(value == 0 for value in dictionary1.values())
        
        else:
            return False
      





# Input  : string
# output : boolean
# Pattern: HashMap / HashSet
