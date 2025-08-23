# importo classi per il programma principale:
import sys
import time

from eleco_ricerca import *
from funzioni_su_fileCSV.letturaFile_csv import creaDataFrame
from funzioni_su_fileCSV.uscita import *
from ricerca_mirata import *

# main effettivo del programma:
# importiamo la funzione per creare il DataFrame da un file CSV

if __name__ == "__main__":
    print("caricamento ...\n")
    time.sleep(
        1
    )  # attesa di 1 secondo per dare tempo all'utente di leggere il messaggio

    try:
        # creiamo il data frame di lavoro:
        df = creaDataFrame("risorse/dipendenti_azienda.csv")
    except FileNotFoundError:
        sys.exit("File non trovato: dipendenti_azienda.csv\n")
    else:
        print("caricamento del file CSV avvenuto con successo.\n")

    # visualizziamo la struttura del DataFrame:
    try:
        print(
            "SCHEDA DI RIFERIMENTO: dipendenti_azienda.CSV\n"
            "struttura definita come segue l'esempio: \n"
        )
        print(df.loc[0].to_string(index=True))
    except AttributeError:
        sys.exit("Errore nell'accesso al DataFrame. Controlla il file CSV.\n")
    ###################################################################################################
    #
    #
    #
    # Ciclo principale per l'interazione con l'utente
    while True:

        # primo inserimento da parte dell'utente
        while True:
            try:
                print("\n\n")
                input_utente: str = input(
                    "inserire valore per la ricerca di un dipendente;\n"
                    "(ricerca mirata) per cercare un dipendente specifico;\n"
                    "(ricerca statistica) per vedere alcuni parametri aziendali;\n"
                    "(exit) per uscire dal programma.\n"

                ).lower()
            except ValueError:
                # Gestione dell'errore in caso di inserimento non valido
                print("errato inserimento")
            break  # Uscita dal ciclo dopo il primo input (probabilmente da rimuovere per un ciclo continuo)

        # uscita dal programma se exit
        if input_utente == "exit":
            uscire()

        # sezione condizioni con ricerca mirata
        elif input_utente == "ricerca mirata":
            ricerca_mirata(df)

        elif input_utente == "ricerca statistica":
            pass

    # l'input sarà generico: se è numerico considera i numeri altrimenti cerca valori testuali
