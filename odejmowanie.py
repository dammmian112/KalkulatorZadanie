def odejmowanie(a, b):
    """
    Funkcja odejmująca drugą liczbę od pierwszej.
    
    Args:
        a (float): Pierwsza liczba (odjemna)
        b (float): Druga liczba (odjemnik)
    
    Returns:
        float: Wynik odejmowania (a - b)
    """
    return a - b


def main():
    """
    Główna funkcja kalkulatora z funkcją odejmowania.
    """
    print("=" * 40)
    print("KALKULATOR - ODEJMOWANIE")
    print("=" * 40)
    
    try:
        # Pobieranie pierwszej liczby
        liczba1 = float(input("\nPodaj pierwszą liczbę: "))
        
        # Pobieranie drugiej liczby
        liczba2 = float(input("Podaj drugą liczbę: "))
        
        # Wykonanie odejmowania
        wynik = odejmowanie(liczba1, liczba2)
        
        # Wyświetlenie wyniku
        print("\n" + "-" * 40)
        print(f"Wynik: {liczba1} - {liczba2} = {wynik}")
        print("-" * 40)
        
    except ValueError:
        print("\nBłąd! Proszę podać poprawne liczby.")
    except Exception as e:
        print(f"\nWystąpił błąd: {e}")


if __name__ == "__main__":
    main()
