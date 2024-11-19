**TrackFlix - Movie & TV Series Tracker**

TrackFlix is an application that is based on Python that gives users the ability to monitor how much they have watched movies and television shows. Users are able to manage their watchlists, favorite shows, filter content based on factors such as genre, country, or status, and more.

**Dummy Dataset**

Please keep in mind that the application's current functionality relies on a dummy dataset. The movie and TV show information, such as titles, genres, countries, and watch statuses, is hardcoded into the program and is only for demonstration purposes.

This means:
The list of films/shows is pre-loaded and does not originate from an external database or API.
The information provided will not include real-time updates or changes from actual movie/show databases such as IMDb, The Movie Database (TMDb), or others.
As the project progresses, you may want to consider integrating a real dataset or API to retrieve live data and provide a more interactive user experience.

**Features**

_Display Menu_: View the watchlist and sort by genre, country, status, or favorite.

_Add Menu_: Add new films/shows to your watchlist or favorite list.

_Update Menu_: Update ongoing films/shows or modify watch status and episodes watched.

_Delete Menu_: Remove films/shows from your main watchlist or favorite list.

_Filter Menu_: Filter films by genre, country, or status.

_Edit Menu_: Edit details of films/shows (e.g., title, genre, country, etc.).

**Installation**

Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/gerraldanantasa/TrackFlix.git


**Install Dependencies**

Make sure you have Python installed (version 3.7 or later). This project also employs the tabulate module to present the watchlist in a tabular format.To install the necessary dependencies,run:

pip install tabulate

**Usage**

**_Running the Program_**

To start the application, run the following command in your terminal or command prompt:
python track_flix.py

**_Main Menu_**

Upon launching the application, you will be presented with the main menu options:

_Display Menu_: View your full list of films/shows with the ability to filter them.

_Update_ _Menu_: Add new films or update the status of ongoing shows.

_Delete Menu_: Remove films from the watchlist or favorite list.

_Filter Menu_: Filter the films/shows based on Genre, Country, or Status.

_Edit Menu_: Edit film/show details like title, genre, and episodes.

_Exit_: Exit the application.

_**Menu Functions**_

_Display_: View your entire watchlist or a filtered list sorted by genre, country, or status.

_Add_: Add new films or TV shows to your watchlist and mark them as favorite.

_Update_: Track ongoing films/shows and update the episodes watched or change the watch status.

_Delete_: Remove films/shows from either the main list or favorite list.

_Filter_: Filter the list by specific attributes such as genre, country, or status (e.g., "Watching", "Finished").

_Edit_: Modify details of existing entries in your list.


**Example**

_Add a Film to the Watchlist_:
You can add a new film by choosing Update Menu > Add films/shows and entering the title, genre, country, episodes, and watch status.

_Update a Show_:
If you're watching a show and need to update it, choose Update Menu > Update ongoing film/shows, and update the number of episodes watched or the status.

_Display Films by Genre_:
Choose Display Menu > Show by genre to list your films sorted by genre.

_Remove a Film_:
Use the Delete Menu to remove a show or film from your watchlist or favorite list.

**Code Structure**

**_track_flix.py_**: The main Python script containing all functions and menus.

_**tabulate module**_: Used to format and display lists in a neat tabular format.

The application keeps two lists: list_film for the main watchlist and favorite_list for films/shows marked as favorites.

**Contributing**

If you'd like to contribute to TrackFlix, feel free to fork the repository and submit a pull request with improvements or bug fixes.

**Bug Reports & Issues**

If you encounter any bugs or have suggestions for new features, please open an issue in the repository.

