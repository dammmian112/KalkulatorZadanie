def dodaj(a, b):
    """Funkcja dodaje dwie liczby i zwraca wynik"""
    return a + b

def odejmowanie(a, b):
    """
    Funkcja odejmująca drugą liczbę od pierwszej.
    """
    return a - b

def main():
    """
    Prosty kalkulator z funkcjami dodawania i odejmowania.
    """
    print("=" * 40)
    print("KALKULATOR")
    print("=" * 40)

    try:
        # Pobieranie pierwszej liczby
        liczba1 = float(input("\nPodaj pierwszą liczbę: "))
        
        # Pobieranie drugiej liczby
        liczba2 = float(input("Podaj drugą liczbę: "))
        
        # Wykonanie działań
        wynik_dodawanie = dodaj(liczba1, liczba2)
        wynik_odejmowanie = odejmowanie(liczba1, liczba2)
        
        # Wyświetlenie wyników
        print("\n" + "-" * 40)
        print(f"{liczba1} + {liczba2} = {wynik_dodawanie}")
        print(f"{liczba1} - {liczba2} = {wynik_odejmowanie}")
        print("-" * 40)
        
    except ValueError:
        print("\nBłąd! Proszę podać poprawne liczby.")
    except Exception as e:
        print(f"\nWystąpił błąd: {e}")

# Test funkcji przy uruchomieniu pliku bez interakcji
if __name__ == "__main__":
    main()
