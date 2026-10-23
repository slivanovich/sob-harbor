{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTimanfaya National Park: Timanfaya National Park (Spanish: \"Parque Nacional de Timanfaya\" ) is a Spanish national park in the southwestern part of the island of Lanzarote, Canary Islands.  It covers parts of the municipalities Tinajo and Yaiza.  The area is 51.07 km2 .  The parkland is entirely made up of volcanic soil.\n\nCortegada Island: Cortegada is an almost tidal island (it is possible to go walking when the lowest tides happen, but a small amount of water flow does not disappear) in a coastal inlet near Pontevedra in Galicia, Spain.  It is part of the Atlantic Islands of Galicia National Park.\n\nAlpine National Park: The Alpine National Park is a national park located in the Central Highlands and Alpine regions of Victoria, Australia.  The 646000 ha national park is located northeast of Melbourne.  It is the largest National Park in Victoria, and covers much of the higher areas of the Great Dividing Range in Victoria, including Victoria's highest point, Mount Bogong at 1986 m and the associated subalpine woodland and grassland of the Bogong High Plains.  The park's north-eastern boundary is along the border with New South Wales, where it abuts the Kosciuszko National Park.  On 7 November 2008 the Alpine National Park was added to the Australian National Heritage List as one of eleven areas constituting the Australian Alps National Parks and Reserves.\n\nYaiza (municipality): Yaiza is a municipality on the island of Lanzarote in the Canary Islands, Spain.  It lies in the southwest of the island and forms part of the province of Las Palmas.  The municipality is bounded by the Atlantic Ocean to the west, south and east.  In the west is the lagoon of Charco Verde.  To the north the Timanfaya National Park is partly within the municipality.  The eastern part of the municipality is mountainous, and south west of the mountains the Rubicon plain stretches to the coast.\n\nLanzarote: Lanzarote ( ; ] ) is a Spanish island, the easternmost of the autonomous Canary Islands in the Atlantic Ocean.  It is located approximately 125 km off the coast of Africa and 1,000 km from the Iberian Peninsula.  Covering 845.94 km2 , Lanzarote is the fourth-largest of the islands in the archipelago.  With 141,938 inhabitants, it is the third-most populous Canary Island, after Tenerife and Gran Canaria.  In the centre-west of the island is Timanfaya National Park, one of its main attractions.  The capital is Arrecife.\n\nAtlantic Islands of Galicia National Park: The Atlantic Islands of Galicia National Park (Galician: \"Parque Nacional das Illas Atlánticas de Galicia\" , Spanish: \"Parque Nacional de las Islas Atlánticas de Galicia\" ) is the only national park located in the autonomous community of Galicia, Spain.  It comprises the archipelagos of Cíes, Ons, Sálvora and Cortegada.  The park covers a land area of 1200 ha and a sea area of 7200 ha .  It is the tenth most visited national park in Spain.  It was the thirteenth national park to be established in Spain.\n\nCíes Islands: The Cíes Islands are an archipelago off the coast of Pontevedra in Galicia (Spain), in the mouth of the Ria de Vigo.  They belong to the parish of San Francisco de Afora, in the municipality of Vigo.  They were declared a Nature Reserve in 1980 and are included in the Atlantic Islands of Galicia National Park (\"Parque Nacional Marítimo-Terrestre das Illas Atlánticas de Galicia\") created in 2002.\n\nAcadia National Park: Acadia National Park is a United States National Park located in the state of Maine, near Bar Harbor.  It reserves much of Mount Desert Island, and associated smaller islands, off the Atlantic coast.  Initially created as the Sieur de Monts National Monument in 1916, the park was renamed Lafayette National Park in 1919, and was given its current name of Acadia in 1929.  Over three million people visited the park in 2016.  Acadia is the oldest designated national park area east of the Mississippi River.\n\nRia de Vigo: Vigo Ria (Galician: \"\" and Spanish: \"Ría de Vigo\" ) is an estuary in Galicia, Spain.  It is the southern most ria of the Rías Baixas.  It is located south of the province of Pontevedra, and extends in northeast direction over a length of 35 km from its mouth at Cape Silleiro to the deepest point in Arcade, with a maximum width of 7 km, and is narrowest in the Strait of Rande at 700 m. Its western entrance is protected by the Cies Islands, which are part of the National Park of the Atlantic Islands, within the islands of Toralla and San Simon.  Its borders the north with Morrazo Peninsula.  In the extreme south lies the Bay of Baiona.  Its easy access, deep draft and calm waters make the Vigo estuary an ideal retreat for sailing and water sports.\n\nSálvora: Sálvora is a small island located on the Ría de Arousa, coast of Galicia, Spain.  It belongs to the municipality of Santa Uxía de Ribeira and is integrated in the Atlantic Islands of Galicia National Park.  It is separated from the mainland by a distance of about 3 kilometers to the north.  It occupies about 190 hectares and has a maximum height of 71 meters (\"As Gralleiras\").  Almost the entire perimeter of the island is rocky but has three beaches of fine white sand.  Since 2001 it has been integrated into the Atlantic Islands of Galicia National Park.\n\nQuestion: Which is the only national park located in Galicia, Spain: Timanfaya National Park or Atlantic Islands of Galicia National Park?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"national_park_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the national park.\"\n    },\n    \"location_region\": {\n      \"type\": \"string\",\n      \"description\": \"The autonomous community or region where the national park is located.\"\n    },\n    \"country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the national park is located.\"\n    },\n    \"is_only_park_in_region\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if this is the only national park in its specified region, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"national_park_name\",\n    \"location_region\",\n    \"country\",\n    \"is_only_park_in_region\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "national_park_name": {
        "type": "string",
        "description": "The name of the national park."
      },
      "location_region": {
        "type": "string",
        "description": "The autonomous community or region where the national park is located."
      },
      "country": {
        "type": "string",
        "description": "The country where the national park is located."
      },
      "is_only_park_in_region": {
        "type": "boolean",
        "description": "True if this is the only national park in its specified region, false otherwise."
      }
    },
    "required": [
      "national_park_name",
      "location_region",
      "country",
      "is_only_park_in_region"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
