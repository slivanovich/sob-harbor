{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnn Wood-Kelly: Ann Wood-Kelly (31 March 1918 – 14 May 2006) was an American aviator who flew with the British Air Transport Auxiliary in the Second World War.\n\nAir Transport Auxiliary: The Air Transport Auxiliary (ATA) was a British civilian organisation set up during the Second World War and headquartered at White Waltham Airfield that ferried new, repaired and damaged military aircraft between factories, assembly plants, transatlantic delivery points, Maintenance Units (MUs), scrap yards, and active service squadrons and airfields, but not to naval aircraft carriers.  It also flew service personnel on urgent duty from one place to another and performed some air ambulance work.  Notably, many of its pilots were women, and from 1943 they received equal pay to their male co-workers, a first for the British government.\n\nMarion Wilberforce: Marion Wilberforce (22 July 1902 – 17 December 1995) was a Scottish aviator and one of the first eight members of the Air Transport Auxiliary (ATA).  She flew many planes including Spitfires, Hurricanes, Lancaster Bombers, Wellington Bombers and Mosquitos.  She rose to become deputy commander of the No. 5 Ferry Pool at Hatfield, and later became commander of the No. 12 Ferry Pool at Cotsford, one of only two women pool commanders in the whole ATA.\n\nLindsay Everard: Sir William Lindsay Everard (13 March 1891 – 11 March 1949) was a brewer, politician, and philanthropist from Leicestershire, United Kingdom.  As the founder and supporter of the Ratcliffe Aerodrome, Sir Lindsay was a pioneer aviator, knighted for his crucial efforts in World War II with the Air Transport Auxiliary (ATA).  He controlled Everards Brewery for nearly 25 years and was a member of parliament.\n\nIndian MRCA competition: The Medium Multi-Role Combat Aircraft (MMRCA) competition, also known as the MRCA tender, was a competition to supply 126 multi-role combat aircraft to the Indian Air Force (IAF).  The Defence Ministry has allocated ₹ crore () for the purchase of these aircraft, making it India's single largest defence deal.  The MRCA tender was floated with the idea of filling the gap between its future Light Combat Aircraft and its in-service Sukhoi Su-30MKI air superiority fighter.\n\nLois Butler: Lois Butler (3 November 1897 – 17 August 1970) was an aviator and one of the early members of the Air Transport Auxiliary (ATA).  By the end of the war, she had more than 1000 flying hours and had flown 36 types of aircraft, and was one of the most experienced service pilots.  She was also an international skier and represented Canada at the 1936 Winter Olympics in Garmisch-Partenkirchen, captaining the women's team and competing in the women’s combined event.\n\nMargaret Fairweather: Margaret Fairweather (23 September 1901 – 4 August 1944) was a British aviator and one of the first eight women members of the Air Transport Auxiliary (ATA).  She flew many planes including Tiger Moths and Hurricanes, and was the first woman to fly a Supermarine Spitfire.  She had previously been an instructor for the Civil Air Guard at Renfrew.\n\nDe Havilland Mosquito: The de Havilland DH.98 Mosquito was a British twin-engine shoulder-winged multi-role combat aircraft.  The crew of two, pilot and navigator, sat side by side.  It served during and after the Second World War.  It was one of few operational front-line aircraft of the era constructed almost entirely of wood and was nicknamed \"The Wooden Wonder\".  The Mosquito was also known affectionately as the \"Mossie\" to its crews.  Originally conceived as an unarmed fast bomber, the Mosquito was adapted to roles including low to medium-altitude daytime tactical bomber, high-altitude night bomber, pathfinder, day or night fighter, fighter-bomber, intruder, maritime strike aircraft, and fast photo-reconnaissance aircraft.  It was also used by the British Overseas Airways Corporation (BOAC) as a fast transport to carry small high-value cargoes to, and from, neutral countries, through enemy-controlled airspace.  A single passenger could ride in the aircraft's bomb bay when it was adapted for the purpose.\n\nMolly Rose: Molly Daphne Rose, {'1': \", '2': \", '3': \", '4': \"} (\"née\" Marshall; 26 November 1920 – 16 October 2016) was a British aviator who flew for the Air Transport Auxiliary in World War II and later served as a magistrate in Oxfordshire.  Her father, David Marshall, formed Marshall Motor Holdings and Marshall Aerospace and Defence Group.\n\nMaureen Dunlop de Popp: Maureen Adele Chase Dunlop de Popp (26 October 1920 – 29 May 2012), née Dunlop, was an Anglo-Argentine pilot who flew for the British Air Transport Auxiliary (ATA) during World War II, and became notable as a pin-up on the cover of the \"Picture Post\" magazine.\n\nQuestion: Marion Wilberforce, was a Scottish aviator and one of the first eight members of the Air Transport Auxiliary (ATA), she flew many planes including which British twin-engine shoulder-winged multi-role combat aircraft? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"aviator_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the aviator in question.\"\n    },\n    \"aircraft_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"model_name\": {\n          \"type\": \"string\",\n          \"description\": \"The specific model name of the aircraft.\"\n        },\n        \"origin_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country of origin for the aircraft.\"\n        },\n        \"engine_configuration\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the engine setup (e.g., 'twin-engine').\"\n        },\n        \"wing_configuration\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the wing type (e.g., 'shoulder-winged').\"\n        },\n        \"primary_role\": {\n          \"type\": \"string\",\n          \"description\": \"The main role of the aircraft as described in the context.\"\n        },\n        \"other_known_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of other roles the aircraft performed.\"\n        },\n        \"nicknames\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of affectionate names or nicknames for the aircraft.\"\n        },\n        \"crew_size\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of crew members typically required for the aircraft.\"\n        },\n        \"construction_material\": {\n          \"type\": \"string\",\n          \"description\": \"The primary material used in the aircraft's construction.\"\n        }\n      },\n      \"required\": [\n        \"model_name\",\n        \"origin_country\",\n        \"engine_configuration\",\n        \"wing_configuration\",\n        \"primary_role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"aviator_flew_this_aircraft\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether the specified aviator flew this particular aircraft.\"\n    }\n  },\n  \"required\": [\n    \"aviator_name\",\n    \"aircraft_details\",\n    \"aviator_flew_this_aircraft\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "aviator_name": {
        "type": "string",
        "description": "The name of the aviator in question."
      },
      "aircraft_details": {
        "type": "object",
        "properties": {
          "model_name": {
            "type": "string",
            "description": "The specific model name of the aircraft."
          },
          "origin_country": {
            "type": "string",
            "description": "The country of origin for the aircraft."
          },
          "engine_configuration": {
            "type": "string",
            "description": "Description of the engine setup (e.g., 'twin-engine')."
          },
          "wing_configuration": {
            "type": "string",
            "description": "Description of the wing type (e.g., 'shoulder-winged')."
          },
          "primary_role": {
            "type": "string",
            "description": "The main role of the aircraft as described in the context."
          },
          "other_known_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of other roles the aircraft performed."
          },
          "nicknames": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of affectionate names or nicknames for the aircraft."
          },
          "crew_size": {
            "type": "integer",
            "description": "The number of crew members typically required for the aircraft."
          },
          "construction_material": {
            "type": "string",
            "description": "The primary material used in the aircraft's construction."
          }
        },
        "required": [
          "model_name",
          "origin_country",
          "engine_configuration",
          "wing_configuration",
          "primary_role"
        ],
        "additionalProperties": false
      },
      "aviator_flew_this_aircraft": {
        "type": "boolean",
        "description": "Indicates whether the specified aviator flew this particular aircraft."
      }
    },
    "required": [
      "aviator_name",
      "aircraft_details",
      "aviator_flew_this_aircraft"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
