# funzioniRicerca.py

from funzioni_su_fileCSV.letturaFile_csv import creaDataFrame
from funzioni_su_fileCSV.stampa import stampa_completa
from funzioni_su_fileCSV.uscita import exit

# Ricerca per ID
#    - Input: ID completo (es. `00045`).
#    - Mostra tutti i dati della persona.
#    - Se l’ID non esiste, mostra messaggio di errore.
# - da usare in casi generici senza sapere che stiamo usando la funzione ricerca_per_id


def ricerca_per_id(df, id_ricerca: str) -> object:
    """
    Funzione per la ricerca di un dipendente per ID.
    - Se `id_ricerca` è `None`, chiede all'utente di inserire un ID.
    - Se l'ID non esiste, mostra un messaggio di errore.
    """
    # Ciclo infinito per permettere all'utente di riprovare in caso di errore
    while True:
        try:
            # Se viene passato un ID come argomento, lo usa per la ricerca
            if id_ricerca != None:
                ricerca: str = id_ricerca
            # Se non viene passato un ID, chiede all'utente di inserirne uno
            elif id_ricerca == None:
                ricerca: str = input(
                    "\ninserisci l'ID del dipendente da cercare, o 'back per annullare operazione' oppure 'exit' per uscire: \n\n"
                ).lower()
            # Gestione uscita dalla funzione
            exit(ricerca)
            # Controlli sull'ID inserito
            if ricerca == None or ricerca == "":
                print("\nErrore: l'ID non può essere vuoto.\n")
                continue
            elif ricerca == "back":
                print("\nOperazione annullata, ritorno al menu precedente.\n")
                return df.iloc[0:0]
            elif len(ricerca) > 4:
                print("\nErrore: l'ID deve essere massimo di 4 caratteri.\n")
                continue
            elif ricerca.isdigit() == False:
                print("\nErrore: l'ID numerico.\n")
                continue
            else:
                # Ricerca nel DataFrame per ID (case insensitive)
                rigaDF = df[
                    df["ID"]
                    .str[: len(ricerca) + 1]
                    .str.lower()
                    .str.contains(f"0{ricerca}")
                ]
                # Stampa messaggio se non trova l'ID, altrimenti mostra i dati trovati
                print(
                    f"nessun id: {ricerca} trovato" if rigaDF.empty else rigaDF.head()
                )
                stampa_completa(rigaDF)
                break

        except ValueError:
            # Gestione errori di inserimento
            print("\nErrore nell'inserimento. Riprova.\n")
            continue
    return rigaDF


# Ricerca per Nome e/o Cognome
#    - Input: nome e cognome.
#    - Ricerca senza distinzione tra maiuscole/minuscole.
#    - Supporto corrispondenza parziale (es. “Lu” trova “Luca”).
def ricerca_per_nominativo(df, nome_ricerca: list) -> object:
    """
    Funzione per la ricerca di un dipendente per nome o cognome.
    """
    while True:
        try:
            # Se viene passato un nome/cognome come argomento
            if nome_ricerca != None:
                ricerca: list = nome_ricerca

            # Se non viene passato nulla, chiede all'utente di inserire nome/cognome
            elif nome_ricerca == None:
                # Chiede all'utente di inserire un nome o cognome da cercare
                valore: str = input(
                    "\ninserisci prima il nome e poi cognome da cercare, o 'back per annullare operazione' oppure 'exit' per uscire:  \n\n"
                ).lower()

                # Gestione uscita dalla funzione
            exit(valore)
            # Se il valore è vuoto
            if valore == None or valore == "":
                print("\nErrore: il valore non può essere vuoto.\n")
                continue
                # Controlli sull'input
            elif valore == "back":
                print("\nOperazione annullata, ritorno al menu precedente.\n")
                return df.iloc[0:0]
            elif not all(v.isalpha() for v in valore.split()):
                print("\nErrore: i nominativi devono contenere solo lettere.\n")
                continue
            # Ricerca nel DataFrame
            else:
                # Se vengono inseriti sia nome che cognome
                if len(valore.split()) == 2:
                    ricerca: list = (
                        valore.split()
                    )  # Divide il valore in una lista di parole
                # Se vengono inseriti più di due parole
                elif len(valore.split()) > 2:
                    print(
                        "\nErrore: inserisci solo il nome e il cognome, separati da uno spazio.\n"
                    )
                    continue
                else:
                    ricerca: list = [
                        valore,
                        "",
                    ]  # Se c'è solo un nome, il cognome è vuoto
                # Ricerca per nome
                nome = df[
                    df["Nome"]
                    .str[: len(ricerca[0])]
                    .str.lower()
                    .str.contains(ricerca[0])
                ]
                if ricerca[1] == "":
                    # Se il cognome non è stato inserito, cerca solo per nome
                    rigaDF = nome
                else:
                    # Ricerca per cognome
                    cognome = df[
                        df["Cognome"]
                        .str[: len(ricerca[1])]
                        .str.lower()
                        .str.contains(ricerca[1])
                    ]

                    # Unisce i risultati della ricerca per nome e cognome
                    # merge serve per trovare le righe che corrispondono sia al nome che al cognome
                    # quindi restituisce solo le righe che hanno entrambi i campi corrispondenti
                    # grazie a inner join per fare interzezione su una base data da on
                    rigaDF = nome.merge(cognome, how="inner", on=list(df.columns))
                print(
                    f"nessun nome o cognome: {ricerca} trovato"
                    if rigaDF.empty
                    else rigaDF.head()
                )
                stampa_completa(rigaDF)
                break
        except ValueError:
            # Gestione errori di inserimento
            print("\nErrore nell'inserimento. Riprova.\n")
            continue
        except IndexError:
            # Gestione errori di accesso agli indici della lista
            print("\nErrore: assicurati di inserire sia il nome che il cognome.\n")
            continue
    return rigaDF


# Ricerca per Professione
#   - Lista professioni disponibili letta dal file.
#   - Filtra tutti i dipendenti con quella professione.
def ricerca_per_professione(df, professione: str) -> object:
    """
    Funzione per la ricerca di un dipendente per professione.
    """
    while True:
        try:
            if professione != None:
                ricerca: str = professione
            elif professione == None:
                # se non viene passato un nome, chiede all'utente di inserirne uno
                ricerca: str = input(
                    "\ninserisci la professione da cercare, o 'back per annullare operazione' oppure 'exit' per uscire: \n\n"
                ).lower()

            exit(ricerca)
            if ricerca == None or ricerca == "":
                print("\nErrore: la professione non può essere vuota.\n")
                continue
            elif ricerca == "back":
                print("\nOperazione annullata, ritorno al menu precedente.\n")
                return df.iloc[0:0]
            elif ricerca.isalpha() == False:
                print("\nErrore: la professione deve contenere solo lettere.\n")
                continue
            else:
                rigaDF = df[
                    df["Professione"]
                    .str[: len(ricerca)]
                    .str.lower()
                    .str.contains(ricerca)
                ]
                print(
                    f"nessuna professione: {ricerca} trovata"
                    if rigaDF.empty
                    else rigaDF.head()
                )
                stampa_completa(rigaDF)
                break
        except ValueError:
            print("Errore nell'inserimento. Riprova.")
            continue
    return rigaDF


# Filtrare per Anno di Inizio
#    - Input: anno esatto o intervallo di anni.
#    - Mostra i dipendenti entrati in quell’anno o periodo.
def ricerca_per_anno_inizio(df, anno: str) -> object:
    """
    Funzione per la ricerca di un dipendente per anno di inizio.
    """
    # Ciclo infinito per permettere all'utente di riprovare in caso di errore
    while True:
        try:
            # Se viene passato un anno come argomento, lo usa per la ricerca
            if anno != None:
                ricerca: str = anno
            # Se non viene passato un anno, chiede all'utente di inserirne uno
            elif anno == None:
                ricerca: str = input(
                    "\ninserisci l'anno di inizio da cercare, o 'back per annullare operazione' oppure 'exit' per uscire: \n"
                ).lower()
                # Gestione uscita dalla funzione
            exit(ricerca)
            # Controllo se l'input è vuoto
            if ricerca == None or ricerca == "":
                print("\nErrore: l'anno non può essere vuoto.\n")
                continue
            elif ricerca == "back":
                print("\nOperazione annullata, ritorno al menu precedente.\n")
                return df.iloc[0:0]
            # Controllo se l'input è numerico
            elif not ricerca.isdigit():
                print("\nErrore: l'anno deve essere numerico.\n")
                continue
            # Controllo se l'anno è di 4 cifre
            elif len(ricerca) != 4:
                print("\nErrore: l'anno deve essere di 4 cifre.\n")
                continue
            else:
                # Filtra il DataFrame per l'anno di inizio
                rigaDF = df[df["AnnoInizio"].str.contains(ricerca)]
                # Stampa messaggio se non trova l'anno, altrimenti mostra i dati trovati
                print(
                    f"\nnessun anno di inizio: {ricerca} trovato\n"
                    if rigaDF.empty
                    else rigaDF.head()
                )
                stampa_completa(rigaDF)
                break
        except ValueError:
            # Gestione errori di inserimento
            print("\nErrore nell'inserimento. Riprova.\n")
            continue
    return rigaDF


def ricerca_per_intervallo(df, anno: list) -> object:
    """
    Funzione per la ricerca di un dipendente per intervallo di anni.
    """
    while True:
        try:
            if anno != None:
                ricerca: list = anno
            elif anno == None:
                # se non viene passato un intervallo, chiede all'utente di inserirne uno
                ricerca: list = (
                    input(
                        "\ninserisci l'intervallo di anni da cercare (es. 2000-2020), o 'back per annullare operazione' oppure 'exit' per uscire:  \n\n"
                    )
                    .lower()
                    .split("-")
                )
            exit(ricerca[0])
            if ricerca[0] == "back":
                print("\nOperazione annullata, ritorno al menu precedente.\n")
                return df.iloc[0:0]
            elif len(ricerca) != 2:
                print("\nErrore: l'intervallo deve essere composto da due anni.\n")
                continue
            elif not all(anno.isdigit() for anno in ricerca):
                print("\nErrore: l'intervallo deve essere numerico.\n")
                continue
            elif not all(len(anno) == 4 for anno in ricerca):
                print("\nErrore: gli anni devono essere di 4 cifre.\n")
                continue
            else:
                rigadf = df[
                    (df["AnnoInizio"] >= ricerca[0]) & (df["AnnoInizio"] <= ricerca[1])
                ]
                # Stampa messaggio se non trova l'intervallo, altrimenti mostra i dati trovati
                print(
                    f"\nnessun dipendente trovato in questa fascia: {ricerca}\n"
                    if rigadf.empty
                    else rigadf.head()
                )
                stampa_completa(rigadf)
                break
        except ValueError:
            # Gestione errori di inserimento
            print("\nErrore nell'inserimento. Riprova.\n")
            continue

    return rigadf


# Filtrare per Numero di Richiami
#   - Input: numero esatto, maggiore di o minore di.
#   - Mostra i dipendenti che rispettano il criterio.


def ricerca_per_numero_richiami(df, numero: str) -> object:
    """
    Funzione per la ricerca di un dipendente per numero di richiami.
    """
    while True:
        try:
            if numero != None:
                ricerca: str = numero
            elif numero == None:
                # se non viene passato un numero, chiede all'utente di inserirne uno
                ricerca: str = input(
                    "\ninserisci il numero di richiami da cercare, o 'back per annullare operazione' oppure 'exit' per uscire: \n\n"
                ).lower()
            exit(ricerca)
            if ricerca == None or ricerca == "":
                print("\nErrore: il numero non può essere vuoto.\n")
                continue
            elif ricerca == "back":
                print("\nOperazione annullata, ritorno al menu precedente.\n")
                return df.iloc[0:0]
            elif not ricerca.isdigit():
                print("\nErrore: il numero deve essere numerico.\n")
                continue
            else:
                rigaDF = df[df["Richiami"] == ricerca]
                print(
                    f"\nnessun richiamo: {ricerca} trovato\n"
                    if rigaDF.empty
                    else rigaDF.head()
                )
                stampa_completa(rigaDF)
                break
        except ValueError:
            # Gestione errori di inserimento
            print("\nErrore nell'inserimento. Riprova.\n")
            continue

    return rigaDF


def ricerca_per_numero_richiami_istruzione(df, n: str, istruzione: str) -> None:
    """
    Funzione per la ricerca di un dipendente per numero di richiami.
    """
    while True:
        try:
            if n != None:
                numero: str = n
            elif n == None:
                # se non viene passato un numero, chiede all'utente di inserirne uno
                numero: str = input(
                    "\ninserisci il numero di richiami da cercare, o 'back per annullare operazione' oppure 'exit' per uscire:  \n\n"
                ).lower()
            if numero == None or numero == "":
                print("\nErrore: il numero non può essere vuoto.\n")
                continue
            elif numero == "back":
                print("\nOperazione annullata, ritorno al menu precedente.\n")
                return df.iloc[0:0]
            elif not numero.isdigit():
                print("\nErrore: il numero deve essere numerico.\n")
                continue
            # Se l'istruzione è "maggiore", filtra i dipendenti con richiami maggiori o uguali al numero
            if istruzione == "maggiore":
                dfriga = df[df["Richiami"] >= numero]

            # Se l'istruzione è "minore", filtra i dipendenti con richiami minori o uguali al numero
            elif istruzione == "minore":
                dfriga = df[df["Richiami"] <= numero]
            # Stampa messaggio se non trova richiami, altrimenti mostra i dati trovati
            print(
                f"\nnessun richiamo: {numero} trovato\n" if dfriga.empty else dfriga.head()
            )
            stampa_completa(dfriga)
            break
        except ValueError:
            # Gestione errori di inserimento
            print("\nErrore nell'inserimento. Riprova.\n")
            continue

    return dfriga


# test
if __name__ == "__main__":
    from letturaFile_csv import creaDataFrame
    from stampa import stampa_completa
    from uscita import exit

    # Nota: Per testare le funzioni, è necessario passare un DataFrame valido
    f = creaDataFrame("../risorse/dipendenti_azienda.csv")
    ricerca_per_id(f, None)
    ricerca_per_nominativo(f, None)
    ricerca_per_professione(f, None)
    ricerca_per_anno_inizio(f, None)
    ricerca_per_intervallo(f, None)
    ricerca_per_numero_richiami(f, None)
    ricerca_per_numero_richiami_istruzione(f, None, "maggiore")
    ricerca_per_numero_richiami_istruzione(f, None, "minore")
