#!/usr/bin/env python3

import requests
import elokeszit #lehet nem mukodik kornyezettol fuggoen mert path meg ilyesmi?
import os
import json

def main(question: str):
    #meghivodik
    #input fileok nevevel meghivja az (elokeszit.py)-t
        #files names in cur dir. to list
    script_dir = os.path.dirname(os.path.abspath(__file__))

    uploads_dir = os.path.join(script_dir, "uploads")
    file_list = ["uploads/"+f for f in os.listdir(uploads_dir) if os.path.isfile(os.path.join(uploads_dir, f)) and not f.endswith(".py") and f != "clearedText.txt"]
    print(file_list)
    elokeszit.func(file_list)
        #wait till finished #elvileg csinálja is

    with open("clearedText.txt",'r', encoding="UTF-8") as clearedTextFile:
        colabUrl="https://b033-35-230-91-197.ngrok-free.app/summarize"
        data={"questions[]":[question]}

        res = requests.post(colabUrl,files={"file": clearedTextFile},data=data)
        d = json.loads(res.text)
        summary= d["summary"]
        
        with open("./front/public/sum/completed.txt",'w') as of:
            print(summary, file=of)
            
    #nezi, hogy kesz/a directoryban van már e a file, nem biztos hogy kell mert gyakorlatilag busy waiting, attol fugg hogy szinkron e a colab api hivas
    while True:
      file_list = [f for f in os.listdir(uploads_dir) if os.path.isfile(os.path.join(uploads_dir, f)) and not f.endswith(".py") and f != "clearedText.txt"]
      for i in file_list:
            if file_list[i] == "completed.txt":
                  break

   


if __name__ == "__main__":
    main()