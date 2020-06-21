# PartyManager
WebApp for ordering beverages and other stuff written in flask

![Screenshot_Home - PartyName](https://user-images.githubusercontent.com/60071372/84798182-f11b3b80-affa-11ea-9924-ccc4389c0f9d.png)
## Repository Structure
```
.
├── admin.py            # ADMIN Flask App
├── dboperations.py     # DB operation module
├── LICENSE
├── party.db            # Database for people, items and orders
├── party.py            # Main Flask App
├── reader.py           # Python reader 
├── README.md
├── static
│   ├── Cantarell-Bold.ttf
│   ├── favicon.ico
│   ├── img
│   │   ├── header.jpg
│   │   └── ok.png
│   ├── Roboto-Bold.ttf
│   ├── Roboto-Regular.ttf
│   ├── Roboto-Thin.ttf
│   └── styles.css
└── templates
    ├── admin.html
    ├── codes.html
    ├── dashboard.html
    ├── error.html
    ├── goback.html
    ├── index.html
    ├── layout.html
    ├── license.html
    ├── policy.html
    └── success.html

```
## Running Flow

### 1) Admin.py: The admin dashboard. Add items and people. marks items outofstock
`python admin.py`
### 3) Party.py: Provides the web interface and saves the orders in the db
`python party.py`
### 4) Reader.py: Read the orders
`python reader.py`
