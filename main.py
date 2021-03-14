import sys
import requests
import argparse

from bs4 import BeautifulSoup
from colorama import Fore, init

def main():
    print(Fore.RED + "Coded by Ehsonjon Gadeov" + Fore.RESET)
    init()
    parser = argparse.ArgumentParser(description='MP3.TJ music downloader')
    parser.add_argument("url", type=str, help="Url of music on MP3.TJ")
    parser.add_argument("--filename", type=str, default='None', help='Filename (for save music)')
    parser.add_argument("--dir", type=str, default="", help='Directory to save file...')
    names = parser.parse_args()

    if not names.url.startswith("http://mp3.tj/song"):
        print(Fore.LIGHTRED_EX + "Invalid url" + Fore.RESET)
        return

    try:
        r = requests.get(names.url)

    except:
        print(Fore.LIGHTRED_EX + "Invalid url or bad connection..." + Fore.RESET)
        return

    if r.status_code != 200:
       print(Fore.LIGHTRED_EX + "Status code is not 200, bad connection or invalid url, you can try again!" + Fore.RESET)
       return

    soup = BeautifulSoup(r.content, 'html.parser')

    if names.filename == 'None':
        music_title = soup.select("strong")[0].text
        filename = music_title
    else:
        filename = names.filename

    filename += '.mp3'

    link = "http://music.mp3.tj/page.php?p=/download/%s/music/%s.html" % (names.url.split('/')[-1], names.url.split('/')[-1])

    print(Fore.LIGHTGREEN_EX + "You music found as " + music_title + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "Music size is " + soup.select(".fa-file-text-o")[0].next + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "Loading... " + filename + Fore.RESET)
    music = requests.get(link)

    if music.status_code != 200:
        print(Fore.LIGHTRED_EX + "Status code is not 200, sorry..." + Fore.RESET)
        return

    if names.dir:
        filename = names.dir + '/' + filename

    f = open(filename, 'wb')
    print(Fore.LIGHTGREEN_EX + "Saving to file..." + Fore.RESET)
    f.write(music.content)
    f.close()
    print(Fore.LIGHTYELLOW_EX + "Closing file" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "Music succefully downloaded to -> \"" + filename + '"' + Fore.RESET)

if __name__ == '__main__':
    main()
