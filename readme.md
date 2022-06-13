# Overview
Web browser search utility through command line

# Usage 
- **help** - `py search.py -h`
- **basic search** - `py search.py apples`
- **multi-line search** - `py search.py "how to center a div in css" -g`
- **search with multiple search engines** `py search.py "humans need not apply" -g -y`

# Adding custom search engines

Simply add a new object in the `search_engines.json` and use.

## Example 
Adding *duckduckgo* as search engine:
1. Search `test query` in *duckduckgo*
2. It shows `https://duckduckgo.com/?q=test+query`
3. Add the following to `search_engines.json`

```js
    "duckduckgo": {
        "shortArg": "d",
        "searchUrl": "https://duckduckgo.com/?q=",
        "seperator": "+"
    }
```
4. Search through *duckduckgo* can now be used `py search.py apples -d`
