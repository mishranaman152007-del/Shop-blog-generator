import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from clothes_shops import get_shop_details
from generate_blog import generate_blog_post

def send_email(recipient_email, subject, body):
    # Replace these with your email configuration
    sender_email = st.secrets["EMAIL"]
    sender_password = st.secrets["EMAIL_PASSWORD"]
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        # Create SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        return True
    except Exception as e:
        st.error(f"Failed to send email: {str(e)}")
        return False

def main():
    st.title("Shop Blog Post Generator")
    
    # Step 1: Fetch Shop Details
    st.header("Step 1: Fetch Shop Details")
    if st.button("Fetch Shop Details"):
        with st.spinner("Fetching shop details..."):
            shop_details = get_shop_details()
            st.session_state.shop_details = shop_details
            st.success("Shop details fetched successfully!")
            st.write(shop_details)

    # Step 2: Generate Blog Post
    st.header("Step 2: Generate Blog Post")
    if 'shop_details' in st.session_state and st.button("Generate Blog Post"):
        with st.spinner("Generating blog post..."):
            blog_post = generate_blog_post(st.session_state.shop_details)
            st.session_state.blog_post = blog_post
            st.success("Blog post generated successfully!")
            st.write(blog_post)

    # Step 3: Send Email
    st.header("Step 3: Send Email")
    if 'blog_post' in st.session_state:
        recipient_email = st.text_input("Enter recipient email:")
        if st.button("Send Email"):
            if recipient_email:
                with st.spinner("Sending email..."):
                    success = send_email(
                        recipient_email,
                        "New Shop Blog Post",
                        st.session_state.blog_post
                    )
                    if success:
                        st.success("Email sent successfully!")
                    else:
                        st.error("Failed to send email.")
            else:
                st.warning("Please enter a recipient email address.")

if __name__ == "__main__":
    main()