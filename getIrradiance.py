import requests
from lxml import html

def getIrradiance():
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
                # Extract the Solar value
                solar_value_str = last_row[0][-1].text_content().strip()  # Assuming the Solar column is the last column in the row

                # Extract the numeric value from the Solar value string
                solar_value = float(solar_value_str.split()[0])

                return solar_value
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
solar_irradiance = getIrradiance()
if solar_irradiance:
    print(f"The most recent Solar irradiance value is: {solar_irradiance}")
