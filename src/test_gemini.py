import google.generativeai as genai
from pprint import pprint

def test_gemini_api(api_key):
    try:
        # Configure the API
        print("Configuring API...")
        genai.configure(api_key=api_key)
        
        # List available models
        print("\nListing available models:")
        for m in genai.list_models():
            print(f"- Name: {m.name}")
            print(f"  Supported generation methods: {m.supported_generation_methods}")
            print()
            
        # Try a simple generation
        print("\nTesting simple generation...")
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content('Write a hello world message')
        print("\nGeneration response:", response.text)
        
    except Exception as e:
        print(f"\nError occurred: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Verify your API key is correct")
        print("2. Check if you have the latest google-generativeai package")
        print("3. Ensure you have internet connectivity")
        print("4. Check if there are any region restrictions")
        print("5. Verify your API quota and billing status")

if __name__ == "__main__":
    API_KEY = "AIzaSyB_Mslm7fKrRZ7WWs9-IW3D595v1VNrXVc"
    test_gemini_api(API_KEY)