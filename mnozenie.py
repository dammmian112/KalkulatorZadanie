def mnozenie(a, b):
    """
    Funkcja mnożąca dwie liczby.
    
    Args:
        a (float): Pierwsza liczba
        b (float): Druga liczba
    
    Returns:
        float: Wynik mnożenia (a * b)
    """
    return a * b

def main():
    print("=" * 40)
    print("KALKULATOR - MNOŻENIE")
    print("=" * 40)
    
    try:
        liczba1 = float(input("\nPodaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
        
        wynik = mnozenie(liczba1, liczba2)
        print("\n" + "-" * 40)
        print(f"Wynik mnożenia: {liczba1} * {liczba2} = {wynik}")
        print("-" * 40)
        
    except ValueError:
        print("\nBłąd! Proszę podać poprawne liczby.")
    except Exception as e:
        print(f"\nWystąpił błąd: {e}")


if __name__ == "__main__":
    main()
