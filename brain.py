import pymongo
from openai import OpenAI

# 1. Verbinding maken met "Brain"
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["the_brain"]
collection = db["embeddings"]

client_openai = OpenAI(api_key="sk-proj") 

def get_embedding(text):
    # Stap A: Zoek in de database
    query = {"name": text}
    result = collection.find_one(query)
    
    if result:
        print(f"'{text}' gevonden in het geheugen!")
        return result["vectors"]
    
    # Stap B: Niet gevonden? Haal op bij OpenAI
    print(f"'{text}' is nieuw. OpenAI raadplegen...")
    
    response = client_openai.embeddings.create(
        input=[text],
        model="text-embedding-3-small"
    )
    
    # We halen de vector op maar 'returnen' nog niet!
    vector = response.data[0].embedding
    
    # Stap C: Nu pas opslaan voor de volgende keer
    new_data = {"name": text, "vectors": vector}
    collection.insert_one(new_data)
    print(f"'{text}' opgeslagen in MongoDB.")
    
    return vector # Nu pas klaar!

# Test van de Opdracht
kenmerk = "vriendelijkheid"
vector_1 = get_embedding(kenmerk) # Deze gaat naar OpenAI en slaat op
vector_2 = get_embedding(kenmerk) # Deze komt direct uit MongoDB

# Test 1: Dit zou "OpenAI aanroepen..." moeten printen
print("Poging 1:")
get_embedding("vriendelijkheid")

# Test 2: Dit zou "gevonden in MongoDB" moeten printen
print("\nPoging 2:")
get_embedding("vriendelijkheid")