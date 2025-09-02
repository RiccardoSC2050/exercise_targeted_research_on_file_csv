import sys
import time

from eleco_ricerca import *
from funzioni_su_fileCSV.letturaFile_csv import creaDataFrame
from funzioni_su_fileCSV.uscita import *
from ricerca_mirata import *
from ricerca_statistica import *
from richiesta_su_nuoviCSV import vuoi_visualizzare

def carica_dataframe():
    print("caricamento ...\n")
    time.sleep(1)
    try:
        df = creaDataFrame("risorse/dipendenti_azienda.csv")
    except FileNotFoundError:
        sys.exit("File non trovato: dipendenti_azienda.csv\n")
    else:
        print("caricamento del file CSV avvenuto con successo.\n")
    return df

def mostra_struttura_dataframe(df):
    try:
        print(
            "SCHEDA DI RIFERIMENTO: dipendenti_azienda.CSV\n"
            "struttura definita come segue l'esempio: \n"
        )
        print(df.loc[0].to_string(index=True))
    except AttributeError:
        sys.exit("Errore nell'accesso al DataFrame. Controlla il file CSV.\n")

def gestisci_input_utente():
    """
    Gestisce l'input dell'utente per selezionare un'operazione da eseguire.

    Mostra un menu con le seguenti opzioni:
        - ricerca mirata: cerca un dipendente specifico
        - ricerca statistica: visualizza parametri aziendali
        - visualizzare file: mostra un file CSV salvato
        - exit: esce dal programma

    Ritorna:
        str: la scelta dell'utente convertita in minuscolo.

    Gestisce eventuali errori di inserimento tramite ValueError.
    """
    while True:
        try:
            print("\n\n")
            input_utente: str = input(
                "inserire valore per la ricerca di un dipendente;\n"
                "(ricerca mirata) per cercare un dipendente specifico;\n"
                "(ricerca statistica) per vedere alcuni parametri aziendali;\n"
                "(visualizzare file) per visualizzare un file CSV salvato in precedenza;\n"
                "(exit) per uscire dal programma.\n"
            ).lower()
        except ValueError:
            print("errato inserimento")
        break
    return input_utente

def ciclo_principale(df):
    while True:
        input_utente = gestisci_input_utente()
        if input_utente == "exit":
            uscire()
        elif input_utente == "ricerca mirata":
            ricerca_mirata(df)
        elif input_utente == "ricerca statistica":
            ricerca_statistica(df)
        elif input_utente == "visualizzare file":
            vuoi_visualizzare()

if __name__ == "__main__":
    df = carica_dataframe()
    mostra_struttura_dataframe(df)
    ciclo_principale(df)
