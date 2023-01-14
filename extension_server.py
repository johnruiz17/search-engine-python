"""
File: extension_server.py
---------------------
This starts a server! Go to http://localhost:8000 to enjoy it. Currently
the server only serves up the HTML. It does not search. Implement code in
the "TODO" parts of this file to make it work.
"""

# This imports the SimpleServer library
import SimpleServer

# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir

# To get the json.dumps function.
import json


# the directory of files to search over
DIRECTORY = 'bbcnews'
# perhaps you want to limit to only 10 responses per search.
MAX_RESPONSES_PER_REQUEST = 10


class SearchServer:
    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        # initializes index and file_titles as dictionaries, filenames as a list of files from DIRECTORY
        # runs create_index to create indexed data and update it in the self.index and self.file_titles dictionaries
        self.html = open('extension_client.html').read()
        self.index = {}
        self.file_titles = {}
        self.filenames = textfiles_in_dir(DIRECTORY)
        create_index(self.filenames, self.index, self.file_titles)


    # this is the server request callback function. You can't change its name or params!!!
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print(request)

        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            # gets user query, searches the query,
            # creates a list of dictionaries containing title and file for each matching result
            collection = []
            params = request.get_params()
            files = search(self.index, params['query'])

            for file in files:
                dictionary = {'title': self.file_titles[file], 'file': file}
                collection.append(dictionary)

            return json.dumps(collection, indent=2)


def main():
    # Make an instance of your Server
    handler = SearchServer()

    # Start the server to handle internet requests at http://localhost:8000
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
