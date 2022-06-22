def isAnagram_1(s, t):
  if len(s)!=len(t):
    return False
  c1={}
  c2={}
  for i in range(len(s)):
    if s[i] not in c1.keys():
      c1[s[i]]=0
      c1[s[i]]+=1
  for i in range(len(t)):
    if t[i] not in c2.keys():
      c2[t[i]]=0
      c2[t[i]]+=1
  return c1==c2
## Below function has a bug
def isAnagram_2(s,t):
  if len(s)!=len(t):
    return False
  val = 0
  for i in range(len(s)):
    val = val+ord(s[i])-ord(t[i])
  if val !=0:
    return False
  return True
   
