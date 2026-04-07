import requests
from bs4 import BeautifulSoup

# Link scraped for this assignment: https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all

def scrape_football_stats():
    # Fetch data
    URL = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table
    table = soup.find("table", {"class": "TableBase-table"})

    if table:
        # Header
        print(f"{'Rank':<5} | {'Player':<20} | {'Pos':<5} | {'Team':<6} | {'Yards':<8} | {'TDs':<5}")
        print("-" * 65)

        # Loop through the rows in the body
        rows = table.find("tbody").find_all("tr")

        for i, row in enumerate(rows[:20], 1):
            cols = row.find_all("td")

            if len(cols) > 5:
                # Manual splitting for the first cell (Name, Pos, Team)
                raw_data = cols[0].text.split()
                player_name = f"{raw_data[0]} {raw_data[1]}"
                pos = raw_data[2]
                team = raw_data[3]

                tds = cols[3].text.strip()
                yards = cols[5].text.strip()

                print(f"{i:<5} | {player_name:<20} | {pos:<5} | {team:<6} | {yards:<8} | {tds:<5}")
    else:
        print("Table not found!")


if __name__ == "__main__":
    scrape_football_stats()