#Capstone Modul 1 
from tabulate import tabulate  
import os 
# Sort list_film by alphabetical order based on the film name
list_film = sorted([
    {'film': 'Haikyuu Season 1', 'genre': ['Anime', 'Sports'], 'country': 'Japan', 'toteps': 24, 'epswatched': 0, 'status': 'Not started'},
    {'film': 'Inception', 'genre': ['Mystery', 'Sci-Fi', 'Thriller'], 'country': 'North America', 'toteps': 1, 'epswatched': 1, 'status': 'Finished'},
    {'film': 'The Witcher', 'genre': ['Fantasy', 'Adventure'], 'country': 'Poland', 'toteps': 8, 'epswatched': 8, 'status': 'Finished'},
    {'film': 'Money Heist', 'genre': ['Crime', 'Thriller'], 'country': 'Spain', 'toteps': 31, 'epswatched': 12, 'status': 'Watching'},
    {'film': 'Attack on Titan', 'genre': ['Anime'], 'country': 'Japan', 'toteps': 75, 'epswatched': 30, 'status': 'Watching'},
    {'film': 'Stranger Things', 'genre': ['Sci-Fi', 'Horror', 'Mystery'], 'country': 'North America', 'toteps': 25, 'epswatched': 0, 'status': 'Not started'},
    {'film': 'Squid Game', 'genre': ['Thriller', 'Drama'], 'country': 'Korea', 'toteps': 9, 'epswatched': 9, 'status': 'Finished'},
    {'film': 'Breaking Bad', 'genre': ['Drama'], 'country': 'North America', 'toteps': 62, 'epswatched': 62, 'status': 'Finished'},
    {'film': 'Dark', 'genre': ['Sci-Fi', 'Mystery', 'Thriller'], 'country': 'Germany', 'toteps': 26, 'epswatched': 13, 'status': 'Watching'},
    {'film': 'Friends', 'genre': ['Comedy', 'Slice of Life'], 'country': 'North America', 'toteps': 236, 'epswatched': 50, 'status': 'Watching'}
], key=lambda x: x['film'])

# favorite list (sorted by film name if you have multiple entries)
favorite_list = sorted([
    {'film': 'Inception', 'genre': ['Mystery', 'Sci-Fi', 'Thriller'], 'country': 'North America', 'toteps': 1, 'epswatched': 1, 'status': 'Finished'},
    {'film': 'Breaking Bad', 'genre': ['Drama', 'Crime', 'Thriller'], 'country': 'North America', 'toteps': 62, 'epswatched': 62, 'status': 'Finished'},
    {'film': 'Dark', 'genre': ['Sci-Fi', 'Mystery', 'Thriller'], 'country': 'Germany', 'toteps': 26, 'epswatched': 13, 'status': 'Watching'}  
], key=lambda x: x['film'])

# Header definitions 
headers_all = ["Index", "Film", "Genre", "Country", "Total Episodes", "Episodes Watched", "Status"]
headers_search= ["Film", "Genre", "Country", "Total Episodes", "Episodes Watched", "Status"]
headers_genre = ["Index", "Film", "Genre"]
headers_country = ["Index", "Film", "Country"]
headers_status = ["Index", "Film", "Total Episodes", "Episodes Watched", "Status"]
def main():
    #Use pre-sorted list for consistent display 
    if list_film:
        film_all = [[idx + 1, film['film'], ','.join(film['genre']), film['country'], film['toteps'], film['epswatched'], film['status']] for idx, film in enumerate(list_film)]
        print('Your watch list:')
        print(tabulate(film_all, headers=headers_all, tablefmt="simple"))
    else:
        print('Your main list is empty.')






# Display menu
def display():
    os.system('cls')
    while True:
        
        print()
        print("Display Menu")
        print("1. Show all films")
        print("2. Show by genre")
        print("3. Show by country")
        print("4. Show by status")
        print("5. Show favorite list")
        print("6. Back to main menu")
        
        try:
            menu1 = int(input("Choose a menu: "))
            print()

            if menu1 == 1: 
                    main()
           

            elif menu1 == 2:
              
                #Display by genre 
                film_genre = sorted([[idx + 1, film['film'], ','.join(film['genre'])]for idx, film in enumerate(list_film)], key=lambda x: x[2])                
                print('Watch list by genre:')
                print(tabulate(film_genre, headers=headers_genre, tablefmt="simple"))

            elif menu1 == 3:
                #Display by country 
                film_country = sorted([[idx + 1, film['film'], film['country']] for idx, film in enumerate(list_film)], key=lambda x: x[2])
                print('Watch list by country:')
                print(tabulate(film_country, headers=headers_country, tablefmt="simple"))

            elif menu1 == 4:
                # Display by status
                film_status = sorted([[idx + 1, film['film'], film['status']] for idx, film in enumerate(list_film)], key=lambda x: x[2])
                print('Watch list by status:')
                print(tabulate(film_status, headers=headers_status, tablefmt="simple"))

            elif menu1 == 5:
                favorite()

            elif menu1==6:
                break
            else:
                print('Menu is unavailable.')
        except ValueError:
            print("Please enter a valid number.")

        print()


def favorite():
    #Display Favorite list 
    if favorite_list:
        fav_all = [[idx + 1, film['film'], ','.join(film['genre']), film['country'], film['toteps'], film['epswatched'], film['status']] for idx, film in enumerate(favorite_list)]
        print('Favorite list:')
        print(tabulate(fav_all, headers=headers_all, tablefmt="simple"))
    else:
        print('Your favorite list is empty.')

def confirm():
    while True:
        confirmation = input('Are you sure? (y/n): ').lower().strip()
        if confirmation == 'y':
            return True
        elif confirmation == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")



def add():
    while True:
        print()
        print("Update Menu:")
        print("1. Add films/shows")
        print("2. Add films/shows to favorite list (by index)")
        print('3. Update ongoing film/shows')
        print("4. Back to main menu") 
    
        try:
            menu2 = int(input("Choose a menu: "))
            print()

            if menu2 == 1:
                # Adding a new film/show to the main list
                film_input = input("Enter the film/show name: ").strip().title()
                
                # Check for duplicates by film name
                # Use any to check duplicates if True return message
                if any(item['film'].lower() == film_input.lower() for item in list_film):
                    print(f"\n'{film_input}' is already in the watch list.")
                
                else:
                    genre = input("Enter the genre: ").title().split(',') # add multiple
                    country = input("Enter the country of origin: ").title()
                    toteps = int(input("Enter the total number of episodes: "))
                    epswatched = int(input("Enter the number of episodes watched: "))

                
                    status = input("Enter the watch status (Watching, Finished, Not started): ").title()

                    new_entry = {
                        'film': film_input,
                        'genre': genre,
                        'country': country,
                        'toteps': toteps,
                        'epswatched': epswatched,
                        'status': status
                    }
                    if confirm():
                        list_film.append(new_entry)
                        list_film.sort(key=lambda x: x['film']) 
                        print(f"\n'{film_input}' has been added to your watch list.")
                        main()
                    
            elif menu2 == 2:
                os.system('cls')
                # Adding films/shows to the favorite list using index from the main list

                #Check if list film is still available
                if not list_film:
                    print("\nThe main watch list is empty. Please add films/shows first.")
                else:
                    # Display the current list with index
                    main()
                    
                    try:
                        index = int(input("\nEnter the index number of the film/show to add to the favorite list: ")) - 1
                        if 0 <= index < len(list_film):
                            selected_film = list_film[index]

                            # Duplicate check
                            if any(item['film'].lower() == selected_film['film'].lower() for item in favorite_list):
                                print(f"\n'{selected_film['film']}' is already in the favorite list.")
                            else:
                                if confirm():
                                    favorite_list.append(selected_film)
                                    favorite_list.sort(key=lambda x: x['film'])
                                    print(f"\n'{selected_film['film']}' has been added to your favorite list.")
                                    favorite()
                        else:
                            print("Invalid index. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")


            elif menu2 == 3:
          
                # Updating an ongoing film/show
                if not list_film:
                    print("\nThe main watch list is empty. Please add films/shows first.")
                else:
                    # Display the current list with index
                    main()
                    
                    try:
                        index = int(input("\nEnter the index number of the film/show to update: ")) - 1
                        if 0 <= index < len(list_film):

                            # Update selected film/show
                            selected_film = list_film[index]
                            new_epswatched = int(input(f"Enter the number of the recent episode (current: {selected_film['epswatched']}/{selected_film['toteps']}): "))
                            selected_film['epswatched'] = new_epswatched 
                            status_update = input(f"Enter the new status (current: {selected_film['status']}): ").title().strip()
                            selected_film['status'] = status_update

                            if confirm():
                                print(f"\n'{selected_film['film']}' has been updated.")
                            main()

                            # Check if item is also in favorite list
                            if favorite_list:
                                for item in favorite_list:
                                    if item["film"] == selected_film["film"]:
                                        item['epswatched'] = selected_film['epswatched']
                                        item['status'] = selected_film['status']
                                        print(f"\n'{item['film']}' has also been updated in your favorite list.")
                                        break
                            favorite()
                        else:
                            print("Invalid index. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            elif menu2 == 4:
                break
            else:
                print('Menu is unavailable.')
        except ValueError:
            print("Please enter a valid number.")

        print()

def display():
    os.system('cls')
    while True:
        
        print()
        print("Display Menu")
        print("1. Show all films")
        print("2. Show by genre")
        print("3. Show by country")
        print("4. Show by status")
        print("5. Show favorite list")
        print("6. Back to main menu")
        
        try:
            menu1 = int(input("Choose a menu: "))
            print()

            if menu1 == 1:
                
                #Use pre-sorted list for consistent display 
                main()

            elif menu1 == 2:
              
                #Display by genre 
                film_genre = sorted([[idx + 1, film['film'], ','.join(film['genre']) if isinstance(film['genre'], list) else film['genre']] for idx, film in enumerate(list_film)], key=lambda x: x[2])                
                print('Watch list by genre:')
                print(tabulate(film_genre, headers=headers_genre, tablefmt="simple"))

            elif menu1 == 3:
                #Display by country 
                film_country = sorted([[idx + 1, film['film'], film['country']] for idx, film in enumerate(list_film)], key=lambda x: x[2])
                print('Watch list by country:')
                print(tabulate(film_country, headers=headers_country, tablefmt="simple"))

            elif menu1 == 4:
                # Display by status
                film_status = sorted([[idx + 1, film['film'], film['status']] for idx, film in enumerate(list_film)], key=lambda x: x[2])
                print('Watch list by status:')
                print(tabulate(film_status, headers=headers_status, tablefmt="simple"))

            elif menu1 == 5:
                favorite()

            elif menu1==6:
                break
            else:
                print('Menu is unavailable.')
        except ValueError:
            print("Please enter a valid number.")

        print()

def delete():
    os.system('cls')

    while True:
        print()
        print("Delete Menu")
        print("1. Delete from main watch list")
        print("2. Delete from favorite list")
        print("3. Back to main menu")
        
        try:
            menu3 = int(input("Choose an option: "))
            
            if menu3 == 1:
                if list_film:
                    main()
                    try:
                        index = int(input("Enter the index of the film to delete: ")) - 1
                        if 0 <= index < len(list_film):
                            if confirm():
                                removed_film = list_film.pop(index)
                                print(f"\n'{removed_film['film']}' has been removed from the watch list.")
                                main()

                            if favorite_list:
                                for idx, item in enumerate(favorite_list):
                                    if item["film"] == removed_film["film"]:
                                        favorite_list.pop(idx)
                                        print(f"\n'{removed_film['film']}' has been removed from the favorite list.")
                                        favorite()
                                    
                        else:
                            print("Invalid index. Please try again.")
                    
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("The main watch list is empty.")
                

            
            elif menu3 == 2:

                if favorite_list:
                    favorite()
                    try:
                        index = int(input("Enter the index of the film to delete: ")) - 1
                        if 0 <= index < len(favorite_list):
                             if confirm():
                                removed_film = favorite_list.pop(index)
                                print(f"\n'{removed_film['film']}' has been removed from the favorite list.")
                                favorite()


                        else:
                            print("Invalid index. Please try again.")

                        
            
            
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("The favorite list is empty.")
               
            elif menu3 == 3:
                break
            else:
                print("Invalid option. Please choose a valid menu option.")
        
        except ValueError:
            print("Please enter a valid number.")
        print()

def filter_movie(chosen_list=list_film):
    os.system('cls')

    while True:
        print()
        print("Filter Options")
        print("1. Filter by Genre")
        print("2. Filter by Country")
        print("3. Filter by Status")
        print('4. Back to previous menu')
        try:
            filter_choice = int(input("Choose an option to filter by: "))
            
            if filter_choice == 1:
                
                print('Available genre:')
                print(sorted({genre for film in chosen_list for genre in film['genre']}))
                filter_key = 'genre'
                filter_value = input("Enter the genre to filter by: ").title().strip()

            elif filter_choice == 2:

                print('Available film status:')
                print(sorted({film['country'] for film in chosen_list}))
                filter_key = 'country'
                filter_value = input("Enter the country to filter by: ").title().strip()

            elif filter_choice == 3:

                print('Available film status:')
                print(sorted({film['status'] for film in chosen_list}))
                filter_key = 'status'
                filter_value = input("Enter the watch status to filter by (Watching, Finished, Not started): ").title().strip()
            
            elif filter_choice == 4:
                print('Return to previous menu')
                break
            
            else:
                print('Option unavailable.')

            
            # Filter the list based on the selected attribute and value
            if filter_key == 'genre':
                # Check if any genre in each film matches the filter value
                filtered_films = [
                    [
                        idx + 1, film['film'], ', '.join(film['genre']), film['country'], 
                        film['toteps'], film['epswatched'], film['status']
                    ] 
                    for idx, film in enumerate(chosen_list) 
                    if filter_value in film['genre']
                ]
            else:
                filtered_films = [
                    [
                        idx + 1, film['film'], ', '.join(film['genre']), film['country'], 
                        film['toteps'], film['epswatched'], film['status']
                    ] 
                    for idx, film in enumerate(chosen_list) 
                    if film[filter_key].lower() == filter_value.lower()
                ]
            
            
            # Display filtered results
            if filtered_films:
                print()
                print(f'Films with {filter_key.capitalize()} "{filter_value}":')
                print(tabulate(filtered_films, headers=headers_all, tablefmt="simple"))
            else:
                print()
                print(f'No films found with {filter_key.capitalize()} "{filter_value}".')
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def edit_function(edit_value, edit_idx, chosen_list=list_film):
    selected_film = chosen_list[edit_idx]

    if edit_value == 'film':
        current_value = selected_film["film"]
        column_name = "film"

    elif edit_value == 'genre':
        current_value = (selected_film["genre"])
        column_name = "genre"

    elif edit_value == 'country':
        current_value = selected_film["country"]
        column_name = "country"

    elif edit_value == 'total episodes':
        current_value = selected_film["toteps"]
        column_name = "toteps"

    elif edit_value == 'episodes watched':
        current_value = selected_film["epswatched"]
        column_name = "epswatched"

    elif edit_value == 'status':
        current_value = selected_film["status"]
        column_name = "status"
        
    else:
        print("Invalid column name.")
        return

    # Ask for the new value
    if column_name=='genre':
        new_value = input(f"Input the new {column_name} (current: {', '.join(current_value)}): ").strip().title().split(',')
        selected_film['genre'] = new_value
        if confirm():
            print(f"{column_name.capitalize()} of '{selected_film['film']}' has been successfully changed to {','.join(new_value)}.")
            main()
    else:
        new_value = input(f"Input the new {column_name} (current: {current_value}): ").strip().title()
        selected_film[column_name] = new_value
        if confirm():
            print(f"{column_name.capitalize()} of '{selected_film['film']}' has been successfully changed to {(new_value)}.")
            main()
     # Update if favorite list exist
    if favorite_list:
        for item in favorite_list:
            if item["film"] == selected_film["film"]:
                item[column_name] = new_value
                break
        favorite()


def track_flix():
    
    while True:
        print()
        print("Welcome to TrackFlix")
        print("Menu list:")
        print("1. Display Menu")
        print("2. Update Menu")
        print("3. Delete Menu")
        print('4. Filter Menu')
        print('5. Edit Menu')
        print("6. Exit Program")
        try:
            main_menu = int(input("Choose a menu: "))

            if main_menu == 1:
                display()


            elif main_menu == 2:
                add()


            elif main_menu == 3:
                delete()


            elif main_menu == 4:
                main_menu4 = input("Choose the list you want tou use (e.g Main/Favorite): ").lower().strip()
                
                try:
                    if main_menu4=='main':
                        os.system('cls')
                        filter_movie()

                    elif main_menu4=='favorite':
                        os.system('cls')
                        filter_movie(favorite_list)
                
                except ValueError:
                    print("Please enter a valid option.")

            elif main_menu == 5:
                os.system('cls')
                print()
                print("Welcome to the edit menu")
               
                try:
                    print("Edit menu")
                    main()
                    edit_idx= int(input('Input the index you want to edit: '))-1
                    print("Available columns:")
                    print("film, genre, country, total episodes, episodes watched, status")
                    edit_value= input('Input the column you want to edit: ').lower().strip()
                    edit_function(edit_value, edit_idx)
                
                except ValueError:
                    print("Please enter a valid option.")
                
            elif main_menu == 6:
                print("Thank you!")
                break
            else:
                print("Menu is unavailable")
        except ValueError:
            print("Invalid option")

track_flix()