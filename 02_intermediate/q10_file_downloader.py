# Q10: Multi-threaded File Downloader
# Task: Download multiple files in parallel using threads
# Concept: concurrent.futures.ThreadPoolExecutor
# Docs: https://docs.python.org/3/library/concurrent.futures.html

import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Sample files to download (public domain images)
FILES = [
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file1.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file2.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file3.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file4.jpg"),
    ("https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table-word.jpg", "file5.jpg"),
]

os.makedirs("downloads", exist_ok=True)

def download_file(url, filename):
    try:
        response = requests.get(url, timeout=10)
        filepath = os.path.join("downloads", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename} ({len(response.content)} bytes)")
        return filename
    except Exception as e:
        print(f"Failed: {filename} - {e}")
        return None

print("=== Single-threaded Download ===")
start = time.time()
for url, filename in FILES:
    download_file(url, f"single_{filename}")
print(f"Time taken: {time.time() - start:.2f}s")

print("
=== Multi-threaded Download ===")
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {
        executor.submit(download_file, url, f"multi_{filename}"): filename
        for url, filename in FILES
    }
    for future in as_completed(futures):
        future.result()
print(f"Time taken: {time.time() - start:.2f}s")

print("
All files saved in downloads/ folder")