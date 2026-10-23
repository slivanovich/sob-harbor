{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSakumo Ramsar Site: The Sakumo Ramsar Site also known as the Sakumo Lagoon is a wetland of international importance.  It covers an area of 1340 ha and is situated along the coastal road between Accra and Tema in the Greater Accra Region of Ghana.  It is about 3 km west of Tema.  The lagoon has fish which is taken during the rainy seasons.  During the dry season from August to March a larger part of the lagoon dries up.  There is general cultivation of vegetables such as tomatoes,onion, spinach and also cassava on the wetlands around the lagoon.  The area is encroached upon by cattle which graze in the dry season and land developers who build very close to the site which is a government properly and should not be used by any developer.\n\nLập Thạch District: Lập Thạch is a rural district of Vĩnh Phúc Province in the Red River Delta region of northern Vietnam.  This district is located in the northwestern Vĩnh Phúc, at coordinates: 105°30′ to 105°45′ E and 21°10′ to 21°30′ N, bordering Tuyên Quang on the north, districts of Tam Đảo and Tam Dương on the east, Vĩnh Tường on the south and Sông Lô District and Phú Thọ Province on the west.\n\nBalphakram National Park: Balpakram National Park is a national park ranging from under 200 to over 800 meters above sea level, near the Garo Hills in Meghalaya, India.  Balpakram is located between latitudes 25°20' N and 25°30' N, and longitudes 90°45' E to 91° E .  The Balpakram National Park is located to the extreme South of Garo Hills, Meghalaya at a distance of 62 km from Baghmara, the district headquarters of South Garo Hills and 167 km from nearest major townTura.  This pocket of pristine beauty named Balpakram National Park is also close to the international boundary of Bangladesh.  It is often compared to the Grand Canyon National Park of United States.\n\nBig Ada: Big Ada is a town in the Dangme East district, a district in the Greater Accra Region of Ghana.  The settlement lies along the road from Ada Kasseh to the district capital Ada Foah, just off the Accra-Aflao motorway.\n\nAda Kasseh: Kasseh is a town in the Ada East district, a district in the Greater Accra Region of Ghana.  It is a major town located between Sege and Sogakope on the Accra-Aflao road.  Kasseh has the biggest market in four districts(Ada West, Ada East, South Tongu and North Tongu) in its area.  Kasseh is connected to almost all the towns and villages in the Ada East district by road or path.  It is the most easily accessible town in the district.  It is connected by road to the district capital town of Ada Foah and the Town called Big Ada.\n\nAda Foah: Ada Foah or Ada is a coastal town in the Greater Accra Region of Ghana.  Just off the Accra-Aflao motorway, this town is located along the Volta River.  It's also the capital of the Dangme East District and the seat of the District Assembly.\n\nSakumono Lagoon: Sakumonon Lagoon is a coastal lagoon in Sakumono near Tema in the Greater Accra Region of Ghana, West Africa.  The site covers 1,340 hectares.  It was designated as Ramsar wetland site of international importance on 14 August 1992.\n\nSonghor Lagoon: The Songor Lagoon is located at 05°45'N 000°30'E on the eastern coast of Ghana, West Africa.  The site covers an area of 28,740 hectares, and it is located just outside the major town of Ada and to the west of the Volta River estuary.  It was designated as Ramsar wetland site of international importance number 566 on June 22, 1988.  In 2011, UNESCO approved the Songor Biosphere Reserve as part of the World Network of Biosphere Reserves.  Among several other important functions, it acts as habitat and/or breeding ground for several notable species.\n\nDangme East District: The Dangme East District is one of the ten (10) districts in the Greater Accra Region of Ghana, and covers a surface of 909 km².  Major Towns in the district are Big Ada and Ada Kasseh.  Ada Foah, which is the district capital, is located at the beach and river estuary.  Most of the inhabitants (85.9%) belong to the cultural group of the Dangme.  It has a population of 71,671.\n\nEllsworth Land: Ellsworth Land is that portion of the Antarctic continent bounded on the west by Marie Byrd Land, on the north by Bellingshausen Sea, on the northeast by the base of Antarctic Peninsula, and on the east by the western margin of Ronne Ice Shelf.  It extends between 103°24'W and 79°45'W.  The area west of 90°W is unclaimed, the area between 84°W and 90°W is claimed by Chile only, and the remainder by Chile and the United Kingdom as a part of the British Antarctic Territory.  Eights Coast stretches between 103°24'W and 89°35'W, and Bryan Coast between 89°35'W and 79°45'W.\n\nQuestion: The Songor Lagoon is located at 05°45'N 000°30'E on the eastern coast of Ghana, West Africa, the site covers an area of 28,740 hectares, and it is located just outside the major town of Ada, or Ada Foah is a coastal town in the Greater Accra Region of where/.\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town.\"\n    },\n    \"town_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of settlement, e.g., coastal town.\"\n    },\n    \"region_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the region where the town is located.\"\n    },\n    \"country_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the country where the town is located.\"\n    },\n    \"is_district_capital\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the town is a district capital.\"\n    },\n    \"district_capital_of\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the district for which this town is the capital.\"\n    }\n  },\n  \"required\": [\n    \"town_name\",\n    \"town_type\",\n    \"region_name\",\n    \"country_name\",\n    \"is_district_capital\",\n    \"district_capital_of\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "town_name": {
        "type": "string",
        "description": "The name of the town."
      },
      "town_type": {
        "type": "string",
        "description": "The type of settlement, e.g., coastal town."
      },
      "region_name": {
        "type": "string",
        "description": "The name of the region where the town is located."
      },
      "country_name": {
        "type": "string",
        "description": "The name of the country where the town is located."
      },
      "is_district_capital": {
        "type": "boolean",
        "description": "Indicates if the town is a district capital."
      },
      "district_capital_of": {
        "type": "string",
        "description": "The name of the district for which this town is the capital."
      }
    },
    "required": [
      "town_name",
      "town_type",
      "region_name",
      "country_name",
      "is_district_capital",
      "district_capital_of"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
