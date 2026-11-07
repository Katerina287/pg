import re
import sys
import requests


def download_url_and_get_all_hrefs(url):
    hrefs = []

    # Stažení stránky pomocí requests.get
    response = requests.get(url)

    # Kontrola, zda je návratový kód 200 (OK)
    if response.status_code == 200:
        # Použijeme response.text pro textový obsah stránky
        html_content = response.text

        # Regulární výraz pro bezpečné nalezení všech href atributů v tagu <a>
        pattern = r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']*)["\']'
        hrefs = re.findall(pattern, html_content)

    return hrefs


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            url = sys.argv[1]
            links = download_url_and_get_all_hrefs(url)
            # Vypsání nalezených odkazů pro kontrolu
            for link in links:
                print(link)
        else:
            print("Zadejte prosím URL jako argument příkazové řádky.")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
