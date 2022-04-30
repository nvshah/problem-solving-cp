# https://leetcode.com/problems/encode-and-decode-tinyurl/
from string import Template

# ref  ---
# Template String :- https://realpython.com/python-string-formatting/#4-template-strings-standard-library

'''
QUE : is very common in  Interview
'''

class Codec:

    def __init__(self):
        self.encodeMap = {}  # original_string -> new_string
        self.decodeMap = {}  # new_string -> original_string
        base = "https://tinyurl.com/"
        self.url = Template(f'{base}$path')

        self.code = 0  # Simply for encoding we use counter way 

    def get_nxt_code(self):
        '''Counter to provide the next code'''
        return self.code + 1


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap: # first time
            # Thus Encode it (ie Register it)
            code = self.get_nxt_code()
            shortUrl = self.url.substitute(path=code)
            self.encodeMap[longUrl] = shortUrl 
            self.decodeMap[shortUrl] = longUrl

        return self.encodeMap[longUrl] 

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))