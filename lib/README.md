# sound-player

'''
pyinstaller --clean -w -y --add-data="lib\startSV.wav;lib" --add-data="lib\startENG.wav;lib" --add-data="lib\blueFlagSV.wav;lib" --add-data="lib\blueFlagENG.wav;lib" --add-data="lib\backaENG.wav;lib" --add-data="lib\backaSV.wav;lib" --add-data="lib\krockaENG.wav;lib" --add-data="lib\krockaSV.wav;lib" --add-data="lib\testSV.wav;lib" --icon="iconR.ico" __main__.py
'''

Ljuden måsta ha följande namn och vara av .wav-format:
"startSV.wav", "startENG.wav": Starta bilen
"blueFlagSV.wav", "blueFlagENG.wav": Hantera blåflagg
"backaSV.wav", "backaENG.wav": Hur man backar
"krockaSV.wav", "krockaENG.wav": Krocka inte
"dropinSV.wav", "dropinENG.wav": Hur ett drop in går till, bästa varvtiderna osv
"practiceSV.wav", "practiceENG.wav": Hur ett uppvärmningsheat går till
"kvalSV.wav", "kvalENG.wav": Hur ett kvalheat fungerar
"finalSV.wav", "finalENG.wav": Hur en final fungerar (obs, olika i GBG vs KNG)
"preppSV.wav", "preppENG.wav": Kolla bälten och hjälmar, snart dags att köra ut osv
"testSV.wav", "testENG.wav": används inte (typ)
"sittSV.wav", "sittENG.wav": Sätt er i bilarna enligt numrerna på skärmen

Ifall en av filerna inte är inlagda korrekt (rätt filformat, namn och plats) kommer ni få smaka på badsalt ;)