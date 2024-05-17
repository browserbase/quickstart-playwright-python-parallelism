import multiprocessing
import os
from playwright.sync_api import sync_playwright, Playwright

def load_and_parse_file(file_path):
    lines = []

    with open(file_path, 'r') as file:
        lines = [line.rstrip() for line in file]

    return lines


def run(url):
    print(f"Scrape: {url}")
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.connect_over_cdp('wss://connect.browserbase.com?apiKey='+ os.environ["BROWSERBASE_API_KEY"])
        context = browser.contexts[0]
        page = context.pages[0]
        page.goto(url)
        return [url, page.content()]


def main():
    urls = load_and_parse_file("wikipedia_urls.txt")

    print(f"urls: {urls}")

    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(run, urls)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
