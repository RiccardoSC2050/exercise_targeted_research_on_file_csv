import os

import pandas as pd


def salva_csv(df, nome_file: str) -> None:
    """Salva il DataFrame in un file CSV."""
    try:
        if nome_file != os.path.join("risorse","istantCSV","istant.csv"):
            if not (df.empty):
                df.to_csv(
                    os.path.join("risorse", "nuoviCSV", nome_file + ".csv"),
                    index=False,
                    encoding="utf-8",
                )
                print(f"\nFile salvato con successo come {nome_file}")

            else:
                print("\nnon salvabile, il file è vuoto\n")
        else:
            if not (df.empty):
                df.to_csv(
                    os.path.join(nome_file),
                    index=False,
                    encoding="utf-8",
                )

            else:
                print("\nnon salvabile, il file è vuoto\n")

    except Exception as e:
        print(f"\nErrore durante il salvataggio del file: {e}\n")


def distruggi_file(nomeFile) ->None:
    try:
        if os.path.exists(nomeFile):
            os.remove(nomeFile)
        else:
            pass
    except Exception as e:
        print("\nerrore durante la canecllazione file", e)

if __name__ == "__main__":
    pass
