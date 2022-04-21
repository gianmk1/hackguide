# Static ain't always noise
*Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/static)? This [BASH script](https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/ltdis.sh) might help!*
<br>

## Soluzione
Possiamo vedere tutte le stringhe che ci ritorna il comando **string** dal binario, oppure, usiamo il programma **ltdis.sh** datoci nel seguente modo:
```bash
./ltdis.sh static
```