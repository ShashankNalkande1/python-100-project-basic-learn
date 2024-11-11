import requests
from bs4 import BeautifulSoup
import openpyxl

# Initialize a new Excel workbook
excel = openpyxl.Workbook()

# Set up the active sheet and its title
sheet = excel.active
sheet.title = 'Top Rated Movies'

# Add headers to the sheet
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDb Rating'])

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Send a GET request to fetch the IMDb Top 250 page, including headers
    response = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the raw HTML to check if the content is loaded correctly
    # Uncomment this line if you need to check the full HTML content
    # print(soup.prettify())  

    # Try to find the table containing the movie list
    movie_table = soup.find('tbody', class_='lister-list')
    
    if not movie_table:
        print("Could not find the movie table. Please check the IMDb page structure.")
        
        # Print the available classes in the HTML structure for debugging
        for element in soup.find_all(class_=True):
            print(element.get('class'))

    if movie_table:  # Check if the table was found
        # Find all movie rows in the table
        movies = movie_table.find_all('tr')

        # Loop through each movie and extract details
        for movie in movies:
            try:
                # Movie rank
                title_column = movie.find('td', class_='titleColumn')
                if title_column:
                    rank = title_column.get_text(strip=True).split('.')[0]

                    # Movie name
                    name = title_column.find('a').text

                    # Year of release
                    year = movie.find('span', class_='secondaryInfo')
                    if year:
                        year = year.text.strip('()')

                    # IMDb rating
                    rating = movie.find('td', class_='imdbRating')
                    if rating:
                        rating = rating.find('strong').text

                    # Append movie data to the sheet
                    sheet.append([rank, name, year, rating])

            except Exception as e:
                # Skip any row that does not have complete data
                print(f"An error occurred while processing a movie row: {e}")
                continue
    else:
        print("Could not find the movie table. Please check the IMDb page structure.")

except Exception as e:
    print(f"An error occurred: {e}")

# Save the workbook to an Excel file
excel.save('Top_Rated_Movies.xlsx')
print("Data saved to Top_Rated_Movies.xlsx")
