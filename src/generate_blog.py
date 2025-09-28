import requests
import google.generativeai as genai
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

def generate_blog_post(shops_data):
    # Configure Gemini API
    genai.configure(api_key='AIzaSyB_Mslm7fKrRZ7WWs9-IW3D595v1VNrXVc')
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    
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
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating blog post: {e}")
        return None

def save_blog_post(blog_content):
    if blog_content:
        try:
            with open('blog_post.md', 'w', encoding='utf-8') as f:
                f.write(blog_content)
            print("Blog post has been saved to blog_post.md")
        except Exception as e:
            print(f"Error saving blog post: {e}")

def send_email(blog_content):
    sender_email = "naman.m25292@nst.rishihood.edu.in"
    receiver_email = "mishranaman152007@gmail.com"
    password = "mswv obsj gunu yrvc"  # App password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Latest Blog Post: Shopping in Satna"

    # Add blog content to email body
    msg.attach(MIMEText(blog_content, 'plain'))

    try:
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable TLS
        server.login(sender_email, password)
        
        # Send email
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    print("Fetching shops data...")
    shops_data = get_shops_data()
    
    if shops_data:
        print("Generating blog post...")
        blog_content = generate_blog_post(shops_data)
        if blog_content:
            save_blog_post(blog_content)
            print("Sending blog post via email...")
            send_email(blog_content)
    else:
        print("Failed to fetch shops data")

if __name__ == "__main__":
    main()