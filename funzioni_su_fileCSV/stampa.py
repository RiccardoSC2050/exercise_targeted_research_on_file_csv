from funzioni_su_fileCSV.salvataggioCSV_valori import salva_csv, distruggi_file
from funzioni_su_fileCSV.letturaFile_csv import visualizzaTabella
import os

def stampa_completa(df) -> None:
    
    if not df.empty:
        try:
            nomeFile_istantaneo : str = os.path.join("risorse","istantCSV","istant.csv")
            salva_csv(df, nomeFile_istantaneo) #crea il file
            visualizzaTabella(nomeFile_istantaneo)
            distruggi_file(nomeFile_istantaneo)
        except Exception as e:
            print("errore in stampa completa: ",e)
    else:
        print("nessun dato da visualizzare")



