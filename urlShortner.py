# pip install pyshorteners

import pyshorteners

def shorten_url(url):
    # Choose a URL shortening service (e.g., TinyURL, Bitly, etc.)
    s = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = s.tinyurl.short(url)

    return shortened_url

if __name__ == "__main__":
    # Example usage
    long_url = "https://www.example.com/this/is/a/long/url"
    short_url = shorten_url(long_url)

    print(f"Long URL: {long_url}")
    print(f"Short URL: {short_url}")
