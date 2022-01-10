import requests
import text2emotion as te
import nltk
nltk.download('omw-1.4')
param = {
    "source": 'bbc-news',
    'sortBy': 'top',
    'apiKey': '5b0234176ce14bdab66943f2dd184f83'
}
url = " https://newsapi.org/v1/articles"
res = requests.get(url, params=param)
data = res.json()
article = data["articles"]
titles = []
for ar in article:
    titles.append(ar['title'])
print("****************************")
# print(titles[6])
# print(te.get_emotion(titles[6]))
emotions = te.get_emotion(titles[6])

count = {'Happy': 0, 'Angry': 0, 'Surprise': 0, 'Sad': 0, 'Fear': 0, 'N/A': 0}
for title in titles:
    emotions = te.get_emotion(title)
    max = 0
    max_em = 'N/A'
    for emotion in emotions:
        if emotions[emotion] > max:
            max_em = emotion
            max = emotions[emotion]
    count[max_em] += 1
print("ABOUT TODAYS NEWS!!!")
l = len(titles)
emotes = {'Happy': '😁', 'Angry': '😡', 'Surprise': '🤩',
          'Sad': '😔', 'Fear': '😱', 'N/A': '🤔'}
for c in count:
    print(c, emotes[c], ":", (count[c]/l)*100, "%")
print("****************************")
print("********HEADLINES***********")
for title in titles:
    print('==>', title)
