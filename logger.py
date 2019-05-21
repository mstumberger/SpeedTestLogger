import speedtest
from bitmath import *
import json
from time import sleep

FILENAME = 'log.json'
DATA = {}

while 1:
    try:
        with open(FILENAME) as json_file:
            DATA = json.load(json_file)
    except Exception:
        pass

    s = speedtest.Speedtest()
    s.get_servers([])
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    results_dict = s.results.dict()
    print(results_dict)
    download = results_dict['download']
    upload = results_dict['upload']
    download_Mbs = Mb(bits=download)
    upload_Mbs = Mb(bits=upload)
    print(download_Mbs)
    print(upload_Mbs)

    results_dict['download_Mbs'] = str(download_Mbs)
    results_dict['upload_Mbs'] = str(upload_Mbs)

    DATA[results_dict['timestamp']] = results_dict

    with open(FILENAME, 'w') as outfile:
        json.dump(DATA, outfile, indent=4, sort_keys=True)
    print("saved to file")
    sleep(5)

