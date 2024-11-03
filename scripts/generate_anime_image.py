import requests

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# You can access the image with PIL.Image for example
def generate_anime_image(description, image_path):
    image_bytes = query({
        "inputs": "{description}",
    })
    import io
    from PIL import Image
    image = Image.open(io.BytesIO(image_bytes))

    image.save(image_path + "/flux-dev.png")
