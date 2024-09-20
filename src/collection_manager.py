from chromadb import Client


chromadb_client = Client()


def get_collection(collection_name):
    """Retrieve/create the collection in the ChromaDB client."""
    try:
        collection = chromadb_client.get_collection(collection_name)
    except Exception:
        collection = chromadb_client.create_collection(collection_name)
    return collection


def add_to_collection(collection, car_problems):
    """Add car problems to the collection."""
    documents = []
    metadatas = []
    ids = []

    for problem in car_problems:
        documents.append(format_car_problem(problem))
        metadatas.append({"source": problem["source"]})
        ids.append(problem["error_code"])

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )


def format_car_problem(problem):
    """Format a car problem into a structured string."""
    return f"""
    Error Code: {problem['error_code']}
    {problem['description']}
    Description: {problem['details']}
    Causes:
    - {'\n- '.join(problem['causes'])}
    Solutions:
    - {'\n- '.join(problem['solutions'])}
    """
