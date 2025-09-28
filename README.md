# 🏪 Shop Blog Generator

A Streamlit-powered application that automatically generates and emails detailed blog posts about clothing shops in Satna, Madhya Pradesh. The app uses Google's Search API (via Serper) and Generative AI to create engaging content.

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- **🔍 Automated Shop Research**: Fetches real-time data about clothing shops using Google Search API
- **🤖 AI-Powered Content Generation**: Uses Google's Generative AI to create engaging blog posts
- **📧 Email Integration**: Automatically sends formatted blog posts via email
- **🎯 User-Friendly Interface**: Simple 3-step process with Streamlit's intuitive UI

## Features

- Fetches top clothing shops in Satna, Madhya Pradesh
- Displays shop names, descriptions, and website links
- Uses Google Search API through Serper
- Easy to read formatted output

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/naman25/shop-blog-generator.git
cd shop-blog-generator
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you have your Serper API key ready
2. Run the script:
```bash
python src/clothes_shops.py
```

The script will display information about various clothing stores in Satna, including:
- Shop names
- Descriptions
- Website links (when available)
- Locations
- Contact information (when available)

## API Key

The script uses the Serper API. The API key is currently hardcoded in the script. For security purposes, it's recommended to move it to an environment variable or configuration file in a production environment.

## Output Format

The output is formatted with clear separators between each shop listing, making it easy to read and understand the information about each store.

## License

This project is open-source and available under the MIT License.

## Note

The search results are based on the Serper API's data and may not include all clothing stores in Satna. The information is as accurate as the data provided by the API.