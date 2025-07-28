class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code={"a":".-" ,"b":"-...","c": "-.-." ,"d": "-.." ,"e": "." ,"f": "..-." ,"g":"--." ,"h": "...." ,"i": ".." ,"j":".---" ,"k": "-.-" ,"l": ".-.." ,"m": "--" ,"n": "-." ,"o": "---" ,"p": ".--." ,"q": "--.-" ,"r":".-." ,"s": "..." ,"t": "-","u": "..-" ,"v": "...-" ,"w": ".--" ,"x": "-..-" ,"y": "-.--" ,"z" : "--.." }
        codes=[]
        for i in words:
            translated=""
            for letter in i:
                translated += code[letter]
            codes.append(translated)
        transformed=set(codes)

            
        return len(transformed)