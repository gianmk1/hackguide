# Mind your Ps and Qs
*In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this?*
<br>

## Metodo 1
### Step_1
Per prima cosa dobbiamo fattorizzare N nei 2 numeri primi. Per fare questo utilizziamo www.factordb.com

### Step_2
Ora che abbiamo i 2 fattori primi possiamo decifrare il testo tramite uno **script python**

```python
from Crypto.Util.number import inverse, long_to_bytes

c = [testo cifrato]
n = [fattore_n1 * fattore_n2]
e = [esponente chiave pubblica]
p = [fattore_n1]
q = [fattore_n2]

phi = (p-1)*(q-1)

# Troviamo l'esponente della chiave privata
d = inverse(e, phi)

# Decifriamo il messaggio
m = pow(c,d,n)

# Stampiamo il plain text
print(long_to_bytes(m))
```
<br>

## Metodo 2
Andiamo sul sito www.dcode.fr/rsa-cipher e immettiamo i seguenti valori:
- **C** : testo cifrato (c in values)
- **E** : chive pubblica (e in values)
- **N** : numero da fattorizzare (n in values)

*Oppure invece di N inseriamo i 2 fattori primi*

Avviamo la decriptazione!

---
[Come funziona RSA](https://www.computersec.it/2019/01/17/algoritmo-di-crittografia-rsa/)