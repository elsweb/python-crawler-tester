import cloudscraper
scraper = cloudscraper.create_scraper()
print(scraper.get("https://mangaschan.net").text)