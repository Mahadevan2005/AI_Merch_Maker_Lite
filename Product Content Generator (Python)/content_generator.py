import json
import shutil
import os
from datetime import datetime

def generate_product_info():
    product_title = "Global eBrand Tshirt"
    product_description = "A simple white T-shirt having Global eBrand logo in the center."
    tags = ["white", "eBrand", "global", "simple", "fashion"]
    return {
        "title": product_title,
        "description": product_description,
        "tags": tags
    }

def generate_ai_image(prompt, save_path):
    sample_image = "sample_input/design.png" 
    if not os.path.exists(sample_image):
        raise FileNotFoundError(f"Sample image not found at: {sample_image}")
    
    shutil.copy(sample_image, save_path)

def main():
    os.makedirs("../Output", exist_ok=True)

    # We start generating the product content
    data = generate_product_info()

    # Here we generate AI Image (but for now we use image from our local system)
    prompt = data["description"]
    image_path = "../Output/product_image.png"
    generate_ai_image(prompt, image_path)

    data["image_path"] = image_path
    data["created_at"] = str(datetime.now())

    # Here we save the JSON into the Output folder
    with open("../Output/product.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Product generated with sample image!")

if __name__ == "__main__":
    main()


# If we are generating the content using OPENAI API and DALL-E the code goes like

# import os
# import json
# import openai
# from datetime import datetime

# openai.api_key = os.getenv("OPENAI_API_KEY") 

# def generate_product_info():
#     prompt = (
#         "Generate a JSON object for an AI-generated fashion product. "
#         "Include a creative product title, a short engaging description, and a list of 5 tags."
#     )
    
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a creative merchandiser."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.8
#     )

#     try:
#         json_text = response['choices'][0]['message']['content']
#         data = json.loads(json_text)
#         return data
#     except Exception as e:
#         print("Error parsing GPT response:", e)
#         print("Raw response:", response)
#         raise

# def generate_ai_image(prompt, save_path):
#     response = openai.Image.create(
#         model="dall-e-3",
#         prompt=prompt,
#         n=1,
#         size="1024x1024",
#         response_format="url"
#     )

#     image_url = response["data"][0]["url"]

#     # Download image
#     import requests
#     img_data = requests.get(image_url).content
#     with open(save_path, "wb") as f:
#         f.write(img_data)

# def main():
#     os.makedirs("../Output", exist_ok=True)

#     print("Generating product content...")
#     data = generate_product_info()

#     print("Generating image with DALL·E...")
#     prompt = data["description"]
#     image_path = "../Output/product_image.png"
#     generate_ai_image(prompt, image_path)

#     data["image_path"] = image_path
#     data["created_at"] = str(datetime.now())

#     with open("../Output/product.json", "w") as f:
#         json.dump(data, f, indent=4)

#     print("Product generated with OpenAI GPT + DALL·E!")

# if __name__ == "__main__":
#     main()
