# 📊 Automated Job Market Scraper & Reporter

A Python automation script that scrapes real-time job data from "We Work Remotely", processes it using **Pandas**, and exports a professionally formatted **Excel report**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458)
![Excel](https://img.shields.io/badge/Export-Excel%20(OpenPyXL)-green)

## 📌 Overview

This tool automates the tedious task of searching for remote Python jobs. Instead of manually browsing, this script:
1.  **Extracts** data (Title, Company, Region, URL) from the web.
2.  **Cleans** and structures the data into a DataFrame.
3.  **Generates** an `.xlsx` file with **auto-adjusted column widths** for immediate readability.

## 🛠 Tech Stack

* **Requests & BeautifulSoup4:** For robust HTML parsing and data extraction.
* **Pandas:** For data manipulation and DataFrame creation.
* **OpenPyXL:** For advanced Excel formatting (styling and dimensions).

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/job-market-scraper.git](https://github.com/your-username/job-market-scraper.git)
cd job-market-scraper
