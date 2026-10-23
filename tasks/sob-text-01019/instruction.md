{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNational Centre for the Performing Arts (China): The National Centre for the Performing Arts (NCPA) (; literally: National Grand Theatre), and colloquially described as \"The Giant Egg\" (巨蛋), is an arts centre containing an opera house in Beijing, People's Republic of China.  The Centre, an ellipsoid dome of titanium and glass surrounded by an artificial lake, seats 5,452 people in three halls and is almost 12,000 m² in size.  It was designed by French architect Paul Andreu.  Construction started in December 2001 and the inaugural concert was held in December 2007.\n\nAttenborough and the Giant Egg: Attenborough and The Giant Egg is a 2011 British nature documentary presented and written by David Attenborough.  The documentary is a follow-up of an episode in Madagascar, filmed in 1960, for Attenborough's earliest nature documentary series, \"Zoo Quest\".  In that episode, a native boy gave Attenborough a collection of large pieces of eggshell, which Attenborough temporarily pieced together with sticky tape to form a complete eggshell of the extinct elephant bird.  The egg is the subject of the 2011 documentary, which is an hour long and premiered on 2 March 2011.\n\nShun Nakamura: Shun Nakamura (中村 俊 , Nakamura Shun ) is a game designer for Sonic Team, whose works include \"Samba de Amigo\", \"Billy Hatcher and the Giant Egg\" and \"Sonic the Hedgehog\".\n\nBilly Hatcher and the Giant Egg: Billy Hatcher and the Giant Egg (ジャイアントエッグ～ビリー・ハッチャーの大冒険～ , Jaianto Eggu: Birī Hatchā no Daibōken ) is a 2003 video game developed by Sonic Team and published by Sega for the GameCube.  It was ported to Microsoft Windows and Mac OS X in 2006, for release in Europe.\n\nLaevicardium elatum: Laevicardium elatum, common name's the giant egg cockle, giant Pacific cockle and the yellow cardinal cockle is a species of saltwater clam, a cockle, a marine bivalve mollusc in the family Cardiidae, the cockles.  This species is found in the tropical Panamic Province, from Southern California south through the Pacific coast of Mexico and the Gulf of California, and as far south as Panama.\n\nEmpire Subang: Empire Subang is a mixed-commercial development located in Subang Jaya, Selangor, Malaysia which comprises soho office towers, an upscale shopping mall and a 4-star hotel.  It is located in the downtown area of Subang Jaya, near Subang Parade, Wisma Consplant (formerly the HQ for oil palm giant Sime Darby Plantation) and the Subang Jaya railway station.  The building is categorized into four sections, notably Empire Soho, Empire Tower, Empire Hotel and Empire Shopping Gallery.  Empire Shopping Gallery and Empire Hotel were opened in 2010.\n\nMerced Grove Ranger Station: The Merced Grove Ranger Station in Yosemite National Park was designed by the National Park Service and completer in 1935.  An example of the National Park Service Rustic style, it features log construction.  The station is near the Merced Grove of giant sequoias, in the Crane Flat region of the park.\n\nTiananmen West Station: Tiananmen West Station () is a station on Line 1 of the Beijing Subway.  It is located near Tiananmen Square, the Forbidden City, and the National Centre for the Performing Arts.\n\nApartment Building 63: Apartment Building 63, also called Commune 63 (Romanian \"Comuna 63\") is an apartment building located in the Dristor neighbourhood in the south-eastern part of Bucharest (Sectorul 3) and it is the largest single residential building in Romania with a total of 950 apartments, with one room, and holding just over 1,600 residents.  The building is nicknamed the \"commune\" because of the large number of apartments that could house an entire village or commune, and because of the long corridors that stretch from one end of the building to the other and resemble a long country road.  The apartment building has four staircases of 10 floors each and is built in the shape of a giant Z with an extension in the southern part of the structure.  It is also located near the Dristor metro station, a major node of the Bucharest Metro's railway network.\n\nQuestion: What station is near \"The Giant Egg\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The formal name of the entity colloquially known as 'The Giant Egg'.\"\n    },\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of facility or structure the entity is.\"\n    },\n    \"nearby_station\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the station located near 'The Giant Egg'.\"\n    },\n    \"station_line\": {\n      \"type\": \"string\",\n      \"description\": \"The subway line the nearby station is on.\"\n    },\n    \"station_location_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the station and the entity are located.\"\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"entity_type\",\n    \"nearby_station\",\n    \"station_line\",\n    \"station_location_city\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The formal name of the entity colloquially known as 'The Giant Egg'."
      },
      "entity_type": {
        "type": "string",
        "description": "The type of facility or structure the entity is."
      },
      "nearby_station": {
        "type": "string",
        "description": "The name of the station located near 'The Giant Egg'."
      },
      "station_line": {
        "type": "string",
        "description": "The subway line the nearby station is on."
      },
      "station_location_city": {
        "type": "string",
        "description": "The city where the station and the entity are located."
      }
    },
    "required": [
      "entity_name",
      "entity_type",
      "nearby_station",
      "station_line",
      "station_location_city"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
