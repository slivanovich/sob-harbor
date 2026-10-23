{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChippewas of Georgina Island First Nation 33A: Chippewas of Georgina Island First Nation 33A is a First Nations reserve near the shores of Lake Simcoe.  It is one of three reserves of the Chippewas of Georgina Island First Nation.  It is an enclave within Georgina, Ontario, surrounded by the unincorporated community of Virginia Beach.  It is separated from the mainland portion of the Chippewas of Georgina Island First Nation reserve by Black River Road and the private properties along it.\n\nTreaty 6: Treaty 6 is an agreement between the Canadian monarch and the Plains and Woods Cree, Assiniboine, and other band governments of First Nations at Fort Carlton and Fort Pitt.  The area agreed upon by the Plains and Woods Cree represents most of the central area of the current provinces of Saskatchewan and Alberta.  One Manitoba band also signed on to the treaty by adhesion in 1898.  The treaty signings began in August 1876, with adhesions added later, the last being signed in 1898 in central Saskatchewan in the Montreal Lake area.\n\nMichael Greyeyes: Michael Greyeyes (born June 4, 1967) is a Canadian actor, director and educator.  He is Plains Cree from the Muskeg Lake First Nation in Saskatchewan.  His father was from the Muskeg Lake First Nation and his mother was from the Sweetgrass First Nation, both located in Saskatchewan.\n\nSweetgrass First Nation: The Sweetgrass First Nation is a Cree First Nation reserve in Cut Knife, Saskatchewan, Canada.  Their territory is located 35 kilometers west of Battleford.  The reserve was established as part of Treaty 6.  The Nation is led by Chief Lori Whitecalf.  Registered population -1751.\n\nNorth Spirit Lake First Nation: North Spirit Lake First Nation is a small Oji-Cree First Nation reserve in Northern Ontario, located north of Red Lake, Ontario.  It is connected to Sandy Lake First Nation, and Deer Lake First Nation by winter/ice roads.  It is part of the Keewaytinook Okimakanak Council (Northern Chiefs) and the Nishnawbe Aski Nation.\n\nMarten Falls First Nation: Marten Falls First Nation is an Anishinaabe First Nation reserve located in northern Ontario.  The First Nation occupies communities on both sides of the Albany River in Northern Ontario, including Ogoki Post (Ojibwe: \"Ogookiing\") in the Cochrane District and Marten Falls in the Kenora District.  As of December 2013, the First Nation had a total registered population of 728 people, of which their on-reserve population was 328 people.\n\nGinoogaming First Nation: Ginoogaming First Nation (formerly the Long Lake 77 First Nation) is a small Anishinaabe (Ojibway) First Nation reserve located in Northern Ontario, located approximately 40 km east of Geraldton, Ontario, Canada, on the northern shore of Long Lake, immediately south of Long Lake 58 First Nation and the community of Longlac, Ontario.  As of September, 2006, their total registered population was 773 people, of which their on-Reserve population was 168.\n\nWikwemikong First Nation: The Wikwemikong First Nation is a First Nation on Manitoulin Island in northern Ontario.  The Wikwemikong Unceded Reserve (also called Wikwemikong, Wiikwemkoong, or simply Wiky) is their First Nation reserve in the north-eastern section of Manitoulin Island in Manitoulin District, Ontario, Canada.  Wikwemikong is an unceded Indian reserve in Canada, which means that it has not \"relinquished title to its land to the government by treaty or otherwise.\"\n\nKeeseekoose First Nation: Keeseekoose First Nation is a Saulteaux First Nation reserve located in Kamsack, Saskatchewan, Canada.  It is located next to the Coté First Nation reserve.  The Keeseekoose were originally set aside the Swan River First Nation of Manitoba but flooding forced a relocation away from Manitoba, to where the Coté lived.  They are a Saulteaux band who spoke the Saulteaux Dialect of the Ojibwe Language.\n\nFort Albany First Nation: Fort Albany First Nation is a Cree First Nation reserve in Cochrane District in Northeastern Ontario, Canada.  Situated on the southern shore of the Albany River, Fort Albany First Nation is only accessible by air or by winter road.  The community is policed by the Nishnawbe-Aski Police Service, an Aboriginal-based service.  It shares the Fort Albany 67 Indian Reserve with the Kashechewan First Nation.  Fort Albany First Nation controls the Fort Albany Indian Settlement on the north shore of the Albany River, and the Kashechewan First Nation controls the Kashechewan Indian Settlement directly across the river.\n\nQuestion: The  The Sweetgrass First Nation reserve was established as part of what agreement between the Canadian monarch? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"first_nation_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the First Nation.\"\n    },\n    \"agreement_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"agreement_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the agreement or treaty.\"\n        },\n        \"agreement_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of agreement, e.g., 'Treaty'.\"\n        },\n        \"parties_involved\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Key parties involved in the agreement.\"\n        }\n      },\n      \"required\": [\n        \"agreement_name\",\n        \"agreement_type\",\n        \"parties_involved\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"establishment_context\": {\n      \"type\": \"string\",\n      \"description\": \"Context of how the reserve was established in relation to the agreement.\"\n    }\n  },\n  \"required\": [\n    \"first_nation_name\",\n    \"agreement_details\",\n    \"establishment_context\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "first_nation_name": {
        "type": "string",
        "description": "The name of the First Nation."
      },
      "agreement_details": {
        "type": "object",
        "properties": {
          "agreement_name": {
            "type": "string",
            "description": "The name of the agreement or treaty."
          },
          "agreement_type": {
            "type": "string",
            "description": "The type of agreement, e.g., 'Treaty'."
          },
          "parties_involved": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Key parties involved in the agreement."
          }
        },
        "required": [
          "agreement_name",
          "agreement_type",
          "parties_involved"
        ],
        "additionalProperties": false
      },
      "establishment_context": {
        "type": "string",
        "description": "Context of how the reserve was established in relation to the agreement."
      }
    },
    "required": [
      "first_nation_name",
      "agreement_details",
      "establishment_context"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
