{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDungiven: Dungiven (from Irish: \"Dún Geimhin\" , meaning \"Gevin's fort\" ) is a small town, townland and civil parish in County Londonderry, Northern Ireland.  It is on the main A6 Belfast to Derry road.  It lies where the rivers Roe, Owenreagh and Owenbeg meet at the foot of the 1525 ft Benbradagh.  Nearby is the Glenshane Pass, where the road rises to over 1000 ft .  It had a population of 2,993 people in the 2001 Census, an increase of 6% over 1991.  It is within Causeway Coast and Glens district.\n\nDorsey Knob: Dorsey Knob is a mountain summit located off U.S. Route 119 at the southern edge of Morgantown in Monongalia County, West Virginia, United States.  Dorsey Knob is contained within a park spanning 71 acres (29 ha) that features the mountain's landmark Sky Rock (also referred to as Dorsey Knob).  The top of Sky Rock is at an altitude of 1398 ft , rising nearly 600 feet (180 m) above the surrounding landscape.  It overlooks the Monongahela River and the Appalachian Mountains.  Also located in the park is Dorsey's Knob Lodge, operated by Boparc, Morgantown's municipal park authority.\n\nMount Norwottuck: Mount Norwottuck or Mount Norwottock, 1106 ft feet above sea level, is the highest peak of the Holyoke Range of traprock mountains located in the Connecticut River Valley of Massachusetts and part of the greater Metacomet Ridge which stretches from Long Island Sound to nearly the Vermont border.  The peak rises steeply from the valley 1000 ft below and offers sweeping views of the surrounding countryside.  It is located within the towns of Amherst and Granby, Massachusetts.\n\nPenistone: Penistone ( ) is a market town and civil parish in the Metropolitan Borough of Barnsley, South Yorkshire, England, which had a population of 22,909 at the 2011 census.  Historically in the West Riding of Yorkshire, it is 8 mi west of Barnsley, 17 mi north-east of Glossop, 14.2 mi north-west of Sheffield, and 29 mi east of Manchester in the foothills of the Pennines.  The highest point, Hartcliffe Tower, is 1194 ft above sea level and has views over the Woodhead bypass and the Dark Peak.  The surrounding countryside is predominantly rural with farming on rich well-watered soil on mainly gentle slopes rising to the bleak moorland to the west of the town.  Dry stone walls, small hamlets and farms surrounded by fields and livestock are synonymous with the area.  The area is known for its rugged breed of sheep, the Whitefaced Woodland.  The market town itself stands at its highest point around St Johns Church at around 250 m above sea level.  However, the surrounding land rises well over 1000 ft towards Cubley and Thurlstone Moors and out towards smaller hamlets at Carlecotes, Victoria, Dunford, and Crow Edge, elevated at points above 1200 ft .  There are several vantage points that afford panoramic views of the surrounding areas of West Yorkshire and North Derbyshire.\n\nHoward Knob: Howard Knob (variant: Howard's Knob) is a mountain in the North Carolina High Country, located in the town of Boone.  According to the US Geological Survey, the mountain's proper name is Howard Knob, but it is known to locals and tourists as Howard's Knob.  Howard Knob and the surrounding area are part of the Appalachian Mountain Range.  The mountain has an elevation of 4396 ft above sea level, and rises nearly 1000 ft above the town of Boone and the campus of Appalachian State University.\n\nPilot Knob (Imperial County, California): Pilot Knob (also, Avie Quah-la-Altwa, Ha-bee-co-la-la, and San Pablo) is a peak in Imperial County, California.  Pilot Knob is located 8 mi southeast of Ogilby, It rises to an elevation of 876 ft .  Pilot Knob is a rocky landform, geologically a Volcanic plug, west of Yuma, Arizona–Winterhaven, California; it is connected to the Cargo Muchacho Mountains, the central portion of the mountains being about 7 mi north.  Pilot Knob was named for its prominence as a landmark for riverboat traffic in the 19th-20th centuries on the Colorado River which borders Winterhaven–Yuma.\n\nBare Mountain (Massachusetts): Bare Mountain, 1014 ft above sea level, is a prominent peak of the Holyoke Range of traprock mountains located in the Connecticut River Valley of Massachusetts, and part of the greater Metacomet Ridge that stretches from Long Island Sound to nearly the Vermont border.  The peak rises steeply from the river valley 1000 ft below; its bald summit offers sweeping views.  Bare Mountain is located within the towns of Amherst and South Hadley, Massachusetts.  Part of its northeastern flanks are in Hadley and part of its southern flanks are in Granby.  It is traversed by the 110 mi Metacomet-Monadnock Trail.\n\nAppalachian State University: Appalachian State University (also referred to as Appalachian, App State, App, ASU) is a comprehensive (Master's L), public, coeducational university in Boone, North Carolina, United States.\n\nElk Hill (Pennsylvania): Elk Hill, also known as North Knob at its highest point or Elk Mountain, is a mountain in Herrick Township, Susquehanna County, Pennsylvania.  It is the highest peak in eastern Pennsylvania, east of the Susquehanna River, as well as the highest peak on the Allegheny Plateau.  Elk Hill rises conspicuously above the surrounding landscape.  The mountain actually has two peaks; the main summit of North Knob is 2693 ft , and the lower summit known as South Knob is 2602 ft .  It is home to Elk Mountain Ski Area which has a 1000 ft vertical drop and 27 ski trails.\n\nWhite Grass Ski Touring Center: White Grass Ski Touring Center is a cross-country skiing facility located in Canaan Valley in Tucker County, West Virginia.  It originally opened in 1979 on White Grass Knob near Harrisonburg, Virginia.  Two years later, the operation was moved to the site of the second Weiss Knob Ski Area.  The resort uses Weiss Knob's former lodge as its day lodge; it is one of the oldest dedicated cross country ski areas in the United States.  Because of its status as a former downhill slope, White Grass is an unusually steep cross country area, with nearly 1200 ft of vertical rise—more than at neighboring downhill slope Canaan Valley Resort State Park.  Its 45 trails are rated approximately 30% easy, 55% intermediate, 15% most difficult; climbs are available to the summit of 4436 ft Weiss Knob by intermediate skiing, and to 4308 ft Bald Knob via easier or intermediate trails.  White Grass staff also conduct back-country tours into the wilderness areas that surround the center.\n\nQuestion: Howard Knob rises nearly 1000 ft above the town of Boone and a campus also referred to as?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"mountain_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the mountain.\"\n    },\n    \"rises_above_feet\": {\n      \"type\": \"integer\",\n      \"description\": \"The height in feet the mountain rises above the specified location.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"town_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the town.\"\n        },\n        \"campus\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"full_name\": {\n              \"type\": \"string\",\n              \"description\": \"The full name of the campus.\"\n            },\n            \"alternative_names\": {\n              \"type\": \"array\",\n              \"items\": {\n                \"type\": \"string\"\n              },\n              \"description\": \"A list of alternative names or abbreviations for the campus.\"\n            }\n          },\n          \"required\": [\n            \"full_name\",\n            \"alternative_names\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"town_name\",\n        \"campus\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"mountain_name\",\n    \"rises_above_feet\",\n    \"location_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "mountain_name": {
        "type": "string",
        "description": "The name of the mountain."
      },
      "rises_above_feet": {
        "type": "integer",
        "description": "The height in feet the mountain rises above the specified location."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "town_name": {
            "type": "string",
            "description": "The name of the town."
          },
          "campus": {
            "type": "object",
            "properties": {
              "full_name": {
                "type": "string",
                "description": "The full name of the campus."
              },
              "alternative_names": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "A list of alternative names or abbreviations for the campus."
              }
            },
            "required": [
              "full_name",
              "alternative_names"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "town_name",
          "campus"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "mountain_name",
      "rises_above_feet",
      "location_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
