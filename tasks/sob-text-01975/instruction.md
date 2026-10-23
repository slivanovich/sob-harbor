{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTruckee River: The Truckee River is a river in the U.S. states of California and Nevada.  The river flows northeasterly and is 121 mi long.  The Truckee is the sole outlet of Lake Tahoe and drains part of the high Sierra Nevada, emptying into Pyramid Lake in the Great Basin.  Its waters are an important source of irrigation along its valley and adjacent valleys.\n\nRossinver: Rossinver or Rosinver (Irish: \"Ros Inbhir\" , meaning \"wooded estuary\" ) is a small village in north County Leitrim, Ireland.  The village is at the southern shore of Lough Melvin.  The lake is home to two unusual species of trout - the \"Gillaroo\" and the \"Sonaghan\" - as well as the common brown trout.  There is a fishery at Eden Quay and boats and gillies are available locally.  There are some excellent walks in the area, in particular the mile long river walk to Fowley's Falls on the Glenaniff River which follows a series of waterfalls.\n\nMokelumne River: The Mokelumne River is a 95 mi -long river in northern California in the United States.  The river flows west from a rugged portion of the central Sierra Nevada into the Central Valley and ultimately the Sacramento–San Joaquin River Delta, where it empties into the San Joaquin River.  Together with its main tributary, the Cosumnes River, the Mokelumne drains 2143 mi2 in parts of five California counties.  Measured to its farthest source at the head of the North Fork, the river stretches for 157 mi .\n\nLowe River: The Lowe River is a 28 mile long river in Alaska.  It begins at glacier known as \"Deserted Glacier\" in the Chugach Mountains, passes through Keystone Canyon and flows into Prince William Sound near Valdez.  It was named by William R. Abercrombie in honor of Lt. Perceval Lowe, a member of an exploratory mission in the area led by Abercrombie.\n\nAfon Lwyd: The Afon Lwyd (English: Grey River ) is a 13-mile long river in south-east Wales which flows from its source north of Blaenavon, through Abersychan, Pontnewynydd, Pontypool, Llanfrechfa and Cwmbran before flowing into the River Usk at Caerleon, which subsequently flows into the Bristol Channel in Newport.\n\nPyramid Lake (Nevada): Pyramid Lake is the geographic sink of the Truckee River Basin, 40 mi northeast of Reno.\n\nTwin Lakes (Alaska): Twin Lakes is a complex of two large lakes in Lake Clark National Park in the U.S. state of Alaska near the northeast corner of Lake and Peninsula Borough.  It contains a 6-mile long (9.7 km) upper lake and a smaller 4-mile long (6.5 km) lower lake, joined by a short connecting stream.  The lakes outflow westward into the Chilikadrotna River (and eventually into the Mulchatna and Nushagak Rivers and Nushagak Bay).  It is quite remote and unpopulated, except in the late summer as it is a popular hunting spot.\n\nKnee Lake: Knee Lake is part of the Hayes River in Manitoba, Canada.  It was on the voyageur route from York Factory on Hudson Bay to Norway House, Manitoba on Lake Winnipeg.  It gets its name from a knee-like bend in the middle.  The upstream western part is about 6 miles from south to north and less than 4 miles broad.  The lake narrows to less than half a mile and then extends about 20 miles northeast, this section being at most 4 miles across.  Near the knee is Magnetic Island with an ore body that is said to make compasses useless.  Upstream from the lake, the Hayes River exits eastward out of Oxford Lake, goes over Trout Falls and widens into a long lake which joins Knee Lake at its southwest corner.  The river exits the northeast end of the lake and after about 7 miles and four portages broadens into Swampy Lake.  At the east end of Swampy Lake is the dramstone where west-bound voyageurs took a dram to celebrate leaving the most difficult part of the river.\n\nRiver Cerne: The River Cerne is a ten mile long river in Dorset, England, which rises in the Chalk hills of the Dorset Downs at Minterne Magna, between High Stoy and Dogbury Hill, flows down a valley through Cerne Abbas and Charminster, and flows into the River Frome in Dorchester.  The Cerne Valley lies in the Dorset Area of Outstanding Natural Beauty.\n\nLittle Creek (New Jersey): Little Creek is a 12.58 mile long river in Burlington County, New Jersey.  It drains into the Southwest Branch Rancocas Creek.  Little Creek itself drains an area of 6.32 square miles.  Little Creek has been found to be impaired for primary recreation, but safe and suitable for aquatic life.  Little Creek drains mostly a suburban/rural area, and has been classified as a low-gradient stream.\n\nQuestion: How many miles northeast of Reno is the Lake that a 121 mile long river in California and Nevada empties into?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"river_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"length_miles\": {\n          \"type\": \"integer\"\n        },\n        \"states\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"length_miles\",\n        \"states\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"lake_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"distance_from_reno_miles\": {\n          \"type\": \"integer\"\n        },\n        \"direction_from_reno\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"distance_from_reno_miles\",\n        \"direction_from_reno\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_distance_miles\": {\n      \"type\": \"integer\"\n    }\n  },\n  \"required\": [\n    \"river_details\",\n    \"lake_details\",\n    \"answer_distance_miles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "river_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "length_miles": {
            "type": "integer"
          },
          "states": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "length_miles",
          "states"
        ],
        "additionalProperties": false
      },
      "lake_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "distance_from_reno_miles": {
            "type": "integer"
          },
          "direction_from_reno": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "distance_from_reno_miles",
          "direction_from_reno"
        ],
        "additionalProperties": false
      },
      "answer_distance_miles": {
        "type": "integer"
      }
    },
    "required": [
      "river_details",
      "lake_details",
      "answer_distance_miles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
