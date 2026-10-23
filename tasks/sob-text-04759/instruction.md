{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDalberg: Dalberg is the name of an ancient and distinguished German noble family, derived from the hamlet and castle (now in ruins) of Dalberg or Dalburg near Kreuznach in Rhineland-Palatinate.  In the 14th century the original house of Dalberg became extinct in the male line, the fiefs passing to Johann Gerhard, chamberlain of the see of Worms, who married the heiress of his cousin, Anton of Dalberg, about 1330.  His own family was of great antiquity, his ancestors having been hereditary ministerials of the bishop of Worms since the time of Ekbert the chamberlain, who founded in 1119 the Augustinian monastery of Frankenthal and died in 1132.  By the mid 15th century the Dalberg family had grown to be of such importance that, in 1494, the German King Maximilian I granted them the honor of being the first to receive knighthood at the coronation; this part of the ceremonies being opened by the herald asking in a loud voice \"Ist kein Dalberg da?\"  (\"Is no Dalberg present?\") .  This picturesque privilege the family enjoyed till the end of the Holy Roman Empire.  The elder line of the family of Dalberg-Dalberg became extinct in 1848, the younger, that of Dalberg-Herrnsheim, in 1833.  The male line of the Dalbergs is now represented only by the family of Hessloch, descended from Gerhard of Dalberg (c. 1239), which in 1809 succeeded to the title and estates in Moravia and Bohemia of the extinct counts of Ostein.\n\nOrder of Merit of the Italian Republic: The Order of Merit of the Italian Republic (Italian: \"Ordine al merito della Repubblica Italiana\" ) was founded as the senior order of knighthood by the second President of the Italian Republic, Luigi Einaudi in 1951.  The highest ranking honour of the Republic, it is awarded for \"merit acquired by the nation\" in the fields of literature, the arts, economy, public service, and social, philanthropic and humanitarian activities and for long and conspicuous service in civilian and military careers.  The post-nominal letters for the order are OMRI.  The order effectively replaced as national orders the Civil Order of Savoy (1831), the Order of the Crown of Italy (1868), the Order of Saints Maurice and Lazarus (1572) and the Supreme Order of the Most Holy Annunciation (1362).\n\nWhat You See Is What You Get (book): What You See Is What You Get is the autobiography of British businessman and TV personality Lord Alan Sugar.  The 640-page book, which was published in May 2011, tells the story of Alan Sugar's birth and childhood in a deprived part of London, how he founded the company Amstrad aged just 21 years old, and how he eventually became a successful multi-millionaire tycoon, received a knighthood, and was appointed to the House of Lords.  Sir Alan also reveals his main method of business and entrepreneurial activity: (a) observing what market leaders are doing, (b) making better and cheaper products than the market leaders, and (c) not focusing on the exclusive or more expensive parts of the market, rather selling to the mass market.\n\nGino Cassinis: Gino Cassinis (27 January 1885 – 13 January 1964) was an Italian Democratic Socialist Party politician.  He was born in Milan.  He was mayor of Milan.  He was knight grand cross and grand officer of the Order of Merit of the Italian Republic.  He died in Rome.\n\nOrder of Saint Stanislaus (House of Romanov): The Order of Saint Stanislaus (Polish: Order św.  Stanisława, Russian: Орденъ Св.  Станислава), also spelled Stanislas, is a Russian dynastic order of knighthood founded as \"Order of the Knights of Saint Stanislaus, Bishop and Martyr\" in 1765 by King Stanisław II Augustus of the Polish-Lithuanian Commonwealth.  In 1831 after the downfall of the November Uprising, the order was incorporated into the Chapter of Russian Orders as part of the honours system of the Russian Empire by Emperor Nicholas I of Russia.\n\nQuestion: Who founded the knighthood in which Gino Cassinis was part of?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"founder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who founded the knighthood order.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the founder at the time of the order's establishment.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"knighthood_order\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the knighthood order.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the knighthood order was founded.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founding_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"recipient_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was part of this knighthood order.\"\n    }\n  },\n  \"required\": [\n    \"founder_details\",\n    \"knighthood_order\",\n    \"recipient_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "founder_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who founded the knighthood order."
          },
          "role": {
            "type": "string",
            "description": "The role of the founder at the time of the order's establishment."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "knighthood_order": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the knighthood order."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the knighthood order was founded."
          }
        },
        "required": [
          "name",
          "founding_year"
        ],
        "additionalProperties": false
      },
      "recipient_name": {
        "type": "string",
        "description": "The name of the person who was part of this knighthood order."
      }
    },
    "required": [
      "founder_details",
      "knighthood_order",
      "recipient_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
