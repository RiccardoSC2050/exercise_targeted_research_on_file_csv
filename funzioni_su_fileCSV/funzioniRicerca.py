import time

from funzioni_su_fileCSV.letturaFile_csv import creaDataFrame
from funzioni_su_fileCSV.uscita import exit
from funzioni_su_fileCSV.stampa import stampa_completa


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
                    "inserisci l'ID del dipendente da cercare, oppure 'exit' per uscire: "
                ).lower()
            # Gestione uscita dalla funzione
            exit(ricerca)
            # Controlli sull'ID inserito
            if ricerca == None or ricerca == "":
                print("Errore: l'ID non può essere vuoto.")
                continue
            elif ricerca.isdigit() == False:
                print("Errore: l'ID numerico.")
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
            print("Errore nell'inserimento. Riprova.")
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
                    "inserisci prima il nome e poi cognome da cercare, oppure 'exit' per uscire: "
                ).lower()

                # Gestione uscita dalla funzione
            exit(valore)
            # Se il valore è vuoto
            if valore == None or valore == "":
                print("Errore: il valore non può essere vuoto.")
                continue
                # Controlli sull'input
            elif not all(v.isalpha() for v in valore.split()):
                print("Errore: i nominativi devono contenere solo lettere.")
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
                        "Errore: inserisci solo il nome e il cognome, separati da uno spazio."
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
            print("Errore nell'inserimento. Riprova.")
            continue
        except IndexError:
            # Gestione errori di accesso agli indici della lista
            print("Errore: assicurati di inserire sia il nome che il cognome.")
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
                    "inserisci la professione da cercare, oppure 'exit' per uscire: "
                ).lower()

            exit(ricerca)
            if ricerca == None or ricerca == "":
                print("Errore: la professione non può essere vuota.")
                continue
            elif ricerca.isalpha() == False:
                print("Errore: la professione deve contenere solo lettere.")
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
                    "inserisci l'anno di inizio da cercare, oppure 'exit' per uscire: "
                ).lower()
                # Gestione uscita dalla funzione
            exit(ricerca)
            # Controllo se l'input è vuoto
            if ricerca == None or ricerca == "":
                print("Errore: l'anno non può essere vuoto.")
                continue
            # Controllo se l'input è numerico
            elif not ricerca.isdigit():
                print("Errore: l'anno deve essere numerico.")
                continue
            # Controllo se l'anno è di 4 cifre
            elif len(ricerca) != 4:
                print("Errore: l'anno deve essere di 4 cifre.")
                continue
            else:
                # Filtra il DataFrame per l'anno di inizio
                rigaDF = df[df["AnnoInizio"].str.contains(ricerca)]
                # Stampa messaggio se non trova l'anno, altrimenti mostra i dati trovati
                print(
                    f"nessun anno di inizio: {ricerca} trovato"
                    if rigaDF.empty
                    else rigaDF.head()
                )
                stampa_completa(rigaDF)
                break
        except ValueError:
            # Gestione errori di inserimento
            print("Errore nell'inserimento. Riprova.")
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
                        "inserisci l'intervallo di anni da cercare (es. 2000-2020), oppure 'exit' per uscire: "
                    )
                    .lower()
                    .split("-")
                )
            exit(ricerca)
            if len(ricerca) != 2:
                print("Errore: l'intervallo deve essere composto da due anni.")
                continue
            elif not all(anno.isdigit() for anno in ricerca):
                print("Errore: l'intervallo deve essere numerico.")
                continue
            elif not all(len(anno) == 4 for anno in ricerca):
                print("Errore: gli anni devono essere di 4 cifre.")
                continue
            else:
                rigadf = df[
                    (df["AnnoInizio"] >= ricerca[0]) & (df["AnnoInizio"] <= ricerca[1])
                ]
                # Stampa messaggio se non trova l'intervallo, altrimenti mostra i dati trovati
                print(
                    f"nessun dipendente trovato in questa fascia: {ricerca}"
                    if rigadf.empty
                    else rigadf.head()
                )
                stampa_completa(rigadf)
                break
        except ValueError:
            # Gestione errori di inserimento
            print("Errore nell'inserimento. Riprova.")
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
                    "inserisci il numero di richiami da cercare, oppure 'exit' per uscire: "
                ).lower()
            exit(ricerca)
            if ricerca == None or ricerca == "":
                print("Errore: il numero non può essere vuoto.")
                continue
            elif not ricerca.isdigit():
                print("Errore: il numero deve essere numerico.")
                continue
            else:
                rigaDF = df[df["Richiami"] == ricerca]
                print(
                    f"nessun richiamo: {ricerca} trovato"
                    if rigaDF.empty
                    else rigaDF.head()
                )
                stampa_completa(rigaDF)
                break
        except ValueError:
            # Gestione errori di inserimento
            print("Errore nell'inserimento. Riprova.")
            continue
    
    return rigaDF

def ricerca_per_numero_richiami_istruzione(df, numero: str, istruzione: str) -> None:
    """
    Funzione per la ricerca di un dipendente per numero di richiami.
    """
    while True:
        try:
            # Se l'istruzione è "maggiore", filtra i dipendenti con richiami maggiori o uguali al numero
            if istruzione == "maggiore":
                dfriga = df[df["Richiami"] >= numero]
            # Se l'istruzione è "minore", filtra i dipendenti con richiami minori o uguali al numero
            elif istruzione == "minore":
                dfriga = df[df["Richiami"] <= numero]
            # Stampa messaggio se non trova richiami, altrimenti mostra i dati trovati
            print(
                f"nessun richiamo: {numero} trovato" if dfriga.empty else dfriga.head()
            )
            stampa_completa(dfriga)
            break
        except ValueError:
            # Gestione errori di inserimento
            print("Errore nell'inserimento. Riprova.")
            continue

    return dfriga


# test
if __name__ == "__main__":
    # Nota: Per testare le funzioni, è necessario passare un DataFrame valido
    f = creaDataFrame("../risorse/dipendenti_azienda.csv")
    ricerca_per_id(f, None)
    ricerca_per_nominativo(f, None)
    ricerca_per_professione(f, None)
    ricerca_per_anno_inizio(f, None)
    ricerca_per_intervallo(f, None)
    ricerca_per_numero_richiami(f, None)
    ricerca_per_numero_richiami_istruzione(f, "2", "maggiore")
    ricerca_per_numero_richiami_istruzione(f, "2", "minore")
