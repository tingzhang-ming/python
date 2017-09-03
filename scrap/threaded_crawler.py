import time
import re
import threading
import urlparse
import robotparser
from downloader import Downloader
from mongo_cache import MongoCache
from ScrapeCallback import ScrapeCallback
SLEEP_TIME = 1

def threaded_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, cache=None, scrape_callback=None, user_agent='wswp', proxies=None,
                     num_retries=1, max_threads=10, timeout=60):
    """Crawl this website in multiple threads
    """
    # the queue of URL's that still need to be crawled
    #crawl_queue = Queue.deque([seed_url])
    crawl_queue = [seed_url]
    # the URL's that have been seen
    seen = {seed_url: 0}
    rp = get_robots(seed_url)
    D = Downloader(cache=cache, delay=delay, user_agent=user_agent, proxies=proxies, num_retries=num_retries, timeout=timeout)

    def process_queue():
        while crawl_queue:
            url = crawl_queue.pop()
            depth = seen[url]
            # check url passes robots.txt restrictions
            if rp.can_fetch(user_agent, url):
                html = D(url)
                links = []
                if scrape_callback:
                    links.extend(scrape_callback(url, html) or [])

                if depth != max_depth:
                    # can still crawl further
                    if link_regex:
                        # filter for links matching our regular expression
                        links.extend(reversed([link for link in get_links(html) if re.match(link_regex, link)]))

                    for link in links:
                        link = normalize(seed_url, link)
                        # check whether already crawled this link
                        if link not in seen:
                            seen[link] = depth + 1
                            # check link is within same domain
                            if same_domain(seed_url, link):
                                # success! add this new link to queue
                                crawl_queue.append(link)
            else:
                print 'Blocked by robots.txt:', url


    # wait for all download threads to finish
    threads = []
    while threads or crawl_queue:
        # the crawl is still active
        for thread in threads:
            if not thread.is_alive():
                # remove the stopped threads
                threads.remove(thread)
        while len(threads) < max_threads and crawl_queue:
            # can start some more threads
            thread = threading.Thread(target=process_queue)
            thread.setDaemon(True) # set daemon so main thread can exit when receives ctrl-c
            thread.start()
            threads.append(thread)
        # all threads have been processed
        # sleep temporarily so CPU can focus execution on other threads
        time.sleep(SLEEP_TIME)


def normalize(seed_url, link):
    """Normalize this URL by removing hash and adding domain
    """
    link, _ = urlparse.urldefrag(link) # remove hash to avoid duplicates
    return urlparse.urljoin(seed_url, link)

def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp

def same_domain(url1, url2):
    """Return True if both URL's belong to same domain
    """
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc

def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

if __name__ == '__main__':
    cache = MongoCache()
    cache.clear()
    #link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler')
    threaded_crawler('http://example.webscraping.com', '/places/default/(index|view)', delay=5, num_retries=1, max_depth=1,
                 user_agent='sdfdfdf', cache=cache, scrape_callback=ScrapeCallback())