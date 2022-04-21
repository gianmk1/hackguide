import hashlib

# Username in bytes necessario per la chiave
username_trial = b"FREEMAN"

# Definiamo le parti che conosciamo della chiave
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
# Questa è la composizione della chiave finale
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

# Parte mancante della chiave (quella calcolata DINAMICAMENTE)
# Dal codice sorgente notiamo che OGNI CARATTERE della chiave dinamica viene verificato
# basandosi su un preciso carattere dell'HASH DELL'USERNAME

# Mettiamo in un array le posizioni dei caratteri che verrano controllati
positions = [4, 5, 3, 6, 2, 7, 1, 8]
potential_dyn_key = ""

print(hashlib.sha256(username_trial))

# Calcoliamo l'hash dell'username e salviamo i caratteri corrispondenti alle posizioni salvate
# NB. L'hash utilizzato è formattato in codifica esadecimale
for pos in positions:
    potential_dyn_key += hashlib.sha256(username_trial).hexdigest()[pos]

print(potential_dyn_key)

# Stampiamo la chiave finale
key = key_part_static1_trial + potential_dyn_key + key_part_static2_trial
print(key)
