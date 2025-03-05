Code By: CK Chong (mychongck@gmail.com)

To use the DALL-E API to generate and display an image, you'll need to follow these steps:

Step 1: Install the OpenAI Python library
Make sure you have the latest version of the OpenAI library installed:
pip install openai

Step 2: Set up your OpenAI API key
You need to have an OpenAI account and obtain an API key from the OpenAI dashboard.

Step 3: Write the Python code to generate and display the image
Here's a complete example:
	import openai
	from PIL import Image
	import requests
	from io import BytesIO
	
	def generate_image(description):
	response = openai.Image.create(
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
	openai.api_key = 'your_openai_api_key_here'
	
	description = "a portrait of a pretty cyborg lady with detailed features, realistic style"
	image_url = generate_image(description)
	print(f"Generated image URL: {image_url}")
	
	display_image(image_url)
	
	if __name__ == "__main__":
	main()


Step-by-Step Explanation:

1.	Import Libraries:
•	openai for interacting with the DALL-E API.
•	Pillow (PIL) for image handling.
•	requests for fetching the image from the URL.
•	io.BytesIO for handling the image data in memory.

3.	Generate Image:
•	The generate_image function uses the DALL-E API to create an image based on the provided description.
•	It returns the URL of the generated image.

4.	Display Image:
•	The display_image function fetches the image from the URL and displays it using Pillow.

5.	Main Function:
•	Sets the OpenAI API key.
•	Defines the description for the image.
•	Calls generate_image to get the image URL.
•	Calls display_image to display the image.

Important Notes:
•	Replace 'your_openai_api_key_here' with your actual OpenAI API key.
•	Ensure you have internet access to fetch the image from the URL.
•	The Image.show() method will open the image using your default image viewer.
This code should work with the latest version of the OpenAI API as of October 2023. If there are any updates to the API or the library, you may need to refer to the official OpenAI documentation for any changes in the API endpoints or parameters.

