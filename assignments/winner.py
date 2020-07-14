import re

def checkWinner(codeList, shoppingCart):
    #a='anything'.join(codeList)
    a="";txt=""
    for elem in shoppingCart:
        txt=txt+','+elem
    for elem in codeList:
        a=a+','.join(elem)
        a=a+',anything,'
    a=a.replace(',anything,','.*')
    x = re.search(a, txt)
    if x:
        return "we found"
    else:
        return "no match"


if __name__ == "__main__":
    print(checkWinner((['apple,apple'], ['banana', 'anything', 'banana']),
                (['apple','apple','fruit', 'banana', 'banana', 'banana'])))
