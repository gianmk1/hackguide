# keygenme-py
*[keygenme-trial.py](https://mercury.picoctf.net/static/fb75b48f9214cf992a2199b5785564e7/keygenme-trial.py)*
<br>

## Soluzione
Analizzando il codice sorgente datoci, notiamo che è già presente parte della flag.

```python
static1 = "picoCTF{1n_7h3_|<3y_of_"
dynamic = "xxxxxxxx"
static1 = "}"
key_full_template_trial = static1 + dynamic + static2
```

Concentriamoci sulla parte **dynamic**.

Più avanti nel codice ogni carattere della parte dinamica che immettiamo viene confrontato con un **carattere in una posizione specifica** dell'**hash** dell username ("FREEMAN").

Ci salviamo le posizioni che confronta in una lista, successivamente **troviamo il carattere corrispondente alle posizioni salvate dall'hash dell'username**, uniamo il tutto e abbiamo così la parte dinamica della chiave.

Ricostruiamo la chiave finale e abbiamo trovato la flag!

*Vedi lo script python per la soluzione nella cartella della challenge!*