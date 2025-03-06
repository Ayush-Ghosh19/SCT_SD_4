from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# Headers for requests
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

# HTTP Request
webpage = requests.get(url, headers=headers)

if webpage.status_code == 200:
    soup = BeautifulSoup(webpage.text, 'html.parser')

    # Extract product information
    products = soup.find_all("div", class_="thumbnail")

    data = []
    for product in products:
        # Extract name
        name = product.find("a", class_="title").text.strip()

        # Extract price
        price = product.find("h4", class_="price").text.strip()

        # Extract reviews
        review = product.find("p", class_="review-count").text.strip()

        # Extract rating (count number of stars)
        stars = len(product.find_all("span", class_="glyphicon glyphicon-star"))

        data.append([name, price, review, stars])

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["Product Name", "Price", "Reviews", "Rating"])
    
    # Print the DataFrame
    print(df)

else:
    print(f"Failed to retrieve webpage. Status code: {webpage.status_code}")
# Convert to DataFrame
df = pd.DataFrame(data, columns=["Product Name", "Price", "Reviews", "Rating"])

# Save DataFrame to CSV file
df.to_csv("SCT_SD_4.csv", index=False, encoding="utf-8")

print("Data successfully saved to tablets_data.csv")
