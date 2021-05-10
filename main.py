import string
import random
 
import requests
 
BASE_URL = 'https://i.imgur.com/'
 
def get_url():
    counter = 0
    url_hash = ''
    while counter < 5:
        random_letter = random.choice(string.ascii_letters)
        url_hash += random_letter
        counter += 1
    return BASE_URL + url_hash + '.jpg'
 
 
print('START')
 
while True:
    img_url = get_url()
    r = requests.get(img_url + '.jpg')
 
    while r.url == 'https://i.imgur.com/removed.png':
        img_url = get_url()
        r = requests.get(img_url)
 
    filename = img_url.split("/")[-1]
 
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        data={
            'image': img_url + '.jpg',
        },
        headers={'api-key': '14103e5d-0884-41fd-8883-6f0037c5c2b3'}
    )
    json_response = r.json()
    if len(json_response['output']['detections']):
        print(img_url)
        print(json_response)
        detections = []
        for i in range(0, len(json_response['output']['detections'])):
          detections.append(json_response['output']['detections'][i]['name'])
          nsfw = json_response['output']['nsfw_score']
          print("It was found a NSFW of: " + detections[i] + "  with a HOTNESS of: " + str(nsfw))


