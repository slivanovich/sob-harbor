{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRoad Trip: A road trip is a journey on roads.  Road Trip, Road trip, or Roadtrip may also refer to:\n\nRoad Trip: The Arcade Edition: Road Trip: The Arcade Edition, known as Gadget Racers in Europe and Choro Q!  in Japan, is a racing video game released in 2002 by Takara.  This 3D game is only available for the Nintendo GameCube.  Road Trip: The Arcade Edition is based mainly upon Road Trip Adventure, a predecessor, however was only sold for the Gamecube.  Allowing this, weapons were added to a more racing perspective to make it an arcade version.  It involves tiny little toy cars known in real life as Choro-Q or Penny Racers.  There are many different modes in this game.  The game also include weapons such as machine guns and shot guns.\n\nBloquera: Bloquera is an EP created by Maanumental, Newman, Sir Kado, Superbrush 427 (Giant Panda) and Thes One (People Under The Stairs).  The group decided to take a spur of the moment road trip to Mexico as an ultimate road trip.  The album was a result of a two-week road trip to Mulegé, Baja California Sur, Mexico which was the inspiration for the album.\n\nTanana Valley State Fair: The Tanana Valley State Fair is an annual state fair held in College, Alaska, United States.  The event commences on the first Friday in August, and is a major annual event in Interior Alaska.  The fair is held on a hundred-acre plot of land just outside the city limits of Fairbanks, in the approximate center of College Road.  The fairgrounds, along with portions of the Creamer's Field Migratory Waterfowl Refuge and surrounding businesses on the north side of College Road, comprise the eastern reaches of the College census-designated place adjacent to Fairbanks.\n\nRoad Trip (Girl Authority album): Road Trip is the second and final album from American girl group Girl Authority.  Unlike the first album, \"Road Trip\" is a mixture of cover songs and original songs performed by Girl Authority.  \"Road Trip\" is also featured with a DVD, documenting a behind the scenes glance into the production of the album and the girls.\n\nCollege Road Trip: College Road Trip is a 2008 American family comedy film directed by Roger Kumble and starring Martin Lawrence, Raven-Symoné, Brenda Song, Margo Harshman, and Donny Osmond.  The film centers on college-bound teen Melanie Porter (Raven-Symoné), who goes on a road trip to different colleges with her father.  The film was released by Walt Disney Pictures in the United States on March 7, 2008.\n\nThe Castaway Cowboy: The Castaway Cowboy is a 1974 American adventure film released by Walt Disney Productions starring James Garner, Vera Miles, Eric Shea, and Robert Culp about a Texas rancher who gets shanghaied, then jumps ship and finds himself washed ashore in Hawaii.  Filmed on location in Hawaii, the movie was directed by Vincent McEveety and written by Don Tait and Richard M. Bluel.\n\nJonathan Drubner: Jonathan Scott Drubner (born June 15, 1972) is a stand up comedian, writer, and television personality.  He is the former host and producer for the ESPNU College Road Trip.  Drubner has also served as co-producer to head writer for the ESPY awards since 2005.  His work on the show earned him an Outstanding Original Music and Lyrics Emmy nomination in 2009 for the song \"I Love Sports,\" which was performed during the show.  In 2007 Drubner made a guest appearance on ABC College Football awards show as a photographer pranking college football stars.\n\nLaw College Road: Law College Road is one of the a major roads in Pune and is a residential locality.  It starts at Karve Road near Nal Stop Junction and ends at the National Cadet Corps ground near Bhandarkar Oriental Research Institute.  Original name of the road is \"Chiplunkar Road\" named after great Marathi writer of the 19th century.  However, with famous institutions like Film and Television Institute of India and ILS Law College, the road is also known as Film Institute Road and more popularly as Law College Road.  Other landmarks along this road are Film and Television Institute of India (FTII), National Film Archives and IndSearch.  It is surrounded on one side by Hanuman Tekdi and on the other side is a residential area called Prabhat Road.\n\nCollege Road drill hall, Hanley: The College Road drill hall is a former military installation at College Road (formerly Victoria Road) in Hanley, Stoke-on-Trent, Staffordshire.\n\nQuestion: What does College Road Trip and The Castaway Cowboy have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_type\": {\n      \"type\": \"string\",\n      \"description\": \"The primary common type of the two entities.\"\n    },\n    \"shared_attributes\": {\n      \"type\": \"array\",\n      \"description\": \"A list of other attributes shared by both entities.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"entities_compared\": {\n      \"type\": \"array\",\n      \"description\": \"The names of the entities being compared.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"common_type\",\n    \"shared_attributes\",\n    \"entities_compared\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_type": {
        "type": "string",
        "description": "The primary common type of the two entities."
      },
      "shared_attributes": {
        "type": "array",
        "description": "A list of other attributes shared by both entities.",
        "items": {
          "type": "string"
        }
      },
      "entities_compared": {
        "type": "array",
        "description": "The names of the entities being compared.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "common_type",
      "shared_attributes",
      "entities_compared"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
