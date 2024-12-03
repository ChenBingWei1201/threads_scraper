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
    user_agent="Your User Agent"
)

# Start the scraper
scraper.get_driver()

if scraper.login():
    data = scraper.scrape(["keyword1", "keyword2"])
    scraper.save_to_csv(data, "data/threads_posts.csv")

scraper.close()
```