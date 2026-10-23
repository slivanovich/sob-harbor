{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBrad Anderson (director): Brad Anderson (born 1964) is an American film director, producer and writer.  A director of thriller and horror films and television projects, he is best known for having directed \"The Machinist\" (2004), starring Christian Bale, and \"The Call\" (2013), starring Halle Berry.  He also produced and directed several installments of the FOX science fiction television series \"Fringe\".\n\nThe Last Horse Carriage in Berlin: The Last Horse Carriage in Berlin (German:Die letzte Droschke von Berlin) is a 1926 German silent comedy drama film directed by Carl Boese and starring Lupu Pick, Hedwig Wangel and Maly Delschaft.  The film's art direction was by Franz Schroedter.  The film premiered in Berlin on 18 March 1926.\n\nThe Uncle from America: The Uncle from America (German: Der Onkel aus Amerika) is a 1953 West German comedy film directed by Carl Boese and starring Hans Moser, Georg Thomalla and Joe Stöckel.  It was based on a play by Ferdinand Altenkirch which had previously been made into the 1932 film \"No Money Needed\".\n\nThe Golem: How He Came into the World: The Golem: How He Came into the World (German: Der Golem, wie er in die Welt kam , also referred to as The Golem) is a 1920 silent horror film co-directed by and starring Paul Wegener.  The picture was directed by Carl Boese and Wegener, written by Wegener and Henrik Galeen, and stars Wegener as the golem.  The film was the third of three films that Wegener made featuring the golem, the other two being \"The Golem\" (1915) and the short comedy \"The Golem and the Dancing Girl\" (1917), in which Wegener dons the Golem make-up in order to frighten a young lady he is infatuated with.  It is a prequel to \"The Golem\" and is the best known of the series, largely because it is the only one of the three films that has not been lost.  One of the early horror films, the film was sensational upon its release and has left a lasting legacy within the film industry, alongside another early German expressionist horror film, \"The Cabinet of Dr. Caligari\" (1920).\n\nMy Aunt, Your Aunt (1956 film): My Aunt, Your Aunt (German: Meine Tante, deine Tante) is a 1956 West German comedy crime film directed by Carl Boese and starring Theo Lingen, Hans Moser and Georg Thomalla.  Boese had previously made a 1939 film of the same title.\n\nBashful Felix: Bashful Felix or Felix is Right on Target (German: Schützenkönig wird der Felix) is a 1934 German comedy film directed by Carl Boese and starring Rudolf Platte, Ursula Grabley and Jakob Tiedtke.  It was made by Terra Film, with sets designed by art directors Robert A. Dietrich and Bruno Lutz.\n\nMy Aunt, Your Aunt (1939 film): My Aunt, Your Aunt (German: Meine Tante - deine Tante) is a 1939 German comedy film directed by Carl Boese and starring Ralph Arthur Roberts, Johannes Heesters and Olly Holzmann.  Boese later directed a 1956 film of the same title.\n\nWithout Meyer, No Celebration is Complete: Without Meyer, No Celebration is Complete (German: Keine Feier ohne Meyer) is a 1931 German comedy film directed by Carl Boese and starring Sig Arno, Ralph Arthur Roberts and Dina Gralla.  Boese made a number of films featuring Jewish comedians during the Weimar Era.\n\nGreetings and Kisses, Veronika: Greetings and Kisses, Veronika (German:Gruß und Kuß - Veronika) is a 1933 German comedy film directed by Carl Boese and starring Franciska Gaal, Paul Hörbiger and Otto Wallburg.  The film's art direction was by Kurt Dürnhöfer and Max Heilbronner.  The film's popularity made Gaal an international star.  However the rise of the Nazi Party to power meant that the Jewish Gaal had to make her next films in Hungary and Austria.\n\nCarl Boese: Carl Boese (] ; 26 August 1887 – 6 July 1958) was a German film director, screenwriter and producer.  He directed 158 films between 1917 and 1957.\n\nQuestion: Are Brad Anderson and Carl Boese both American film directors?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"are_both_american_directors\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both directors are American film directors, false otherwise.\"\n    },\n    \"director_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first director.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the first director.\"\n        },\n        \"is_film_director\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the first person is a film director.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"is_film_director\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second director.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the second director.\"\n        },\n        \"is_film_director\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the second person is a film director.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"is_film_director\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"are_both_american_directors\",\n    \"director_1\",\n    \"director_2\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "are_both_american_directors": {
        "type": "boolean",
        "description": "True if both directors are American film directors, false otherwise."
      },
      "director_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first director."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the first director."
          },
          "is_film_director": {
            "type": "boolean",
            "description": "True if the first person is a film director."
          }
        },
        "required": [
          "name",
          "nationality",
          "is_film_director"
        ],
        "additionalProperties": false
      },
      "director_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second director."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the second director."
          },
          "is_film_director": {
            "type": "boolean",
            "description": "True if the second person is a film director."
          }
        },
        "required": [
          "name",
          "nationality",
          "is_film_director"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "are_both_american_directors",
      "director_1",
      "director_2"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
