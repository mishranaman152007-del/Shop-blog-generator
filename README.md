# Clothes Shops Finder - Satna

A Python script that uses the Serper API to fetch information about clothing stores in Satna, Madhya Pradesh. The script provides details about various clothing shops including their names, descriptions, locations, and contact information when available.

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
git clone <repository-url>
cd Serper - agent
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