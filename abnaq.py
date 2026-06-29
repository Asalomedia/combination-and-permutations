print("bismilah")
def abnaqe(tiro:int)->int:
    index=tiro
    maxsuul=1
    while(index>0):
        maxsuul*=index
        index-=1
    return maxsuul

# abnaq=abnaqe(5)#waa in uu noqdaa 5x4x3x2x1=120
# print(abnaq)

def imisa_raac_weeyi(tirada_xubnaha:int,tirada_ururkiiba:int)->int:
    n=abnaqe(tiro=tirada_xubnaha)
    r=abnaqe(tiro=tirada_ururkiiba)
    faraq=abnaqe(tiro=(tirada_xubnaha-tirada_ururkiiba))
    h=faraq*r
    racayn=n/h
    return racayn

# #nCr=3C2=3 waa sida abc ay u noqonayso ab,bc,ac
# print(imisa_raac_weeyi(tirada_xubnaha=3,tirada_ururkiiba=2))

# 5C2 waa 10
# print(imisa_raac_weeyi(5,2))

# 12C8 waa 495 qaab waa qaababka world cup 2026 booska sadexaad 12 ka ah ay 8 uga soo  baxayaan
# print(imisa_raac_weeyi(12,8))

# Hadaba su'aashu waxa weeyi sidee ayaan u taxaa?
def raceeye_2(ururka:list)->list:
    # kaliya marka tirada_raaciiba==2
    racaysane=[]
    urur=ururka
    while(len(urur)>=2):
        last=urur[-1]
        urur=urur[:-1]
        for x in urur:
            raac=str(x)+str(last)
            racaysane.append(raac)
    return racaysane

def raceeye_3(ururka: list)->dict:
    # kaliya marka tirada raaciiba ay tahay 3
    racaysane=[]
    urur=ururka
    while(len(urur)>=3):
        last=urur[-1]
        urur=urur[:-1]
        uracee_2=raceeye_2(ururka=urur)
        for x in uracee_2:
            raac=str(x)+str(last)
            racaysane.append(raac)
    return {'racaynta':racaysane,'dhererka':imisa_raac_weeyi(tirada_xubnaha=len(ururka),tirada_ururkiiba=3),"ama":len(racaysane)}

print(raceeye_3(ururka=['a','b','c','d','e','f','g','h','i','j','k','l']))

    




