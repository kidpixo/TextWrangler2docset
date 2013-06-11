## What do it does?

Translate existing help file from TextWrangler located in `/TextWrangler.app/Contents/Resources/TextWrangler Help/`
to navigable documentation (docset) file to use with [Dash](http://kapeli.com/dash)

I translated the `<h3>` and `<h4>` header to Table of Contents items (Alt-Up/Down arrow to navigate in [Dash](http://kapeli.com/dash)).

Thanks [Bogdan](https://github.com/Kapeli) for the explanation!

![Dash open at the TextWrangler2docset](https://dl.dropboxusercontent.com/u/4762299/github_img/TextWrangler2docset/dash_in_action.png)

## How to to : Short Version

1. clone/download the repository
- add the `TextWrangler2docset.docset`
- enjoy it!

## How to to : Long Version

The python script does:

- copy the whole html `/TextWrangler Help/` to `/Documents/` in the docset.
- Delete :
    - grep.htm
    - searching.htm
    - index.htm
- cycle all the html file to the DB to:
    - delete all files with <frame> & the first referenced <frame> source
    - add the good files to the SQLite DB
- **Extra** : run the `table_of_contents.sh` to get the TOC items, it is written for [fish,a command
line shell for the 90s](http://fishshell.com/)

You can run the `TextWrangler2docset.py` script, adapting the path pointing to `TextWrangler.app`, default is

    source_dir = '/Applications/TextWrangler.app/Contents/Resources/TextWrangler Help/'

 and taking care of all the dependencies:

- multimarkdow (needed to translate markdown files)

- Python modules (needed to move file,parse it and a lot of stuff) :

    - sqlite3
    - glob
    - os
    - subprocess
    - BeautifulSoup4 (not essential, but I like prettified html code)

I installed everything with macports on a Mac OSX 10.7.5 and on 10.8.2, works fine. 

