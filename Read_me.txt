TrackFlix - Movie & TV Series Tracker
TrackFlix is an application that is based on Python that gives users the ability to monitor how much they have watched movies and television shows. Users are able to manage their watchlists, favorite shows, filter content based on factors such as genre, country, or status, and more.


Dummy Dataset
Please keep in mind that the application's current functionality relies on a dummy dataset. The movie and TV show information, such as titles, genres, countries, and watch statuses, is hardcoded into the program and is only for demonstration purposes.
This means:
* The list of films/shows is pre-loaded and does not originate from an external database or API.
* The information provided will not include real-time updates or changes from actual movie/show databases such as IMDb, The Movie Database (TMDb), or others.
As the project progresses, you may want to consider integrating a real dataset or API to retrieve live data and provide a more interactive user experience.
Features
* Display Menu: View the watchlist and sort by genre, country, status, or favorite.
* Add Menu: Add new films/shows to your watchlist or favorite list.
* Update Menu: Update ongoing films/shows or modify watch status and episodes watched.
* Delete Menu: Remove films/shows from your main watchlist or favorite list.
* Filter Menu: Filter films by genre, country, or status.
* Edit Menu: Edit details of films/shows (e.g., title, genre, country, etc.).
Installation
1. Clone the Repository
Clone this repository to your local machine:


git clone https://github.com/gerraldanantasa/TrackFlix.git




   2. Install Dependencies
Make sure you have Python installed (version 3.7 or later). This project also employs the tabulate module to present the watchlist in a tabular format.To install the necessary dependencies,run:

pip install tabulate
Usage
Running the Program
To start the application, run the following command in your terminal or command prompt:
python track_flix.py


Main Menu
Upon launching the application, you will be presented with the main menu options:
      1. Display Menu: View your full list of films/shows with the ability to filter them.
      2. Update Menu: Add new films or update the status of ongoing shows.
      3. Delete Menu: Remove films from the watchlist or favorite list.
      4. Filter Menu: Filter the films/shows based on Genre, Country, or Status.
      5. Edit Menu: Edit film/show details like title, genre, and episodes.
      6. Exit: Exit the application.
Menu Functions
      * Display: View your entire watchlist or a filtered list sorted by genre, country, or status.
      * Add: Add new films or TV shows to your watchlist and mark them as favorite.
      * Update: Track ongoing films/shows and update the episodes watched or change the watch status.
      * Delete: Remove films/shows from either the main list or favorite list.
      * Filter: Filter the list by specific attributes such as genre, country, or status (e.g., "Watching", "Finished").
      * Edit: Modify details of existing entries in your list.




Example
      1. Add a Film to the Watchlist:
You can add a new film by choosing Update Menu > Add films/shows and entering the title, genre, country, episodes, and watch status.
      2. Update a Show:
If you're watching a show and need to update it, choose Update Menu > Update ongoing film/shows, and update the number of episodes watched or the status.
      3. Display Films by Genre:
Choose Display Menu > Show by genre to list your films sorted by genre.
      4. Remove a Film:
Use the Delete Menu to remove a show or film from your watchlist or favorite list.
Code Structure
         * track_flix.py: The main Python script containing all functions and menus.
         * tabulate module: Used to format and display lists in a neat tabular format.
         * The application keeps two lists: list_film for the main watchlist and favorite_list for films/shows marked as favorites.
Contributing
If you'd like to contribute to TrackFlix, feel free to fork the repository and submit a pull request with improvements or bug fixes.
Bug Reports & Issues
If you encounter any bugs or have suggestions for new features, please open an issue in the repository.