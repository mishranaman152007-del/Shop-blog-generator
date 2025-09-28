import streamlit as st
import requests
import google.generativeai as genai
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import re  # Added for email validation

# Configure the page
st.set_page_config(page_title="Shop Blog Generator", page_icon="🏪")

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
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error occurred while fetching shop details: {e}")
        return None

def generate_blog_post(shops_data):
    # Configure Gemini API
    genai.configure(api_key='AIzaSyB_Mslm7fKrRZ7WWs9-IW3D595v1VNrXVc')
    model = genai.GenerativeModel('models/gemini-pro')
    
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
    
    Please write a well-structured blog post that includes:
    1. An engaging introduction
    2. Overview of shopping options
    3. Detailed section about V-Mart
    4. Information about other notable shops
    5. Conclusion
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating blog post: {e}")
        return None

def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_blog_email(blog_content):
    formatted_content = f"""
Dear Reader,

I'm excited to share with you a comprehensive blog post about shopping opportunities in Satna, Madhya Pradesh.

{blog_content}

Best regards,
Shop Blog Generator
    """
    return formatted_content

def send_email(blog_content, recipient_email):
    if not is_valid_email(recipient_email):
        st.error("Please enter a valid email address.")
        return False
        
    try:
        # Email configuration
        sender_email = "naman.m25292@nst.rishihood.edu.in"
        sender_password = "qnii hggi qhtp guya"
        st.info(f"Starting email process from {sender_email} to {recipient_email}")
        
        # Create message with detailed logging
        st.info("Creating email message...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Shopping Blog: Clothing Stores in Satna"
        
        # Add formatted blog content
        formatted_content = format_blog_email(blog_content)
        msg.attach(MIMEText(formatted_content, 'plain'))
        
        # Connect to SMTP with detailed logging
        st.info("Connecting to SMTP server...")
        
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Using SSL connection
                st.info("Attempting login...")
                server.login(sender_email, sender_password)
                
                st.info("Sending email...")
                server.send_message(msg)
                
                st.success("✉️ Email sent successfully!")
                return True
                
        except smtplib.SMTPAuthenticationError as auth_error:
            st.error(f"⚠️ Authentication failed. Please make sure you have:\n1. Enabled 2-Step Verification in your Google Account\n2. Using the correct App Password\nError: {str(auth_error)}")
            return False
        except smtplib.SMTPException as smtp_error:
            st.error(f"📧 SMTP Error: {str(smtp_error)}")
            return False
        except Exception as e:
            st.error(f"❌ Unexpected error: {str(e)}")
            return False
            
    except Exception as e:
        st.error(f"❌ Error preparing email: {str(e)}")
        return False
            
    except smtplib.SMTPAuthenticationError:
        st.error("Failed to authenticate with the email server. Please check your email credentials.")
        return False
    except smtplib.SMTPException as smtp_error:
        st.error(f"SMTP error occurred: {smtp_error}")
        return False
    except Exception as e:
        st.error(f"Unexpected error occurred while sending email: {e}")
        return False

def main():
    st.title("🏪 Shop Blog Generator")
    
    # Step 1: Fetch Shop Details
    if 'shops_data' not in st.session_state:
        st.session_state.shops_data = None
    if 'blog_content' not in st.session_state:
        st.session_state.blog_content = None
    
    with st.container():
        st.header("Step 1: Fetch Shop Details")
        if st.button("Fetch Shop Data"):
            with st.spinner("Fetching shop details..."):
                st.session_state.shops_data = search_clothes_shops()
                if st.session_state.shops_data:
                    st.success("Shop data fetched successfully!")
                    
    # Step 2: Generate Blog Post
    if st.session_state.shops_data:
        with st.container():
            st.header("Step 2: Generate Blog Post")
            if st.button("Generate Blog"):
                with st.spinner("Generating blog post..."):
                    st.session_state.blog_content = generate_blog_post(st.session_state.shops_data)
                    if st.session_state.blog_content:
                        st.success("Blog post generated successfully!")
                        st.markdown("### Preview:")
                        st.write(st.session_state.blog_content)
    
    # Step 3: Send Email
    if st.session_state.blog_content:
        with st.container():
            st.header("Step 3: Send Blog Post via Email")
            
            # Email input with validation
            recipient_email = st.text_input("Enter recipient email:", key="email_input")
            
            # Show email preview
            if recipient_email:
                if is_valid_email(recipient_email):
                    with st.expander("Preview Email"):
                        st.markdown("### Email Preview")
                        st.text(format_blog_email(st.session_state.blog_content))
                    
                    # Send email button
                    if st.button("Send Email"):
                        with st.spinner("Sending email..."):
                            if send_email(st.session_state.blog_content, recipient_email):
                                st.success("✉️ Email sent successfully!")
                                # Clear the email input after successful send
                                st.session_state.email_input = ""
                else:
                    st.warning("Please enter a valid email address.")

if __name__ == "__main__":
    main()