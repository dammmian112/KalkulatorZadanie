def dodaj(a, b):
    """Funkcja dodaje dwie liczby i zwraca wynik"""
    return a + b

def odejmowanie(a, b):
    """Funkcja odejmująca drugą liczbę od pierwszej"""
    return a - b

def main():
    """Prosty kalkulator z funkcjami dodawania i odejmowania"""
    print("=" * 40)
    print("KALKULATOR - DODAWANIE I ODEJMOWANIE")
    print("=" * 40)

    try:
        liczba1 = float(input("\nPodaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
        
        wynik_dodawanie = dodaj(liczba1, liczba2)
        wynik_odejmowanie = odejmowanie(liczba1, liczba2)
        
        print("\n" + "-" * 40)
        print(f"{liczba1} + {liczba2} = {wynik_dodawanie}")
        print(f"{liczba1} - {liczba2} = {wynik_odejmowanie}")
        print("-" * 40)
        
    except ValueError:
        print("\nBłąd! Proszę podać poprawne liczby.")
    except Exception as e:
        print(f"\nWystąpił błąd: {e}")

if __name__ == "__main__":
    main()
