from abnaqe import imisa_raac_weeyi


# Hadaba su'aashu waxa weeyi sidee ayaan u taxaa?
def combinator_2(theSet:list,r:int)->list:
    # kaliya marka tirada_raaciiba==2
   combinated=[]
   for x in range(len(theSet),r-1,-1):
      for e in theSet[:x-1]:
         subset_As_str=str(e)+str(theSet[x-1])
         combinated.append(subset_As_str)
   return combinated

def combinator(theSet:set,r:int)->set:
    if r==1:
       return theSet
    if r==2:
       return combinator_2(theSet,r)
    if r>2:
       combinated=[]
       for x in range(len(theSet),r-1,-1):
           for element in combinator(theSet[:x-1],r-1):
              subset_As_str=str(element)+str(theSet[x-1])
              combinated.append(subset_As_str)
       return combinated      
   
third_place=['a','b',"c",'d','e','f','g','h','i','j','k','l']
r=8
combination=combinator(theSet=third_place,r=r)
print(f"{combination}, with length of {len(combination)}")
print(f'length is :{imisa_raac_weeyi(tirada_xubnaha=len(third_place),tirada_ururkiiba=r)}')

