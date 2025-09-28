import requests
import openai
import json
from typing import Optional

def get_shops_data():
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
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def generate_blog_post_openai(shops_data: dict, api_key: str) -> Optional[str]:
    openai.api_key = api_key
    
    # Prepare the context from shops data
    shops_context = ""
    vmart_info = ""
    
    for item in shops_data.get('organic', []):
        if 'V-Mart' in item.get('title', ''):
            vmart_info += f"{item.get('title', '')}\n{item.get('snippet', '')}\n{item.get('link', '')}\n\n"
        shops_context += f"{item.get('title', '')}\n{item.get('snippet', '')}\n\n"

    prompt = f"""
    Write an engaging and informative blog post about clothing shopping in Satna, Madhya Pradesh.
    Focus particularly on V-Mart while also mentioning other notable shops.
    
    Here's the information about V-Mart:
    {vmart_info}
    
    And here's information about other shops in the area:
    {shops_context}
    
    Requirements for the blog post:
    1. Engaging title
    2. Introduction about Satna's fashion scene
    3. Detailed section about V-Mart (highlight its advantages, location, and offerings)
    4. Brief mentions of other notable shops
    5. Conclusion with why V-Mart is a great choice
    6. Use a friendly, conversational tone
    7. Include practical shopping tips
    8. Around 800-1000 words
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional content writer specializing in retail and fashion blogs."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating blog post: {e}")
        return None

def save_blog_post(blog_content: Optional[str], filename: str = 'blog_post.md'):
    if blog_content:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(blog_content)
            print(f"Blog post has been saved to {filename}")
        except Exception as e:
            print(f"Error saving blog post: {e}")

def main():
    # You would need to replace this with your OpenAI API key
    OPENAI_API_KEY = "your-openai-api-key"
    
    print("Fetching shops data...")
    shops_data = get_shops_data()
    
    if shops_data:
        print("Generating blog post...")
        blog_content = generate_blog_post_openai(shops_data, OPENAI_API_KEY)
        save_blog_post(blog_content, 'blog_post_openai.md')
    else:
        print("Failed to fetch shops data")

if __name__ == "__main__":
    main()