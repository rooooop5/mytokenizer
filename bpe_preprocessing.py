from google.colab import files
uploaded=files.upload()

with open("dataset.txt","r",encoding="utf-8") as f:
  chars=f.read()

#converts all the characters present in the dataset to their corresponding unicode and stores them in a list
def toUni(chars):
  ids=chars.encode("utf-8")
  ids=list(map(int,ids))
  return ids
ids=toUni(chars)


#returns the dict:{key=pair,value=no of occurences of pair}
def count_pairs(ids):
  count={}
  for pair in zip(ids,ids[1:]):#zip function returns the pairs and together with (ids,ids[1:]) basically returns consecutive elements
    count[pair]=count.get(pair,0)+1#pair is the key, get(key,0) returns the value of the key, if the key doesnt exist, gives 0 as value
  return count


#takes the dict{pair:occurences} and then converts to dict{occurences:pair}
#this enables calling max() func by key on the dict so that we can get the pair with max occurences
def get_top(byte_pairs):
  pairs={}
  for key,val in byte_pairs.items():
    pairs[val]=key
  top_pair=max(pairs.items())
  return top_pair



def make_toks(ids,top_pair,newcode):
  newids=[]
  i=0
  while i<len(ids)-1:
    tup=(ids[i],ids[i+1])
    if tup==top_pair[1]:
      newids.append(newcode)
      i+=2
    else:
        newids.append(ids[i])
        i+=1
    if i==len(ids)-1:
      newids.append(ids[i])
  return newids
def merges():
    merge_rules={}
    i=0
    newcode=max(ids)+1
    new=ids.copy()
    while i<2000:
        byte_pairs=count_pairs(new)
        top_pair=get_top(byte_pairs)
        merge_rules[top_pair[1]]=newcode
        new=make_toks(new,top_pair,newcode)
        i+=1
        newcode+=1

import pickle
with open("merge_rules.pkl","wb") as f:
  pickle.dump(merge_rules,f)


rev_merge_rules={}
for k,v in merge_rules.items():
  rev_merge_rules[v]=k
with open("rev_merge_rules.pkl","wb") as f:
  pickle.dump(rev_merge_rules,f)