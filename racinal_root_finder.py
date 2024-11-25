import numpy as np
import matplotlib.pyplot as plt

"""
This program finds the rational roots of a polynomial with integer coefficients using the Rational Root Theorem. 
The user can input a polynomial by selecting their language (French or English), and the program will:
1. Determine the divisors of the constant term and the leading coefficient.
2. Generate candidates (p/q) to test as potential rational roots.
3. Evaluate whether each candidate is a root of the polynomial.
4. Return, display and plot the rational roots (if any).

Key features:
- Multilingual support (French/English).
- User input validation.
- Accurate root calculation using `numpy`.
- Error handling for invalid polynomials.
"""

"""
Ce programme permet de trouver les racines rationnelles d'un polynôme à coefficients entiers en utilisant le théorème des racines rationnelles. 
L'utilisateur peut saisir un polynôme en choisissant sa langue (français ou anglais), après quoi le programme :
1. Vérifie les diviseurs du terme constant et du coefficient dominant.
2. Génère les candidats (p/q) à tester en tant que racines rationnelles potentielles.
3. Évalue si chaque candidat est une racine du polynôme.
4. Retourne, affiche et représente les racines rationnelles (s'il y en a).

Fonctionnalités :
- Gestion multilingue (français/anglais).
- Validation des entrées utilisateur.
- Calcul précis des racines avec `numpy`.
- Gestion des erreurs pour les polynômes non valides.
"""

def find_divisors(n):
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(-i)
    return divisors

def find_rational_roots(coeffs, lang):    
    if not coeffs or coeffs[0] == 0:
        if lang == 2:
            raise ValueError("Le polynôme doit avoir un coefficient dominant non nul.")
        else:
            raise ValueError("The polynomial must have a non-zero leading coefficient.")  

    a0 = coeffs[-1]
    an = coeffs[0]
    list_p = find_divisors(a0)
    list_q = find_divisors(an)
    
    candidates = set()
    
    for p in list_p:
        for q in list_q:
            if q != 0:
                candidates.add(p/q)
    
    racinals = []
    for r in candidates:
        if np.isclose(np.polyval(coeffs, r), 0):
            racinals.append(r)
    
    if lang == 2:
        if racinals:
            print("\nRacines rationnelles trouvées :", racinals)
        else:
            print("\nAucune racine rationnelle trouvée.")
    
    else:
        if racinals:
            print("\nRational roots found:", racinals)
        else:
            print("\nNo rational roots found.")
    
    plot_polynomial(coeffs, racinals, lang)
    return racinals

def plot_polynomial(coeffs, roots, lang):
    x = np.linspace(-10, 10, 500)
    y = np.polyval(coeffs, x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Polynom', color='blue')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    if roots:
        plt.scatter(roots, [0] * len(roots), color='red', label="Racines", zorder=5)
    plt.title("Représentation du polynôme" if lang == 2 else "Polynomial Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()
    
def lang_selector():
    lang = int(input("""Tape :
1: English
2: French  
"""))
    if lang == 1:
        return request_en()
    elif lang == 2:
        return request_fr()
    else:
        return lang_selector()

def request_fr(lang=2):
    coeffs = []
    deg = input('\nQuel est le degré de votre polynome : ')
    try:
        deg = int(deg)
        if deg < 0:
            print('Le degré doit être positif')
            return request_fr()
        elif deg == 0:
            coeffs = [1]
            return coeffs, deg
        else:
            print("\nVeuillez entrer les coeffs un par un dans l'ordre : ")
            for i in range(int(deg)+1):
                coeffs.append(int(input(f"coefficient {i + 1} (x^{deg - i}): ")))
            print("Coéfficients :", coeffs)

            return find_rational_roots(coeffs, lang)
        
    except ValueError:
        print('Veuillez entrer un nombre entier')

def request_en(lang=1):
    coeffs = []
    deg = input('\nWhat is the degree of your polynomial: ')
    try:
        deg = int(deg)
        if deg < 0:
            print('The degree must be positive')
            return request_en()
        elif deg == 0:
            coeffs = [1]
            return coeffs, deg
        else:
            print("\nPlease enter the coefficients one by one in order: ")
            for i in range(int(deg)+1):
                coeffs.append(int(input(f"coefficient {i + 1} (x^{deg - i}): ")))
            print("Coefficients :", coeffs)
            
            return find_rational_roots(coeffs, lang)
    
    except ValueError:
        print('Please enter an integer')

lang_selector()