import requests
import re
import os
from bs4 import BeautifulSoup
import json

gita_data={}
def parse_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    return soup

def form_json(chapter,sutra,shlok):

    
#   {
#     "chapter_1": {
#       "verse_1":{
#         "lyrics":"",
#         "music_filepath":""
#       }
#     }
#   }
    gita = {}
    chapter_name= "chapter_" + str(chapter)
    verse_name="verse_"+ str(sutra)
    
    verse = {
        verse_name: {
            "lyrics" : shlok,
            "music_filepath": ""
        }
    }

    gita_data[chapter_name].update(verse)


    # try:
    #     gita[chapter_name].append([verse_name]:verse.
    # except KeyError:
    #     gita[chapter_name] = {verse}
    # gita['sutra']=sutra
    # gita['text']=shlok
    # print(gita.items())


if __name__ == "__main__":
    link = "https://www.gitasupersite.iitk.ac.in/srimad?language=dv&field_chapter_value={}&field_nsutra_value={}"

    chap = 1
    chapter = "chapter_"
    for i in range(1,19):
        a = chapter + str(i)
        gita_data.update({a:{}})
    # print(gita_data)


    while chap <= 2:
        bsoup_ini = parse_html(link.format(chap,1))
        sutra = bsoup_ini.find_all('div', attrs={'class': 'form-item form-type-select form-item-field-nsutra-value'})
        for su in sutra:
            for suo in su.find_all('option'):
                bsoup = parse_html(link.format(chap,suo.text))
                container = bsoup.find_all('div', attrs={'class': 'custom_display_even'})
                        
                shloka = ""
                shloka = ' '.join(chap.text.strip() for chap in container)

                shloka = os.linesep.join([s for s in shloka.splitlines() if s])
                form_json(chap,int(suo.text),shloka.strip('मूल श्लोकः'))
        chap += 1
    with open("test.txt", "a") as myfile:
        myfile.write(json.dumps(gita_data))


# print(r.text)

# soup = BeautifulSoup(r.text,'lxml')
# print(soup.prettify().encode('utf-8'))
# print(soup.text)
# chapter = soup.find_all('div', attrs={'class': 'form-item form-type-select form-item-field-chapter-value'})
# for x in chapter:
#     for v in x.find_all('option'):
#         print(v.text)

# container = soup.find_all('div', attrs={'class': 'custom_display_even'})
# text = ' '.join(i.text.strip() for i in container)

# text = os.linesep.join([s for s in text.splitlines() if s])
# print(text)
# gita = {}
# gita['chapter'] = 1
# gita['sloka']=1
# gita['text']=text

# with open("test.txt", "a") as myfile:
#     myfile.write(json.dumps(gita))