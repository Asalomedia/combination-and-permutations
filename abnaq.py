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
def raceeye(ururka:list,tirada_raaciiba:int)->list:
    # kaliya marka tirada_raaciiba==2
    racaysane=[]
    urur=ururka
    while(len(urur)>=tirada_raaciiba):
        last=urur[-1]
        urur.remove(last)
        for x in urur:
            raac=str(x)+str(last)
            racaysane.append(raac)
    return racaysane

print(raceeye(ururka=['a','b','c','d'],tirada_raaciiba=2))

    




