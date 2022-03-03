#!/usr/bin/python3

import math, cgi, json
import cgitb; cgitb.enable(display=1)

def smartAddStr(res, ap):
    if res == "":
        return res+str(ap)
    else:
        return res + " x " + str(ap)
    
def dictoJSON(n, dicto):
    res = dict()
    res["n"] = n
    res["prime_factors"] = []
    for k in dicto.keys():
        res["prime_factors"].append({"prime" : str(k), "power" : str(dicto[k])})
    return res

def dictAdd(dicto, chiffre):
    if str(chiffre) in dicto.keys():
        dicto[str(chiffre)] += 1
    else:
        dicto[str(int(chiffre))] = 1
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



form = cgi.FieldStorage()

# print 
# response={'Price':54,'Cost':'99'}
# print(json.JSONEncoder().encode(response))

if "n" in form :
    print("Content-type: application/json")
    print("")
    n = form.getvalue("n")
    try:
        n = int(n)
    except ValueError:
        print("Could not parse integer. Is it formatted correctly ?")

    response = dictoJSON(n, primefactors(n))
    print(json.JSONEncoder().encode(response))
else :
    print("Content-type: text/html")
    print("")
    print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Primes - Téo Haÿs</title>
</head>

<body>
    <form method="get" id="primeForm">
        <label for="n">Number :</label><br>
        <input type="text" id="n" name="n" value="1337"><br>
        <input type="submit" value="Go">
    </form>
    <div id="resultat">

    </div>
</body>

<script>
    document.getElementById("primeForm").addEventListener("submit", function (e) {
        e.preventDefault() //to block page reload
        number = document.querySelector("#n").value
        console.log(number)
        fetch('http://localhost/cgi-bin/td3.py?n=' + number)
            .then(function (response) {
                return response.json();
            })
            .then(function (json) {
                console.log(json);
                doc = document.querySelector("#primeForm")
                inner = "<p>"
                console.log(json.prime_factors)
                primes = json.prime_factors
                for (prime in primes){
                    console.log(prime.prime)
                    inner += primes[prime].prime
                    if (primes[prime].power > 1){
                        inner += "<sup>" + primes[prime].power + "</sup>"
                    }
                    if (prime < primes.length-1){
                        inner += " &times;"
                    }
                }
                document.querySelector("#resultat").innerHTML = inner;
            });

        return false;
    })
</script>

</html>
""")