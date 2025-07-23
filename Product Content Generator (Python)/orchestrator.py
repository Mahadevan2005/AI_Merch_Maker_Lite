import os
import subprocess
import time
import json
import requests
from datetime import datetime

# Generate product content (calling content_generator.py)
def generate_product():
    print("Process 1 : Generating content for product")
    subprocess.run(["python", "content_generator.py"], check=True)

# Reading the generated JSON
def read_product_data():
    print("Process 2 : Analyzing generated product data")
    with open("../Output/product.json", "r") as f:
        data = json.load(f)
    return data

# Simulating mockup (but for realtime we can do by opening index.html of Mock Product Visualizer folder)
def generate_mockup(product_data):
    print("Process 3 : Simulating mockup generation")
    mockup = {
        "mockups": [
            {
                "placement": "front",
                "image_url": product_data["image_path"],
                "dimensions": { "width": 512, "height": 512 },
                "position": { "x": 100, "y": 150 }
            }
        ],
        "status": "success",
        "created_at": datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    }
    return mockup

# POST it to Java server
def publish_product(mockup_data, product_data):
    print("Process 4 : Publishing product to a fake endpoint")

    payload = {
        "product_data": product_data,
        "mockups": mockup_data["mockups"],
        "created_at": mockup_data["created_at"]
    }

    url = "http://localhost:8080/publish"
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Product Published successfully!")
            result = response.json()
            result["product_data"] = product_data
            result["mockups"] = mockup_data["mockups"]
            return result
        else:
            print(f"Error {response.status_code}: {response.text}")
            return {"status": "error"}
    except requests.exceptions.RequestException as e:
        print("Connection Error: Is the Java server running at http://localhost:8080/publish?")
        print(e)
        return {"status": "error"}


# Saving the final output
def save_final_output(response_data):
    with open("../Output/final_result.json", "w") as f:
        json.dump(response_data, f, indent=4)
    print('Final response saved to "Output/final_result.json"')

# All processes start here
def main():
    generate_product()
    time.sleep(1)  # slight delay for file write
    product = read_product_data()
    mockup = generate_mockup(product)
    response = publish_product(mockup, product)
    save_final_output(response)

if __name__ == "__main__":
    main()
