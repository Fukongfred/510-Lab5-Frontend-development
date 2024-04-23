# GIX 510-Lab5
# Frontend-development

A webapp to store and quickly access your favorite ChatGPT prompts✨.

## Get started
```
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Activate virtual environment
source venv/bin/activate

# pip install requests beautifulsoup4 pandas
```

## Lessons Learned
- Learning the basics of HTTP requests and how to use the requests library to fetch web data.
- Utilizing BeautifulSoup to parse HTML content and extract relevant information.
- Introduction to Pandas for organizing data in a more structured form which is pivotal for analysis.
- Applying these techniques to real-world data extraction tasks, such as scraping websites or accessing API data.

## Questions
- In the actual development of UI interfaces and interactions, is it necessary to use a platform such as streamlit? For example, if I want to design some UI components and user interactions that are not available in streamlit, how do I need to do it?

## TODO
### Part A
1. Create a scraper that scrapes [http://books.toscrape.com](http://books.toscrape.com/)
2. Store the data in database
3. Create a Streamlit app to query and filter the data
    1. Search by name, description
    2. Filter and Order by rating/price

### Part B (optional)
1. Run the scraper periodically using GitHub Actions
2. Create a weather app that allows the users to look up the weather by location name
    1. Use [openstreetmap API](http://nominatim.openstreetmap.org) to geocode text addresses into longitude, latitude
    2. Use [weather.gov API](https://www.weather.gov/documentation/services-web-api) to look up the weather from longitude, latitude