{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVienna Opera Ball: The Vienna Opera Ball (German: \"Wiener Opernball\") is an annual Austrian society event which takes place in the building of the Vienna State Opera in Vienna, Austria on the Thursday preceding Ash Wednesday (a religious holiday).  Together with the New Year Concert, the ball is one of the highlights of the Viennese carnival season.\n\nVienna State Ballet: Vienna State Ballet, \"Wiener Staatsballett\", is considered one of the world´s top ballet companies.  It was formerly named the Vienna State Opera Ballet as it is based at the Vienna State Opera building.  In 2005 the ballets of the Vienna State Opera and the Vienna Volksoper were merged together under the name \"Das Ballett der Wiener Staatsoper und Volksoper\" and Gyula Harangozo became the artistic director.  The further name change, on September 1, 2010, was accompanied by a change in leadership.  Manuel Legris, a former principal dancer with the Paris Opera Ballet, succeeded as the artistic director.\n\nEno Peçi: Eno Peçi is an Albanian male ballet dancer, living in Austria.  Born in Tirana, he was educated at the Tirana Academy of Ballet and the Ballet School of the Vienna State Opera.  He joined the Vienna State Opera in 2000, becoming a soloist in 2003.  He is recognized as the first Albanian dancer to perform live in concert in Vienna.\n\nVienna State Opera: The Vienna State Opera (German: Wiener Staatsoper ) is an Austria opera house and opera company based in Vienna, Austria.  It was originally called the Vienna Court Opera (Wiener Hofoper).  In 1920, with the replacement of the Habsburg Monarchy by the First Austrian Republic, it was renamed the Vienna State Opera.  The members of the Vienna Philharmonic are recruited from its orchestra.\n\nOtto Edelmann: Otto Edelmann (February 5, 1917 in Vienna – May 14, 2003 in Vienna) was an Austrian bass.  He was born in Vienna and studied singing in Vienna with Gunnar Graarud.  His debut was at Gera as Figaro in Mozart's \"The Marriage of Figaro\".  He later sang the Vienna State Opera, the Edinburgh Festival and the Metropolitan Opera.  He sang at the Bayreuth Festival immediately after its reopening in 1951 after World War II, performing the role of Hans Sachs in Wagner's \"Die Meistersinger von Nürnberg\".  (He also recorded as Veit Pogner the goldsmith in the same work in one of Hans Knappertsbusch's early recorded performances.)  He also sang Ochs in Richard Strauss's \"Der Rosenkavalier\" at the first performances in the new Salzburg Festspielhaus in 1960.  In 1957, he recorded the role of Wotan opposite Kirsten Flagstad in Georg Solti's recording of Act III of Wagner's \"Die Walküre\" (an album made prior to the later famous complete set of \"Der Ring des Nibelungen\").  He died in Vienna.\n\nOpernball (novel): Opernball is a 1995 novel by Austrian writer Josef Haslinger in which thousands of people are killed in a Neo-Nazi terrorist attack taking place during the Vienna Opera Ball.  The novel was the basis of a 1998 made-for-TV movie by Urs Egger with the same title.\n\nOpernball (film): Opernball \"(Opera Ball)\" is a 1998 made-for-TV movie by Urs Egger based on a 1995 novel by Austrian writer Josef Haslinger in which thousands of people are killed in a Neo-Nazi terrorist attack taking place during the Vienna Opera Ball.  The film starred Heiner Lauterbach, Franka Potente, Frank Giering, Caroline Goodall, Richard Bohringer, Gudrun Landgrebe and Désirée Nosbusch.\n\nEsther Réthy: Esther Réthy (22 October 1912 – 28 January 2004) was a Hungarian operatic soprano who had a major career in Europe from 1934 through 1968.  She was notably a principal artist at the Vienna State Opera for over a decade and was a frequent performer at the Salzburg Festival.  She performed a broad opera repertoire that encompassed French, German, Italian, Czech, and Hungarian operas.  The latter part of her career was dedicated mainly to performing the German operetta literature at the Vienna Volksoper.  A very beautiful woman, she was a greatly admired Angele in Richard Heuberger’s \"Der Opernball\".\n\nMcCloy Viennese Ball: The McCloy Viennese Ball at Harvard University is an annual gala event at the Harvard Club of Boston jointly organized between the Harvard Club of Austria and the McCloy Fellows at Harvard Kennedy School.  The first ball was held in 1985 and as of 2016 it is one of two balls in North America co-sponsored by the City of Vienna.  Modeled on the Vienna Opera Ball, the McCloy Ball is an annual Austrian society event that draws a variety of diplomats, politicians, and business leaders.\n\nBudapest Opera Ball: The Budapest Opera Ball (\"Budapesti Operabál\" in Hungarian, \"Budapester Opernball\" in German) is an annual Hungarian society event taking place in the building of the Budapest Opera (\"Operaház\") on the last Saturday of the carnival season, usually late February.  On this occasion the stage and the auditorium of the Opera is transformed into a huge ballroom.  The dress code is evening dress: white tie and tails for men; floor-length gowns for women.  The ball is opened by more than a hundred debutante dancers after a show consisting of selected arias, followed by the 'Alles Walzer' with people dancing until dawn.  Recent star guests include Montserrat Caballé, Ornella Muti, Yevgeny Nesterenko, Walter Berry, Heinz Zednik, Katia Ricciarelli, Patrizio Buanne, Catherine Deneuve, Katarina Witt, Gina Lollobrigida, Daryl Hannah and Guy de Rothschild.  Besides international guests, the balls are highlighted by the most well known Hungarian opera singers.\n\nQuestion: What annual Austrian society event which takes place in the building of Vienna State Opera in Vienna was featured in the made-for-TV movie Opernball?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the annual Austrian society event.\"\n    },\n    \"event_description\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of the event's nature.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"building_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the building where the event takes place.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the event takes place.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the event takes place.\"\n        }\n      },\n      \"required\": [\n        \"building_name\",\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"featured_in_film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"film_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film in which the event was featured.\"\n        },\n        \"film_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of film (e.g., made-for-TV movie).\"\n        }\n      },\n      \"required\": [\n        \"film_title\",\n        \"film_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"event_description\",\n    \"location\",\n    \"featured_in_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the annual Austrian society event."
      },
      "event_description": {
        "type": "string",
        "description": "A brief description of the event's nature."
      },
      "location": {
        "type": "object",
        "properties": {
          "building_name": {
            "type": "string",
            "description": "The name of the building where the event takes place."
          },
          "city": {
            "type": "string",
            "description": "The city where the event takes place."
          },
          "country": {
            "type": "string",
            "description": "The country where the event takes place."
          }
        },
        "required": [
          "building_name",
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "featured_in_film": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the film in which the event was featured."
          },
          "film_type": {
            "type": "string",
            "description": "The type of film (e.g., made-for-TV movie)."
          }
        },
        "required": [
          "film_title",
          "film_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "event_name",
      "event_description",
      "location",
      "featured_in_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
