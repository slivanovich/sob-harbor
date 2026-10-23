{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJean-Michel Basquiat: Jean-Michel Basquiat (] ; December 22, 1960 – August 12, 1988) was an American artist.  Basquiat first achieved fame as part of SAMO©, an informal graffiti duo who wrote enigmatic epigrams in the cultural hotbed of the Lower East Side of Manhattan during the late 1970s where the hip hop, post-punk, and street art movements had coalesced.  By the 1980s, he was exhibiting his neo-expressionist paintings in galleries and museums internationally.  The Whitney Museum of American Art held a retrospective of his art in 1992.\n\nSAMO: SAMO is a graffiti tag used on the streets of New York City from 1977 to early 1980.  It accompanied short phrases, in turns poetic and sarcastic, mainly painted on the streets of downtown Manhattan.\n\nLower Manhattan: Lower Manhattan, also known as Downtown Manhattan, is the southernmost part of Manhattan, the central borough for business, culture, and government in the City of New York, which itself originated at the southern tip of Manhattan Island in 1624.\n\nGiacomo Dondoli: Giacomo Dondoli (active 17th -18th century) was an Italian painter active in Verona.  He studied in Verona initially under Giovanni Battista Zannoni, then under Cavalier Coppa, and then Pietro Ricchi (il Lucchese) in Trento.  He painted for the Duke Carlo of Mantua.  He mainly painted sacred subjects including a \"San Carlo\" for the church of the Ghiara in Verona; a \"Last Supper\" for San Fermo; a \"Death of Sant'Alessio\" for the church of the same name.  He painted \"Nero watching Rome Burn\" and \"Story of Jacob\".  He was active in Verona circa 1717.\n\nSantos Party House: Santos Party House was a New York City nightclub located at 96 Lafayette Street between Walker and White Streets in the TriBeCa neighborhood of downtown Manhattan.  Originally named the \"Lafayette Street Jungle Gym\", Santos Party House was recognized as the \"Best New Nightclub\" by \"Paper\" magazine's Annual Nightlife Awards, and has also won awards for its parties, sound system, lighting, and dance floor.\n\nDoctors Hospital (Manhattan): Doctors Hospital was a hospital located at 170 East End Avenue, between 87th and 88th Streets opposite Gracie Mansion in the Yorkville neighborhood of Manhattan.  It served as the primary maternity hospital for uptown Manhattan births (Manhattan General served as such for downtown Manhattan).  It was also known as a \"fashionable treatment center for the well-to-do.\"\n\nAll Saint's Episcopal Day School: All Saints Episcopal Day School is an interdenominational school that has been serving more than 250 students from all faiths in Nursery through Eighth Grade since 1985.  The school is located in Hoboken, New Jersey, a small urban community in Northeast New Jersey, and is just minutes from downtown Manhattan, New York.  The school occupies two campuses: the Elementary school and Middle school which is located at 707 Washington St., on the corner of 7th and Washington Streets, and houses Grades 1-8, and the Early Learning Center, which is located at 527 Clinton St. on the corner of Sixth and Clinton Streets, houses the Nursery, Pre-Kindergarten and Kindergarten programs.  Both campuses boast historic landmark buildings, and include a gymnasium, movement room, library, science lab, art room, assembly space in the church, and private outdoor play yards.  There are SMART Boards in all classrooms and networked computers throughout all of the buildings.\n\nBenedetto Zallone: Benedetto Zallone, or also called Zalone da Cento, (1595-1644) was an Italian painter of the Baroque period.  He mainly painted religious subjects.  He was born in Pieve di Cento.  He was a pupil of Guercino.  He worked in Rome and Cento.  His name of Zalone was attributed to his appearance.  In Cento, he painted a \"St Matthew and the Virgin\" for the church of San Agostino and \"St Gregory with Saints\" for San Pietro.  Some of his works are now collected in the Pinacoteca of Pieve di Cento.\n\nMargareta Capsia: Margareta Capsia (1682 – June 20, 1759) was a Swedish/Finnish artist, the first professional native female artist in Finland, which during her lifetime was a part of Sweden.  She mainly painted altarpieces, but was also active as a portrait painter.\n\n28 Liberty Street: 28 Liberty Street, formerly known as One Chase Manhattan Plaza, is a banking skyscraper located in the downtown Manhattan Financial District of New York City, between Pine, Liberty, Nassau, and William Streets.  Construction on the building was completed in 1961.  It has 60 floors, with 5 basement floors, and is 248 meters (813 ft) tall, making it the 15th tallest building in New York City, the 43rd tallest in the United States, and the 200th tallest building in the world.\n\nQuestion: What is the name of the American artist who was part of a duo that mainly painted on the streets of downtown Manhattan?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American artist.\"\n    },\n    \"duo_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the graffiti duo the artist was part of.\"\n    },\n    \"art_form\": {\n      \"type\": \"string\",\n      \"description\": \"The type of art created by the duo.\"\n    },\n    \"primary_painting_location\": {\n      \"type\": \"string\",\n      \"description\": \"The main area where the duo painted their art.\"\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"duo_name\",\n    \"art_form\",\n    \"primary_painting_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the American artist."
      },
      "duo_name": {
        "type": "string",
        "description": "The name of the graffiti duo the artist was part of."
      },
      "art_form": {
        "type": "string",
        "description": "The type of art created by the duo."
      },
      "primary_painting_location": {
        "type": "string",
        "description": "The main area where the duo painted their art."
      }
    },
    "required": [
      "artist_name",
      "duo_name",
      "art_form",
      "primary_painting_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
