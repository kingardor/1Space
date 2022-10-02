import os
import json
from urllib.parse import quote

parsed_dataset = []

keywords = [
    ["antartica","snow"],
    ["mars","planet"],
    ["uranus","planer"],
    ["himalayas","mountains"],
    ["amazon","forest"],
    ["Nile River","river"]
]
for keyword in keywords:
    data_combined = []
    os.system('mkdir {}'.format(keyword[0]))
    keyword_encrypted = quote(keyword[0])
    op = os.popen(
        'curl "https://images-api.nasa.gov/search?q={}&description={}&media_type=image"'.format(
            keyword_encrypted,
            keyword[1]
        )
    ).read()
    outputs = json.loads(op)
    for item in outputs["collection"]["items"]:
        parsed_list = []
        for data in item["data"]:
            try:
                parsed_list.append(data["keywords"])
            except:
                continue
            parsed_list.append(data["description"])
        for link in item["links"]:
            parsed_list.append(link["href"])
            os.system("wget -P {} {}".format(keyword[0],link["href"]))

        parsed_dataset.append({keyword[0]:parsed_list})
with open('dataset.json', 'w') as fp:
    json.dump(parsed_dataset, fp)

fp.close()
