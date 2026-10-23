{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSmiggin Holes 2010 Winter Olympic bid: The Smiggin Holes 2010 Winter Olympic bid was a joke campaign initiated by Australian comedians Roy and HG to bring the 2010 Winter Olympics to the tiny and little-known village of Smiggin Holes, part of the Perisher Blue ski resort, in New South Wales, Australia.  The bid was first proposed on the television show \"The Ice Dream\", which aired as part of the Seven Network's coverage of the 2002 Winter Olympics in Salt Lake City.\n\nMount Rose Ski Tahoe: Mount Rose Ski Tahoe is the closest ski resort to Reno, Nevada.  And the only ski resort that offers a 360 degree view into Nevada's Truckee Meadows and Lake Tahoe.  At the top of the peak on a clear day one can see a unique transition of arid desert to the east and lush evergreen forest of the Sierra Mountain Range to the west.  The Resort is located about 30 miles (50 km) south of Reno in the Carson Range.  Mt. Rose is Tahoe's highest base elevation at about 8260 ft and the summit is 9700 ft .  The resort area is 1200 acre , and is located in the Toiyabe National Forest.\n\nPerisher Valley, New South Wales: Perisher Valley, commonly called Perisher, is a valley formed below Mount Perisher, a mountain that is located in the Snowy Mountains of New South Wales, Australia.\n\nKosciuszko Road: The Kosciuszko Road is a road in the Snowy Mountains of New South Wales, Australia which runs from Pine Valley , to the ski resort of Charlotte Pass .  It passes through the towns of Berridale and Jindabyne before entering Kosciuszko National Park.  Within the national park it provides access to Smiggin Holes and Perisher Valley and Charlotte Pass ski resorts, and terminates just past the entry to the latter.\n\nSmiggin Holes, New South Wales: Smiggin Holes is a village located in the ski resort area of Snowy Mountains of New South Wales, Australia, in the Snowy Monaro Regional Council.  It is primarily a winter-only resort village.  It is within the Kosciuszko National Park, and is administered by New South Wales Department of Environment and Climate Change.  Access to the village is via road.  There is an access fee payable to the national park, and motor vehicles are not permitted to stay overnight in the winter months.\n\nSugarbush Resort: Sugarbush Resort is a ski resort located in the Mad River valley in Warren, Vermont.  It is one of the largest ski resorts in New England.  The resort encompasses more than 4000 acres (16 km²) total, 578 trail acres (2.34 km²) skiable, 53 miles (85 km) of trails, and 16 ski lifts. Sugarbush has 111 ski trails, 18 additional marked wooded area, substantial off-piste skiing and riding, a summit elevation of 4083 ft , and a vertical drop of 2600 ft , second largest in Vermont after Killington, and the third largest in New England after Killington and Sugarloaf.\n\nPerisher Ski Resort: Perisher (known as Perisher Blue until 2009) is the largest ski resort in the Southern Hemisphere.  Located in the Australian Snowy Mountains, the resort is an amalgamation of four villages (Perisher Valley, Smiggin Holes, Guthega, and Blue Cow) and their associated ski fields, covering approximately 12 km2 , with the base elevation at 1720 m AHD, and the summit elevation of 2054 m at the top of Mount Perisher.  4.4 km2 of this area is covered by 240 snow guns, which are used to artificially supplement the natural snowfall.  Perisher was acquired by Vail Resorts, United States on March 30, 2015 for a sum of approximately AU$177 million.\n\nBlue Cow Mountain: Blue Cow is a ski resort that is part of Perisher located in the Snowy Mountains of New South Wales, Australia, within the Snowy Monaro Regional Council.  The resort is situated within the Kosciuszko National Park and is administered by the NSW National Parks & Wildlife Service.  During winter months, the only access to the village is via the Skitube underground railway.  In summer, access is via off-road only.  Blue Cow is one of the four resort bases within Perisher, Australia's largest ski resort.\n\nVail Resorts: Vail Resorts, Inc. runs four ski resorts in Colorado (Vail Ski Resort, Beaver Creek Resort, Keystone Resort, and Breckenridge Ski Resort), three in Lake Tahoe (Heavenly Mountain Resort, Kirkwood Mountain Resort, Northstar California), one in Utah (Park City Mountain Resort in Park City), one in Vermont (Stowe Mountain Resort), one in Minnesota (Afton Alps), one in Michigan (Mount Brighton), one in Wisconsin (Wilmot Mountain), one in New South Wales, Australia (Perisher Ski Resort), one in British Columbia (Whistler Blackcomb), and a summer resort in Wyoming.  They also own luxury resort hotels throughout the world.  The company trades on the New York Stock Exchange, symbol MTN.  The company is headquartered in Broomfield, Colorado.\n\nMount Bachelor ski area: Mount Bachelor ski resort is a ski resort located in central Oregon, approximately 22 mi west of Bend, along the Century Drive Highway.  The ski runs are on the northern face of Mount Bachelor, a stratovolcano built atop a volcanic shield in the Cascade Range.  Since 2001, the ski area has been owned by Powdr Corporation of Park City, Utah.  It is the largest ski resort (by area) by more than 1000 acre in Oregon, the second largest single-mountain ski resort in the U.S., behind Vail, and the sixth largest of all ski resorts in the nation.\n\nQuestion: Blue Cow is a ski resort that is part of which is the largest ski resort in the Southern Hemisphere, and is in the Australian Snowy Mountains, the resort is an amalgamation of four villages (Perisher Valley, Smiggin Holes, Guthega, and Blue Cow) and their associated ski fields, covering approximately 12 km2 , with the base elevation at 1720 m AHD, and the summit elevation of 2054 m at the top of Mount Perisher?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"resort_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the ski resort.\"\n    },\n    \"is_largest_in_southern_hemisphere\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the resort is the largest in the Southern Hemisphere.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the resort is located.\"\n        },\n        \"mountain_range\": {\n          \"type\": \"string\",\n          \"description\": \"The mountain range where the resort is located.\"\n        }\n      },\n      \"required\": [\n        \"country\",\n        \"mountain_range\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"amalgamated_villages\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of villages amalgamated into the resort.\"\n    },\n    \"area_km2\": {\n      \"type\": \"number\",\n      \"description\": \"The total area covered by the resort in square kilometers.\"\n    },\n    \"elevations\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"base_elevation_m_ahd\": {\n          \"type\": \"integer\",\n          \"description\": \"The base elevation of the resort in meters AHD.\"\n        },\n        \"summit_elevation_m\": {\n          \"type\": \"integer\",\n          \"description\": \"The summit elevation of the resort in meters.\"\n        }\n      },\n      \"required\": [\n        \"base_elevation_m_ahd\",\n        \"summit_elevation_m\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"resort_name\",\n    \"is_largest_in_southern_hemisphere\",\n    \"location\",\n    \"amalgamated_villages\",\n    \"area_km2\",\n    \"elevations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "resort_name": {
        "type": "string",
        "description": "The name of the ski resort."
      },
      "is_largest_in_southern_hemisphere": {
        "type": "boolean",
        "description": "Indicates if the resort is the largest in the Southern Hemisphere."
      },
      "location": {
        "type": "object",
        "properties": {
          "country": {
            "type": "string",
            "description": "The country where the resort is located."
          },
          "mountain_range": {
            "type": "string",
            "description": "The mountain range where the resort is located."
          }
        },
        "required": [
          "country",
          "mountain_range"
        ],
        "additionalProperties": false
      },
      "amalgamated_villages": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of villages amalgamated into the resort."
      },
      "area_km2": {
        "type": "number",
        "description": "The total area covered by the resort in square kilometers."
      },
      "elevations": {
        "type": "object",
        "properties": {
          "base_elevation_m_ahd": {
            "type": "integer",
            "description": "The base elevation of the resort in meters AHD."
          },
          "summit_elevation_m": {
            "type": "integer",
            "description": "The summit elevation of the resort in meters."
          }
        },
        "required": [
          "base_elevation_m_ahd",
          "summit_elevation_m"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "resort_name",
      "is_largest_in_southern_hemisphere",
      "location",
      "amalgamated_villages",
      "area_km2",
      "elevations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
