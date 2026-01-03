import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
URL = "https://weworkremotely.com/categories/remote-python-jobs"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_jobs():
    """Fetches and parses job listings from We Work Remotely."""
    try:
        logging.info(f"Connecting to {URL}...")
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        jobs_container = soup.find("section", class_="jobs")
        
        job_list = []
        
        # Iterating through job items
        for item in jobs_container.find_all("li", class_="feature"):
            try:
                # Extracting data
                company = item.find("span", class_="company").text.strip()
                title = item.find("span", class_="title").text.strip()
                region = item.find("span", class_="region")
                region = region.text.strip() if region else "Remote (Global)"
                
                # Link is relative, so we append the base domain
                link_tag = item.find_all("a")[1] # The second <a> usually contains the job link
                link = "https://weworkremotely.com" + link_tag["href"]
                
                job_list.append({
                    "Title": title,
                    "Company": company,
                    "Region": region,
                    "Link": link,
                    "Date Scraped": datetime.now().strftime("%Y-%m-%d")
                })
            except (AttributeError, IndexError):
                continue # Skip malformed items

        logging.info(f"Successfully scraped {len(job_list)} jobs.")
        return job_list

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return []

def save_to_excel(data):
    """Saves the data to an Excel file with auto-adjusted column widths."""
    if not data:
        logging.warning("No data to save.")
        return

    df = pd.DataFrame(data)
    filename = f"python_jobs_{datetime.now().strftime('%Y-%m-%d')}.xlsx"

    # Using ExcelWriter to access the workbook and sheet for formatting
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Jobs")
        
        # Access the workbook and sheet
        worksheet = writer.sheets["Jobs"]

        # Auto-adjust column width
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter  # Get the column name
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column_letter].width = adjusted_width

    logging.info(f"Data saved to {filename} successfully.")

if __name__ == "__main__":
    jobs = get_jobs()
    save_to_excel(jobs)
