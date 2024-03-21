from bs4 import BeautifulSoup
import requests

def html_to_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        # Get the text content
        text = soup.get_text()
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading HTML content: {e}")
        return None
    
#pip install beautifulsoup4
def download_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading HTML content: {e}")
        return None


def download_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading HTML content: {e}")
        return None

# Example usage:
url = "https://www.iic.com/job-opening/informatica-data-engineer/z5G7h3l6a1kMvyS65NP3c44OM2b84E4JnF5hYh58fH4="
html_content = download_html(url)
text_content = html_to_text(url)
if text_content:
    print(text_content)