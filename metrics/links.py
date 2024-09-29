import requests
import re

def extract_links(content):
    """Extract links from markdown content."""
    link_pattern = r'\[([^\[]+)\]\(([^)]+)\)'
    return re.findall(link_pattern, content)

def classify_links(links):
    """Classify links as internal or external."""
    internal_links = []
    external_links = []
    for link_text, url in links:
        if url.startswith("http://") or url.startswith("https://"):
            external_links.append({"link_text": link_text, "url": url})
        else:
            internal_links.append({"link_text": link_text, "url": url})
    return internal_links, external_links

def analyze_links(content):
    """Main function to analyze links and return structured data."""
    links = extract_links(content)
    internal_links, external_links = classify_links(links)
    return {
        "internal_links": internal_links,
        "external_links": external_links
    }

def check_link(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 404:
            return f"Broken link (404): {url}"
        elif response.status_code == 200:
            return f"Valid link: {url}"
        else:
            return f"Link returned status {response.status_code}: {url}"
    except requests.exceptions.RequestException as e:
        return f"Error checking link: {url}, Error: {str(e)}"

# Example use
if __name__ == "__main__":
    links = ["https://example.com", "https://nonexistent.com"]
    for link in links:
        print(check_link(link))


# Ideally this is two different functions
# One checks individual links so you can check everything as you go
# Another takes a list of links and checks every unique domain or possible unique link
# Basically, checking links is resource intensive and we'd like to avoid duplicates wherever possible