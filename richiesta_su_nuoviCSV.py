import os

# Importa la funzione per visualizzare una tabella da un file CSV
from funzioni_su_fileCSV.letturaFile_csv import visualizzaTabella
# Importa tutte le funzioni di salvataggio CSV
from funzioni_su_fileCSV.salvataggioCSV_valori import *


def vuoi_creare(df) -> None:
    """
    Chiede all'utente se vuole salvare il DataFrame in un file CSV.
    Se confermato, richiede il nome del file e salva il DataFrame.
    """
    while True:
        try:
            richiesta = input("Vuoi salvarlo in un file CSV? (s/n)\n\n").lower()
        except ValueError as e:
            print(e)
            continue

        # Verifica input valido
        if richiesta != "s" and richiesta != "n":
            print("Errore di inserimento, riprovare\n")
            continue

        elif richiesta == "s":
            while True:
                # Controlla se il DataFrame è vuoto
                if df.empty:
                    print("Nessun dato da salvare, ritorno al menu precedente")
                    break
                nome: str = input("Che nome vuoi assegnare al file: ")
                # Verifica che il nome non sia solo numerico
                if nome.isdigit():
                    print("Riprova inserimento nome")
                    continue
                else:
                    salva_csv(df, nome)
                break

        elif richiesta == "n":
            break

        break


def vuoi_visualizzare() -> None:
    """
    Chiede all'utente se vuole visualizzare un file CSV.
    Se confermato, mostra la lista dei file disponibili e visualizza quello scelto.
    """
    while True:
        try:
            richiesta = input("Vuoi visualizzare un file CSV? (s/n)\n\n").lower()
        except ValueError as e:
            print(e)
            continue

        # Verifica input valido
        if richiesta != "s" and richiesta != "n":
            print("Errore di inserimento, inserire solo s o n\n")
            continue

        elif richiesta == "s":
            # Ottiene la lista dei file CSV disponibili
            listaDR: list = os.listdir(os.path.join("risorse", "nuoviCSV"))
            if len(listaDR) == 0:
                print("Non ci sono file da visualizzare")
            else:
                print("FILE DISPONIBILI:\n\n")
                for f in listaDR:
                    print(f)
                print("\n\n")
                while True:
                    try:
                        richiesta = input("Quale file vuoi visualizzare?\n\n")
                        nomeFile_csv: str = richiesta + ".csv"
                        # Verifica che il file esista nella lista
                        if nomeFile_csv in listaDR:
                            nomeFileCompleto = os.path.join(
                                "risorse", "nuoviCSV", nomeFile_csv
                            )
                            visualizzaTabella(nomeFileCompleto)
                            break
                        else:
                            print("Devi inserire un nome file esistente")
                            continue
                    except ValueError as e:
                        print(e)

        elif richiesta == "n":
            break

        break
