import re
import requests
import random
import argparse
import string as st
  
def Find(string):
    """
    Find all urls in a single string and return as a python list
    """
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

def filtering_function(URLS):
    """
    Accepts a list of URLS and filter them basis condition
    """
    filtered_urls = []
    for URL in URLS:
        if "neeraj" not in URL:
            filtered_urls.append(URL)
    return filtered_urls

def generate_random_string(N=10):
    s = ''.join(random.choices(st.ascii_uppercase + st.digits, k=N))
    return s

def download_img(image_url):
    """
    Downloads image from a valid image url and returns the saved image name
    """
    img_data = requests.get(image_url).content
    img_name = generate_random_string()
    full_img_name = "./files/posts/{}/{}".format(CLEANED_FILENAME, img_name)
    with open(full_img_name, 'wb') as handler:
        handler.write(img_data)
    return full_img_name

def url_processing(string):
    """
    1. Finds all URLs
    2. Filter URLs basis specific condition
    3. downloads the images in the URL to a local location
    4. Replace the web url with the local url
    """
    found_urls = Find(string)
    filtered_urls = filtering_function(found_urls)
    name_mapping = {}
    for URL in filtered_urls:
        LOCAL_NAME = download_img(URL)
        name_mapping[URL] = LOCAL_NAME
    return name_mapping

def replace_remote_assetts_with_local():
    with open("./{}/{}".format(DIRECTORY, FILENAME), "r") as f:
        s = f.read()
    mapping = url_processing(s)
    # replace remote asset with local
    for old_asset, new_asset in mapping.items():
        s = s.replace(old_asset, new_asset)
    with open("./{}/new_{}".format(DIRECTORY, FILENAME), "w") as f:
        f.write(s)

def clean_filename(f):
    """
    expects filename to be in format YYYY-MM-DD-filename.extension
    """
    f = f[11:] # removes date from name
    fl = f.split(".")[0].split("-")
    fl = [x[0].upper()+x[1:] for x in fl]
    f = "-".join(fl)
    return f

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d")
    parser.add_argument("-f")
    args = parser.parse_args()
    DIRECTORY = args.d
    FILENAME = args.f
    CLEANED_FILENAME = clean_filename(args.f)
    replace_remote_assetts_with_local()