import requests
from bs4 import BeautifulSoup
import locale
from datetime import datetime, timedelta


def extract():
    """
    Date: August 25, 2023, 18:42:23 WIB
    Magnitude: 4.0
    Depth: 3 km
    Geolocation: 4.52 N - 96.45 E
    Center: The earthquake center is located on land 35 km northeast of Nagan Raya Regency
    Felt: Felt (MMI Scale): II Nagan Raya
    """
    try:
        content = requests.get("https://www.bmkg.go.id/en.html") # <Response [200]> means good!
        # Check this for more information about HTTP response status codes:
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    except Exception:
        return None
    if content.status_code == 200:
        # print(content.status_code)
        # print(content.text)
        soup = BeautifulSoup(content.text, "html.parser")
        title = soup.find("title")
        print(title.string)

        date = soup.find("span", {"class": "waktu"})
        date_string = date.text
        # Remove the timezone abbreviation from the date string
        date_string = date_string.replace("WIB", "")
        # Create a dictionary to map Indonesian month names to English month names
        month_map = {
            "Januari": "January",
            "Februari": "February",
            "Maret": "March",
            "April": "April",
            "Mei": "May",
            "Juni": "June",
            "Juli": "July",
            "Agustus": "August",
            "September": "September",
            "Oktober": "October",
            "November": "November",
            "Desember": "December"
        }

        # Split the date string into parts
        date_parts = date_string.split()

        # Translate the month name from Indonesian to English
        date_parts[1] = month_map[date_parts[1]]

        # Rejoin the date string
        date_string = ' '.join(date_parts)

        # Parse the date string
        date_format = "%d %B %Y, %H:%M:%S"
        date_object = datetime.strptime(date_string, date_format)
        timestamp = date_object.timestamp()
        # Convert the timestamp to a datetime object in UTC timezone
        date_object = datetime.utcfromtimestamp(timestamp)

        # Add the UTC offset to get the date and time in UTC+07:00 timezone
        date_object = date_object + timedelta(hours=7)

        # Format the datetime object as a string
        date_string = date_object.strftime('%Y-%m-%d %H:%M:%S')
        # print(soup.prettify())

        # Find the magnitude element
        magnitude = soup.find("span", {"class": "ic magnitude"})
        # Get the magnitude value
        magnitude = magnitude.next_sibling.strip()

        # Find the other elements
        depth_element = soup.find('span', {'class': 'ic kedalaman'})
        geolocation_element = soup.find('span', {'class': 'ic koordinat'})
        location_element = soup.find('span', {'class': 'ic lokasi'})
        felt_element = soup.find('span', {'class': 'ic dirasakan'})

        # Get the values
        depth = depth_element.next_sibling.strip()
        geolocation = geolocation_element.next_sibling.strip()
        central_location = location_element.next_sibling.strip()
        felt = felt_element.next_sibling.strip()

        # Split the geolocation value into latitude and longitude
        latitude, longitude = geolocation.split(' - ')
        # Replace the Indonesian abbreviations with their English equivalents
        latitude = latitude.replace('LU', 'N')
        latitude = latitude.replace('LS', 'S')
        longitude = longitude.replace('BT', 'E')
        # Create a dictionary to store the geolocation data
        geolocation = {'latitude': latitude, 'longitude': longitude}

        earthquake = dict()
        earthquake["date"] = date_string # "August 25, 2023"
        earthquake["magnitude"] = magnitude
        earthquake["depth"] = depth
        earthquake["geolocation"] = geolocation
        earthquake["central_location"] = central_location
        earthquake["felt"] = felt
        return earthquake
    else:
        return None


def show_data(data):
    if data is None:
        print("Cannot find data")
        return
    print("Recent Earthquake in Indonesia")
    print(f"Date and Time: {data['date']} (UTC+07:00)")
    print(f"Magnitude: {data['magnitude']}")
    print(f"Depth: {data['depth']}")
    print(f"Geolocation: Latitude= {data['geolocation']['latitude']}, Longitude= {data['geolocation']['longitude']}")
    print(f"Center: {data['central_location']}")
    print(data['felt'])
