# Matryoshka doll
*Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/205adad23bf9d8303081a0e71c9beab8/dolls.jpg)*
<br>

## Soluzione
Guardano il contenuto del file con **strings** non troviamo nulla e anche i metadati (tramite **exiftool**) non riportano nulla di interessante.

Tramite la descrizione della challenge supponiamo che ci siano dei **file nascosti** all'interno dell'immagine. 
Utilizziamo quindi [Binwalk](https://github.com/ReFirmLabs/binwalk) e tramite il seguente comando **analizziamo la signature del file ** e **estraiamo i file nascosti**:

```bash
binwalk -e dools.jpg
```

L'estrazione ci ritorna una cartella con all'interno un'altra immagine.

*Ripetiamo il passaggio varie volte fino ad arrivare all'estrazione del file **flag.txt**. *