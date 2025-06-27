import requests
from bs4 import BeautifulSoup

def scrape_newegg(query):
    url = f"https://www.newegg.com/p/pl?d={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    items = []
    for item in soup.select(".item-cell")[:5]:
        name = item.select_one(".item-title")
        price = item.select_one(".price-current")
        img = item.select_one("img")
        link = name["href"] if name else ""
        items.append({
            "name": name.text if name else "N/A",
            "price": price.text.strip() if price else "N/A",
            "link": link,
            "image": img["src"] if img else ""
        })
    return items

def scrape_jawa(query):
    url = f"https://www.jawa.gg/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    items = []
    for item in soup.select(".sc-kZmsYB"):
        name = item.select_one(".sc-jRQBWg")
        price = item.select_one(".sc-hlQUhX")
        link = item.select_one("a")
        img = item.select_one("img")
        if name and link and img:
            items.append({
                "name": name.text.strip(),
                "price": price.text.strip() if price else "N/A",
                "link": "https://www.jawa.gg" + link["href"],
                "image": img["src"]
            })
    return items

def scrape_all(query):
    return {
        "newegg": scrape_newegg(query),
        "jawa": scrape_jawa(query),
        "amazon": []  # Placeholder
    }