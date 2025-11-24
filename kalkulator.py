from dodawanie import dodaj
from odejmowanie import odejmowanie
from mnozenie import mnozenie

def main():
    """Prosty kalkulator wywołujący wszystkie funkcje"""
    print("=" * 40)
    print("KALKULATOR - DODAWANIE, ODEJMOWANIE, MNOŻENIE")
    print("=" * 40)

    try:
        liczba1 = float(input("\nPodaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
        
        print("\n" + "-" * 40)
        print(f"{liczba1} + {liczba2} = {dodaj(liczba1, liczba2)}")
        print(f"{liczba1} - {liczba2} = {odejmowanie(liczba1, liczba2)}")
        print(f"{liczba1} * {liczba2} = {mnozenie(liczba1, liczba2)}")
        print("-" * 40)
        
    except ValueError:
        print("\nBłąd! Proszę podać poprawne liczby.")
    except Exception as e:
        print(f"\nWystąpił błąd: {e}")

if __name__ == "__main__":
    main()
