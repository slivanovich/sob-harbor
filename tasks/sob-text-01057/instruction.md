{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCharly Charrier: Charly Charrier (born 27 May 1986) is a French footballer.  He currently plays for Amiens SC.  On 27 April 2012, he scored his first goal in Ligue 2 in a 1–0 win over CS Sedan Ardennes.  During the last 5 games of the 2011-2012 season, he scored 3 goals and added 2 assists, convincing his club to offer him a new 2-year-contract.\n\nWally Dieng: Wally Dieng (born November 17, 1973 in Paris, France) is a retired French footballer who played 8 matches in Ligue 1 for SM Caen in the period 1992–1994 and 13 matches in Ligue 2 for CS Sedan Ardennes in the 1994–1995 season.\n\nGroupe Caisse d'Épargne: Groupe Caisse d'épargne is a French semi-cooperative banking group, founded in 1818, with around 4700 branches in the country.  The group is active in retail and private banking, as well as holding a significant stake in the publicly traded investment bank Natixis.\n\nArnaud Monney: Arnaud Monney (born 18 September 1981) is an Ivorian football player who currently plays for CS Sedan Ardennes in France as defender.\n\nCS Sedan Ardennes: Club Sportif Sedan Ardennes, commonly referred to as CS Sedan or simply Sedan (] ), is a French association football club based in Sedan.  The club was formed in 1919 and plays its home matches at the Stade Louis Dugauguez located within the city.  The team is managed by Nicolas Usaï and captained by defender Damien Dufour.  Sedan is sponsored by Invicta France and Caisse d'Épargne, the latter being one of France's largest banks.  Macron are Sedan's current kit supplier.\n\nStade Émile Albeau: Stade Emile Albeau was a multi-use stadium in Sedan, France.  It was initially used as the stadium of CS Sedan Ardennes matches.  It was replaced by the current Stade Louis Dugauguez in 2000.  The capacity of the stadium was 17,000 spectators.\n\nStade Louis Dugauguez: Stade Louis Dugauguez is a multi-use stadium in Sedan, France.  It is currently used mostly for football matches and is the home stadium of CS Sedan Ardennes.  The stadium holds 23,189 people and was built in 2000.  It replaced Stade Emile Albeau.\n\nSébastien Cantini: Sébastien Cantini (born 31 July 1987) is a French professional football player who currently plays as a defender for amateur-side ES Fosséenne .  He started his career with CS Sedan Ardennes, and had a loan spell at Vannes OC during the 2010–11 season.\n\nStéphane Morisot: Morisot's previous clubs include FC Metz, Troyes AC, CS Sedan Ardennes, Dijon FCO and FC Rouen.\n\nMamadi Berthe: Mamadi Berthe (born 17 January 1983) is a Malian- French footballer.  As of 2003, he plays for Club Sportif Sedan Ardennes.\n\nQuestion: What banking group, founded in 1818, sponsors Club Sportive Sedan Ardennes?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"banking_group_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the banking group.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the banking group was founded.\"\n    },\n    \"sponsored_entity\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the entity being sponsored.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of entity being sponsored (e.g., 'football club').\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"relationship_type\": {\n      \"type\": \"string\",\n      \"description\": \"The nature of the relationship between the banking group and the entity (e.g., 'sponsor').\"\n    }\n  },\n  \"required\": [\n    \"banking_group_name\",\n    \"founding_year\",\n    \"sponsored_entity\",\n    \"relationship_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "banking_group_name": {
        "type": "string",
        "description": "The name of the banking group."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the banking group was founded."
      },
      "sponsored_entity": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity being sponsored."
          },
          "type": {
            "type": "string",
            "description": "The type of entity being sponsored (e.g., 'football club')."
          }
        },
        "required": [
          "name",
          "type"
        ],
        "additionalProperties": false
      },
      "relationship_type": {
        "type": "string",
        "description": "The nature of the relationship between the banking group and the entity (e.g., 'sponsor')."
      }
    },
    "required": [
      "banking_group_name",
      "founding_year",
      "sponsored_entity",
      "relationship_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
