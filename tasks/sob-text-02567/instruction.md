{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouthern Maalhosmadulu Atoll: Southern Maalhosmadulu Atoll (code name Baa) is an administrative division of the Maldives.  It consists of two separate natural atolls, namely the southern part of Maalhosmadulhu Atoll (which is 42 km long and 32 km wide and consists of 10 inhabited islands) and the smaller natural atoll known as Goifulhafehendhu Atoll (Horsburgh Atoll in the Admiralty charts).\n\nGan (Laamu Atoll): Gan (Dhivehi: () is one of the inhabited islands of Haddhunmathi Atoll, administrative code Laamu and the proposed capital for the Mathi-Dhekunu Province of the Maldives.  Gan is the longest island of the Maldives.  It is divided in wards, the northernmost of which is called Thundi in middle Mathimaradhu and at the end Mukurimagu.  Gan is connected with Maandhoo, the uninhabited island at its south.  Maandhoo is linked with the regional domestic airport at Kadhdhoo by a short causeway.  Kadhdhoo adjoins at its south with Fonadhoo, the capital of the atoll.  The causeway which links between Kadhdhoo and Fonadhoo has almost one kilometer.  The four islands Gan, Maandhoo, Kadhdhoo and Fonadhoo where it is linked with causeways stretches up to about 18 kilometers in length making up the longest lengthen of dry land in the Maldives.\n\nMakunudhoo (Haa Dhaalu Atoll): Makunudhoo (Dhivehi: މަކުނުދޫ) is one of the inhabited islands of Haa Dhaalu Atoll administrative division and geographically part of \"Māmakunudhoo\" Atoll (Malcolm Atoll) in the north of the Maldives.  It is the westernmost inhabited island in the Maldives.\n\nAddu City: Addu City (local administrative code Seenu) is a city in Maldives that consists of the inhabited islands of the southernmost atoll of the archipelago.\n\nBaa Atoll: Baa Atoll (also known as Southern Maalhosmadulu Atoll or Maalhosmadulu Dhekunuburi) is an administrative division of the Maldives.  It consists of three separate natural atolls, namely southern Maalhosmadulu Atoll (which is 42 km long and 32 km wide and consists of 9 inhabited islands), the Fasdūtherē Atoll (wedged in between the two Maalhosmadulu Atolls and separated from north Maalhosmasdulu Atoll by Hani Kandu or Moresby Channel) and the smaller natural atoll known as Goifulhafehendhu Atoll (Horsburgh Atoll in the Admiralty charts).\n\nHuvadhu Atoll: Huvadhu is sometimes referred to as the largest atoll of the Maldives.  The fact is, however, that it is the second largest natural atoll, taking into account that Thiladhunmathi Atoll and Miladhunmadulu Atoll together stand for the largest.  Even so, with an area of 3152 km², land area 38.5 km², Huvadhu is 10th largest atoll in the world, larger than Ontong Java Atoll and Lihou Reef in the SW Pacific area.  On its reef rim are many inhabited islands.\n\nHulhumeedhoo: Hulhumeedhoo (Dhivehi: ހުޅުމީދޫ) or Hulhudhoo-Meedhoo is one of the inhabited islands of the Addu Atoll (also known as Seenu Atoll) in Maldives.  Hulhumeedhoo is one of the largest islands in the Maldives.  Hulhumeedhoo is the only inhabited island in Eastern side of Addu Atoll.  Although the island is geographically a single island, it is administratively divided into two.  That is Hulhudhoo and Meedhoo.  The exact reason for the separation of people is unknown.  This is the only island in Maldives which is geographically one, but politically and administratively two islands.  When Addu Atoll declared status of a city, the two administrative offices was brought under one council office where the Councillor is elected from the votes of the residents of Hulhumeedhoo.\n\nEquatorial Convention Centre: Equatorial Convention Centre (ECC) is a convention centre which is located in Hithadhoo, Addu City of Maldives.  It was specially build for the seventeenth SAARC summit which was held in November 2011 in Addu City and nearby Fuvahmulah island.  ECC was formally opened by the President of the Maldives H.E Mohamed Nasheed on November 10, 2011.\n\nUtheemu (Haa Alif Atoll): Utheemu (Maldivian: އުތީމު ) is one of the inhabited islands of Haa Alif Atoll administrative division and geographically part of Thiladhummathi Atoll in the north of the Maldives.  It is an island-level administrative constituency governed by the Utheemu Island Council.  Utheemu is famed as the birthplace of Sultan Mohamed Thakurufaanu, who with his brothers and his companions fought an eight-year-long war to drive out the Portuguese invaders who occupied the Maldives from 1558 to 1573.  \"Utheemu Ganduvaru\" is the wooden palace in which Sultan Mohamed Thakurufaanu lived and grew up.  It is well preserved and evokes more than any other existing building in the Maldives, the lifestyle of the rich, centuries ago.\n\nKendhikolhudhoo (Noonu Atoll): Kendhikulhudhoo (Dhivehi: ކެނދިކުޅުދޫ) is one of the inhabited islands of Noonu Atoll in the north province of Maldives.  The island is among the 10th biggest islands in the Maldives archipelago.\n\nQuestion: The Equatorial Convention Centre is located in what city in Maldives that consists of the inhabited islands of the southernmost atoll of the archipelago?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"city_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the city where the convention centre is located.\"\n    },\n    \"city_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the city as provided in the context, specifically regarding its location and composition.\"\n    },\n    \"convention_centre\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the convention centre.\"\n        },\n        \"location_island\": {\n          \"type\": \"string\",\n          \"description\": \"The specific island within the city where the convention centre is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location_island\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"city_name\",\n    \"city_description\",\n    \"convention_centre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "city_name": {
        "type": "string",
        "description": "The name of the city where the convention centre is located."
      },
      "city_description": {
        "type": "string",
        "description": "A description of the city as provided in the context, specifically regarding its location and composition."
      },
      "convention_centre": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the convention centre."
          },
          "location_island": {
            "type": "string",
            "description": "The specific island within the city where the convention centre is located."
          }
        },
        "required": [
          "name",
          "location_island"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "city_name",
      "city_description",
      "convention_centre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
