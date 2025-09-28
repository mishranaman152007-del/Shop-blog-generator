import requests
import json

def search_clothes_shops():
    url = "https://google.serper.dev/search"
    
    headers = {
        'X-API-KEY': '5abce63108fa0916d4a9fd2b68635d875c0ddfa5',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "q": "clothes shops in Satna Madhya Pradesh",
        "num": 10
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        if 'organic' in data:
            print("\n=== Top Clothes Shops in Satna, Madhya Pradesh ===\n")
            
            for item in data['organic']:
                print(f"Shop Name: {item.get('title', 'N/A')}")
                print(f"Description: {item.get('snippet', 'N/A')}")
                if 'link' in item:
                    print(f"Link: {item['link']}")
                print("-" * 50)
                
        else:
            print("No results found")
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except KeyError as e:
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    search_clothes_shops()