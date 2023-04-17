class Node:
    def __init__(self,key=None,data=None):
        self.key=key
        self.data=data
        self.children={}

class Trie:
    def __init__(self):
        self.root=Node()
    
    def insert(self,string):
        current_node=self.root
        
        for ch in string:
            if ch not in current_node.children:
                current_node.children[ch]=Node(ch)
            current_node=current_node.children[ch]
        current_node.data=string

    def search(self,string):
        current_node=self.root
        for ch in string:
            if ch not in current_node.children:
                return False
            current_node=current_node.children[ch]
            print(current_node.key)
        if current_node.data==string:
            return True
        else:
            return False
    
trie=Trie()
trie.insert("good")
trie.insert("goodasd")
print(trie.search("goodasd"))