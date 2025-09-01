import os

from funzioni_su_fileCSV.letturaFile_csv import visualizzaTabella
from funzioni_su_fileCSV.salvataggioCSV_valori import *


def vuoi_creare(df) -> None:
    while True:
        try:
            richiesta = input("vuoi salvarlo in un file CSV? (s/n)\n\n").lower()
        except ValueError as e:
            print(e)
            continue

        if richiesta != "s" and richiesta != "n":
            print("errore di inserimento, riprovare\n")
            continue

        elif richiesta == "s":
            while True:
                if df.empty:
                    print("nessun dato da salvare, ritorno al menu precedente")
                    break
                nome: str = input("che nome vuoi assegnare al file: ")
                if nome.isdigit():
                    print("riprova inserimento nome")
                    continue
                else:
                    salva_csv(df, nome)
                break

        elif richiesta == "n":
            break

        break


def vuoi_visualizzare() -> None:
    while True:
        try:
            richiesta = input("vuoi visualizzare un file CSV? (s/n)\n\n").lower()
        except ValueError as e:
            print(e)
            continue

        if richiesta != "s" and richiesta != "n":
            print("errore di inserimento, inserire solo s o n\n")
            continue

        elif richiesta == "s":

            listaDR: list = os.listdir(os.path.join("risorse", "nuoviCSV"))
            if len(listaDR) == 0:
                print("non ci sono file da visualizzare")
            else:
                print("FILE DISPONIBILI:\n\n")
                for f in listaDR:
                    print(f)
                print("\n\n")
                while True:
                    try:
                        richiesta = input("quale file vuoi visualizzare?\n\n")
                        nomeFile_csv: str = richiesta + ".csv"
                        if nomeFile_csv in listaDR:
                            nomeFileCompleto = os.path.join(
                                "risorse", "nuoviCSV", nomeFile_csv
                            )
                            visualizzaTabella(nomeFileCompleto)
                            break
                        else:
                            print("devi inserire un nome file esistente")
                            continue
                    except ValueError as e:
                        print(e)

        elif richiesta == "n":
            break

        break
