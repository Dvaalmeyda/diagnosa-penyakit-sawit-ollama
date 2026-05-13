from inference_sdk import InferenceHTTPClient
import os

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="58c7Qs0Cbmt5M5MvbPXk"
)

image_path = "playground/original.jpg"

if os.path.exists(image_path):
    try:
        #input_image = input("Enter the path to your image: ")
        result = CLIENT.infer(image_path, model_id="palm-tree-leaves-diseases-old/2")

        print(result)
    
    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"Image file '{image_path}' does not exist.")