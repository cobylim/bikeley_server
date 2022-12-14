# Setup
Download and/or clone this repository as needed. Create a new Python environment and install the dependencies with

```sh
$ pip install -r requirements.txt
```

Run the server on your local environment with

```sh
$ cd bikeley_server
$ python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000/` 

# Admin page

Go to `http://127.0.0.1:8000/admin` to access the admin page. Instructions for navigating the admin page are [here](https://wealthy-catmint-f7d.notion.site/Bikeley-Admin-af351dfad1b347cd82ec631dafdaf4bc).

# API

The Locations API should also be running at `http://127.0.0.1:8000/admin`. Accessing the site in your browser should give you a GUI to interact with the admin. 
Alternatively, you can also use a tool such as Postman to access the server. The full API documentation is available [here](https://wealthy-catmint-f7d.notion.site/Bikeley-API-Specs-7e8cee3ffcf445bbb3ed81b4333a1108).
