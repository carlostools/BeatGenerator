import os 

import json 

try:
  os.mkdir("Output")

except:
  def beatgenerator():
    
    _clips_ = []
    
    _beats_ = {}
    
    mileseconds = int(input("Song Mileseconds: "))
    
    bpm =  60000
    
    for x in range(0,mileseconds,434):
      
      _clips_.append(x)
      
      _beats_["beats"] = _clips_
      
    with open("Output//" + "beats.json","w") as g:
      g.write(json.dumps(_beats_))
      g.close()
  
  beatgenerator()