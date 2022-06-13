import argparse
import json
import webbrowser as wb

DEFAULT_SEARCH_ENGINE = 'google'

def get_search_engines():
    search_engines = []
    with open('search_engines.json', 'r') as se_json:
        search_engines = json.load(se_json)
    return search_engines

def get_args(search_engines):
    parser = argparse.ArgumentParser()
    parser.add_argument("search", help="search string", type=str) 
    for se in search_engines:
        # parser.add_argument(f"-g", f"--google", help=f"Use google as search engine", action="store_true")
        parser.add_argument(f"-{search_engines[se]['shortArg']}", f"--{se}", help=f"use {se} as search engine", action="store_true")

    args = parser.parse_args()
    # print("args: ", args.__dict__)
    return args
        
if __name__ == "__main__":
    search_engines = get_search_engines()
    args = get_args(search_engines)

    search = args.search
    search_engines_to_use = [engine for engine in args.__dict__ if engine in search_engines and args.__dict__[engine]]
    if len(search_engines_to_use) == 0:
        search_engines_to_use = [DEFAULT_SEARCH_ENGINE]

    print("searching: ", search)
    print("search engines to use: ", search_engines_to_use)

    for engine in search_engines_to_use:
        search_url = search_engines[engine]["searchUrl"]
        sep = search_engines[engine]["seperator"]
        query = search.replace(' ', sep)
        link = f'{search_url}{query}'
        wb.open_new_tab(link)