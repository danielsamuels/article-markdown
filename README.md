# article-markdown
Parse a webpage and convert it to Markdown, prefixing it with Jekyll front matter.  This script uses a very naïve method to determine the content, but it's surprisingly effective (it just looks for the element with the most p tags).

## Installation
```pip install -r requirements.txt```

## Usage
```python main.py <url>```
