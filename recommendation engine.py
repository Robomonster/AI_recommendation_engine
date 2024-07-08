# Demo implementation of a simple recommendation engine using text embeddings and faiss for vector storage & searching.
# Obviously many parts of this implementation would be changed in a production environment. This provides a simple interface for querying embeddings to get recommendations.

from fastapi import FastAPI
import faiss
from langchain_community.embeddings import FakeEmbeddings
import requests
from pydantic import BaseModel
import numpy as np
import json

DIMENSIONS = 4096

class Product(BaseModel):
    name: str
    price: float
    description: str

index = faiss.IndexFlatL2(DIMENSIONS)
random_embeddings = FakeEmbeddings(size=DIMENSIONS)

with open('products.json', 'r') as products_file:
    products = json.load(products_file)
    product_strings = [str(p) for p in products]


def get_embedding(text: str):
    """
    Uses a local instance of ollama to get embeddings for a given string.

    Raises an Exception if the status code is not ok (2xx).

    returns a list as the vector
    """
    # Use a local ollama instance to get the vector
    # response = requests.post('http://localhost:11434/api/embeddings', json={
    #     'model': 'llama3:latest',
    #     'prompt': text
    # })
    
    # if not response.ok:
    #     raise Exception(f'Response is not ok: {response.status_code}, {response.text}')
    
    # return response.json()['embedding']

    # Use random embeddings for fast demonstrations
    return random_embeddings.embed_query(text)


def query_index(product: str):
    search = get_embedding(product)
    search = np.array([search], dtype='float32')
    n_results = 5
    distances, indices = index.search(search, n_results)
    return np.array(products)[indices[0]]


print('generating embeddings (This might take a while)')
embeddings_list = [get_embedding(product_string) for product_string in product_strings]
embeddings_list = np.array(embeddings_list, dtype='float32')
index.add(embeddings_list)


app = FastAPI()


@app.get("/recommendations")
def add_items(item: Product):
    """
    Gets n best recommendations for the given product.
    """
    return list(query_index(str(item.model_dump())))

