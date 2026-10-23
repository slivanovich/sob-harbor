{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNorthorpe railway station: Northorpe railway station was a railway station in Northorpe, Lincolnshire, England.  It opened on 2 April 1849 and closed on 4 July 1955.  Originally named \"Northorpe\", it became \"Northorpe (Lincs)\" at some point after January 1948.  Although the station is now closed, the signal box here remains in use to supervise a level crossing and passing loop on the single track section of the route between Gainsborough Central and Kirton Lindsey.\n\nGainsborough Central railway station: Gainsborough Central railway station is a railway station in the town of Gainsborough, Lincolnshire, England.  The town's other station is the busier Gainsborough Lea Road.  Until as recently as 2006, the station was shown to be one of the least busy in the country as trains only call there one day a week.\n\nBitragunta railway station: Bitragunta railway station (station code:BTTR) is an Indian Railway station located at Bitragunta town of Nellore district, in the Indian state of Andhra Pradesh.  It is under the administration of Vijayawada Railway Division of South Central Railway zone.  Bitragunta railway station have 2 platforms and 10 Halting Tracks.  Daily 2 trains Originating from here and 32 trains halt in this station.  It is 723rd busiest railway station in India.\n\nGainsborough station group: The Gainsborough station group is a small station group of two railway stations in Gainsborough, England consisting of Central and Lea Road.  The station group is printed on national rail tickets as GAINSBOROUGH STNS.\n\nHua Takhe Railway Station: Hua Takhe Railway Station is a railway station located in Lat Krabang Subdistrict, Lat Krabang District, Bangkok.  It is a class 1 railway station located 30.911 km from Bangkok Railway Station.  This station is the nearest station to Suvarnabhumi Airport, as well as the nearest large railway station to King Mongkut's Institute of Technology Ladkrabang.  However, the nearest railway station to KMITL is Phra Chom Klao halt, located only 580 m from Hua Takhe Station.  Hua Takhe is also the junction (although not officially one) for the freight-only line to the Inland Container Depot (ICD)\n\nNew Delhi railway station: The New Delhi Railway Station (station code NDLS), situated between Ajmeri Gate and Paharganj is the main railway station in Delhi.  It is the fourth busiest Railway Station in the country in terms of frequency of trains after Kanpur Central, Vijayawada Junction and Delhi Junction and most busiest Railway station in India in terms of passenger movement.  Around 185 trains starts, ends, or passes through the station daily and handles 500,000 passengers daily with 16 platforms.  The New Delhi railway station holds the record for the largest route interlocking system in the world along with the Kanpur Central Railway Station i.e. 48.  The station is about two kilometres north of Connaught Place, in central Delhi.\n\nCentral railway station, Sydney: The Central railway station is a railway station located at the southern end of the central business district in Sydney, New South Wales, Australia.  Often abbreviated as Central or Central station, the station is the largest and busiest railway station in New South Wales.  It services almost all of the lines on the Sydney Trains network, and is the major terminus for NSW TrainLink services.  Actual patronage was 11.35 million passenger movements in 2013.\n\nDharmabad railway station: Dharmabad railway station is a railway station belonging to Hyderabad railway division of South Central Railway.  The station is situated in Nanded district of Maharashtra, India.  Its station code is DAB.  The station is on a single track non-electrified broad gauge line.  There is a demand to transfer this railway station from South Central Railway zone to Central Railway zone.\n\nBihar Sharif Junction railway station: Bihar Sharif Junction railway station, station code BEHS, is a railway station and under Danapur railway division of East Central Railway.  Bihar sharif is connected to metropolitan areas of India, by the Delhi-Kolkata Main Line via Mugalsarai-Patna route.  Station is located in Bihar sharif city in Nalanda district in the Indian state of Bihar.  Due to its location on the Bakhtiyarpur-tilaiya main line many Patna and other cities via express trains coming from Rajgir and Gaya Junction stops here.  Bihar Sharif has well connected trains running frequently to New Delhi railway station, Patna Junction, Varanasi Junction railway station, and Howrah Junction railway station.  Bihar Sharif is well connected with Gaya Junction, Rajgir railway station, Tilaiya railway station, Bhagalpur railway station, and Kiul Junction through daily passenger and express train services.\n\nGainsborough Lea Road railway station: Gainsborough Lea Road railway station is one of two stations that serve the town of Gainsborough in Lincolnshire, England, the other station being Gainsborough Central, which is located in the town centre.  The station is managed by East Midlands Trains and is located 14.25 mi northwest of Lincoln Central on the A156 Lea Road in the south of the town.  The station opened in 1867 on a single line of the Great Northern Railway, who ran four trains a day from Gainsborough to Lincoln.\n\nQuestion: Where are the Gainsborough station group and the Gainsborough Central railway station located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the entities are located.\"\n        },\n        \"town\": {\n          \"type\": \"string\",\n          \"description\": \"The town where the entities are located.\"\n        }\n      },\n      \"required\": [\n        \"country\",\n        \"town\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"located_entities\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the railway entities whose location is being described.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"number_of_entities\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of entities whose location is being described.\"\n    }\n  },\n  \"required\": [\n    \"location\",\n    \"located_entities\",\n    \"number_of_entities\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "object",
        "properties": {
          "country": {
            "type": "string",
            "description": "The country where the entities are located."
          },
          "town": {
            "type": "string",
            "description": "The town where the entities are located."
          }
        },
        "required": [
          "country",
          "town"
        ],
        "additionalProperties": false
      },
      "located_entities": {
        "type": "array",
        "description": "A list of the railway entities whose location is being described.",
        "items": {
          "type": "string"
        }
      },
      "number_of_entities": {
        "type": "integer",
        "description": "The total number of entities whose location is being described."
      }
    },
    "required": [
      "location",
      "located_entities",
      "number_of_entities"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
