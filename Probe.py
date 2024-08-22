import sys
import requests

# usage
def urls(file):
    urls2 = sys.stdin.read().splitlines()

    good_urls = []
    bad_urls = []

    for url in urls2:
        try:
            response = requests.head(url)

            if response.status_code == 200:
                good_urls.append(url)
            
        except requests.exceptions.MissingSchema:
            bad_urls.append(url)
            continue
        except requests.exceptions.ConnectionError:
            bad_urls.append(url)
            continue

    with open(file, 'w') as file:
        file.write('\n'.join(good_urls))
    
    print(f"Saved URLS {file}")
        

file = 'filtered_urls.txt'

urls(file)