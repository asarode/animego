import webbrowser
import csv

animeList = {}

print 'Your anime:'
notes = open("animelist.csv")
for row in csv.reader(notes):
    code = row[0]
    title = row[1]
    episode = row[3]
    URL = row[2].replace('USER_ENTRY', episode)

    animeList[code] = URL
    print '{0} | {1} --> {2}'.format(code, title, episode)
notes.close()

while True:
    anime_input = raw_input('Enter the code of the anime you wish to launch: ')
    if animeList.has_key(anime_input):

        break
    elif anime_input.lower() == 'list':
        notes = open("animelist.csv")
        for row in csv.reader(notes):
            code = row[0]
            title = row[1]
            episode = row[3]
            URL = row[2].replace('USER_ENTRY', episode)
        notes.close()

        animeList[code] = URL
        print '{0} | {1} --> {2}'.format(code, title, episode)
    elif anime_input.lower() == 'q':
        quit()


    print animeList



webbrowser.open('{}'.format(animeList[anime_input]))

