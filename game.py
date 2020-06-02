import json
def set_charact(name):
    character = {
        "name" : name,
        "level" : 1,
        "hp" : 100,
        "items" : ["대나무헬리콥터","빅라이트","어디로든 문"],
        "skill" : ["펀치","핵펀치","피하기"]
    }
    with open("static/save.txt", "w" , encoding="uth-8") as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
        return character
        def save_game(filename, charact):
            f = open(filename, "w" encoding="utf-8")