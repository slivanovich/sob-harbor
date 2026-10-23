{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSmoky Hills Wind Farm: The Smoky Hills Wind Farm (Phase I & Phase II) is a 250 megawatt (MW) wind farm in Lincoln and Ellsworth Counties, 140 miles west of Topeka in Kansas, north of Ellsworth.  The farm is operated by Enel Green Power.  Highway K-14 and Interstate 70 pass through parts of the wind farm, with clear views of many of the wind turbines.  The project uses 56 Vestas V80 1.8 MW wind turbines and produces enough electricity to power some 37,000 average Kansas homes annually.  s of 19 2008 , phase II is under construction with 99 GE 1.5 MW wind turbines for an additional 148.5 MW, to bring the total nameplate capacity to 249.3 MW.\n\nIndian Mesa Wind Farm: Indian Mesa Wind Farm is a wind farm located in Pecos County, Texas.  The farm consists of one hundred twenty-five Vestas V-47 660 kilowatt wind turbines that produce up to 82.5 megawatts of electricity.  Electricity produced by the project is purchased by the Lower Colorado River Authority (51 megawatts) and TXU (31.5 megawatts).  The project is built on land owned by local ranches and the University of Texas.  The project was completed in 2001 by Orion Energy LLC and development partner National Wind Power.  Florida Power & Light acquired the farm in June, 2002.\n\nStockyard Hill Wind Farm: Stockyard Hill Wind Farm is a wind farm project being developed by Origin Energy.  The proposed facility will have 157 wind turbines at a site approximately 35 km west of Ballarat between Beaufort and Skipton.  The forecast cost is $900 million ($950 million US dollars) In December 2009, the original plan for 242 turbines, the plan was changed to only have 157 turbines.  The Victorian minister of planning approved the 157 turbines, in October 2010.\n\nTrent Wind Farm: The Trent Wind Farm, also known as the Trent Mesa Wind Project, is a 150 megawatt wind power station located between Abilene and Sweetwater in West Texas.  The wind farm consists of 100 GE wind turbines each rated at 1.5 megawatts.  American Electric Power owns the Trent Wind Farm and TXU purchases the electricity produced under a long-term agreement.\n\nVoie Sacrée wind farm: The Voie Sacrée wind farm is located in the Lorraine region of France, between the cities of Beausite, Raival, Courcelles-sur-aire, Érize-la-petite, and Maurechamp.  The onshore wind farm was proposed and installed in 2007, and today contains 27 Gamesa G90/2000 wind turbines, each with a hub height of 78 meters and diameter of 90 meters.  Individually, each of the Voie Sacrée wind turbines has a rated capacity of 2,000 kW, for a total capacity of 54,000 kW for the wind farm.  In 2013, the power contribution from the Voie Sacrée wind farm accounted for approximately 0.65% of the total wind power in France (8,254 MW).  The wind farm developer is SFE Française d’Eoliennes and the farm is currently owned and operated by Sorgenia France.\n\nVestas: Vestas Wind Systems A/S is a Danish manufacturer, seller, installer, and servicer of wind turbines.  It was founded in 1945, and as of 2013, it is the largest wind turbine company in the world.  The company operates manufacturing plants in Denmark, Germany, India, Italy, Romania, the United Kingdom, Spain, Sweden, Norway, Australia, China, and the United States, and employs more than 21,000 people globally.\n\nAltamont Pass Wind Farm: The Altamont Pass Wind Farm is located in the Altamont Pass of the Diablo Range in Northern California.  It is one of the earliest wind farms in the United States.  The first wind turbines were placed on the Altamont by Fayette Manufacturing Corporation on land owned by cattle rancher Joe Jess.  The wind farm is composed of 4930 relatively small wind turbines of various types, making it at one time the largest wind farm in the world in terms of capacity.  Altamont Pass is still the largest concentration of wind turbines in the world, with a capacity of 576 megawatts (MW), producing about 125 MW on average and 1.1 terawatt-hours (TWh) yearly.  They were installed after the 1970s energy crisis in response to favorable tax policies for investors.\n\nGros-Morne Wind Farm: The Gros-Morne Wind Farm is a large 211.5 megawatt (MW) wind farm comprising 141 1.5MW wind turbines that provides electricity to over 40,000 homes.  It is located about 50 kilometers north-west of Gaspe, Quebec and it is owned and operated by Cartier Wind Energy.  The wind farm was constructed in 2 phases, the first phase, involving 100.5 MW and 67 wind turbines, was completed on November 29, 2011.  Construction of phase II involved 111MW and 74 wind turbines, and it was finalized on November 6, 2012.\n\nSherbino Wind Farm: The Sherbino Mesa Wind Farm is located in Pecos County in west Texas.  The first 150 megawatts (MW) of the project, which has a potential capacity of 750 MW, is in operation.  Phase I utilizes 50 Vestas V-90 Mk.5 wind turbine generators, each with a rated capacity of 3 MW.  BP will operate phase I of the project.\n\nAlto Minho Wind Farm: The Alto Minho Wind Farm in the Viana do Castelo district, of Portugal, became fully operational in November, 2008, when Portugal's Economy Minister Manuel Pinho inaugurated it.  At the time of completion, it was Europe's largest on-shore wind farm.  The wind farm began generating electricity in 2007, with production increasing as more wind turbines came online, reflecting the modular nature of wind farms.  The wind farm consists of 68 Enercon E-82 2MW wind turbines and 52 Enercon E-70 E4 2MW turbines, totaling 136 MW and 104 MW, respectively, for a grand total of 240 MW of nameplate capacity.  The wind farm will produce 530 GWh annually, avoiding 370,000 tonne of carbon dioxide emissions.\n\nQuestion: The manufacturer of the wind turbines generators used in Phase I of the Sherbino Mesa Wind Farm project was founded in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"wind_farm_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the wind farm.\"\n    },\n    \"project_phase\": {\n      \"type\": \"string\",\n      \"description\": \"The specific phase of the wind farm project.\"\n    },\n    \"turbine_manufacturer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the wind turbine manufacturer.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the manufacturer was founded.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founding_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"wind_farm_name\",\n    \"project_phase\",\n    \"turbine_manufacturer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "wind_farm_name": {
        "type": "string",
        "description": "The name of the wind farm."
      },
      "project_phase": {
        "type": "string",
        "description": "The specific phase of the wind farm project."
      },
      "turbine_manufacturer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the wind turbine manufacturer."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the manufacturer was founded."
          }
        },
        "required": [
          "name",
          "founding_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "wind_farm_name",
      "project_phase",
      "turbine_manufacturer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
