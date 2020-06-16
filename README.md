# PartyManager
WebApp for ordering beverages and other stuff written in flask

## Repository Structure
```
.
├── dboperations.py   # module for database operations
├── filler.py         # python script to populate the database
├── .gitignore
├── LICENSE
├── manager.py        # python script to mark the end of an item
├── party.db          # the database
├── party.py          # the flask application
├── reader.py         # python script to display orders
├── README.md
├── static            # webpage static elements
│   ├── img           # webpage images
│   └── styles.css    # webpage css style
└── templates         # webpage html pages
    ├── error.html
    ├── goback.html
    ├── index.html
    ├── layout.html
    ├── license.html
    ├── policy.html
    └── success.html
```
## Running Flow

### 1) Filler.py: Creates the database and inserts the data provided by the sysadmin in the tables 
 `python filler.py`
### 2) Codes.py: Prints the user codes in a spreadsheet
### 3) Party.py: Provides the web interface and saves the orders in the db
`python party.py`
### 4) Reader.py: Read the orders
`python reader.py`
### 5) Manager.py: Marks products out of stock
`python manager.py`