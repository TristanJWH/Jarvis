import wikipedia
import wolframalpha
import os
import random as rand

def web(url):
    random = 0
    os.system(f"nohup alacritty -e firefox {url} > /dev/null 2>&1 &")
    os.system("wmctrl -s 1")
    random = rand.randint(0,3)
    if random == 0:
        return "opening"
    elif random == 1:
        return "okay"
    elif random == 2:
        return "affirmative"
    elif random == 3:
        return "check"

def search(querry, command_phrase, api):
    client = wolframalpha.Client(api)
    search_term = querry.split(command_phrase)[-1]
    res = client.query(search_term)
    try:
        answer = next(res.results).text
    except:
        return "There is no specific information for this search. Would you like me to search wikipedia?"
    return answer

def show_me_search(querry):
    search_term = querry.split("search for")[-1]
    # Changing banned characters to character codes
    search_term = search_term.replace("%", "%25")
    search_term = search_term.replace(" + ", "+%2B+")
    search_term = search_term.replace("=", "%3D")
    search_term = search_term.replace("/", "%2F")
    search_term = search_term.replace(" ", "+")
    web(f"https://www.wolframalpha.com/input/?i={search_term}")
    random = rand.randint(0,3)
    if random == 0:
        return "opening"
    elif random == 1:
        return "okay"
    elif random == 2:
        return "affirmative"
    elif random == 3:
        return "check"

def wiki(querry, command_phrase):
    search_term = querry.split(command_phrase)[-1]
    try:
        response = f"Showing results for {wikipedia.search(search_term)[0]}. {wikipedia.summary(search_term, sentences=1)}"
    except:
        response = "No wikipedia articles found"
    return response

def show_me_wiki(querry):
    search_term = querry.split("for")[-1]
    search = wikipedia.search(search_term)[0]
    page = wikipedia.page(search)
    return [page.url, f"Showing results for {search}"]
