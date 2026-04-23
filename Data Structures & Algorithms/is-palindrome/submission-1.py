class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower().replace(" ","").replace("?","")
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]

# i : string , sentence
# o : Boolean


# Generator expressions - learn this concepts
