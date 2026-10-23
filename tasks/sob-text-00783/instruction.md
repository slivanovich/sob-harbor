{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWhat Never Dies: What Never Dies (French: Ce qui ne meurt pas ) is an 1884 novel by the French writer Jules Barbey d'Aurevilly.  It tells the story of the orphan Allan who falls in love with his protectress, Mme de Scudemot, who has become indifferent due to erotic excesses in her youth; Allan eventually marries his lover's daughter Camille, but has been smitten by the older woman's indifference.  The book is divided into two parts, where the first focuses on Allan and Mme de Scudemot and the second on Allan and Camille.\n\nThe Bewitched: The Bewitched (French: L'Ensorcelée ) is an 1852 novel by the French writer Jules Barbey d'Aurevilly.  The narrative is set in Normandy in the early 19th century.  It tells the story of a young woman, married to a farmer ruined by the French Revolution, who falls in love with a priest and commits suicide when the infatuation comes to nothing.  Her widowed husband then sets out to kill the priest out of jealousy.\n\nA Floating City: A Floating City, or sometimes translated The Floating City, (French: \"Une ville flottante\" ) is an adventure novel by French writer Jules Verne first published in 1871 in France.  At the time of its publication, the novel enjoyed a similar level of popularity as \"Around the World in Eighty Days\".  The first UK and US editions of the novel appeared in 1874.  Jules Férat provided the original illustrations for the novel.\n\nAsia Argento: Asia Argento [pronounced \"ah-see-ah ar-jen-toe] (born Aria Maria Vittoria Rossa Argento; 20 September 1975) is an Italian actress, singer, model, and director.  Argento is best known for the role of Yelena in the action film \"xXx\", the first installment in the \"xXx\" franchise.\n\nDon Giovanni (1970 film): Don Giovanni is a 1970 Italian comedy-drama film directed by Carmelo Bene.  The narrative follows how Don Giovanni tries to seduce a young woman who is manically searching for Christian icons.  The film is loosely based on Jules Barbey d'Aurevilly's short story \"The Greatest Love of Don Juan\", from the collection \"Les Diaboliques\".\n\nUne vieille maîtresse: Une vieille maîtresse (\"An old mistress\") is an 1851 novel by the French writer Jules Barbey d'Aurevilly.  It tells the story of a wayward dandy who falls in love with a young woman but is unable to fully leave his former mistress behind.  The book was published by Alexandre Cadot in three volumes, with 327, 316 and 341 pages respectively.\n\nThe Mother of Tears: The Mother of Tears (Italian: \"La Terza madre\" , literally \"The Third Mother\") is a 2007 supernatural horror film written and directed by Dario Argento.  The film stars Asia Argento, Daria Nicolodi, Moran Atias, Udo Kier, and Coralina Cataldi-Tassoni.  The film has also been billed in English-speaking media as \"Mater Lachrymarum\", \"The Third Mother\" (English translation of the film's original Italian title), and \"Mother of Tears: The Third Mother\".  Written by Argento, Jace Anderson, Walter Fasano, Adam Gierasch and Simona Simonetti, the film is the concluding installment of Argento's supernatural horror trilogy \"The Three Mothers\", which began with \"Suspiria\" in 1977.  The film depicts the confrontation with the final \"Mother\" witch, known as Mater Lachrymarum.\n\nOn Dandyism and George Brummell: On Dandyism and George Brummell (French: Du dandysme et de George Brummell ) is a 1845 biographical essay by the French writer Jules Barbey d'Aurevilly.  It has also been published in English as Of Dandyism and of George Brummell and The Anatomy of Dandyism.  It uses the English fashion icon Beau Brummell (1778–1840) as the starting point for a discussion on dandyism.  The book is dedicated to the author's friend César Daly.\n\nThe Story Without a Name (novel): The Story Without a Name (French: Une histoire sans nom ) is an 1882 novel by the French writer Jules Barbey d'Aurevilly.  It tells the story of an inexplicable pregnancy and the destructive consequences it has for its surroundings.\n\nThe Last Mistress: The Last Mistress (French: \"Une vieille maîtresse\" , literally \"An old mistress\") is a 2007 French-Italian film based on the novel \"Une vieille maîtresse\" by the French writer Jules Barbey d'Aurevilly.  It stars Asia Argento and Fu'ad Aït Aattou as the two main characters.  The movie was directed by the French filmmaker Catherine Breillat and was entered into the 2007 Cannes Film Festival.\n\nQuestion: The Last Mistress, is a French-Italian film, released in what year, based on the novel \"Une vieille maîtresse\" by the French writer Jules Barbey d'Aurevilly, it stars Asia Argento, an Italian actress, singer, model, and director?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"film_origin\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The countries of origin for the film.\"\n    },\n    \"based_on_novel\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"novel_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the novel the film is based on.\"\n        },\n        \"novel_author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the novel.\"\n        }\n      },\n      \"required\": [\n        \"novel_title\",\n        \"novel_author\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"main_actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actress_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the main actress mentioned.\"\n        },\n        \"actress_nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actress.\"\n        },\n        \"actress_professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions of the actress.\"\n        }\n      },\n      \"required\": [\n        \"actress_name\",\n        \"actress_nationality\",\n        \"actress_professions\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"film_origin\",\n    \"based_on_novel\",\n    \"main_actress\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "film_origin": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The countries of origin for the film."
      },
      "based_on_novel": {
        "type": "object",
        "properties": {
          "novel_title": {
            "type": "string",
            "description": "The title of the novel the film is based on."
          },
          "novel_author": {
            "type": "string",
            "description": "The author of the novel."
          }
        },
        "required": [
          "novel_title",
          "novel_author"
        ],
        "additionalProperties": false
      },
      "main_actress": {
        "type": "object",
        "properties": {
          "actress_name": {
            "type": "string",
            "description": "The name of the main actress mentioned."
          },
          "actress_nationality": {
            "type": "string",
            "description": "The nationality of the actress."
          },
          "actress_professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions of the actress."
          }
        },
        "required": [
          "actress_name",
          "actress_nationality",
          "actress_professions"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "film_origin",
      "based_on_novel",
      "main_actress"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
