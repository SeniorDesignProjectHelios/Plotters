import requests
from lxml import html

def getTemp():
    url = "https://www.wunderground.com/dashboard/pws/KTNKNOXV761/table/2023-03-27/2023-03-27/daily"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using lxml
        doc = html.fromstring(response.content)

        # Extract the table rows using the provided XPath
        history_table = doc.xpath('//*[@id="main-page-content"]/div/div/div/lib-history/div[2]/lib-history-table/div/div/div/table/tbody')

        if history_table:
            # Get the last row of data
            last_row = history_table[0].xpath('./tr[last()]')

            if last_row:
                # Extract the Temperature value
                temperature_str = last_row[0][1].text_content().strip()  # Assuming the Temperature column is the second column in the row

                # Extract the numeric value from the Temperature string
                temperature_value = float(temperature_str.split()[0])

                return temperature_value
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
temperature = getTemp()
if temperature:
    print(f"The most recent temperature value is: {temperature}")
