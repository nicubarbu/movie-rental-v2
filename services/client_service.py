from domain.client import Client
from repository.repository import Repository
from domain.exceptions.name_not_found_error import NameNotFoundError


class ClientService:
    def __init__(self, client_repository: Repository):
        self.__client_repository = client_repository
        
    def get_all_clients(self):
        '''
        return all clients as list
        input: -
        return: Client type objects list
        '''
        return self.__client_repository.get_all()
    
    def get_by_id(self, id_client):
        '''
        return a client by id
        input: id_client - int
        return: Client type object
        '''
        return self.__client_repository.get_by_id(id_client)
    
    def add(self, id_client, name, pin):
        '''
        add a client
        input: id_client - int
               name - string
               pin - string
        output: -
        '''
        client = Client(id_client, name, pin)
        self.__client_repository.add(client)
        
    def modify(self, id_client, new_name, new_pin):
        '''
        modify a client
        input: id_client - int
               new_name - string
               new_pin - string
        output: -
        '''
        client = Client(id_client, new_name, new_pin)
        self.__client_repository.modify(client)
        
    def remove(self, id_client):
        '''
        remove a client
        input: id_client - int
        return: -
        '''
        self.__client_repository.remove(id_client)
        
    def search(self, name):
        '''
        search clients by name
        input: name - string
        return: Client type objects list
        '''
        clients = self.__client_repository.get_all()
        clients_found = []
        for client in clients:
            if name in client.name:
                clients_found.append(client)
        if len(clients_found) == 0:
            raise NameNotFoundError(f'There is no client named {name}!')
        return clients_found
    