ta_data = [['Peter', 'USA', 'CS262'],
           ['Andy', 'USA', 'CS212'],
           ['Sarah', 'England', 'CS101'],
           ['Gundega', 'Latvia', 'CS373'],
           ['Job', 'USA', 'CS387'],
           ['Sean', 'USA', 'CS253']]

remote_ta_facts = [name + 'live in ' + country + ' and is the TA for ' + 
            course for name, country, course in ta_data if country != 'USA']

for row in remote_ta_facts:
    print row
