# OpenData Extractor (Python/Playwright) 📊

## 🎯 Objective
This project is an automated Python script designed to extract public data (Open Data) from geographical directories (like Google Maps) using **Playwright**. It demonstrates the ability to interact with dynamic web pages (SPA), handle infinite scrolling, and parse complex DOM structures reliably.

## 🛠️ Technical Stack
- **Language:** Python 3.10+
- **Automation:** Playwright (Headless Chromium)
- **Export Format:** CSV

## 🛡️ Educational Purpose
This script was built as a proof of concept (PoC) to understand dynamic DOM manipulation, anti-bot mechanisms, and robust data extraction. It strictly extracts publicly available information.

## 🚀 Usage (Development only)
#### 1. Installation
```bash
git clone https://github.com/CyprienThuillier/opendata-extractor.git
cd opendata-extractor
./install.sh
```
#### 2. Usage
```bash
python src/main.py -q="restaurant" -l="London" -m=150 -w -o="output.csv" -a
```
```bash
usage: main.py [-h] --query QUERY --location LOCATION --max-results MAX_RESULTS [--website-search] [--output OUTPUT] [--append]

Scrape search results

options:
  -h, --help            show this help message and exit
  --query, -q QUERY     Search query
  --location, -l LOCATION
                        Location
  --max-results, -m MAX_RESULTS
                        Max results
  --website-search, -w  Enable website search
  --output, -o OUTPUT   Output file path
  --append, -a          Append to existing file
```