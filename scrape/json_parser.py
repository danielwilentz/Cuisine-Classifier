import json
import pandas as pd
title_list = []

files = ['may_2015', 'june_2015', 'july_2015', 'august_2015', 'september_2015', 
        'october_2015', 'november_2015', 'december_2015', 'january_2016', 
        'february_2016', 'march_2016', 'april_2016', 'may_2016', 'june_2016',
        'july_2016', 'august_2016', 'september_2016', 'october_2016', 
        'november_2016', 'december_2016', 'january_2017', 'february_2017',
        'march_2017', 'april_2017', 'may_2017', 'june_2017', 'july_2017', 
        'august_2017', 'september_2017', 'october_2017', 'november_2017', 
        'december_2017', 'january_2018', 'february_2018', 'march_2018', 
        'april_2018', 'may_2018', 'june_2018', 'july_2018', 'august_2018', 
        'september_2018', 'october_2018', 'november_2018', 'december_2018', 
        'january_2019', 'february_2019', 'march_2019', 'april_2019']      

for file in files:
    path = 'data/' + file + '.json'
    with open(path) as json_file:  
        data = json.load(json_file)
        for p in data['data']:
            title_list.append(p['title'])

print(len(set(title_list)))
df = pd.DataFrame(set(title_list))
df.to_pickle('data/posts.pkl')