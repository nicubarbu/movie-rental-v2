from domain.exceptions.duplicate_error import DuplicateError
from services.client_service import ClientService
from services.client_movie_service import ClientMovieService
from services.movie_service import MovieService


class Console:
    def __init__(self, client_service: ClientService,
               movie_service: MovieService,
               client_movie_service: ClientMovieService):
        self.__client_service = client_service
        self.__client_movie_service = client_movie_service
        self.__movie_service = movie_service
        
    def print_all_clients(self):
        clients = self.__client_service.get_all_clients()
        if len(clients) == 0:
            print("There are no clients!")
        else:
            for client in clients:
                print(client)
                
    def print_all_movies(self):
        movies = self.__movie_service.get_all_movies()
        if len(movies) == 0:
            print("There are no movies!")
        else:
            for movie in movies:
                print(movie)
        
    def print(self, entities):
        for entity in entities:
            print(entity)
        
    def add_client(self):
        try:
            id_client = input("Client ID: ")
            name = input("Client name: ")
            pin = input("Client PIN: ")
            self.__client_service.add(id_client, name, pin)
        except KeyError as ke:
            print(ke)
        except DuplicateError as de:
            print(de)
        except ValueError as ve:
            print(ve)
        # except Exception as e:
        #     print(e)
            
    def modify_client(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients to modify!")
            else:
                self.print_all_clients()
                id_client = int(input("Client ID: "))
                new_name = input("New name: ")
                new_pin = int(input("New pin: "))
                self.__client_service.modify(id_client, new_name, new_pin)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        # except Exception as e:
        #     print(e)
            
    def remove_client(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients to modify!")
            else:
                self.print_all_clients()
                id_client = int(input("Client ID: "))
                self.__client_service.remove(id_client)
        except KeyError as ke:
            print(ke)
        # except Exception as e:
        #     print(e)
            
    def add_movie(self):
        try:
            id_movie = int(input("Movie ID: "))
            title = input("Title: ")
            description = input("Description: ")
            genre = input("Genre: ")
            self.__movie_service.add(id_movie, title, description, genre)
        except DuplicateError as de:
            print(de)
        except ValueError as ve:
            print(ve)
        # except Exception as e:
        #     print(e)
            
    def modify_movie(self):
        try:
            if len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies to modify!")
            else:
                id_movie = int(input("Movie ID: "))
                new_title = input("New title: ")
                new_description = input("New description: ")
                new_genre = input("New genre: ")
                self.__movie_service.modify(id_movie, new_title, new_description, new_genre)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print (ve)    
        # except Exception as e:
        #     print(e)
            
    def remove_movie(self):
        try:
            if len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies to modify!")
            else:
                id_movie = int(input("Movie ID: "))
                self.__movie_service.remove(id_movie)
        except KeyError as ke:
            print(ke)
        # except Exception as e:
        #     print(e)
            
    def input_client_movie(self):
        try:
            id_client_movie = int(input("Id client-movie: "))
            id_client = int(input("Client ID: "))
            id_movie = int(input("Movie ID: "))
            self.__client_movie_service.add_input(id_client_movie, id_client, id_movie)
        except DuplicateError as e:
            print(e)
        except KeyError as e:
            print(e)
            
    def remove_input(self):
        id_client = int(input("Client ID: "))
        id_movie = int(input("Movie ID: "))
        self.__client_movie_service.remove_input(id_client, id_movie)
        
        
    def print_menu(self):
        print("""
                ADDITION, MODIFICATION & DELETION
            1. Add client
            2. Modify client
            3. Delete client
            4. Add movie
            5. Modify movie
            6. Delete movie
            
                            SEARCH
            7. Search movie
            8. Search client
            
                            RENTAL & RETURN
            9. Rent movie
            10. Return movie
            
                            REPORTS
            11. Reports for clients who rented movies ordered by name
            12. Reports for clients who rented movies ordered by the number of rented movies
            13. Reports for the most rented movies
            14. Reports for top 30% clients who rented the most movies
            
                            PRINT
            c. Print all clients
            m. Print all movies
            
            x. Exit
            """)
    
    def menu(self):
        
        while True:
            self.print_menu()
            option = input("Option: ")
            if option == '1':
                self.add_client()
            elif option == '2':
                self.modify_client()
            elif option == '3':
                self.remove_client()
            elif option == '4':
                self.add_movie()
            elif option == '5':
                self.modify_movie()
            elif option == '6':
                self.remove_movie()
            elif option == 'x':
                break
            elif option == 'c':
                self.print_all_clients()
            elif option == 'm':  
                self.print_all_movies()
            else:
                print("Invalid option!")
                self.print_menu()
                option = int(option)
            