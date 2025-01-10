import multiprocessing
import os
import time
from playwright.sync_api import sync_playwright, TimeoutError, Error

def load_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        return [line.rstrip() for line in file]

def run(url):
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            print(f"Scraping {url} (Attempt {attempt + 1}/{max_retries})")
            with sync_playwright() as playwright:
                browser = playwright.chromium.connect_over_cdp(
                    'wss://connect.browserbase.com?apiKey=' + os.environ["BROWSERBASE_API_KEY"]
                )
                context = browser.new_context()  # Create new context instead of using existing one
                page = context.new_page()
                
                # Add headers to appear more like a regular browser
                page.set_extra_http_headers({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                })
                
                response = page.goto(url, wait_until='networkidle', timeout=30000)
                if response.status == 200:
                    content = page.content()
                    context.close()
                    browser.close()
                    return [url, content]
                else:
                    raise Error(f"Received status code {response.status}")
                    
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                return [url, f"Failed after {max_retries} attempts: {str(e)}"]

def main():
    urls = load_and_parse_file("wikipedia_urls.txt")
    print(f"Starting scraping of {len(urls)} URLs")
    
    # Reduce number of parallel processes to avoid overwhelming the connection
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(run, urls)

    # Process results
    for url, content in results:
        if isinstance(content, str) and content.startswith("Failed"):
            print(f"Failed URL: {url}")
            print(f"Error: {content}")
        else:
            print(f"Successfully scraped: {url}")

    print(f"Results: {results}")

if __name__ == "__main__":
    main()
