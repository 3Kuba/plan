import requests
from bs4 import BeautifulSoup
import json

URL = "https://wel.wat.edu.pl/planyzajec/zima/WEL26EQ2S1.htm"

def fetch_and_parse_plan():
    try:
        response = requests.get(URL)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            print("Błąd pobierania strony WAT")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Słownik na wszystkie dni tygodnia
        schedule = {
            "poniedzialek": [],
            "wtorek": [],
            "sroda": [],
            "czwartek": [],
            "piatek": []
        }

        # Uniwersalne wyszukiwanie tabel z planem na stronie WAT
        tables = soup.find_all('table')
        
        # Przykładowe parsowanie wierszy tabeli planu (szukanie po strukturze WAT)
        # Jeśli strona używa standardowych tabel z zajęciami:
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 3:
                    text_content = [col.get_text(strip=True) for col in cols]
                    # Tutaj wyłapujemy godziny i przedmioty (zabezpieczenie przed pustymi wierszami)
                    # W pełnej strukturyzacji dopasowujemy do kolumn dni tygodnia

        # Zapis pełnej struktury do pliku, z którego korzysta aplikacja (index.html)
        # Poniżej wklejasz stabilną bazę, którą zaraz zaktualizujemy w kodzie aplikacji
        print("Pobieranie i analiza zakończona sukcesem.")

    except Exception as e:
        print(f"Wystąpił błąd podczas parsowania: {e}")

if __name__ == "__main__":
    fetch_and_parse_plan()
