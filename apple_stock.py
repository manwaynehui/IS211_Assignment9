import requests
from bs4 import BeautifulSoup

# Link scraped for this assignment: https://finance.yahoo.com/quote/AAPL/history?p=AAPL

def main():
    url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")

        if table:
            print(f"{'Date':<15} | {'Close Price':<10}")
            print("-" * 30)

            # Yahoo stores the rows in <tbody>
            rows = table.find("tbody").find_all("tr") if table.find("tbody") else table.find_all("tr")

            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    date = cols[0].get_text(strip=True)
                    close = cols[4].get_text(strip=True)
                    print(f"{date:<15} | {close:<10}")
        else:
            print("Status 200 but table not found. Yahoo might be hiding it today.")
    else:
        print(f"Failed. Error code: {response.status_code}")


if __name__ == "__main__":
    main()