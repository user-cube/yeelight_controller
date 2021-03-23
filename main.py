from tabulate import tabulate
from operations.operations import list_info, turn_lights, adjust_brightness, content, headers, list_bulb_properties, \
    properties_content, properties_headers
from yeelight import discover_bulbs
import readline


def menu(bulbs):
    print("""
    [5] - Adjust brightness
    [4] - Turn on lights
    [3] - Turn off lights
    [2] - List Bulb Properties
    [1] - List bulbs
    [0] - Exit
    [F] - Force Bulb Reload
    """)
    ans = input("Option => ")
    if ans == "0" or ans.lower() == "exit":
        pass
    elif ans == "1":
        list_info(bulbs)
        print(tabulate(content, headers, "pretty"))
        menu(bulbs)
    elif ans == "2":
        list_bulb_properties(bulbs)
        print(tabulate(properties_content, properties_headers, "pretty"))
        menu(bulbs)
    elif ans == "3":
        turn_lights(bulbs, "off")
        menu(bulbs)
    elif ans == "4":
        turn_lights(bulbs, "on")
        menu(bulbs)
    elif ans == "5":
        adjust_brightness(bulbs)
        menu(bulbs)
    elif ans == "F":
        bulbs = list_info(bulbs, True)
        print(tabulate(properties_content, properties_headers, "pretty"))
        menu(bulbs)
    else:
        print("Please select a valid option")
        menu(bulbs)


if __name__ == '__main__':
    bulbs = discover_bulbs()
    list_info(bulbs)
    menu(bulbs)
