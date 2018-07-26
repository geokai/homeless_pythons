import requests
import json

###--- All data:
all_data = requests.get('https://thingspeak.com/channels/1417/feeds.json')

###--- to extract data from whole page:
all_data.raise_for_status()
print()
print(all_data.status_code)
print()
print(len(all_data.text))
print()
print(all_data.content)
print()
json.loads(all_data)


###--- last feed:
last_feed = requests.get('https://thingspeak.com/channels/1417/last.json')




###--- last color:
last_color = requests.get('https://thingspeak.com/channels/1417/field/1/last.txt')
print()
last_color.raise_for_status()
print()


#print(feeds)
#print(type(feeds))

#last = feeds[-1]
#print(last)
#print(type(last))

#color = last['field1']
#print(color)
#print(type(color))
#print(type(one_color))
print(type(one_feed))
#print(one_color.content)
print(one_feed.content)
