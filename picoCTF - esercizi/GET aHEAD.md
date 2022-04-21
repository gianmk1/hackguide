# GET aHEAD
*Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:15931/](http://mercury.picoctf.net:15931/)*
<br>

# Soluzione
Dobbiamo inviare una **richiesta HEAD** al sito.
Per fare ciò possiamo utilizzare **CURL**

```bash
`curl -I HEAD [http://mercury.picoctf](http://mercury.picoctf)[.]net:15931/`
```

*Oppure:*

Utilizziamo un tool come **Postman**.