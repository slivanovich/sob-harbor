{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCarle Place, New York: Carle Place is a hamlet and census-designated place (CDP) in the Town of North Hempstead in Nassau County, New York, United States.  The CDP's population was 4,981 at the 2010 census.\n\nGarden City Park, New York: Garden City Park is a hamlet and census-designated place (CDP) located in the Town of North Hempstead in Nassau County on Long Island in the U.S. state of New York.  The population was 7,806 at the 2010 census.  From about 1787 until about 1874, when the area was known as Clowesville, the county seat of Queens County was located here, along with the county courthouse and jail.\n\nEast Garden City, New York: East Garden City is a hamlet and census-designated place (CDP) in the northeast part of the Town of Hempstead, in the central part of Nassau County, New York, along the Hempstead/North Hempstead town line.  The population was 6,028 at the 2010 census.  East Garden City is a hamlet (an unincorporated area) and a mostly commercial and industrial area.  Part of Hofstra University's north campus is located in East Garden City.\n\nSingwango Secondary School: Singwango Secondary School is located in Filabusi, Matabeleland South Province, Zimbabwe.  It had a sister school in Carle Place, New York, United States, although Carle Place High School still donates sports equipment and clothes.\n\nManhasset Hills, New York: Manhasset Hills is a hamlet and census-designated place (CDP) in Nassau County, New York, United States.  The population was 3,592 at the 2010 census.  Manhasset Hills is an unincorporated area of the Town of North Hempstead.  Neighboring communities include Herricks, North New Hyde Park, and Lake Success.\n\nToll Gate House: The Roslyn East Gate Toll House is located within the \"Roslyn Cemetery\" on Route 25A (Northern Boulevard) in Greenvale in the Town of North Hempstead, Nassau County, New York It was built in 1864 and is the last remaining toll house for the North Hempstead Turnpike.  It is frequently but incorrectly assumed to be a toll house for the \"Vanderbilt Motor Parkway\" which ran considerably south of this location.\n\nWinslow Township High School: Winslow Township High School (WTHS) is a four-year comprehensive public high school in Winslow Township, in Camden County, New Jersey, United States, that serves students in ninth through twelfth grades as the lone secondary school of the Winslow Township School District.  Until 2000, the facility that is now Winslow Township High School was part of the Lower Camden County Regional School District and was known as Edgewood Regional High School, which was the sister school of Overbook Regional Senior High School in Pine Hill (now known as Overbrook High School).\n\nManhasset, New York: Manhasset is a hamlet and census-designated place (CDP) in Nassau County, New York, on the North Shore of Long Island.  As of the 2010 United States Census, the population was 8,080.  As with other unincorporated communities in New York, its local affairs are administered by the town in which it is located, the Town of North Hempstead, New York.\n\nGlen Cove Road: Glen Cove Road is a major north–south thoroughfare through north-central Nassau County on Long Island, New York, in the United States.  It is the main road leading to the communities on the east shore of Hempstead Harbor.  The portion south of the North Hempstead–Oyster Bay town line is the unsigned County Route 1 (CR 1), while the portion north of the town line until its intersection with NY 107 is designated as New York State Route 900B (NY 900B), an unsigned reference route, New York State Route 107 (NY 107), and County Route 243 (CR 243), an unsigned county route.\n\nGarden City, New York: Garden City is an incorporated village in the town of Hempstead, in central Nassau County, New York, in the United States.  It was founded by multi-millionaire Alexander Turney Stewart in 1869, and is on Long Island, to the east of New York City, 18.5 miles (29.8 km) from midtown Manhattan.  The village is located mostly in the Town of Hempstead with a small portion in the Town of North Hempstead.\n\nQuestion: Singwango Secondary School had a sister school in a census-designated place in the town of North Hempstead in what county of New York?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"school_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the school that had a sister school.\"\n    },\n    \"sister_school_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"place_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the census-designated place where the sister school is located.\"\n        },\n        \"place_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the place (e.g., CDP, hamlet).\"\n        },\n        \"town_name\": {\n          \"type\": \"string\",\n          \"description\": \"The town where the place is located.\"\n        },\n        \"county_name\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the place is located.\"\n        },\n        \"state_name\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the place is located.\"\n        }\n      },\n      \"required\": [\n        \"place_name\",\n        \"place_type\",\n        \"town_name\",\n        \"county_name\",\n        \"state_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_county\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the county in New York where the sister school's CDP is located.\"\n    }\n  },\n  \"required\": [\n    \"school_name\",\n    \"sister_school_details\",\n    \"answer_county\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "school_name": {
        "type": "string",
        "description": "The name of the school that had a sister school."
      },
      "sister_school_details": {
        "type": "object",
        "properties": {
          "place_name": {
            "type": "string",
            "description": "The name of the census-designated place where the sister school is located."
          },
          "place_type": {
            "type": "string",
            "description": "The type of the place (e.g., CDP, hamlet)."
          },
          "town_name": {
            "type": "string",
            "description": "The town where the place is located."
          },
          "county_name": {
            "type": "string",
            "description": "The county where the place is located."
          },
          "state_name": {
            "type": "string",
            "description": "The state where the place is located."
          }
        },
        "required": [
          "place_name",
          "place_type",
          "town_name",
          "county_name",
          "state_name"
        ],
        "additionalProperties": false
      },
      "answer_county": {
        "type": "string",
        "description": "The name of the county in New York where the sister school's CDP is located."
      }
    },
    "required": [
      "school_name",
      "sister_school_details",
      "answer_county"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
