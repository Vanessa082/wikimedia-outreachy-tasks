import csv
import requests
import time

HEADER = {"user-agent": "Outreachy-Task-Bot"}
file_name = 'Task 2 - Intern.csv'
count = 0
success = 0
failure = 0

def fetch_status_url(url):
    try:
      res = requests.get(url, headers = HEADER, timeout = 3)
      return res.status_code
    except Exception as e:
      return "Error"
with open(file_name, mode="r", encoding="utf-8") as file:
  reader = csv.reader(file)
  next(reader)
  for row in reader:
    if not row: continue
    count += 1
    url = row[0].strip()
    result = fetch_status_url(url)
    print(f"({result}) {url}")
    if isinstance(result, int) and result < 400:
      success += 1
    else:
      failure += 1
    time.sleep(0.2)
