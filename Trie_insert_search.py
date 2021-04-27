class Trie:
    head = {}
    
    def insert(self,word):
        curr = self.head
        
        for ch in word:
            if(ch not in curr):
                curr[ch] = {}
            
            curr = curr[ch]
        
        curr['*'] = True
    
        
    def search(self,word):
        curr = self.head
        
        for ch in word:
            if(ch not in curr):
                return False
            
            curr = curr[ch]
        
        
        if('*' not in curr):
            return False
        else:
            return True
            
            

trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("hi")
trie.insert("wororororo")
print(trie.search("worl"))
print(trie.search("worororo"))
print(trie.search("hello"))
print(trie.search("wororororo"))
