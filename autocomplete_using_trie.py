class Trie:
    head = {}
    
    def insert(self,word):
        curr =self.head
        
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
            
        
        
    
    def autocomplete(self,prefix):
        curr = self.head
        
        for ch in prefix:
            if(ch not in curr):
                return []
            
            curr = curr[ch]
        
        res = []
        
        self.autocomplete_helper(curr,prefix,res)
        return res
    
    
    def autocomplete_helper(self,curr,prefix,res):
        
        for ch in curr:
            if(ch == '*'):
                res.append(prefix)
                
            else:
                self.autocomplete_helper(curr[ch],prefix + ch,res)
            
            
        
        
        
        

trie = Trie()
trie.insert('foo')
trie.insert('foosha')
trie.insert('food')
trie.insert('aisa')
trie.insert('alien')
trie.insert('align')
trie.insert('foodie')
trie.insert('alignment')
trie.insert('albeit')
trie.insert('alibaba')

# print(trie.search('foosha'))
# print(ans)
# ans = trie.search('albeit')
# print(ans)
# ans = trie.search('alien')
# print(ans)

# print(trie.search('foodmap'))
print(trie.autocomplete('foo'))
print(trie.autocomplete('food'))
print(trie.autocomplete('al'))
