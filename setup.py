from setuptools import setup, find_packages

setup(
    name="threads-scraper",
    version="1.1.0",
    description="A Python package for scraping Threads posts.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="ChenBingWei1201",
    author_email="rain4030633@gmail.com",
    url="https://github.com/ChenBingWei1201/threads_scraper",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
        "pandas>=1.0.0",
        "python-dotenv>=0.20.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
