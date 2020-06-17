import requests, json
import pandas as pd
from api import ocr_key


def ocr_space_file(
    filename, overlay=False, api_key=ocr_key, language="eng", istable=True, scale=True
):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7

    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    :param istable: parses output as a table
    """

    payload = {
        "isOverlayRequired": overlay,
        "apikey": api_key,
        "language": language,
        "istable": istable,
    }
    with open(filename, "rb") as f:
        r = requests.post(
            "https://api.ocr.space/parse/image", files={filename: f}, data=payload,
        )
    return r.content.decode()


def ocr_space_url(
    url, overlay=False, api_key=ocr_key, language="eng", isTable=True, scale=True
):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7

    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    :param isTable: parses output as a table
    """

    payload = {
        "url": url,
        "isOverlayRequired": overlay,
        "apikey": api_key,
        "language": language,
        "isTable": isTable,
    }
    r = requests.post("https://api.ocr.space/parse/image", data=payload,)
    # return r.content.decode()
    
    # Change this return in source code to return JSON object, not string
    return r.json()

#API response and obtaing "LineText"
    return r.json()

def parse():
    words = []
    data = ocr_space_url("https://ocr.space/Content/Images/receipt-ocr-original.jpg")
    for i in data.get("ParsedResults")[0]["TextOverlay"]["Lines"]:
        words.append(i.get("LineText"))

#Query the excel sheet and obtain the target food groups. Note not all used
def FoodDatabase():
    df = pd.read_excel("food.xlsx", usecols="B:C")
    dairy = df.query("FdGrp_Cd == 100")["Long_Desc"].tolist()
    grain = df.query("FdGrp_Cd == 1800 or FdGrp_Cd == 2000")["Long_Desc"].tolist()
    meat = df.query(
        "FdGrp_Cd == 500 or FdGrp_Cd == 700 or FdGrp_Cd == 1000 or FdGrp_Cd == 1300 or FdGrp_Cd == 1500 or FdGrp_Cd == 1700"
    )["Long_Desc"].tolist()
    fruit_veg = df.query("FdGrp_Cd == 900 or FdGrp_Cd == 1100 or FdGrp_Cd == 1600 ")[
        "Long_Desc"
    ].tolist()
    return dairy, grain, meat, fruit_veg


# print(food_data)        
# print(data.get('ParsedResults')[0]['TextOverlay']['Lines'][22].get('LineText'))
# print(i.get('LineText'))
# print((new_data["ParsedResults"][0].values()))
# filtered_data = (new_data["ParsedResults"][0].get('LineText'))
# data['Words'] = [json.loads(s) for s in data['Words']]

# with open('rawdata.json') as json_file:
#     raw_data = json.load(json_file)
# with open('rawdata.json', 'w') as f:
#     f.write(json.dump(data,f))

if __name__ == "__main__":
    parse()
    FoodDatabase()
