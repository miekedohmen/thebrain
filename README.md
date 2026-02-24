Dit project implementeert een slim "geheugen" voor vector embeddings. Het voorkomt dubbele API-kosten door embeddings van OpenAI op te slaan in een lokale MongoDB database.

De kern van de logica zit in de functie get_embedding(text)
1. Er wordt gezocht in de collectie embeddings binnen de database the_brain.
2. Indien gevonden, wordt de vector direct uit MongoDB teruggegeven.
3. Indien niet gevonden, haalt de OpenAI client een nieuwe embedding op en slaat deze op in de database.

### Toekomstige Uitbreidingen
- Cosine Similarity: Integratie van een rekenmodule om de gelijkenis tussen opgeslagen embeddings te berekenen
- Bulk import: mogelijkheid om grote lijsten met kenmerken in een keer te verwerken en op te slaan.
