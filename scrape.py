import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.imdb.com/title/tt0338348/reviews"

reviews = []

# loop through the first 5 pages of reviews (20 reviews per page)
for page in range(1, 6):
    # make a request to the URL for the current page
    url = base_url + "?start=" + str((page-1)*20)
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # find all the review containers on the page
    review_containers = soup.find_all("div", {"class": "lister-item-content"})

    # iterate through the review containers and extract the review text
    for container in review_containers:
        review_text = container.find("div", {"class": "text"}).text
        reviews.append(review_text)

        if len(reviews) == 100:
            break

with open("polar_express_reviews.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Review"]) 
    for review in reviews:
        writer.writerow([review])
