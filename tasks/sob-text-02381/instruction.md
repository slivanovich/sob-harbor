{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFletcher Union Church: The Fletcher Union Church, also known as the Fletcher Community House, is a historic former church building on TH 1 (Cambridge Road) in Fletcher, Vermont.  Built in 1871, it is one of only a few public public buildings in the small community, and has for over a century been a secular community meeting space.  It was listed on the National Register of Historic Places in 1982.\n\nPennybacker Bridge: The Percy V. Pennybacker Jr.  Bridge in Austin, Texas, is a through-arch bridge across Lake Austin which connects the northern and southern sections of the Loop 360 highway, also known as the \"Capital of Texas Highway.\"  The road is widely considered one of the most scenic urban drives in Texas, in large part due to this arched weathering-steel bridge and the rolling hills that flank the road.  In 2001, 48,000 vehicles crossed the bridge daily.  Ten years prior to this, 22,000 vehicles had crossed the bridge daily.\n\nSpital Brook: Spital Brook is a minor tributary of the River Lea which rises in Hoddesdonpark Wood in the county of Hertfordshire, England.  Spital Brook flows eastwards from Hoddesdonpark Wood, passing through Barclay Park, the former Hoddesdon Common, on its journey to the Lea, while an unnamed parallel stream to the south has been diverted to form ornamental waterbodies located within the former parkland of Broxbournebury.  The stream crosses the Roman road, Ermine Street, before going under the A10 and Cock Lane.  The original crossing place or ford of Spital Brook in Cock Lane remains and the original route it took ran parallel to the brook in a north-south direction.  The brook passes through its namesake area, Spital Brook and marks the traditional boundary between the two parishes of Hoddesdon and Broxbourne.  The stream runs parallel to the Lea Valley Lines by Broxbourne Station until it meets the River Lea close to Broxbourne Riverside, the former Broxbourne Lido.\n\nBlack Brook (Chorley): Black Brook in Lancashire has its source at Great Hill in the West Pennine Moors.  The water is acidic due to a high level of peat in the uplands near to Round Loaf, giving the brook its brown colour.  The young river was known as Warth Brook in olden Heapey.  A feeder stream also known as Black Brook joins near Kittiwake Road - this short and weak water course commences at Eagle Tower.  The jointed brook feeds Anglezarke Reservoir, and joins the River Yarrow in lowland Chorley at Yarrow Bridge.  The entire course of Black Brook and the River Yarrow fall within Chorley and its villages.\n\nBrook silverside: Labidesthes sicculus, also known as the Brook silverside is a North American species of Neotropical silverside.  The brook silverside lives in slow moving rivers and lakes from the Great Lakes to the Mississippi Basin and Gulf Coastal Plains.  The brook silverside survives best in clear water with aquatic vegetation.  \"L. sicculus\" feeds on a diet of copepods, insect larvae, and winged insects.  The spawning season of the brook silverside occurs during the spring and early summer.  The survival of freshwater fishes such as the brook silverside is increasingly threatened.  In order to ensure survival of the brook silverside, turbidity of natural habitats should be monitored.\n\nA10 road (England): The A10 (in certain sections known as \"Great Cambridge Road\" or Old North Road) is a major road in England.  Its southern end is at London Bridge in the London Borough of Southwark, and its northern end is the Norfolk port town of King's Lynn.  From London to Royston it chiefly follows the line of Roman Ermine Street.\n\nVia Augusta: Via Augusta (also known as Via Herculea or Via Exterior) was a Roman road crossing all of Hispania Province, from Cádiz in the southern tip of current Spain, to the Coll de Panissars, where it crossed the Pyrenees close to the Mediterranean Sea, and joined the \"Via Domitia\".  The road stretched around 1500 km ), passing through the cities of \"Gades\" (Cádiz), \"Carthago Nova\" (Cartagena), \"Valentia\" (Valencia), \"Saguntum\" (Sagunto), \"Tarraco\" (Tarragona), \"Barcino\" (Barcelona), and \"Gerunda\" (Girona).  It had branches passing through \"Hispalis\" (Seville) (where it joined the \"Via Lusitanorum\"), \"Corduba\" (Córdoba), and \"Emerita Augusta\" (Mérida).  The road was named after Emperor Augustus, who ordered it renovated between 8 BC and 2 BC.  It was mainly a commercial road.  Its path is currently followed by the N-340 road and the A-7 highway.  North of Tarragona there remains a Roman Triumphal arch, the Arc de Berà, around which the road divides.  At Martorell, the ancient Via crosses the river Llobregat on the Pont del Diable which dates from the High Middle Ages (1289 CE)\n\nBulls Cross: Bulls Cross is a road and hamlet located in the London Borough of Enfield, north London, and is part of London's Metropolitan Green Belt.  It is located west of the A10 Great Cambridge Road and south from the M25 motorway.  Crews Hill is located to the west, Bury Green (near Cheshunt) to the north, and Bullsmoor to the east.\n\nGreat Hollow Road Stone Arch Bridge: The Great Hollow Road Stone Arch Bridge (also known as Etna Stone Bridge) is a historic bridge on Great Hollow Road, over Mink Brook, approximately 100 feet north of the junction with Smith Lane in Hanover, New Hampshire.  The stone and concrete bridge was built in 1914 by the town.  It is 33 ft long and 24.5 ft wide, with a road width of 21.5 ft .  The vault of the stone arch is 24.5 feet in width, and is constructed of mortared rubble stone lined with ashlar voussoirs.  The stonework has been topped by six inches of concrete, which is believed to be a later addition intended to protect the stonework from the elements.\n\nHobson's Conduit: Hobson's Conduit, also called Hobson's Brook, is a watercourse that was built from 1610 to 1614 by Thomas Hobson and others to bring fresh water into the city of Cambridge, England from springs at Nine Wells, a Local Nature Reserve ( ), near the village of Great Shelford.  It is now a Scheduled Ancient Monument and historical relic.  The watercourse currently runs overground until Cambridge University Botanic Garden and Brookside, where it is at its widest.  At the corner of Lensfield Road stands an octagonal monument to Hobson, which once formed part of the market square fountain, and was moved to this location in 1856, after a fire in the Market.  The flow of water runs under Lensfield Road, and subsequently runs along both sides of Trumpington Street in broad gutters towards Peterhouse and St Catharine's College, and also St Andrew's Street.  The conduit currently ends at Silver Street.\n\nQuestion: How far does the road, also known as \"Great Cambridge Road\" go that is crossed by the Spital Brook?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"road_name\": {\n      \"type\": \"string\",\n      \"description\": \"The primary name of the road.\"\n    },\n    \"alternative_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other names by which the road is known.\"\n    },\n    \"southern_end\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"location_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the location at the southern end.\"\n        },\n        \"borough_or_town\": {\n          \"type\": \"string\",\n          \"description\": \"The borough or town where the southern end is located.\"\n        }\n      },\n      \"required\": [\n        \"location_name\",\n        \"borough_or_town\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"northern_end\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"location_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the location at the northern end.\"\n        },\n        \"type_of_location\": {\n          \"type\": \"string\",\n          \"description\": \"The type of location (e.g., port town).\"\n        }\n      },\n      \"required\": [\n        \"location_name\",\n        \"type_of_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"crossed_by_spital_brook\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if Spital Brook crosses this road.\"\n    }\n  },\n  \"required\": [\n    \"road_name\",\n    \"alternative_names\",\n    \"southern_end\",\n    \"northern_end\",\n    \"crossed_by_spital_brook\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "road_name": {
        "type": "string",
        "description": "The primary name of the road."
      },
      "alternative_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other names by which the road is known."
      },
      "southern_end": {
        "type": "object",
        "properties": {
          "location_name": {
            "type": "string",
            "description": "The name of the location at the southern end."
          },
          "borough_or_town": {
            "type": "string",
            "description": "The borough or town where the southern end is located."
          }
        },
        "required": [
          "location_name",
          "borough_or_town"
        ],
        "additionalProperties": false
      },
      "northern_end": {
        "type": "object",
        "properties": {
          "location_name": {
            "type": "string",
            "description": "The name of the location at the northern end."
          },
          "type_of_location": {
            "type": "string",
            "description": "The type of location (e.g., port town)."
          }
        },
        "required": [
          "location_name",
          "type_of_location"
        ],
        "additionalProperties": false
      },
      "crossed_by_spital_brook": {
        "type": "boolean",
        "description": "Indicates if Spital Brook crosses this road."
      }
    },
    "required": [
      "road_name",
      "alternative_names",
      "southern_end",
      "northern_end",
      "crossed_by_spital_brook"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
