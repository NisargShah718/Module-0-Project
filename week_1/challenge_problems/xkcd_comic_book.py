import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# Base URL
original_url = "https://xkcd.com/"

# Generate list of XKCD page URLs
list_of_pages = [original_url + str(i) for i in range(1, 3055+1)]  # Testing with 5 pages

# List to store image data
images = []
i = 0

for url in list_of_pages:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the comic image inside <div id="comic"> and get its 'src' attribute
    comic_div = soup.find("div", id="comic")
    if comic_div:
        img_tag = comic_div.find("img")
        img_url = "https:" + img_tag["src"]  # Add "https:" for absolute URL
        if "xkcd.com/" not in img_url:
            img_url = "https://xkcd.com/" + img_url

        # Download the image
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img = Image.open(BytesIO(img_response.content)).convert("RGB")  # Convert to RGB for PDF
            images.append(img)
            i += 1
            print("Image "+str(i)+" added")

        else:
            print(f"Failed to download {img_url}")
    else:
        print(f"No comic found at {url}")

# Save images as a PDF
if images:
    images[0].save("xkcd_comics.pdf", save_all=True, append_images=images[1:])
    print("Saved XKCD comics to xkcd_comics.pdf")
else:
    print("No images found!")
