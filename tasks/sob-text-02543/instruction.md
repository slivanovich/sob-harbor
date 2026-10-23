{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLincoln, New Hampshire: Lincoln is a town in Grafton County, New Hampshire, United States.  It is the second-largest town by area in New Hampshire.  The population was 1,662 at the 2010 census.  The town is home to the New Hampshire Highland Games and to a portion of Franconia Notch State Park.  Set in the White Mountains, large portions of the town are within the White Mountain National Forest.  The Appalachian Trail crosses in the northeast.  Lincoln is the location of the Loon Mountain ski resort and associated recreation-centered development.\n\nSugar Hill, New Hampshire: Sugar Hill is a town in Grafton County, New Hampshire, United States.  The population was 563 at the 2010 census.  Sugar Hill is a tightly knit community which overlooks the White Mountain National Forest, with views of the Presidential, Franconia, Kinsman and Dalton ranges.  Sugar Hill was incorporated as a town in 1962, making it the most recent in New Hampshire to be split from another town.\n\nWhite Mountain National Forest: The White Mountain National Forest (WMNF) is a federally managed forest contained within the White Mountains in the northeastern United States.  It was established in 1918 as a result of the Weeks Act of 1911; federal acquisition of land had already begun in 1914.  It has a total area of 750852 acre (1,225 sq mi).  Most of the WMNF is in New Hampshire; a small part (about 5.65% of the forest) is in the neighboring state of Maine.  While often casually referred to as a park, this is a National Forest, used not only for hiking, camping, and skiing, but for logging and other limited commercial purposes.  The WMNF is the only National Forest located in either New Hampshire or Maine.  Most of the major peaks over 4,000 feet high for peak-bagging in New Hampshire are located in the National Forest.  Over 100 mi of the Appalachian Trail traverses the White Mountain National Forest.  In descending order of land area the forest lies in parts of Grafton, Coos, and Carroll counties in New Hampshire, and Oxford County in Maine.\n\nGlencliff, New Hampshire: Glencliff is an unincorporated community within the White Mountain National Forest in the town of Warren in Grafton County, New Hampshire, United States.  The village consists of fewer than one hundred residents and some forty man-made structures, including the Willing Workers Hall, the Glencliff Community Chapel, the old firefighter's garage, the Glencliff Improvement Cooperative (community water system), the post office (located in one of the dwellings) and the Glencliff Home for the Elderly (located higher up the mountain).\n\nWoodstock, New Hampshire: Woodstock is a town in Grafton County, New Hampshire, United States.  The population was 1,374 at the 2010 census.  Woodstock includes the village of North Woodstock, the commercial center.  Its extensive land area is largely forested, and includes the Hubbard Brook Experimental Forest.  Parts of the White Mountain National Forest are in the east and west.  The Appalachian Trail crosses the town's northwest corner.  Russell Pond Campground is in the east.  West of North Woodstock is the Lost River Reservation.\n\nFranconia, New Hampshire: Franconia is a town in Grafton County, New Hampshire, United States.  The population was 1,104 at the 2010 census.  Set in the White Mountains, Franconia is home to the northern half of Franconia Notch State Park.  Parts of the White Mountain National Forest are in the eastern and southern portions of the town.  The Appalachian Trail crosses the southern part.\n\nCampton, New Hampshire: Campton is a town in Grafton County, New Hampshire, United States.  The population was 3,333 at the 2010 census.  Campton, which includes the villages of Blair, Campton Hollow, Lower Campton and West Campton, is home to Blair State Forest and Livermore Falls State Forest.  It is located in the foothills of the White Mountains, and parts of the White Mountain National Forest are in the northeast.\n\nWarren, New Hampshire: Warren is a town in Grafton County, New Hampshire, United States.  The population was 904 at the 2010 census.  As of 2015, the estimated population of Warren was 893.  Warren includes the village of Glencliff.\n\nBethlehem, New Hampshire: Bethlehem is a hillside town in Grafton County, New Hampshire, United States.  The population was 2,526 at the 2010 census.  It is home to Cushman and Strawberry Hill state forests.  The eastern half of the town is within the White Mountain National Forest.  The Appalachian Trail crosses in the south.\n\nMoose Mountain (New Hampshire): Moose Mountain is an 8 mi -long ridge located in the eastern part of the town of Hanover in Grafton County, New Hampshire.  The mountain is flanked to the north by Holts Ledge, at 2110 ft , and to the south (across Mascoma Lake) by Shaker Mountain, at 1690 ft .  It is traversed by the Appalachian Trail, a 2170 mi National Scenic Trail from Georgia to Maine.  Moose Mountain is outside the White Mountain National Forest, but the trail runs through a narrow corridor along the ridge which is administered by the U.S. Forest Service.  The trail can be accessed from the south along Three Mile Road in Hanover, and from the north along Goose Pond Road in Lyme, New Hampshire.\n\nQuestion: Glencliff is an unincorporated community within the White Mountain National Forest in the town of Warren, Warren is a town in Grafton County, New Hampshire, in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"community_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the community.\"\n        },\n        \"is_unincorporated\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the community is unincorporated.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_unincorporated\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"parent_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"town_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the town the community is within.\"\n        },\n        \"county_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the county the town is in.\"\n        },\n        \"state_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the state the county is in.\"\n        }\n      },\n      \"required\": [\n        \"town_name\",\n        \"county_name\",\n        \"state_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the locations are situated.\"\n    },\n    \"is_located_within_national_forest\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the community is located within a national forest.\"\n    },\n    \"national_forest_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the national forest the community is within.\"\n    }\n  },\n  \"required\": [\n    \"community_info\",\n    \"parent_location\",\n    \"country\",\n    \"is_located_within_national_forest\",\n    \"national_forest_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "community_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the community."
          },
          "is_unincorporated": {
            "type": "boolean",
            "description": "Indicates if the community is unincorporated."
          }
        },
        "required": [
          "name",
          "is_unincorporated"
        ],
        "additionalProperties": false
      },
      "parent_location": {
        "type": "object",
        "properties": {
          "town_name": {
            "type": "string",
            "description": "The name of the town the community is within."
          },
          "county_name": {
            "type": "string",
            "description": "The name of the county the town is in."
          },
          "state_name": {
            "type": "string",
            "description": "The name of the state the county is in."
          }
        },
        "required": [
          "town_name",
          "county_name",
          "state_name"
        ],
        "additionalProperties": false
      },
      "country": {
        "type": "string",
        "description": "The country where the locations are situated."
      },
      "is_located_within_national_forest": {
        "type": "boolean",
        "description": "Indicates if the community is located within a national forest."
      },
      "national_forest_name": {
        "type": "string",
        "description": "The name of the national forest the community is within."
      }
    },
    "required": [
      "community_info",
      "parent_location",
      "country",
      "is_located_within_national_forest",
      "national_forest_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
