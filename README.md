# AI Merchandise Maker Lite
A multi-language automation pipeline that simulates the daily generation and publication of AI-designed product listings. Built using Python, JavaScript and Java, this project showcases full-stack automation, API integrations, and AI-powered creativity.

## 🎯 Objective
To automate the creation and publishing of AI-generated product listings, simulating a real-world merch production pipeline. This includes:

- AI-based content and image generation
- Product mockup visualization
- Fake API publishing
- Orchestrated end-to-end automation

## 🔁 Workflow Overview

### Product Content Generator (Python)
    - Uses OpenAI GPT to generate product title, description, and tags.
    - Uses DALL·E API to generate product images.

### Mock Product Visualizer (JavaScript)
    - Overlays the generated image on a mock product (e.g., t-shirt or mug) using HTML5 Canvas.
    - Returns a mockup-style JSON response similar to Printful.

### Fake Product Publisher (Java)
    - Accepts product data via a fake API.
    - Logs the data and returns a dummy product ID.

### Automation Orchestrator (Python)
    - Triggers the pipeline (manually).
    - Automates the full flow from content to publishing.

## 📹 Task Walkthrough Video
    - https://drive.google.com/file/d/1v7yRMiIXKfL_uqxS9EMdFClDbOslgLgO/view?usp=sharing

## ⚙️ Installation Steps

### 1. Clone the Repository
```bash
    git clone https://github.com/Mahadevan2005/AI-Merch-Maker-Lite.git
    cd AI-Merch-Maker-Lite
```

### 2. Create & Activate Virtual Environment
- #### Create Virtual Environment
  
```bash
    python -m venv venv
```

- #### Activate Virtual Environment
For Linux/macOS:
```
    source venv/bin/activate
```
For Windows:
```
    venv\\Scripts\\activate
```

### 3. Install Required Backend Package Dependencies
```bash
    pip install -r requirements.txt
```

### 4. Install "gson-2.10.1.jar" for converting Java objects into their JSON representation from:
```bash
    https://search.maven.org/artifact/com.google.code.gson/gson/2.10.1/jar
```

### 5. In terminal move into the directory "Fake Product Publisher (Java)"
```bash
    cd Fake Product Publisher (Java)
```

### 6. Now first command is to compile the FakeProductPublisher.java and second is to run
```bash
    javac -cp gson-2.10.1.jar -d . FakeProductPublisher.java
    java -cp ".;gson-2.10.1.jar" FakeProductPublisher
```

### 7. Now in another terminal move into the directory "Product Content Generator (Python)"
```bash
    cd Product Content Generator (Python)
```

### 8. Now run the orchestrator.py to begin the entire flow
```bash
    python orchestrator.py
```

### 9. Now all the below output files can be seen under the folder "Output"
```bash
    final_result.json
    product.json
    product_image.png
```

## ⚙️ Sample Output
### Product.json
```bash
    {
    "title": "Global eBrand Tshirt",
    "description": "A simple white T-shirt having Global eBrand logo in the center.",
    "tags": [
        "white",
        "eBrand",
        "global",
        "simple",
        "fashion"
    ],
    "image_path": "../Output/product_image.png",
    "created_at": "2025-07-23 17:14:31.838926"
}
```
### final_result.json
```bash
    {
    "status": "success",
    "product_id": "fake-6241a0",
    "product_data": {
        "title": "Global eBrand Tshirt",
        "description": "A simple white T-shirt having Global eBrand logo in the center.",
        "tags": [
            "white",
            "eBrand",
            "global",
            "simple",
            "fashion"
        ],
        "image_path": "../Output/product_image.png",
        "created_at": "2025-07-23 22:40:49.814411"
    },
    "mockups": [
        {
            "placement": "front",
            "image_url": "../Output/product_image.png",
            "dimensions": {
                "width": 512,
                "height": 512
            },
            "position": {
                "x": 100,
                "y": 150
            }
        }
    ]
}
```

🌟 You are all set!
<hr>

## 📸 Screenshots
![Mockup Simulation](https://github.com/user-attachments/assets/216e5095-4ae7-4841-89b3-01318c9e00b3)
![Mockup Simulation](https://github.com/user-attachments/assets/a8ab72d1-976e-4ff0-83f2-17e6af13d512)

<h3 align="center">
Thank You ❤️
</h3>
