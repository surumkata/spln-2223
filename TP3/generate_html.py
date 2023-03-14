import pickle

def only_termos (list):
    r = f""

    for l in list:
        if "termo" in l: 
            termo = l['termo']
            r += f"{termo},"
        else:pass

    return r[:-1]

file = open('medicina_bin','rb')

dic = pickle.load(file)
file.close()

#print(dic)

pagHTML = '''
<!DOCTYPE html>
  <html>
    <head>
      <meta charset="" />
      <title>Medicine dictionary</title>
      <link rel="stylesheet" href="w3.css">
      <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            font-size: 12px;
            }
      </style>
    </head>
    <body>
        <h1>Medicine dictionary</h1>
      <div>
        <table>
            <tr>
                <th style="width: 10%;" >Areas</th>
                <th style="width: 20%;" >PT</th>
                <th style="width: 20%;" >GL</th>
                <th style="width: 20%;" >ES</th>
                <th style="width: 20%;" >EN</th>
                <th style="width: 20%;" >LA</th>
            </tr>

            '''

for entry in dic:
    areas = entry["areas"]
    linguas = entry["linguas"]
    pt = en = es = gl = la = []
    if("PT:" in linguas): pt = linguas["PT:"]
    if("ES:" in linguas): es = linguas["ES:"]
    if("EN:" in linguas): en = linguas["EN:"]
    if("GL:" in linguas): gl = linguas["GL:"]
    if("LA:" in linguas): la = linguas["LA:"] 
    pagHTML += f'''
        <tr>
            <td>{areas}</td>
            <td>{only_termos(pt)}</td>
            <td>{only_termos(es)}</td>
            <td>{only_termos(en)}</td>
            <td>{only_termos(gl)}</td>
            <td>{only_termos(la)}</td>
        <tr>
    '''


pagHTML+='''

        </table>
      </div>
    </body>

        '''

file = open("dicionario.html",'w')

file.write(pagHTML)
file.close()