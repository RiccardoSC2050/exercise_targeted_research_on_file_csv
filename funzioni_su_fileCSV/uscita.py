import sys
import time


def uscire() -> None:
    """
    Funzione per uscire dal programma.
    """
    print("Uscita dal programma. Grazie per aver utilizzato il sistema.")
    sys.exit(0)

    # Questa funzione può essere richiamata quando l'utente desidera uscire dal programma.
    # Ad esempio, può essere collegata a un comando di uscita nel menu principale.

def exit(n) -> None:
    if n == "exit":
        """
        Funzione per uscire dal programma.
        """
        print("Uscendo...")
        time.sleep(0.5)
        uscire()
    else:
        pass