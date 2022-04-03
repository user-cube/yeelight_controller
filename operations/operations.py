from yeelight import Bulb, discover_bulbs
from tabulate import tabulate

headers = ['ID', 'IP', 'Name', 'Type']
content = []
properties_headers = ["ID", "Name", "Power", "Brightness", "Saturation", "Music On"]
properties_content = []


def list_info(bulbs, force=False):
    if force:
        bulbs = discover_bulbs()
    if len(content) > 0:
        content.clear()
    for i in range(0, len(bulbs)):
        content.append([i, bulbs[i]['ip'], bulbs[i]['capabilities']['name'], bulbs[i]['capabilities']['model']])
    return bulbs


def turn_lights(bulbs, event):
    print(tabulate(content, headers, "pretty"))
    try:
        ans = input("\nBulb IDs (separated by space) => ")
        for a in ans.split(" "):
            bulb = Bulb(bulbs[int(a)]['ip'])
            if event == "off":
                bulb.turn_off()
            else:
                bulb.turn_on()
    except Exception as e:
        print(e)


def adjust_brightness(bulbs):
    print(tabulate(content, headers, "pretty"))
    try:
        ans = input("\nBulb IDs (separated by space) => ")
        bright = input("Brightness level => ")
        for a in ans.split(" "):
            bulb = Bulb(bulbs[int(a)]['ip'])
            bulb.set_brightness(int(bright))
    except Exception as e:
        print(e)


def list_bulb_properties(bulbs):
    if len(properties_content) > 0:
        properties_content.clear()
    for i in range(0, len(bulbs)):
        bulb = Bulb(bulbs[0]['ip'])
        props = bulb.get_properties()
        properties_content.append([i, props['name'], props['power'], props['bright'], props['sat'], props['music_on']])