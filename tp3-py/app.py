#!/usr/bin/python3

import math, cgi
import cgitb; 

#cgitb.enable()

def smartAddStr(res, ap):
    if res == "":
        return res+str(ap)
    else:
        return res + " x " + str(ap)
    
def htmlExpRendered(dicto):
    res = "<p>"
    #print(dicto)
    for k in dicto.keys():
        if dicto[k] > 1 :
            res += str(k) + "<sup>" + str(dicto[k]) + "</sup> &times; "
        else :
            res += str(k) + " &times; "
    res = res[:len(res) - 8]
    res += "</p>"
    return res

def dictAdd(dicto, chiffre):
    if str(chiffre) in dicto.keys():
        dicto[str(chiffre)] += 1
    else:
        dicto[str(chiffre)] = 1
    return dicto

def primefactors(n):
    res = dict()
    while n % 2 == 0:
        res = dictAdd(res, 2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):

        while (n % i == 0):
            res = dictAdd(res, i)
            n = n / i

    if n > 2:
        res = dictAdd(res, n)
    
    return res

print("Content-Type: text/html")
print("")

form = cgi.FieldStorage()
print("""<!DOCTYPE html>

<head>
    <title>Primes - Téo Haÿs</title>
</head>

<body>
    <form action="/cgi-bin/td3.py">
        <label for="n">Number :</label><br>
        <input type="text" id="n" name="n" value="1337"><br>
        <input type="submit" value="Go">
    </form>
</body>

</html>""")

if "n" in form :
    n = form.getvalue("n")
    try:
        n = int(n)
    except ValueError:
        print("Could not parse integer. Is it formatted correctly ?")

    print(htmlExpRendered(primefactors(n)))