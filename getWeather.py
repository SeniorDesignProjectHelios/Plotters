import requests
from lxml import html
from datetime import datetime


def getWeather():
    today = datetime.now().strftime('%Y-%m-%d')
    url = f"https://www.wunderground.com/dashboard/pws/KTNKNOXV761/table/{today}/{today}/daily"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using lxml
        doc = html.fromstring(response.content)

        # Extract the table rows using the provided XPath
        history_table = doc.xpath(
            '//*[@id="main-page-content"]/div/div/div/lib-history/div[2]/lib-history-table/div/div/div/table/tbody')

        if history_table:
            # Get the last row of data
            last_row = history_table[0].xpath('./tr[last()]')

            if last_row:
                # Extract the Time value
                time_str = last_row[0][0].text_content().strip()

                # Combine the current date with the extracted time
                today_date = datetime.now().date()
                time_obj = datetime.strptime(time_str, '%I:%M %p').time()
                date_time = datetime.combine(today_date, time_obj)

                # Extract the Temperature value
                temperature_str = last_row[0][
                    1].text_content().strip()  # Assuming the Temperature column is the second column in the row
                temperature_value = float(temperature_str.split()[0])

                # Extract the Solar value
                solar_value_str = last_row[0][
                    -1].text_content().strip()  # Assuming the Solar column is the last column in the row
                solar_value = float(solar_value_str.split()[0])

                return date_time, temperature_value, solar_value
            else:
                print("No rows found in the history table.")
                return None
        else:
            print("History table not found.")
            return None
    else:
        print(f"Request failed with status code {response.status_code}.")
        return None


# Example usage
weather_data = getWeather()
if weather_data:
    date_time, temperature, solar_irradiance = weather_data
    print(f"The most recent DateTime is: {date_time}")
    print(f"The most recent temperature value is: {temperature}")
    print(f"The most recent Solar irradiance value is: {solar_irradiance}")

# import requests
# from lxml import html
# from datetime import datetime
#
# def getWeather():
#     today = datetime.now().strftime('%Y-%m-%d')
#     url = f"https://www.wunderground.com/dashboard/pws/KTNKNOXV761/table/{today}/{today}/daily"
#     response = requests.get(url)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content using lxml
#         doc = html.fromstring(response.content)
#
#         # Extract the table rows using the provided XPath
#         history_table = doc.xpath('//*[@id="main-page-content"]/div/div/div/lib-history/div[2]/lib-history-table/div/div/div/table/tbody')
#
#         if history_table:
#             # Get the last row of data
#             last_row = history_table[0].xpath('./tr[last()]')
#
#             if last_row:
#                 # Extract the Time value
#                 time_str = last_row[0][0].text_content().strip()
#
#                 # Combine the current date with the extracted time
#                 today_date = datetime.now().date()
#                 time_obj = datetime.strptime(time_str, '%I:%M %p').time()
#                 date_time = datetime.combine(today_date, time_obj)
#
#                 # Extract the Temperature value
#                 temperature_str = last_row[0][1].text_content().strip()  # Assuming the Temperature column is the second column in the row
#                 temperature_value = float(temperature_str.split()[0])
#
#                 # Extract the Solar value
#                 solar_value_str = last_row[0][-1].text_content().strip()  # Assuming the Solar column is the last column in the row
#                 solar_value = float(solar_value_str.split()[0])
#
#                 return date_time, temperature_value, solar_value
#             else:
#                 print("No rows found in the history table.")
#                 return None
#         else:
#             print("History table not found.")
#             return None
#     else:
#         print(f"Request failed with status code {response.status_code}.")
#         return None
#
# # Example usage
# weather_data = getWeather()
# if weather_data:
#     date_time, temperature, solar_irradiance = weather_data
#     print(f"The most recent DateTime is: {date_time}")
#     print(f"The most recent temperature value is: {temperature}")
#     print(f"The most recent Solar irradiance value is: {solar_irradiance}")
