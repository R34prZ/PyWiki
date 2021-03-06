# PyWiki

The idea of PyWiki is to be a **simple project**, capable of searching for information in Wikipedia and returning it's results on the screen.


## About
PyWiki is made using **Python**. **Pygame** is used to handle the display and **wikipedia** is used to get the search results.

## Running
You can run PyWiki with **python3**. I recommend using a virtual environment with:
> Clone the repo  using `git clone https://github.com/R34prZ/PyWiki`.  
> `python3 -m venv env` in the repo root.   
  
> You should see the following file structure:  
> PyWiki  
> -- env  
> -- src  
> ------ ...  
> ------ [main.py](./src/main.py)  
> -- .gitignore  
> -- README.md  
> -- requirements.txt  
  
> Activate the virtual environment with `source env/bin/activate`.  
> Download the requirements with `pip` (see the Requirements section).  
> Then run `python3 ./src/main.py`.  
> Once done, you can leave the virtual environment with `deactivate`.  

## Requirements
The requirements can be found in [here](./requirements.txt). You can download them with **pip** using `python3 -m pip install -r requirements.txt`.  
I recommend using at least python `3.10`, as `match case` is needed (otherwise you will need to change all the `match` structures to traditional `if` statements).

### TODO
---
 - [x] Text input for search
 - [X] Link the wikipedia search function to the search button
 - [X] Get the wikipedia search result and display it
 - [X] Better process search
 - [X] Option to favorite results
 - [ ] Clickable bookmarks that act as a link to search
 - [ ] Option to save results locally
 - [ ] Language selection
 
###### OBS:  The command instructions above work on linux and are not tested on Windows, though it should work, i'm not sure.
  
##### [R34prZ](https://github.com/R34prZ)
