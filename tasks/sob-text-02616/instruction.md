{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDubbel: The term dubbel (also double) is a Belgian Trappist beer naming convention.  The origin of the dubbel was a strong version of a brown beer brewed in Westmalle Abbey in 1856, which is known to have been on sale to the public by June 1861.  In 1926, the recipe was changed, and it was sold as \"Dubbel Bruin\".  Following World War Two, abbey beers became popular in Belgium and the name \"dubbel\" was used by several breweries for commercial purposes.\n\nTrappist beer: Trappist beer is a beer brewed by Trappist breweries.  Eleven monasteries — six in Belgium, two in the Netherlands and one each in Austria, Italy and United States — currently brew beer and sell it as \"Authentic Trappist Product\".\n\nLeszynski naming convention: The Leszynski naming convention (or LNC) is a variant of Hungarian notation popularized by consultant Stan Leszynski specifically for use with Microsoft Access development.  Although the naming convention is nowadays often used within the Microsoft Access community, and is the standard in Visual Basic programming, it is not widely used elsewhere.\n\nBurgasko: Burgasko is a light Bulgarian beer originally made in the seaside city of Burgas (Bulgarian: Бургаско пиво ).  It was established in 1971, in 1995 was bought by Kamenitza, and is currently brewed at the Astika Brewery in Haskovo.  It is owned by parent company Molson Coors.  It is a light beer with 4.4% ABV and is sold in central and eastern Bulgaria.\n\nExoplanet naming convention: The exoplanet naming convention is an extension of the system used for naming multiple-star systems as adopted by the International Astronomical Union (IAU).  For exoplanets orbiting a single star, the name is normally formed by taking the name of its parent star and adding a lowercase letter.  A provisional IAU-sanctioned standard exists to accommodate the naming of circumbinary planets.  A limited number of exoplanets have IAU-sanctioned proper names.  Other naming systems exist.\n\nHungarian notation: Hungarian notation is an identifier naming convention in computer programming, in which the name of a variable or function indicates its intention or kind, and in some dialects its type.  The original Hungarian Notation uses intention or kind in its naming convention and is sometimes called Apps Hungarian as it became popular in the Microsoft Apps division in the development of Word, Excel and other apps.  As the Microsoft Windows division adopted the naming convention, they used the actual data type for naming, and this convention became widely spread through the Windows API; this is sometimes called Systems Hungarian notation.\n\nMetacarcinus gracilis: The graceful rock crab or slender crab, Metacarcinus gracilis (the naming convention recognized by WoRMS) or Cancer gracilis (the naming convention recognized by ITIS), is one of only two members of the genus \"Metacarcinus,\" recognized by WoRMS, whose chelae (claws) are white tipped, the other crab being \"M. magister\" (Dungeness crab).  Both of these eastern Pacific crab species are recognized by ITIS as belonging to the much larger genus Cancer.  \"M. gracilis\" has been caught from Alaska to Bahía Magdelena, Baja California.  Although \"M. gracilis\" is only found in the Pacific Ocean, it has cousins in the Atlantic Ocean.  The genus \"Cancer\" (\"sensu lato\") apparently evolved in the Pacific Ocean and later migrated to the Atlantic Ocean.  Larvae and small juveniles of this species are often seen riding jellyfish, especially \"Phacellophora camtschatica\".  The juvenile crabs steal food from the jellyfish and also clean off parasitic amphipods.\n\nProduct naming convention: A product naming convention is a process of product or good description or titling.  Consistent use of alphanumeric characters and separating devices defines a Naming convention.  The naming convention will create an identifier for that version or model of product or goods.\n\nDungeness crab: The Dungeness crab, Metacarcinus magister (the naming convention recognized by WoRMS) or Cancer magister (the naming convention recognized by ITIS), is a species of crab that inhabits eelgrass beds and water bottoms on the west coast of North America.  It typically grows to 20 cm across the carapace and is a popular seafood prized for its sweet and tender flesh.  Its common name comes from the port of Dungeness, Washington.\n\nSaint Thomas Christian names: Saint Thomas Christian names describes the naming convention that is in use by the Saint Thomas Christians of Kerala, the south western state of India.  These Christians known as Syrian Malabar Nasranis, trace their origins to the evangelistic activity of Thomas the Apostle in the 1st century.  They still follow a very old naming convention, which is entirely different from other races and religions.\n\nQuestion: What type of beer uses dubbel as a naming convention and is currently brewed at eleven monasteries?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"beer_type_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the beer type.\"\n    },\n    \"naming_convention_term\": {\n      \"type\": \"string\",\n      \"description\": \"The specific term used as a naming convention for this beer type.\"\n    },\n    \"number_of_monasteries_brewing\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of monasteries currently brewing this beer type.\"\n    },\n    \"monastery_locations\": {\n      \"type\": \"array\",\n      \"description\": \"A list of countries where these monasteries are located, with the count for each.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"country\": {\n            \"type\": \"string\",\n            \"description\": \"The country where monasteries are located.\"\n          },\n          \"count\": {\n            \"type\": \"integer\",\n            \"description\": \"The number of monasteries in that country.\"\n          }\n        },\n        \"required\": [\n          \"country\",\n          \"count\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"beer_type_name\",\n    \"naming_convention_term\",\n    \"number_of_monasteries_brewing\",\n    \"monastery_locations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "beer_type_name": {
        "type": "string",
        "description": "The name of the beer type."
      },
      "naming_convention_term": {
        "type": "string",
        "description": "The specific term used as a naming convention for this beer type."
      },
      "number_of_monasteries_brewing": {
        "type": "integer",
        "description": "The total number of monasteries currently brewing this beer type."
      },
      "monastery_locations": {
        "type": "array",
        "description": "A list of countries where these monasteries are located, with the count for each.",
        "items": {
          "type": "object",
          "properties": {
            "country": {
              "type": "string",
              "description": "The country where monasteries are located."
            },
            "count": {
              "type": "integer",
              "description": "The number of monasteries in that country."
            }
          },
          "required": [
            "country",
            "count"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "beer_type_name",
      "naming_convention_term",
      "number_of_monasteries_brewing",
      "monastery_locations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
