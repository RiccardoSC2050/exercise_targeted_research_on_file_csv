# Statistiche aziendali
#    - Numero totale di dipendenti.
#    - Numero dipendenti per professione.
#    - Media richiami.
#    - Media anni di anzianità in azienda.

from datetime import date


def numero_totale_dipendenti(df):
    """Restituisce il numero totale di dipendenti."""
    return len(df)


def numero_dipendenti_per_istruzione(df) -> int:
    i: int = 0
    while True:
        try:
            istruzione: str = input(
                "per quale parametro vuoi il conteggio dei dipendenti? chiave-valore es: Nome-Giorgio: "
            )

            valori: list = istruzione.split("-")

            if valori[0] in df.columns:
                i = (df[valori[0]] == valori[1]).sum()

            elif istruzione.isdigit():
                print(f"Parametro '{istruzione}' non valido. Deve essere una stringa.")
            else:
                print(f"Parametro '{istruzione}' non trovato nel DataFrame.")
            break
        except Exception as e:
            print("errore inserimento", e)

    return i


def media_richiami(df) -> float:

    numeri: list = df["Richiami"].tolist()
    float_numeri: list = [float(n) for n in numeri]
    return sum(float_numeri) / len(float_numeri)


def media_anni_anzianita_aziendale(df) -> float:

    anni: list = df["AnnoInizio"].tolist()
    int_anni: list = [int(anno) for anno in anni]
    anni_lavoro: list = [(date.today().year - anno) for anno in int_anni]
    return (sum(anni_lavoro) / len(anni_lavoro)).__round__(1)


if __name__ == "__main__":
    import pandas as pd
    from letturaFile_csv import *

    # Esempio di utilizzo delle funzioni
    df = creaDataFrame("../risorse/dipendenti_azienda.csv")

    print("Numero totale di dipendenti:", numero_totale_dipendenti(df))
    print("Numero dipendenti per professione:", numero_dipendenti_per_istruzione(df))
    print("Media richiami:", media_richiami(df))
    print("Media anni di anzianità in azienda:", media_anni_anzianita_aziendale(df))
