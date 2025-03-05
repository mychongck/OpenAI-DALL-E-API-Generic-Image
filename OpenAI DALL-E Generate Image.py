# Sample Python Script that call OpenAI API and uses DALL-E API model to generic a graphic


import openai
from PIL import Image
import requests
from io import BytesIO
def generate_image(description):
    response = openai.Image.create(
        model='dall-e-3',
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url
def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()
def main():
    # Set your OpenAI API key here
    openai.api_key = 'Your OpenAI API Key'          # Replace with your OpenAI API Key
    description = "an realistic image of pretty asian lady with detailed features, realistic style"
    image_url = generate_image(description)
    print(f"Generated image URL: {image_url}")
    display_image(image_url)
if __name__ == "__main__":
    main()
