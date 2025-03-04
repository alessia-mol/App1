from datetime import datetime

def berechne_zeit(d, K):
    """
    Berechnet die benötigte Zeit t basierend auf der Formel t = (d / K)².

    :param d: Eindringtiefe (in Metern)
    :param K: Materialkonstante (K > 0)
    :return: Dictionary mit berechneter Zeit, Kategorie und Zeitstempel
    """
    if K > 0:
        t = (d / K) ** 2
        return {
            "time": round(t, 4),
            "timestamp": datetime.now(),
            "message": "Berechnung erfolgreich"
        }
    else:
        return {
            "time": None,
            "timestamp": datetime.now(),
            "message": "Ungültige Eingabe. K darf nicht 0 sein."
        }
        