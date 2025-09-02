# Import delle funzioni e moduli necessari
from eleco_ricerca import elenco_ricerca_mirata
from funzioni_su_fileCSV.funzioniRicerca import *
from funzioni_su_fileCSV.uscita import *
from richiesta_su_nuoviCSV import *

def controlo_input_ricerca_mirata(df_nano):
    """
    Controlla se il DataFrame risultante dalla ricerca non è vuoto.
    Se non è vuoto, chiede se si vuole creare un nuovo file.
    """
    if not(df_nano.empty):
        vuoi_creare(df_nano)
    else:
        pass  # Nessuna azione se il DataFrame è vuoto

def ricerca_mirata(df) -> None:
    """
    Funzione principale per la ricerca mirata su un DataFrame.
    Mostra il menu delle ricerche disponibili e gestisce l'input utente.
    """
    print("\n")
    while True:
        try:
            elenco_ricerca_mirata()  # Stampa il menu delle ricerche
            ricerca_mirata: str = input(
                "(exit) per uscire\n"
                "(back) per tornare indietro\n"
                "oppure inserire numero corrispondente al tipo di ricerca: "
            )
        except ValueError:
            print("inserimento sconosciuto")

        exit(ricerca_mirata)  # Gestione uscita dal programma

        # Gestione dell'opzione "back" per tornare indietro
        if ricerca_mirata == "back":
            break

        # Controllo che l'input sia numerico e valido
        elif ricerca_mirata.isalpha() and ricerca_mirata != "exit":
            print(
                "l'inserimento deve corrispondere con i valori designati: indice numerico"
            )
            continue

        elif not (int(ricerca_mirata) > 0 and int(ricerca_mirata) < 9):
            print(
                "l'inserimento deve corrispondere con i valori designati: indice numerico"
            )
            continue

        else:
            # Struttura di controllo per selezionare la funzione di ricerca
            match ricerca_mirata:
                case "1":
                    # Ricerca per ID
                    df_nano = ricerca_per_id(df, None)
                    controlo_input_ricerca_mirata(df_nano) 
                case "2":
                    # Ricerca per nominativo
                    df_nano = ricerca_per_nominativo(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "3":
                    # Ricerca per professione
                    df_nano = ricerca_per_professione(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "4":
                    # Ricerca per anno di inizio
                    df_nano = ricerca_per_anno_inizio(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "5":
                    # Ricerca per intervallo di anni
                    df_nano = ricerca_per_intervallo(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "6":
                    # Ricerca per numero di richiami
                    df_nano = ricerca_per_numero_richiami(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "7":
                    # Ricerca per numero di richiami istruzione (maggiore)
                    df_nano = ricerca_per_numero_richiami_istruzione(
                        df, None, "maggiore"
                    )
                    controlo_input_ricerca_mirata(df_nano)
                case "8":
                    # Ricerca per numero di richiami istruzione (minore)
                    df_nano = ricerca_per_numero_richiami_istruzione(df, None, "minore")
                    controlo_input_ricerca_mirata(df_nano)
