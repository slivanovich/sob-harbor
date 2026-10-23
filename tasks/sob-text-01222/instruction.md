{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSquirrel Island, Maine: Squirrel Island, Maine is a summer resort colony off the coast of Boothbay Harbor.  The origin of the name is not related to its squirrel population, since according to island chronicler Charles McLane \"[s]quirrels do not inhabit the island (or if they do now, they did not in early times according to local pundits),\" but, rather, refers to the shape of the island which, when seen from above, resembles a squirrel holding an acorn.\n\nSprucewold Lodge: Sprucewold Lodge is a historic summer tourist accommodation at 4-9 Nahanada Road in Boothbay Harbor, Maine.  Its main lodge built in 1927, it was the centerpiece of an extensive rustic retreat on the Spruce Point peninsula southeast of downtown Boothbay Harbor.  The lodge is one of the state's finest examples of rustic Adirondack architecture, and was listed on the National Register of Historic Places in 2014.  In 2016, the lodge was listed for sale.\n\nPythian Opera House: The Pythian Opera House, also known historically as the Knights of Pythias Hall, Boothbay Harbor Opera House and The Opera House, and formally as The Opera House at Boothbay Harbor, is a historic meeting hall and multifunction building at 86 Townsend Avenue in Boothbay Harbor, Maine.  Built in 1894, it has housed government offices of the town, and the meeting spaces of fraternal organizations, prior to its present use as a performance venue.  It was listed on the National Register of Historic Places on December 30, 2008.\n\nBoothbay Harbor, Maine: Boothbay Harbor is a town in Lincoln County, Maine, United States.  The population was 2,165 at the 2010 census.  During summer months, the entire Boothbay Harbor region is a popular yachting and tourist destination.  ZIP Code is 04538.  The community is served by the 633 exchange in Area Code 207.\n\nBoothbay Harbor (CDP), Maine: Boothbay Harbor is a census-designated place (CDP) in the town of Boothbay Harbor in Lincoln County, Maine, United States.  The population was 1,237 at the 2000 census.\n\nThe Cuckolds Light: The Cuckolds Light, known as the Cuckolds Island Fog Signal and Light Station or just Cuckolds Light Station, is a lighthouse located on the eastern pair of islets known as the \"Cuckolds\" in Lincoln County, Maine.  The islets are southeast and in sight of Cape Island, that is just off the southern tip of Cape Newagen on Southport Island, south of Booth Bay, that leads to Boothbay Harbor, Maine.\n\nWest Boothbay Harbor, Maine: West Boothbay Harbor is an unincorporated village in the town of Boothbay Harbor, Lincoln County, Maine, United States.  The community is located along Maine State Route 27 10.7 mi south of Wiscasset.  West Boothbay Harbor has a post office with ZIP code 04575.\n\nSouthport, Maine: Southport is a town in Lincoln County, Maine, United States.  The population was 606 at the 2010 census.  It includes the villages of Southport, West Southport, Cape Newagen, and Squirrel Island.  The majority of the town's residents live on its main island, Southport Island.\n\nDamariscove Island: Damariscove is an uninhabited island that is part of Boothbay Harbor, Lincoln County, Maine, United States, about 5 nmi off the coast at the mouth of the Damariscotta River.  The long, narrow island is approximately 2 mi long and 1500 ft at its widest point.  The island has served in the past as a fishing settlement and a Coast Guard life saving station.\n\nBoothbay Harbor Memorial Library: Boothbay Harbor Memorial Library is the public library of Boothbay Harbor, Lincoln County, Maine.  It is located at 4 Oak Street, in an architecturally significant Greek Revival building constructed as a private residence in 1842.  The building was listed on the National Register of Historic Places in 1977.  The building also serves as a war memorial to the town's soldiers of the First World War.\n\nQuestion: Southport, Maine contains what village off the coast of Boothbay Harbor? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town.\"\n    },\n    \"contained_village\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the village located within the town.\"\n    },\n    \"village_location_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the village's location relative to other places.\"\n    }\n  },\n  \"required\": [\n    \"town_name\",\n    \"contained_village\",\n    \"village_location_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "town_name": {
        "type": "string",
        "description": "The name of the town."
      },
      "contained_village": {
        "type": "string",
        "description": "The name of the village located within the town."
      },
      "village_location_description": {
        "type": "string",
        "description": "A description of the village's location relative to other places."
      }
    },
    "required": [
      "town_name",
      "contained_village",
      "village_location_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
