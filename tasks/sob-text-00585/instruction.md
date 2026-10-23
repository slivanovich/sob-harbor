{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCíes Islands: The Cíes Islands are an archipelago off the coast of Pontevedra in Galicia (Spain), in the mouth of the Ria de Vigo.  They belong to the parish of San Francisco de Afora, in the municipality of Vigo.  They were declared a Nature Reserve in 1980 and are included in the Atlantic Islands of Galicia National Park (\"Parque Nacional Marítimo-Terrestre das Illas Atlánticas de Galicia\") created in 2002.\n\nCortegada Island: Cortegada is an almost tidal island (it is possible to go walking when the lowest tides happen, but a small amount of water flow does not disappear) in a coastal inlet near Pontevedra in Galicia, Spain.  It is part of the Atlantic Islands of Galicia National Park.\n\nRia de Vigo: Vigo Ria (Galician: \"\" and Spanish: \"Ría de Vigo\" ) is an estuary in Galicia, Spain.  It is the southern most ria of the Rías Baixas.  It is located south of the province of Pontevedra, and extends in northeast direction over a length of 35 km from its mouth at Cape Silleiro to the deepest point in Arcade, with a maximum width of 7 km, and is narrowest in the Strait of Rande at 700 m. Its western entrance is protected by the Cies Islands, which are part of the National Park of the Atlantic Islands, within the islands of Toralla and San Simon.  Its borders the north with Morrazo Peninsula.  In the extreme south lies the Bay of Baiona.  Its easy access, deep draft and calm waters make the Vigo estuary an ideal retreat for sailing and water sports.\n\nSálvora: Sálvora is a small island located on the Ría de Arousa, coast of Galicia, Spain.  It belongs to the municipality of Santa Uxía de Ribeira and is integrated in the Atlantic Islands of Galicia National Park.  It is separated from the mainland by a distance of about 3 kilometers to the north.  It occupies about 190 hectares and has a maximum height of 71 meters (\"As Gralleiras\").  Almost the entire perimeter of the island is rocky but has three beaches of fine white sand.  Since 2001 it has been integrated into the Atlantic Islands of Galicia National Park.\n\nPagué District: Pagué is the single district of Príncipe Province.  Out of the seven districts that make up the equatorial Atlantic islands of São Tomé and Príncipe, its population is one of the smallest: 7,542 (2012).  Its capital, Santo António, is also the provincial capital of Príncipe.  This district as well as the province includes several small islands around the island of Príncipe.  The Obo National Park covers the southern part of the island and since 2012, Island of Príncipe Biosphere Reserve which covers the area of parts of the island and the islets.\n\nBükk National Park: Bükk National Park (Hungarian: \"Bükki Nemzeti Park\" ) is a national park in the Bükk Mountains of Northern Hungary, near Miskolc.  It was founded in 1976 as the third national park in the country.  It contains 431.3 km² (of which 37.74 km² is under increased protection).  Mountainous and forested, Bükk is Hungary's largest national park and is situated in the northern mountains, between Szilvásvárad and Lillafüred.  Bükk's important geological features include various karst formations within its limestone mountains - particularly caves (once inhabited by pre-historic people), swallow-holes, and ravines.  The country's longest (4,000 metres) and deepest (245 metres) cave, Istvánlápa, is located in the park.  Bükk National Park also contains ninety species of nesting birds, some considered endangered.\n\nCabañeros National Park: Cabañeros National Park (in Spanish: \"Parque Nacional de Cabañeros\") is a national park in the Montes de Toledo, Spain.  It falls within two provinces, the northwest of Ciudad Real and the southwest of Toledo.\n\nAtlantic Islands of Galicia National Park: The Atlantic Islands of Galicia National Park (Galician: \"Parque Nacional das Illas Atlánticas de Galicia\" , Spanish: \"Parque Nacional de las Islas Atlánticas de Galicia\" ) is the only national park located in the autonomous community of Galicia, Spain.  It comprises the archipelagos of Cíes, Ons, Sálvora and Cortegada.  The park covers a land area of 1200 ha and a sea area of 7200 ha .  It is the tenth most visited national park in Spain.  It was the thirteenth national park to be established in Spain.\n\nAcadia National Park: Acadia National Park is a United States National Park located in the state of Maine, near Bar Harbor.  It reserves much of Mount Desert Island, and associated smaller islands, off the Atlantic coast.  Initially created as the Sieur de Monts National Monument in 1916, the park was renamed Lafayette National Park in 1919, and was given its current name of Acadia in 1929.  Over three million people visited the park in 2016.  Acadia is the oldest designated national park area east of the Mississippi River.\n\nCaneel Bay: Caneel Bay Set on a 170-acre peninsula in the Virgin Islands National Park, near seven picturesque beaches, the Resort is one of the vacation destinations in the Caribbean.  It is located on the northwest side of St. John, one of the US Virgin Islands.  The resort is within Virgin Islands National Park on property once owned by Laurance Rockefeller.  The hotel was one of the early members of Rockefeller's hotel chain, Rockresorts.  The resort takes its name from the location of the property at Caneel Bay (Caneel means cinnamon in old Dutch).  Rockefeller was so impressed by the area's beauty that he arranged to buy up most of the island of St. John.  He then donated most of it to the U.S. government for the creation of the Virgin Islands National Park, the 29th U.S. national park.  Rockefeller had the resort buildings designed to blend in with the landscape, and most property lighting is indirect so that guests can be able to see the stars at night.  Caneel Bay was a Rosewood Resort until the fall of 2013.  The resort is a member of Leading Hotels of the World.\n\nQuestion: Cabañeros National Park and Atlantic Islands of Galicia National Park are both located in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"country_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the country where the national parks are located.\"\n    },\n    \"national_parks_info\": {\n      \"type\": \"array\",\n      \"description\": \"Information about the national parks mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"park_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the national park.\"\n          },\n          \"is_located_in_country\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the park is located in the identified country.\"\n          }\n        },\n        \"required\": [\n          \"park_name\",\n          \"is_located_in_country\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"all_parks_in_same_country\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if all national parks mentioned in the question are located in the same country.\"\n    }\n  },\n  \"required\": [\n    \"country_name\",\n    \"national_parks_info\",\n    \"all_parks_in_same_country\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "country_name": {
        "type": "string",
        "description": "The name of the country where the national parks are located."
      },
      "national_parks_info": {
        "type": "array",
        "description": "Information about the national parks mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "park_name": {
              "type": "string",
              "description": "The name of the national park."
            },
            "is_located_in_country": {
              "type": "boolean",
              "description": "True if the park is located in the identified country."
            }
          },
          "required": [
            "park_name",
            "is_located_in_country"
          ],
          "additionalProperties": false
        }
      },
      "all_parks_in_same_country": {
        "type": "boolean",
        "description": "True if all national parks mentioned in the question are located in the same country."
      }
    },
    "required": [
      "country_name",
      "national_parks_info",
      "all_parks_in_same_country"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
