{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDoug Benson: Douglas Steven \"Doug\" Benson (born July 2, 1962) is an American comedian, marijuana rights advocate, television host, actor and judge who has appeared on \"Getting Doug With High\", \"Comedy Central Presents\", \"Best Week Ever, Trailer Park Boys,\" and was a contestant on \"Last Comic Standing\" in the show's fifth season.  He currently serves as a judge for the Comedy Central series \"The High Court with Doug Benson\".\n\nPatrice O'Neal: Elephant in the Room: Elephant in the Room is a stand up special by comedian Patrice O'Neal, released by Comedy Central.  It premiered on February 19, 2011.  It is the comedian's only \"hour-length\" special and his first to be released on DVD or CD.  The DVD was released by Comedy Central on February 22, 2011.  Although the original televised version ran only 42 minutes (an hour with commercials), the full-length edit released on DVD and Netflix's streaming service runs at 77 minutes.  The DVD includes additional \"deleted scenes\" as well as O'Neal's 2003 \"Comedy Central Presents\", available on DVD for the first time.\n\nRené Hicks: René Hicks is an African American comedian and actress.  She has appeared on Comedy Central's \"Comedy Central Presents\" and in numerous college shows.  She was twice named NACA Comedy Entertainer of the Year, in 1995 and 1997.  Hicks is also a former accountant and former college athlete.  Her television credits include guest appearances on \"Hangin' with Mr. Cooper\" and \"Midnight Caller\".\n\nReno Collier: Reno Collier is a stand up comedian who gained celebrity as the opening act for Larry the Cable Guy and with his own Comedy Central Presents special.  He was also featured as a roaster for the Comedy Central Roast of Larry the Cable Guy.  Collier was featured on the Blue Collar Comedy Tour: The Next Generation.\n\nBret Ernst: Bret Ernst is an American stand-up comedian.  He was one of four comedians featured in Vince Vaughn's Wild West Comedy Show: 30 Days & 30 Nights - Hollywood to the Heartland, along with Ahmed Ahmed, John Caparulo, and Sebastian Maniscalco.  Ernst has also appeared on the television programs Comedy Central Presents and The Late Late Show with Craig Ferguson.  He appeared in the 2006 MTV wrestling show Wrestling Society X as a commentator.  Bret was the host of the first season of \"\".  He also appeared in Ke$ha's \"Blah Blah Blah\" music video.  His Comedy Central 1/2 hour special was voted \"TOP 5\" of all of 2010, and his first comedy album \"American Comic\" was an instant success, breaking \"TOP 10\" on iTunes in its first week.  Ernst is best known for his \"Roller Skating Bit.\"  He currently resides in Los Angeles.\n\nMegan Mooney: Megan Anne Mooney, (born 1974 in Houston, Texas) is an American stand-up comedian who has performed at the HBO Comedy Arts Festival and the Just For Laughs Comedy Festival in Montreal.  She has appeared on Comedy Central's \"Premium Blend\" and in 2006 her own \"Comedy Central Presents\" episode debuted.  Mooney transitioned from stand up comedy into television writing.  She wrote for the Nickelodeon game show revival of FIGURE IT OUT seasons five and six.  She also served as a consultant on Nickelodeon's Kids' Choice Awards in 2014, hosted by Mark Wahlberg.  And currently she's a regular contributor on Comedy Central's Tosh.0.  Mooney resides in Los Angeles with her husband Eddie Gossling and son Oliver and daughter Mia.\n\nZach Galifianakis: Zachary Knight Galifianakis ( ; born October 1, 1969) is an American actor, writer and comedian.  He came to prominence with his \"Comedy Central Presents\" special in 2001 and presented his own show called \"Late World with Zach\" on VH1 the following year.  He has also starred in films, such as \"The Hangover\" trilogy (2009–2013), \"Due Date\" (2010), \"The Campaign\" (2012), \"Birdman or (The Unexpected Virtue of Ignorance)\" (2014), \"Puss in Boots\" (2011), \"Masterminds\" (2016) and \"The Lego Batman Movie\" (2017).\n\nChris Porter (comedian): Chris Porter (c. 1979) is an American comedian and finalist on season 4 of \"Last Comic Standing\".  He has also appeared on The Bob & Tom Show, Comedy Central's \"Live Tour\", and appeared on Live at Gotham in Summer 2006.  In 2009, Porter made an appearance on Comedy Central Presents.  His 2014 comedy special \"Chris Porter: Ugly and Angry\" is available for streaming on Hulu.\n\nJeff Dunham: Jeffrey \"Jeff\" Dunham (born April 18, 1962) is an American ventriloquist and comedian who has also appeared on numerous television shows, including \"Late Show with David Letterman\", \"Comedy Central Presents\", \"The Tonight Show\" and \"Sonny With a Chance\".  He has six specials that run on Comedy Central: \"\", \"\", \"Jeff Dunham's Very Special Christmas Special\", \"\", \"\", and \"\".  Dunham also starred in \"The Jeff Dunham Show\", a series on the network in 2009.\n\nBelow (film): Below is a 2002 American World War II mystery horror film directed by David Twohy, written by Darren Aronofsky, Lucas Sussman, and Twohy, and stars Bruce Greenwood, Olivia Williams, Matthew Davis, Holt McCallany, Scott Foley, Zach Galifianakis, Jason Flemyng, and Dexter Fletcher.  The film tells the story of a United States Navy submarine that experiences a series of supernatural events while on patrol in the Atlantic Ocean in 1943.\n\nQuestion: When was the American actor, writer and comedian who was prominence with his \"Comedy Central Presents\" and also a star of Below 2002?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the American actor, writer, and comedian.\"\n    },\n    \"person_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of occupations held by the person.\"\n        },\n        \"prominence_event\": {\n          \"type\": \"string\",\n          \"description\": \"The event that brought the person to prominence.\"\n        },\n        \"film_appearance\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"film_title\": {\n              \"type\": \"string\",\n              \"description\": \"The title of the film the person starred in.\"\n            },\n            \"film_year\": {\n              \"type\": \"integer\",\n              \"description\": \"The release year of the film.\"\n            }\n          },\n          \"required\": [\n            \"film_title\",\n            \"film_year\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"occupations\",\n        \"prominence_event\",\n        \"film_appearance\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the person in 'Month Day, Year' format.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_details\",\n    \"birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the American actor, writer, and comedian."
      },
      "person_details": {
        "type": "object",
        "properties": {
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of occupations held by the person."
          },
          "prominence_event": {
            "type": "string",
            "description": "The event that brought the person to prominence."
          },
          "film_appearance": {
            "type": "object",
            "properties": {
              "film_title": {
                "type": "string",
                "description": "The title of the film the person starred in."
              },
              "film_year": {
                "type": "integer",
                "description": "The release year of the film."
              }
            },
            "required": [
              "film_title",
              "film_year"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "occupations",
          "prominence_event",
          "film_appearance"
        ],
        "additionalProperties": false
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the person in 'Month Day, Year' format."
      }
    },
    "required": [
      "person_name",
      "person_details",
      "birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
