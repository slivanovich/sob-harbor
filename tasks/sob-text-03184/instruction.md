{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMonmouth town walls and defences: The Monmouth town walls and defences comprise the defensive system of town walls and gates built in Monmouth, Wales between 1297 and the early part of the following century.  Wye Bridge Gate, East Gate (Dixton Gate), Monk's Gate, and Monnow Bridge Gate were access points to the town.  West Gate, across Monnow Street, also provided access.  Only the Monnow Bridge Gatehouse survives intact, albeit in a substantially modified version from the original.\n\nMargaret Williamson Hospital: Margaret Williamson Memorial Hospital for Women and Children (婦孺醫院 1932，上海西門婦孺醫院 1937; commonly West Gate Hospital) was a missionary hospital, and the first hospital opened in Shanghai exclusively for the care of Chinese women.  It was located on Siccawei Road, outside the west gate of the Chinese city in the French settlement; for this reason, it was commonly known as the West Gate Hospital.  The nonsectarian hospital was established in 1884 by the Woman’s Union Missionary Society.\n\nWest Gate Freeway: The West Gate Freeway is a major freeway in Melbourne, the busiest urban freeway and the busiest road in Australia, carrying upwards of 200,000 vehicles per day.  It links Geelong (via the Princes Freeway) and the Western suburbs to the Melbourne CBD and beyond.  It is also a link between Melbourne and the west and linking industrial and residential areas west of the Yarra River with the city and port areas.  The iconic West Gate Bridge is a part of the freeway.\n\nWest Gate Bridge: The West Gate Bridge is a steel box girder cable-stayed bridge in Melbourne, Victoria, Australia.  It spans the Yarra River, just north of its mouth into Port Phillip, and is a vital link between the inner city (CBD) and Melbourne's western suburbs; with the industrial suburbs in the west and with the city of Geelong, 80 kilometres (50 mi) to the south-west.  It is one of the busiest road corridors in Australia.\n\nXimen: Ximen () is a Chinese compound surname.  Ximen literally means \"west gate\", the origination story says that there was a noble family in Zheng or Qi state live near the west gate, so the descents took Ximen (west gate) as their family name.  As compound surnames being rare in China, some Ximen families changed their name to single surname Xi(西).\n\nWest Gate Distributor: The West Gate Distributor is a proposed toll road in Melbourne, Australia, to provide access between the West Gate Freeway and the Port of Melbourne, primarily for heavy freight vehicles.  The project, estimated to cost $680 million, was promised in 2013 by the then Victorian Labor Opposition to allow an estimated 5000 trucks a day to bypass the congested West Gate Bridge.  The project is Labor's alternative to the Napthine government's controversial $18 billion East West Link, which it cancelled in April 2015.  Labor promised to have contracts for the West Gate Distributor project signed within six months of forming government following the 2014 state election, and said the road would be completed by 2018.\n\nEast Gate/West Gate: East Gate/West Gate, a public sculpture by Sasson Soffer, is located on the Indiana University-Purdue University Indianapolis campus, which is near downtown Indianapolis, Indiana.  This sculpture is on loan from the Indianapolis Museum of Art and was installed on campus on March 22, 2009.  It was transported from the Indianapolis Museum of Art to its current location, in front of University Library, from the Indianapolis Museum of Art via helicopter.  East Gate/West Gate was constructed in 1973 and consists of stainless steel pipe.  Its dimensions are 24'x 40'x 30' and weighs 840 lbs.\n\nSudley, Virginia: Sudley is a census-designated place (CDP) in Prince William County, Virginia, United States.  As of the 2010 census, Sudley comprises what in the 2000 census were the Sudley and West Gate CDPs.  Sudley's population including West Gate was 16,203 at the 2010 census, and excluding West Gate was 7,719 at the 2000 census.\n\nWest Gate Tunnel: The West Gate Tunnel, originally known as the Western Distributor, is a proposed 5 kilometre toll road in Melbourne, Australia, to link the West Gate Freeway at Yarraville with CityLink at Docklands via a tunnel beneath Yarraville.  The $5.5 billion project was proposed by infrastructure company Transurban in 2014 as a means of alleviating congestion on the M1 corridor, providing a new river crossing as an alternative to the West Gate Bridge and moving trucks away from homes in the city's inner west.  The freeway-standard link would include a 1.5 km-long, six-lane tunnel and a new bridge over the Maribyrnong River.  The Victorian government announced in December 2015 it would proceed with the project.  Major construction of the tunnel and elevated tollway is scheduled to begin in early 2018 and be completed in 2022.\n\nEregion: In the fiction of J. R. R. Tolkien, Eregion or Hollin was a realm of the Noldorin Elves in eastern Eriador during the Second Age, located near the West Gate of Moria under the shadow of the Hithaeglir (Misty Mountains).  Its capital was Ost-in-Edhil (literally \"Town of the Elves\").  This city was established by the Noldor in the year 750 of the Second Age, located where the Sirannon met the Glanduin.  The elves built a highway, the Elven-way, to connect Ost-in-Edhil to the West Gate of Moria.\n\nQuestion: The West Gate Bridge and the West Gate Distributor are located in what country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entities\": {\n      \"type\": \"array\",\n      \"description\": \"List of entities mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity.\"\n          },\n          \"type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of the entity (e.g., bridge, road).\"\n          },\n          \"location_city\": {\n            \"type\": \"string\",\n            \"description\": \"The city where the entity is located.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"type\",\n          \"location_city\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_location_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where all specified entities are located.\"\n    },\n    \"number_of_entities\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of entities mentioned in the question.\"\n    }\n  },\n  \"required\": [\n    \"entities\",\n    \"common_location_country\",\n    \"number_of_entities\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entities": {
        "type": "array",
        "description": "List of entities mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the entity."
            },
            "type": {
              "type": "string",
              "description": "The type of the entity (e.g., bridge, road)."
            },
            "location_city": {
              "type": "string",
              "description": "The city where the entity is located."
            }
          },
          "required": [
            "name",
            "type",
            "location_city"
          ],
          "additionalProperties": false
        }
      },
      "common_location_country": {
        "type": "string",
        "description": "The country where all specified entities are located."
      },
      "number_of_entities": {
        "type": "integer",
        "description": "The total number of entities mentioned in the question."
      }
    },
    "required": [
      "entities",
      "common_location_country",
      "number_of_entities"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
