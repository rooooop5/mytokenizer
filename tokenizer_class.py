import pickle
import os

class Tokenizer:
    def __init__(self,dir_path="tokenizer"):
        with open(os.path.join(dir_path,"merge_rules.pkl"),"rb") as f:
            self.merge_rules=pickle.load(f);
        with open(os.path.join(dir_path,"rev_merge_rules.pkl"),"rb") as f:
            self.rev_merge_rules=pickle.load(f)
    
    def _to_uni(self,ids):
        ids=ids.encode("utf-8")
        ids=list(map(int,ids))
        return ids
    
    def _from_uni(self,ids):
        return "".join([chr(i) for i in ids])
    
    def encode(self,text):
        uni_text=self._to_uni(text)
        newids=[]
        while True:
            i=0
            found_merge=0
            while i<len(uni_text)-1:
                tup=(uni_text[i],uni_text[i+1])
                if tup in self.merge_rules:
                    newids.append(self.merge_rules[tup])
                    i=i+2
                    found_merge=1
                else:
                    newids.append(uni_text[i])
                    i=i+1
            if i == len(uni_text) - 1:
                newids.append(uni_text[-1])
            if(found_merge==0):
                break
            else:
                uni_text,newids=newids,[]
        return uni_text
    

    def decode(self,ids):
        uni_text=ids.copy()
        while True:
            i=0
            flag=0
            decoded=[]
            while i<len(uni_text):
                if uni_text[i] in self.rev_merge_rules:
                    decoded.append(self.rev_merge_rules[uni_text[i]][0])
                    decoded.append(self.rev_merge_rules[uni_text[i]][1])
                    flag=1
                else:
                    decoded.append(uni_text[i])
                i=i+1
            if(flag==0):
                break
            else:
                uni_text,decoded=decoded,[]
        return self._from_uni(uni_text)