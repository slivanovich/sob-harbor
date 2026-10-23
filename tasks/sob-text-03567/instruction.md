{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHôtel de Boisgelin (Rue de Varenne, Paris): The Hôtel de Boisgelin, a.k.a. Hôtel de La Rochefoucauld-Doudeauville, is a hôtel particulier in Paris, France.  It houses the Italian embassy in France.\n\nJean Baptiste Androuet du Cerceau: Jean Baptiste Androuet du Cerceau (1544/47–1590) was a French architect who designed the Pont Neuf (1579), spanning the Seine, Paris, and became supervisor of the royal works under Henri III and Henri IV, including the Louvre.  Several \"hôtels particuliers\" are ascribed to him.  The Hôtel d'Angoulême, the Hôtel de Lamoignon (1584), which houses the Historical Library of the City of Paris, and the Hôtel de Mayenne (rue St-Antoine in the Marais).  The Hôtel de Mayenne, with rhythmically varied dormer windows set in a high slate roof, has the pediments of its piano nobile windows superposed on the frieze above.\n\nLes Ambassadeurs (restaurant): Les Ambassadeurs was a restaurant in Paris, France.  It closed on March 31, 2013, due to renovations of the Hôtel de Crillon.  The hotel will reopen in 2015.\n\nPlace de la Concorde: The Place de la Concorde (] ) is one of the major public squares in Paris, France.  Measuring 8.64 ha in area, it is the largest square in the French capital.  It is located in the city's eighth arrondissement, at the eastern end of the Champs-Élysées.  It was the site of many notable public executions of royalty during the French Revolution.\n\n7th Lumières Awards: The 7th Lumières Awards ceremony, presented by the Académie des Lumières, was held on 25 February 2002.  The winners were announced at a press conference at the Hôtel de Crillon in Paris. \" Amélie\" won three awards including Best Film, Best Actress and Best Screenplay.\n\nHôtel de la Marine: The hôtel de la Marine (also known as the hôtel du Garde-Meuble) is a building on place de la Concorde in Paris, to the east of Rue Royale.  It was built between 1757 and 1774 on what was then known as \"place Louis XV\", with a façade by Ange-Jacques Gabriel, Premier architecte du Roi and designer of the square.  The identical building to its west now houses the Hôtel de Crillon.\n\nBazar de l'Hôtel de Ville: The Bazar de l'Hôtel de Ville or BHV is a department store on rue de Rivoli in the 4th arrondissement of Paris, facing the Hôtel de Ville.  It is part of the Groupe Galeries Lafayette and served by the Metro station \"Hôtel de Ville\".  It occupies four other smaller specialized stores, in the neighborhood, and has also opened several other shops in France and in Beirut, Lebanon.  BHV currently operates several stores in the Paris metropolitan area and two in the Lyon metropolitan area.\n\nLa Force Prison: La Force Prison was a French prison located in the Rue du Roi de Sicile, in what is now the 4th arrondissement of Paris.  Originally known as the Hôtel de la Force, the buildings formed the private residence of Henri-Jacques Nompar de Caumont, duc de la Force.  Towards the end of the reign of Louis XIV, the Hôtel de la Force was divided into two parts, one of which took the name of the Hôtel de Brienne, and had its entrance in the Rue Pavée; the other retained its former name and had its entrance in the Rue du Roi de Sicile.\n\nHôtel de Crillon: The Hôtel de Crillon in Paris is a historic luxury hotel that opened in 1909 — in a building dating to 1758.  Located at the foot of the Champs-Élysées, the Crillon along with the Hotel de la Marine is one of two identical stone palaces on the Place de la Concorde.  With 124 guest rooms and 46 suites, ranging in price from USD $1,350 to USD $15,000 per night.  the facility also features three restaurants, a bar, outdoor terrace, gym and health club on the premises.\n\nHôtel de Rambouillet: The Hôtel de Rambouillet was the Paris residence of Catherine de Vivonne, marquise de Rambouillet, \"Madame de Rambouillet\", who ran a renowned literary salon there from 1620 until 1648.  Formerly the Hôtel de Pisani, it was situated in the \"rue Saint-Thomas-du-Louvre\", in a former quarter of Paris (demolished at the beginning of the 19th century) between the Louvre and Tuileries palaces, near the then much smaller \"Place du Carrousel\", in the area of what was to become the \"Pavillon Turgot\" of the Louvre Museum.  (This Hôtel de Rambouillet, formerly Hôtel de Pisani, should not be confused with the one by same name situated on \"Rue Saint-Honoré\", which belonged to the d'Angennes family who sold it in December 1602, and on which site Cardinal Richelieu began building his Palais-Cardinal in 1624.)\n\nQuestion: The Hôtel de Crillon is located on what major public square in Paris?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"hotel_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the hotel.\"\n    },\n    \"location_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of location where the hotel is situated.\"\n    },\n    \"location_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific location.\"\n    },\n    \"city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the hotel is located.\"\n    },\n    \"is_major_public_square\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the location is a major public square.\"\n    }\n  },\n  \"required\": [\n    \"hotel_name\",\n    \"location_type\",\n    \"location_name\",\n    \"city\",\n    \"is_major_public_square\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "hotel_name": {
        "type": "string",
        "description": "The name of the hotel."
      },
      "location_type": {
        "type": "string",
        "description": "The type of location where the hotel is situated."
      },
      "location_name": {
        "type": "string",
        "description": "The name of the specific location."
      },
      "city": {
        "type": "string",
        "description": "The city where the hotel is located."
      },
      "is_major_public_square": {
        "type": "boolean",
        "description": "Indicates if the location is a major public square."
      }
    },
    "required": [
      "hotel_name",
      "location_type",
      "location_name",
      "city",
      "is_major_public_square"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
