from pycricbuzz import Cricbuzz
c=Cricbuzz()
matches=c.matches()
for match in range(len(matches)):
    print(match)
    if match==len(matches)-1:
        if(matches[match]['mchstate']!='nextlive'):
            print(c.livescore(matches[match]['id']))
            print('**********************')
            print(c.scorecard(matches[match]['id']))
            print("********************************\n\n")
            live=c.livescore(matches[match]['id'])
            print(live['batting']['team'],"Vs ",live['bowling']['team'])
            print(live['batting']['score'][0]['runs'],'-',live['batting']['score'][0]['wickets'])
            print(live['batting']['score'][0]['overs'])
            print("Score Card")
            score=c.scorecard(matches[match]['id'])
            print("Batting\n")
            for i in score['scorecard'][0]['batcard']:
                print(i['name'],i['runs'],'(',i['balls'],")",'4-',i['fours'],'6-',i['six'])
            print('\nBowling')
            for i in score['scorecard'][0]['bowlcard']:
                print(i['name'],i['overs'],'maiden',i['maidens'],i['runs'],i['wickets'],'e-',int(i['wides'])+int(i['nballs']))
