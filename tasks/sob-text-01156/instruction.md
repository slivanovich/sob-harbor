{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMouchette: Mouchette (] ) is a 1967 French film directed by Robert Bresson, starring Nadine Nortier and Jean-Claude Guilbert.  It is based on the novel of the same name by Georges Bernanos.  It was entered into the 1967 Cannes Film Festival, winning the OCIC Award (International Catholic Organization for Cinema and Audiovisual).\n\nFrançois Leterrier: François Leterrier, born 26 May 1929 in Margny-lès-Compiègne, is a French film director and actor.  He entered the film industry when he was cast in Robert Bresson's film \"A Man Escaped\".  After this he went on to become a director himself.\n\nA Man Escaped: A Man Escaped or: The Wind Bloweth Where It Listeth (French: \"Un condamné à mort s'est échappé ou Le vent souffle où il veut\" ) is a 1956 French film directed by Robert Bresson.  It is based on the memoirs of André Devigny, a member of the French Resistance held in Montluc prison by the occupying Germans during World War II.  The protagonist of the film is called Fontaine.  The second part of the title comes from the Bible ( ) using the words of the Authorized King James Version (more recent translations use words like \"wants\" (which is the title in French) or \"pleases\" instead of \"listeth\").  Bresson himself was imprisoned by the Germans as a member of the French Resistance.\n\nL'Argent (1983 film): L'argent (] , meaning \"Money\") is a 1983 French drama film written and directed by Robert Bresson.  The film is loosely inspired by the first part of Leo Tolstoy's novella \"The Forged Coupon\".  It was Bresson's last film, and earned its maker the Director's Prize at the 1983 Cannes Film Festival.\n\nLes Dames du Bois de Boulogne: Les Dames du Bois de Boulogne (French for \"The Ladies of the Bois de Boulogne\") is a 1945 French film directed by Robert Bresson.  It is a modern adaptation of a section of Denis Diderot's \"Jacques le fataliste\" (1796) that tells the story of a man who is tricked into marrying a prostitute.\n\nRobert Bresson: Robert Bresson (] ; 25 September 1901 – 18 December 1999) was a French film director.  Known for his ascetic approach, Bresson contributed notably to the art of cinema; his non-professional actors, ellipses, and sparse use of scoring have led his works to be regarded as preeminent examples of minimalist film.\n\nDiary of a Country Priest: Diary of a Country Priest (French: \"Journal d'un curé de campagne\" ) is a 1951 French film written and directed by Robert Bresson, and starring Claude Laydu.  It was closely based on the novel of the same name by Georges Bernanos.  Published in 1936, the novel received the Grand prix du roman de l'Académie française.  It tells the story of a young, sickly priest, who has been assigned to his first parish, a village in northern France.\n\nAngels of Sin: Angels of Sin (original French title: \"Les anges du péché\") was the first feature film directed by Robert Bresson.  Made in 1943, nine years after his comedy short \"Affaires publiques\", it was Bresson's only film released during the German occupation of France.  Working titles included \"Bethany\", and Bresson's favored title \"The Exchange\", but producers felt these titles weren't sensational enough.\n\nPickpocket (film): Pickpocket is a 1959 French film directed by Robert Bresson, generally believed to have been inspired by the novel \"Crime and Punishment\" by Fyodor Dostoevsky.  It stars the young Uruguayan Martin LaSalle, who was a nonprofessional actor at the time, in the title role, with Marika Green as the ingénue.  It was the first film for which Bresson wrote an original screenplay rather than \"adapting it from an existing text.\"\n\nA Gentle Woman: A Gentle Woman (French: Une femme douce ) is a 1969 French drama film directed by Robert Bresson.  It is Bresson's first film in color, and adapted from Fyodor Dostoevsky's short story \"A Gentle Creature\" (Кроткая ).  The film is set in contemporary Paris.\n\nQuestion: What is the name of the 1956 French film directed by Robert Bresson, based on the memoirs of Andre Devigny and which starred Francois Leterrier in his debut role?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"source_material\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of source material (e.g., novel, memoirs).\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author or subject of the source material.\"\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"author\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"starring_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"role_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the actor's role or significance in the film (e.g., debut role).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director\",\n    \"release_year\",\n    \"source_material\",\n    \"starring_actor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "source_material": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of source material (e.g., novel, memoirs)."
          },
          "author": {
            "type": "string",
            "description": "The author or subject of the source material."
          }
        },
        "required": [
          "type",
          "author"
        ],
        "additionalProperties": false
      },
      "starring_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "role_description": {
            "type": "string",
            "description": "Description of the actor's role or significance in the film (e.g., debut role)."
          }
        },
        "required": [
          "name",
          "role_description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "director",
      "release_year",
      "source_material",
      "starring_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
