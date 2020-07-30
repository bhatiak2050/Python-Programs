import requests, sys, threading
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
from tkinter import *

class MultiThreadScrapper:

    def __init__(self, base_url):
        self.base_url = base_url
        self.root_url = '{}://{}'.format(urlparse(self.base_url).scheme, urlparse(self.base_url).netloc)
        self.pool = ThreadPoolExecutor(max_workers=20)
        self.scraped_pages = set([])
        self.to_crawl = Queue()
        self.to_crawl.put(self.base_url)
        self.exit_request_flag=False

    def parse_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.findAll('a', href=True)
        for link in links:
            url = link['href']
            if url.startswith('/') or url.startswith(self.root_url):
                url = urljoin(self.root_url, url)
                if url not in self.scraped_pages:
                    self.to_crawl.put(url)

    def post_scrape_callback(self, res):
        result = res.result()
        if result and result.status_code == 200:
            self.parse_links(result.text)

    def scrape_page(self, url):
        try:
            res = requests.get(url, timeout=(3, 30))
            return res
        except requests.RequestException:
            return

    def run_scraper(self):
        while not self.exit_request_flag:
            try:
                target_url = self.to_crawl.get(timeout=60)
                if target_url not in self.scraped_pages:
                    print("Scraping URL: {}".format(target_url))
                    set_text("Scraping URL: {}\n".format(target_url))
                    self.scraped_pages.add(target_url)
                    job = self.pool.submit(self.scrape_page, target_url)
                    job.add_done_callback(self.post_scrape_callback)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue
    
    def interrupt_scraper(self):
        self.exit_request_flag=True

def launch():
    if url_field.get() == "":
        print("empty input")
        set_text("empty input")
    else:
        base_url = url_field.get()
        scraper = MultiThreadScrapper(base_url)
        
        scraper_thread = threading.Thread(target=scraper.run_scraper)
        scraper_thread.start()

def set_text(text):
    terminal_field.insert(END, text)
    return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
        var = MultiThreadScrapper(base_url)
        var.run_scraper()
    else:

        root = Tk()
        root.configure(background='light blue')
        root.title("Python Web Crawler")
        root.geometry("450x250")

        heading = Label(root, font = "Helvetica 24 bold", text="Python Web Crawler", bg="light blue")
        url = Label(root, font = "Helvetica 16 bold", text="URL", bg="light blue")

        heading.grid(row=0, column=0)
        url.grid(row=1, column=0)

        url_field = Entry(root, font = "Helvetica 16 bold")
        terminal_field = Text(root, height=2, width=30)

        S = Scrollbar(root)
        S.config(command=terminal_field.yview)
        terminal_field.config(yscrollcommand=S.set)

        url_field.grid(row=1, column=0, ipadx="100")
        terminal_field.grid(row=3, column=0, ipadx="100", ipady="50")

        submit = Button(root, font = "Helvetica 16 bold", text="Scrape!", fg="black", bg="white", command=launch)
        submit.grid(row=2, column=0)

        root.mainloop() 

    print("Done Crawling!\n")
    set_text("Done Crawling!\n")