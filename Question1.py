class Solution(object):
    def longestPalindrome(self, s):
        result = ''
        resultLength = 0
        
        for i in range(len(s)):
            #handling the odd palindrome case first
            left, right = i, i #set the left, right pointer at the middle of the string
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if(right - left +1) > resultLength:
                    result = s[left:right+1] #store the result
                    resultLength = right - left +1 #store the result length
                left -= 1 #expand the left pointer to the left side for 1 char
                right += 1 #expand the right pointer to the right side for 1 char
                    
            #hanlding the even palindrome case
            left, right = i, i+1 #set the left at the middle of the string, and right pointer just beside it
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if(right - left +1) > resultLength:
                    result = s[left:right+1] #store the result
                    resultLength = right - left +1 #store the result length
                left -= 1 #expand the left pointer to the left side for 1 char
                right += 1 #expand the right pointer to the right side for 1 char
        
        return result