{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRocky Mountains subalpine zone: The Rocky Mountains subalpine zone is the biotic zone immediately below tree line in the Rocky Mountains of North America.  In Colorado, the subalpine zone occupies elevations approximately from 9000 to ; while in northern Alberta, the subalpine zone extends from 1350 to .\n\nFleurieu zone: Fleurieu zone is a wine zone located south of Adelaide in South Australia.  It extends from Kangaroo Island in the west as far north as Flagstaff Hill on the west side of the Mount Lofty Ranges and to as far north as Langhorne Creek on the east side of the Mount Lofty Ranges.  It consists of five following wine regions all of which have received appellation as an Australian Geographical Indication (AGI): Currency Creek, Kangaroo Island, Langhorne Creek, McLaren Vale and the Southern Fleurieu.\n\nMar de Grau: Mar de Grau (Spanish: \"Grau's Sea\" ) is the official name for the body of water in the Pacific Ocean under the control of the South American country of Peru.  This body of water extends in length approximately 3079.50 km, from the parallel of the Boca de Capones in northern Peru to the parallel of the \"Punto Concordia\" and the parallel in front of the city of Tacna in southern Peru.  In terms of width, the maritime zone extends from the Peruvian coast to 200 nautical miles (370.4 km) into the Pacific Ocean.\n\nFar North Football League: The Far North Football League (formerly the Woomera & Districts Football League) is an Australian rules football competition based in the Far North region of South Australia.  It is an affiliated member of the South Australian National Football League.\n\nFar North zone (wine): Far North zone is a wine zone located in the state of South Australia which covers the entire extent of the state north of a line of latitude approximately in line with Crystal Brook, i.e. 33 degrees 21 minutes south.  The zone is bounded by the following wine zones to its south: The Peninsulas, the Mount Lofty Ranges and the Lower Murray (from west to east).  The term ‘Far North’ was registered as an Australian Geographical Indication under the \"Wine Australia Corporation Act 1980\" on 27 December 1996.  As of 2003, the zone only contains one region - the Southern Flinders Ranges.\n\nFar North (South Australia): The Far North is a large region of South Australia close to the Northern Territory border.  Colloquial usage of the term in South Australia refers to that part of South Australia north of a line roughly from Ceduna through Port Augusta to Broken Hill.  The South Australian Government defines the Far North region similarly with the exception of the Maralinga Tjarutja Lands.  the Yalata Aboriginal Reserve and other unincorporated crown lands in the state's far west, which are officially considered part of the Eyre and Western region.\n\nKangaroo Island wine region: Kangaroo Island wine region is a wine region which covers the full extent of Kangaroo Island in South Australia.  The wine region is one of five wine regions comprising the Fleurieu zone.  The term ‘Kangaroo Island’ was registered as an Australian Geographical Indication under the \"Wine Australia Corporation Act 1980\" on 8 December 2000.  As of 2014, the region is reported as containing at least 30 growers and 12 wineries.  As of 2014, the most common plantings within the region within a total planted area of 140 ha was reported as being Shiraz (% ) followed by Cabernet Sauvignon (% ) and Chardonnay (% ).\n\nLower Murray zone (wine): Lower Murray zone is a wine zone located in the state of South Australia which covers the portion of the state south of a line of latitude approximately in line with Crystal Brook, east of a line of longitude approximately in line with Truro and north of a line of latitude approximately in line with Cape Willoughby at the east end of Kangaroo Island.  The zone is bounded by the following wine zones: Far North to its north, the Mount Lofty Ranges, Barossa and Fleurieu (from north to south) to its west and the Limestone Coast to its south.  The term ‘Lower Murray’ was registered as an Australian Geographical Indication under the \"Wine Australia Corporation Act 1980\" on 7 December 1996.  As of 1998, the zone only contains one region - the Riverland.\n\nFlagstaff Hill, South Australia: Flagstaff Hill is a suburb in the City of Onkaparinga local government area.  It is named after the hill by that name in the area, where Colonel William Light erected a flagstaff during his survey, which was then used as a trig point.  Flagstaff Hill is a leafy suburb established around the Sturt Gorge Recreation Park, maintaining many parks and reserves throughout the suburb.\n\nMount Lofty Ranges zone (wine): Mount Lofty Ranges zone is a wine zone located in central South Australia west of the Murray River that occupies the Adelaide metropolitan area north of Glenelg, extending as far north as Crystal Brook, and as far south as Mount Compass in the Mount Lofty Ranges.  The zone which encloses the Barossa zone on three sides, consists of the following wine regions all of which have received appellation as an Australian Geographical Indication (AGI): Adelaide Hills, Adelaide Plains and Clare Valley.  The zone received AGI in 1996.\n\nQuestion: Fleurieu zone extends as far north as a suburb in what South Australian city?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"zone_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the wine zone.\"\n    },\n    \"northern_extent_location\": {\n      \"type\": \"string\",\n      \"description\": \"The specific location marking the northern extent of the zone.\"\n    },\n    \"city_of_northern_extent\": {\n      \"type\": \"string\",\n      \"description\": \"The South Australian city or local government area where the northern extent is located.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the zone and city are located.\"\n    }\n  },\n  \"required\": [\n    \"zone_name\",\n    \"northern_extent_location\",\n    \"city_of_northern_extent\",\n    \"state\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "zone_name": {
        "type": "string",
        "description": "The name of the wine zone."
      },
      "northern_extent_location": {
        "type": "string",
        "description": "The specific location marking the northern extent of the zone."
      },
      "city_of_northern_extent": {
        "type": "string",
        "description": "The South Australian city or local government area where the northern extent is located."
      },
      "state": {
        "type": "string",
        "description": "The state where the zone and city are located."
      }
    },
    "required": [
      "zone_name",
      "northern_extent_location",
      "city_of_northern_extent",
      "state"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
