from eleco_ricerca import elenco_ricerca_statistica
from funzioni_su_fileCSV.funzioni_statistiche import *
from funzioni_su_fileCSV.uscita import *
from pausa import pausa


def ricerca_statistica(df) -> None:
    pausa(1.2)
    # Loop principale per la selezione della ricerca statistica
    while True:
        try:
            elenco_ricerca_statistica()  # Mostra elenco delle opzioni disponibili
            
            ricerca_statistica: str = input(
                "\n\n(exit) per uscire\n"
                "(back) per tornare indietro\n"
                "oppure inserire numero corrispondente al tipo di ricerca: \n\n"
            )
        except ValueError:
            # Gestione dell'errore di inserimento non valido
            print("\ninserimento sconosciuto\n")

        exit(ricerca_statistica)  # Gestione uscita dal programma

        if ricerca_statistica == "back":
            # Torna al menu precedente
            break

        elif ricerca_statistica.isalpha() and ricerca_statistica != "exit":
            # Verifica che l'inserimento sia numerico
            print(
                "\nl'inserimento deve corrispondere con i valori designati: indice numerico\n"
            )
            continue

        elif not (int(ricerca_statistica) > 0 and int(ricerca_statistica) < 5):
            # Verifica che il numero sia nell'intervallo valido
            print(
                "\nl'inserimento deve corrispondere con i valori designati: indice numerico\n"
            )
            continue

        else:
            # Esecuzione della funzione corrispondente all'opzione selezionata
            match ricerca_statistica:
                case "1":
                    p = numero_totale_dipendenti(df)
                    pausa(1.2)
                    print("Numero totale di dipendenti:", p)
                case "2":
                    p = numero_dipendenti_per_istruzione(df)
                    pausa(1.2)
                    print("Numero totale:", p)
                case "3":
                    p = media_richiami(df)
                    pausa(1.2)
                    print("Numero richiami medio:", p)
                case "4":
                    p = media_anni_anzianita_aziendale(df)
                    pausa(1.2)
                    print("Numero medio di anni passati in azienda:", p)
