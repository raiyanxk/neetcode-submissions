class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for item in strs:
            length = len(item)
            res += (str(length))
            res += ("#")
            res += item
        
        print(res)
        return res

    
    # "neet","code","love","you"
    # 4#neet4#code4#love3#you

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []

        while i < len(s):

            number = ""

            while s[i].isdigit() and i < len(s):
                number += s[i]
                i += 1
            
            if number != '':
                read_next = int(number)
                i += 1
            
            word = ""
            for k in range(i, i + read_next):
                word +=  s[k]
            
            res.append(word)

            i += read_next 
        
        return res
                








