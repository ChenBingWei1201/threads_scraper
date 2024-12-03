# threads_scraper

A Python package for scraping Threads posts.

## Installation

Install the package using pip:

```bash
pip install threads-scraper
```

## Usage

```python
from threads_scraper.scraper import ThreadsScraper

# Initialize the scraper
scraper = ThreadsScraper(
    username="your_username",
    password="your_password",
    driver_path="/path/to/chromedriver",
)

scroll_times = 10
csv_index = True

# Start the scraper
scraper.get_driver()

if scraper.login_to_threads():
    data = scraper.scrape(["keyword1", "keyword2"], scroll_times) # default scroll_times = 5
    scraper.save_to_csv(data, "data/threads_posts.csv", csv_index) # default csv_index = False

scraper.close()
```