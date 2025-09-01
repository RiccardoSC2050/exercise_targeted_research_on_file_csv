from eleco_ricerca import elenco_ricerca_mirata
from funzioni_su_fileCSV.funzioniRicerca import *
from funzioni_su_fileCSV.uscita import *
from richiesta_su_nuoviCSV import *

def controlo_input_ricerca_mirata(df_nano):
    if not(df_nano.empty):
                        vuoi_creare(df_nano)
    else:
        pass



def ricerca_mirata(df) -> None:
    print("\n")
    while True:
        try:
            elenco_ricerca_mirata()
            ricerca_mirata: str = input(
                "(exit) per uscire\n"
                "(back) per tornare indietro\n"
                "oppure inserire numero corrispondente al tipo di ricerca: "
            )
        except ValueError:
            print("inserimento sconosciuto")

        exit(ricerca_mirata)

        if ricerca_mirata == "back":
            break

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
            match ricerca_mirata:
                case "1":
                    df_nano = ricerca_per_id(df, None)
                    controlo_input_ricerca_mirata(df_nano) 
                case "2":
                    df_nano = ricerca_per_nominativo(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "3":
                    df_nano = ricerca_per_professione(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "4":
                    df_nano = ricerca_per_anno_inizio(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "5":
                    df_nano = ricerca_per_intervallo(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "6":
                    df_nano = ricerca_per_numero_richiami(df, None)
                    controlo_input_ricerca_mirata(df_nano)
                case "7":
                    df_nano = ricerca_per_numero_richiami_istruzione(
                        df, None, "maggiore"
                    )
                    controlo_input_ricerca_mirata(df_nano)
                case "8":
                    df_nano = ricerca_per_numero_richiami_istruzione(df, None, "minore")
                    controlo_input_ricerca_mirata(df_nano)
