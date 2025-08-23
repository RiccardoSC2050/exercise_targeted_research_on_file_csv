import os

import pandas as p


def creaDataFrame(nome_file):
    try:
        f = p.read_csv(nome_file, encoding="utf-8", sep=",", dtype=str)
        return f
    except FileNotFoundError:
        print("nome file csv non valido, errore")


# Visualizzare tutti i dipendenti
#    - Mostra l’intera tabella.
#    - Paginazione (10 righe per volta) per file grandi.


def visualizzaTabella(nome_file):
    df = creaDataFrame(nome_file)
    print(df.head())

    while True:
        try:
            risposta = input("vuoi visualizzare tutto il file per intero? (s/n)")

            if risposta != "s" and risposta != "n":
                print("errore di inserimento, inserire solo s o n")
                continue
            elif risposta == "n":
                break
            elif risposta == "s":
                print("\n")
                for chunck in p.read_csv(
                    nome_file,
                    encoding="utf-8",
                    sep=",",
                    dtype=str,
                    chunksize=20,
                ):
                    print(chunck.to_string(index=False))
                break
        except Exception as e:
            print("errore in qualcosa:", e)


# test funzioni
if __name__ == "__main__":
    f = creaDataFrame(os.path.join("../risorse/dipendenti_azienda.csv"))
    print(f.head())  # primi 5

    visualizzaTabella(os.path.join("../risorse/dipendenti_azienda.csv"))
