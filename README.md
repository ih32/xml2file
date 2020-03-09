# xml2file
python code to write ElementTree to file(pretty print)

Call the writeXMLtoFile() with root Element, output file & indentation text(as needed).

Sample :

def main():

    root = prepareTestData()
    tdata = open('TeslaCars.xml', 'w')
    writeXMLtoFile(root, outFile=tdata, indent='  ')
    
def prepareTestData():
    
    # create root element    
    root = ET.Element('Tesla')
    roadster =	{ "id": "TR",
                  "model": "Tesla Roadster",
                  "range": "620",
                  "rScale":"Miles",
                  "rCharge":"44",
                  "time":"minutes" }
    model_S_LR =	{ "id": "MSL",
                  "model": "Tesla Model S Long Range",
                  "range": "375",
                  "rScale":"Miles",
                  "rCharge":"38",
                  "time":"minutes" }
    model_3_LR =	{ "id": "M3L",
                  "model": "Tesla Model 3 Long range",
                  "range": "340",
                  "rScale":"Miles",
                  "rCharge":"22",
                  "time":"minutes" }

    addCar(root, roadster)
    addCar(root, model_S_LR)
    addCar(root, model_3_LR)
    
    return root

def addCar(parentElm, props):

    car = ET.SubElement(parentElm, 'car', {'id':props['id']})

    model = ET.SubElement(car, 'model')
    model.text = props['model']

    ofcRange = ET.SubElement(car, 'officialRange', {'scale': props['rScale']})
    ofcRange.text = props['range']

    fullCharge = ET.SubElement(car, 'fullCharge')
    rapidCharge = ET.SubElement(fullCharge, 'rapidCharge', {'timeScale':props['time']})
    rapidCharge.text = props['rCharge']
    

output:
------
you will have the file TeslaCars.xml with following content:

```xml
<Tesla>
  <car id="TR">
    <model>Tesla Roadster</model>
    <officialRange scale="Miles">620</officialRange>
    <fullCharge>
      <rapidCharge timeScale="minutes">44</rapidCharge>
    </fullCharge>
  </car>
  <car id="MSL">
    <model>Tesla Model S Long Range</model>
    <officialRange scale="Miles">375</officialRange>
    <fullCharge>
      <rapidCharge timeScale="minutes">38</rapidCharge>
    </fullCharge>
  </car>
  <car id="M3L">
    <model>Tesla Model 3 Long range</model>
    <officialRange scale="Miles">340</officialRange>
    <fullCharge>
      <rapidCharge timeScale="minutes">22</rapidCharge>
    </fullCharge>
  </car>
</Tesla>
```

can pass the indent as empty string if no indentation is needed.
