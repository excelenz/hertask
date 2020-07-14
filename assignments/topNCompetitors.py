import re
def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    numberOccurs={}
    for elem in competitors:
        a=[x for x in reviews if elem in x]
        numberOccurs[elem]=len(a)
    myDict = {key: val for key, val in numberOccurs.items() if val != 0}
    sort_numberOccurs = sorted(myDict.items(), key=lambda x: x[1], reverse=True)
    sort_numberOccurs=sort_numberOccurs[:topNCompetitors]
    return  [k[0] for k in sort_numberOccurs]




if __name__ == "__111main__":
    topNCompetitors(5,1,['anacell','betacellular','cetracular','deltacecullar','eurocell'],3,['Besst anacell','Besst betacellular','bbb anacell'])