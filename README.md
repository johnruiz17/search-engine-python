## Python Search Engine
<img width="872" alt="Screenshot 2024-08-05 at 4 05 00 PM" src="https://github.com/user-attachments/assets/7902cc1b-581e-4a4e-a698-d2b761582cd9">

## Description
The search engine utilizes an inverted index to efficiently map keywords to their corresponding BBC News article text files. Users can leverage this tool to search for specific terms and retrieve all articles containing those terms. <br>

This project provides a search engine for BBC News articles along with two functionalities:

* **Command-Line Search:** Search the BBC News article database for articles containing your specified keywords directly from the terminal.
* **Web-based Search Interface:** Search the BBC News article database through a user-friendly web interface hosted locally on your machine.

## Technologies Used
* Python 3
* http.server module (for web server functionality)

## Installation
1. Download Python: Visit the official Python website (https://www.python.org/downloads/) and download the latest Python version compatible with your operating system (Windows, macOS, or Linux).

2. Open a terminal or command prompt and run the following command to display the installed Python version:
```bash
python --version
```

## Usage
**Option 1: Command-Line Search (searchengine.py):**

1. Save the provided code files (including searchengine.py and any others) in the same directory.

2. Open a terminal or command prompt and navigate to the directory where you saved the files.

3. Run the program with the following command, specifying the search term and desired sorting option (optional):

```bash
python3 searchengine.py <search_term> [-s]
```
* <search_term>: The keyword(s) you want to search for in the BBC News articles.
* -s (optional): This flag sorts the search results by article publication date (most recent first). By default, results are not sorted.

**Option 2: Web-based Search Interface (extension_server.py):**

1. Save the provided code files (including extension_server.py and any others) in the same directory.

2. Open a terminal or command prompt and navigate to the directory where you saved the files.

3. Run the program with the following command to launch the web server:
```bash
python3 extension_server.py
```

4. Open a web browser and visit http://localhost:8000 in the address bar.

5. Enter your search query in the search bar and click "Search."

6. The webpage will display all BBC News articles containing your search term.

**Note:** The web interface is accessible only on your local machine at http://localhost:8000 while the server is running.
