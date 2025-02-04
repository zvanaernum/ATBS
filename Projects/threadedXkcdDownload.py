#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading

os.makedirs('xkcd_threaded', exist_ok=True)    # store comics in ./xkcd_threaded

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        try:
            # Download the page.
            print('Downloading page https://xkcd.com/%s...' % (urlNumber))
            res = requests.get('https://xkcd.com/%s' % (urlNumber))
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'html.parser')

            # Find the URL of the comic image.
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Could not find comic image.')
            else:
                comicUrl = 'https:' + comicElem[0].get('src')
                # Download the image.
                print('Downloading image %s...' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()

                # Save the image to ./xkcd_threaded.
                imageFile = open(os.path.join('xkcd_threaded', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
        except Exception as e:
            print('There was a problem: %s' % (e))

# Total number of comics to download
totalComics = 3050

# Number of threads to use
numThreads = 10

# Comics per thread
comicsPerThread = totalComics // numThreads

# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects

for i in range(numThreads):
    start = i * comicsPerThread + 1
    end = (i + 1) * comicsPerThread + 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
