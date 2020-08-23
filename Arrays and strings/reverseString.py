class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        r = len(s) - 1
        l = 0

        for i in range(0, len(s)//2):
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
