# PartyManager
WebApp for ordering beverages and other stuff written in flask

![Screenshot_Home - PartyName](https://user-images.githubusercontent.com/60071372/84798182-f11b3b80-affa-11ea-9924-ccc4389c0f9d.png)
## Repository Structure
```
.
├── dboperations.py   # module for database operations
├── .gitignore
├── LICENSE
├── admin.py          # second flask application for admin stuff
├── party.db          # the database
├── party.py          # the flask application
├── reader.py         # python script to display orders
├── README.md
├── static            # webpage static elements
│   ├── favicon.ico   # favicon
│   ├── img           # webpage images
│   └── styles.css    # webpage css style
└── templates         # webpage html pages
    ├── error.html
    ├── goback.html
    ├── index.html
    ├── layout.html
    ├── license.html
    ├── policy.html
    ├── admin.html
    ├── codes.html
    ├── dashboard.html
    └── success.html
```
## Running Flow

### 1) Admin.py: The admin dashboard. Add items and people. marks items outofstock
`python admin.py`
### 3) Party.py: Provides the web interface and saves the orders in the db
`python party.py`
### 4) Reader.py: Read the orders
`python reader.py`
