{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAm I Beautiful?: Am I Beautiful?  (German: \"Bin ich schön?\" )  is a 1998 German comedy film directed by Doris Dörrie.\n\nNaked (2002 film): Naked (\"Nackt\" in German) is a German comedy film about the relationship problems of three young couples in Berlin, who meet for a dinner party which does not go well.  Released in 2002, it was directed by Doris Dörrie who also wrote the screenplay.\n\nMen...: Men… (German: \"Männer…\" ) is a 1985 West German comedy film directed by Doris Dörrie.  It was chosen as West Germany's official submission to the 59th Academy Awards for Best Foreign Language Film, but did not manage to receive a nomination.\n\nCherry Blossoms (film): Cherry Blossoms (German: \"Kirschblüten – Hanami\" ) is a 2008 German drama film directed by Doris Dörrie.  This film, starring Elmar Wepper, Hannelore Elsner and Aya Irizuki, tells the story of Rudi: terminally ill, he travels to Japan after the sudden death of his wife Trudi – in order to make up for missed opportunities in life.\n\nDoris Dörrie: Doris Dörrie (] ; born 26 May 1955) is a German film director, producer and author.\n\nThe Hairdresser: The Hairdresser (German: \"Die Friseuse\" ) is a 2010 German comedy film directed by Doris Dörrie.\n\nHal Ashby: Hal Ashby (September 2, 1929 – December 27, 1988) was an American film director and editor associated with the New Hollywood wave of filmmaking.\n\nPierre Sanoussi-Bliss: Pierre Sanoussi-Bliss (born 17 August 1962, Berlin-Mitte) is a German actor and director.  He has appeared in television and films for over 20 years.  He played a leading role in Doris Dörrie's 1994 film, \"Keiner liebt mich\".  He also plays a leading role in the comedy series \"Alles wird gut\".\n\nEnlightenment Guaranteed: Erleuchtung garantiert (\"Enlightenment Guaranteed\") is a 2000 German film directed by Doris Dörrie about two brothers, Uwe (Uwe Ochsenknecht) and Gustav (Gustav-Peter Wöhler), who travel to Japan to sort out the mess of their lives.  Their plan is to visit the Sojiji Monastery in Monzen, near Tokyo.  On their way there, in a rather literal Buddhist moment, they lose all of their belongings.  When they at last make it to the monastery, they find that even there, enlightenment can be elusive.\n\nThe Thing About Men: The Thing About Men is a musical with music by Jimmy Roberts and lyrics and book by Joe DiPietro.  It is based on the 1985 German film Men by Doris Dörrie.  The plot revolves around a love triangle and shows what men will do to keep their pride and love affairs intact.\n\nQuestion: Hal Ashby and Doris Dörrie, have which mutual occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the individuals being compared.\"\n    },\n    \"mutual_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The occupation shared by both individuals.\"\n    },\n    \"occupation_details\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"person_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the person.\"\n          },\n          \"occupations\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"All occupations listed for the person in the context.\"\n          }\n        },\n        \"required\": [\n          \"person_name\",\n          \"occupations\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Detailed list of occupations for each person.\"\n    }\n  },\n  \"required\": [\n    \"person_names\",\n    \"mutual_occupation\",\n    \"occupation_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the individuals being compared."
      },
      "mutual_occupation": {
        "type": "string",
        "description": "The occupation shared by both individuals."
      },
      "occupation_details": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "person_name": {
              "type": "string",
              "description": "The name of the person."
            },
            "occupations": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "All occupations listed for the person in the context."
            }
          },
          "required": [
            "person_name",
            "occupations"
          ],
          "additionalProperties": false
        },
        "description": "Detailed list of occupations for each person."
      }
    },
    "required": [
      "person_names",
      "mutual_occupation",
      "occupation_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
