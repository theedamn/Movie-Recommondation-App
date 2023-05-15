
# Movie-Recommondation-App using AI Semantic Search

This project is a movie recommendation system that suggests movies based on user queries. It utilizes the Sentence Transformer model for encoding movie data into vectors and implements Pinecone Search, an approximate nearest neighbor search service, for efficient and accurate retrieval of movie recommendations.

## Features

- Semantic search: The system employs the Sentence Transformer model to encode movie data into vector representations. These vectors capture semantic information about the movies, enabling meaningful search and recommendation capabilities.

- Pinecone Search: Pinecone is used as a database to store and index the encoded vectors. It provides powerful search capabilities, allowing for fast and accurate retrieval of relevant movie recommendations.

- Local storage: The system stores the encoded vectors locally to ensure quick access and reduce latency during recommendation generation.

- GUI using PySimpleGUI: The user interface of the movie recommendation system is implemented using PySimpleGUI, a Python GUI framework. It provides an intuitive and user-friendly interface for users to input queries and receive movie recommendations.m


## Requirements

To run the movie recommendation system, the following dependencies are required:

- Python3
- PySimpleGUI 
- Sentence Transformer 
- Pinecone 
- Annoy
- Kaggle

```bash

pip install pinecone-client sentence-transformers kaggle annoy PySimpleGUI

```
This command will download all the Requirementsfor the Project
    
## Usage
1. Clone the repository:

```bash
git clone https://github.com/theedamn/Movie-Recommondation-App.git

```

2. Install the required dependencies as mentioned in the 'Requirements' section.

3. Run the GUI:
```bash
python3 GUI.py
```

4. The GUI window will appear, allowing you to input your movie query or preferences.

5. Upon submitting the query, the system will utilize the Sentence Transformer model and Pinecone Search to generate and display relevant movie recommendations.

## Demonstration

Here is the youtube link for the demonstration of the project

[![Watch the demonstration video](https://youtu.be/XptYA3fQBCU)


## Contributing

Contributions are always welcome!

Contributions to the movie recommendation system project are welcome! If you find any bugs, have feature requests, or would like to contribute enhancements, please open an issue or submit a pull request on the GitHub repository.


## Acknowledgements

 - [Sentence Transformer:-](https://pypi.org/project/sentence-transformers/) The Sentence Transformer library for encoding movie data into vectors.
 - [Pinecone:-](https://pinecone.io/)The Pinecone service for storing and searching encoded vectors.
 
 - [PySimpleGUI:-](https://pysimplegui.readthedocs.io/)The PySimpleGUI library for implementing the graphical user interface.
