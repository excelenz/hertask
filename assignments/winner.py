
def checkWinner(codeList, shoppingCart):
    #a='anything'.join(codeList)
    a=""
    for elem in codeList:
        a=a+','.join(elem)
        a=a+',anything,'
    a=a.replace(',anything,','*')
    return a


if __name__ == "__main__":
    print(checkWinner((['apple,apple'], ['banana', 'anything', 'banana']),
                (['apple,apple', 'banana', 'anything', 'banana'])))
