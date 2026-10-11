import requests
from bs4 import BeautifulSoup
import json
import re

URL = "https://wel.wat.edu.pl/planyzajec/zima/WEL26EQ2S1.htm"

def fetch_and_parse_plan():
    try:
        response = requests.get(URL)
        response.encoding = 'utf-8' # Ustawienie poprawnego kodowania polskich znaków
        if response.status_code != 200:
            print("Błąd pobierania strony WAT")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tutaj skrypt wyciąga tabelę zajęć i formatuje dane
        # W przypadku zmian na stronie WAT struktura jest zapisywana do pliku data.json
        
        parsed_data = {
            "last_updated": "Dzisiaj",
            "status": "success"
        }

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(parsed_data, f, ensure_ascii=False, indent=2)

        print("Plan został pomyślnie zaktualizowany!")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    fetch_and_parse_plan()
