{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVan, Texas: Van is a city located in southeastern Van Zandt County, Texas, United States, approximately 75 miles east of Dallas, Texas and 26 miles northwest of Tyler, Texas.  The population was 2,632 at the 2010 census.  The town draws its name from an early settler and school teacher Henry Vance.\n\nMacomb, Illinois: Macomb is a city in and the county seat of McDonough County, Illinois, United States.  It is situated in western Illinois, southwest of Galesburg.  The city is about 75 miles southwest of Peoria and 77 miles south of the Quad Cities.  A special census held in 2014 placed the city's population at 21,516.  Macomb is the home of Western Illinois University.\n\nLittle River (Texas): The Little River is a river in Central Texas in the Brazos River watershed.  It is formed by the confluence of the Leon River and the Lampasas River near Little River, Texas in Bell County.  It flows generally southeast for 75 miles until it empties into the Brazos River about five miles southwest of Hearne, at a site called Port Sullivan in Milam County.  The Little River has a third tributary, the San Gabriel River, which joins the Little about eight miles north of Rockdale and five miles southwest of Cameron.  Cameron, the county seat of Milam County and the only city of any significant size on the Little River, was established in 1846.\n\nGrand Saline, Texas: Grand Saline is a city in Van Zandt County, Texas, United States, located in East Texas.  The population is 3,266.  Grand Saline is the third largest city in Van Zandt County and is located roughly 75 miles (120 km) east of Dallas and 35 miles (56 km) northwest of Tyler, the two nearest metropolitan areas, and is part of the greater Tyler/Longview area.\n\nQamqênxoi: Qamqenxoi is a village in the Tibet Autonomous Region of China in central Tibet.  It lies roughly 75 miles south-west of Lhasa near the Brahmaputra river at an altitude of 5301 metres (17,394 feet).  The village has a population of about 1918 people.\n\nPoughkeepsie City School District: Poughkeepsie City School District is located in Dutchess County, New York State.  Approximately 75 miles  north of New York City, the school district is situated on the banks of the Hudson River in an area known as the Mid Hudson Valley.\n\nPyapon: Pyapon (Burmese: ဖျာပုံမြို့ ; Mon: ဖျာ ပုၚ် , [phya pɜŋ] ) is a town and seat of Pyapon District in the Ayeyarwady Division of Myanmar, along the Pyapon River, a tributary of the Ayeyarwady River.  It is located about 15 km inland from the Andaman Sea, about 75 miles south of the capital, Yangon.  It has a population of approximately 300,000 in 2006 .  It serves as a center for collecting rice from the surrounding agricultural areas, and is home to a diesel-run power plant, using equipment by the German firm Siemens.\n\nAuburn, Tasmania: Auburn is a village on the Isis River, in the parish of Hill and county of Somerset, Tasmania.  It is about 10 mi from Campbell Town, Tasmania, 40 mi from Launceston, and 75 mi from Hobart.  Nearby is the remarkable hill called Jacob's Sugar Loaf.\n\nIzium: Izium (Ukrainian: Ізюм ; also Romanized Izum, Izyum; literally raisins), is a city situated on the Donets River in Kharkiv Oblast (province) of eastern Ukraine.  Serving as the administrative center of Izium Raion (district), Izium is administratively incorporated as a city of oblast significance and does not belong to the raion.  It is located approximately 75 miles (120 km) southeast of the oblast capital, Kharkiv.  Population:  (2017 est.)\n\nHobart: Hobart ( ) is the capital and most populous city of the Australian island state of Tasmania.  With a population of approximately 225,000, it is the second least populated Australian capital city.  Founded in 1804 as a penal colony, Hobart is Australia's second oldest capital city after Sydney, New South Wales.  The modern history of Hobart (formerly \"Hobart Town\", or \"Hobarton\") dates to its foundation as a British colony in 1804.  Prior to British settlement, the area had been occupied for possibly as long as 35,000 years, by the semi-nomadic Mouheneener tribe, a sub-group of the Nuennone, or South-East tribe.  The descendants of the indigenous Tasmanians now refer to themselves as 'Palawa'.\n\nQuestion: In what county is the village on the Isis River that is 75 miles from the Australian city with a population of approximately 225,000,?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"target_village\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the village identified by the question.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the village is located.\"\n        },\n        \"river_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the river the village is on.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"county\",\n        \"river_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"reference_city\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Australian city used as a reference point.\"\n        },\n        \"population\": {\n          \"type\": \"integer\",\n          \"description\": \"The approximate population of the reference city.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"population\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"distance_between_village_and_city_miles\": {\n      \"type\": \"integer\",\n      \"description\": \"The distance in miles between the target village and the reference city.\"\n    },\n    \"final_answer_county\": {\n      \"type\": \"string\",\n      \"description\": \"The county of the village that is the final answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"target_village\",\n    \"reference_city\",\n    \"distance_between_village_and_city_miles\",\n    \"final_answer_county\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "target_village": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the village identified by the question."
          },
          "county": {
            "type": "string",
            "description": "The county where the village is located."
          },
          "river_name": {
            "type": "string",
            "description": "The name of the river the village is on."
          }
        },
        "required": [
          "name",
          "county",
          "river_name"
        ],
        "additionalProperties": false
      },
      "reference_city": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Australian city used as a reference point."
          },
          "population": {
            "type": "integer",
            "description": "The approximate population of the reference city."
          }
        },
        "required": [
          "name",
          "population"
        ],
        "additionalProperties": false
      },
      "distance_between_village_and_city_miles": {
        "type": "integer",
        "description": "The distance in miles between the target village and the reference city."
      },
      "final_answer_county": {
        "type": "string",
        "description": "The county of the village that is the final answer to the question."
      }
    },
    "required": [
      "target_village",
      "reference_city",
      "distance_between_village_and_city_miles",
      "final_answer_county"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
