class Solution:


    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        string =str(x)
        reversed_string = string[::-1]
        if string == reversed_string:
            return True
        else:
            return False


## class Solution:
##  def isPalindrome(self, x: int) -> bool:
##        return str(x) == str(x)[::-1]
