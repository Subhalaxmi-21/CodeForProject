class Solution:
    def isPalindrome(self, x: int) -> bool:
        z=x
        i=0
        if x<0:
                return False
        while x!=0:
            i=i*10+x%10
            
            x=x//10
        
        if i==z:
            return True
        else:
            return False
                
