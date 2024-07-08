# README.md

## Install instructions
**NOTE:** faiss, installed through PyPi is only available for Linux/MacOs

1. Clone this repository
2. Install requirements `pip install -r requirements.txt`
3. **(OPTIONALLY)** Install [ollama](https://ollama.com/)
    - start ollama `ollama serve`
    - Pull a model `ollama pull llama3:latest`
    - Uncomment the section in `get_embedding()` using ollama
4. Start the API `fastapi run "recommendation engine.py"`


## Usage

Send a GET request to `http://localhost:8000/recommendations`

```json
{
    "name": "A pillow",
    "price": 20.00,
    "description": "A simple comfortable pillow."
}
```

Observe the recommendations (Using ollama with llama3)
```json
[
    {
        "name": "Travel Pillow",
        "price": 22.99,
        "description": "Memory foam travel pillow with ergonomic design for neck support."
    },
    {
        "name": "Electric Kettle",
        "price": 29.99,
        "description": "1.7-liter stainless steel electric kettle with auto shut-off."
    },
    {
        "name": "Yoga Mat",
        "price": 25.99,
        "description": "Eco-friendly, non-slip yoga mat with carrying strap."
    },
    {
        "name": "Electric Shaver",
        "price": 59.99,
        "description": "Rechargeable electric shaver with multi-flex head and pop-up trimmer."
    },
    {
        "name": "Wireless Mouse",
        "price": 14.99,
        "description": "Ergonomic wireless mouse with adjustable DPI."
    }
]
```