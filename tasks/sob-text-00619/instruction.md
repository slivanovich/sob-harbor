{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNorthwest Montana Wetland Management District: The Northwest Montana Wetland Management District is located in the U.S. state of Montana and is an integral part of the National Bison Range Complex along with four other wildlife refuges and the National Bison Range.  The district comprises numerous small wetland environments set aside primarily to protect areas for waterfowl.  The district comprises 14 separate Waterfowl Production Areas (WPA)'s totalling 8452 acre and one 6300 acre conservation easement along the north shores of Flathead Lake.  Some of the land is located on the Flathead Indian Reservation (known as the Tribal Trust Lands of the Confederated Salish and Kootenai Tribes) and they continue to have claim over the land provided they assist in maintaining the resource.  The Northwest Montana Wetland Management District is administered by the U.S. Fish and Wildlife Service, an agency within the U.S. Department of the Interior.  The individual lands were acquired beginning in 1970 by purchasing plots from willing landowners, and an ongoing effort to continue to increase area.\n\nKulm Wetland Management District: Located in south-central North Dakota, Kulm Wetland Management District was established in 1971.  Located in the Prairie Pothole Region of North America, Kulm Wetland Management District provides breeding, nesting, and brood rearing areas for many species of waterfowl and other migratory birds.  The District currently manages 201 waterfowl production areas that total 45683 acre , 3 national wildlife refuges that are easement refuges (Bone Hill NWR, Dakota Lake NWR, Maple River NWR), and 120000 acre of wetland and grassland easements.  The District's headquarters is in Kulm, North Dakota.\n\nLong Lake Wetland Management District: Long Lake Wetland Management District encompasses three counties in south-central North Dakota, an area famed for its wealth of waterfowl-producing potholes and native prairie grasslands. Headquarters for the Wetland Management District is located in the Long Lake National Wildlife Refuge office near Moffit, North Dakota, which is about 35 miles southeast of Bismarck.  Topographical landforms of the area include Missouri Coteau and Missouri River Slope.  Precipitation averages just under 16 inches per year.  Approximately 68 percent of the land in the three county area remains virgin sod - native mixed-grass prairie.  The dominant land use is cattle grazing.  The Coteau wetlands found in the northeastern portion of the Wetland Management District are classic prairie potholes of various sizes and types that are prime duck production habitat.  These areas, when wet, are very productive.  Soils in this area are generally deep and quite productive.  Due to the rolling nature of the landscape on the Coteau, a lot of the land is also characterized as highly erodible.  Conversely, many of the wetlands on Missouri River Slope portion of the Wetland Management District are large semi-permanent and permanent alkali wetlands.  There are 21 wetland sites on the Missouri River Slope that have a history of periodic avian botulism outbreaks.  These areas occasionally present localized problems for significant numbers of migratory birds.  Soils on the Missouri River Slope are characteristically shallow with high proportions of sand and gravel.  Much of the land is highly erodible.  Since 1985, substantial land acreage in the three county area that was once farmed has been retired to Conservation Reserve Program grasslands.  The program has assisted in restoring waterfowl populations for many species in the Wetland Management District which exceed the highest level ever recorded since surveys began.\n\nLouisiana Wetland Management District: The Louisiana Wetland Management District was established in September 1990 in response to growing U.S. Fish and Wildlife Service responsibilities on lands that were off traditional refuges.  These include Farmer's Home Administration (FmHA) and fee title tracts, leases and work on private lands.  The Wetland Management District encompasses 20 parishes in the northern half of the state.  Most of the 37 FmHA easements, 10 fee title tracts, and 4 leases are concentrated in northeastern Louisiana.  Louisiana Wetland Management District currently oversees Service interests on 25710 acre not including Partners agreements\n\nNational Bison Range Complex: The National Bison Range Complex includes four National Wildlife Refuges and the Northwest Montana Wetland Management District, and is located in the northwestern region of Montana in the northwestern United States.\n\nMorris Wetland Management District: The Morris Wetland Management District includes 244 waterfowl production areas, encompassing over 50000 acre scattered throughout an eight-county area.  Like other wetland management districts in the prairie states, the goal of the Morris District is to restore and protect sufficient wetland and grassland habitat to meet the needs of prairie wildlife, particularly breeding waterfowl, as well as provide places for public recreation.\n\nLeopold Wetland Management District: The Leopold Wetland Management District is named after Aldo Leopold, who is widely acknowledged as the father of wildlife conservation in America.  Leopold is perhaps best known as the author of \"A Sand County Almanac\", a book compiled of essays written on his farm in central Wisconsin.  In tribute to his philosophy, the Leopold Wetland Management District is dedicated to preserving, restoring, and enhancing wildlife habitat in Wisconsin for the benefit of present and future generations.\n\nDevils Lake Wetland Management District: Devils Lake Wetland Management District is located in the heart of the Prairie Pothole Region of the United States.  The District was established in 1962 to purchase and protect wetland habitat for migratory waterfowl and other wildlife in northeastern North Dakota.  One of the primary objectives of Devils Lake Wetland Management District is to provide wetland and grassland habitat for waterfowl in the spring and summer for nesting and feeding.  The other primary objective is to provide migration habitat for waterfowl in the spring and fall.\n\nNational Bison Range: The National Bison Range (NBR) is a National Wildlife Refuge located in western Montana established in 1908 to provide a sanctuary for the American bison.  The NBR is one of the oldest National Wildlife Refuges in the United States.  The size of the bison herd at the NBR is relatively small, numbering between 350 and 500 individuals.  The initial herd of American bison was provided by organizations such as the American Bison Society, and today the refuge serves as the central point for bison research in the United States.\n\nSand Lake Wetland Management District: Sand Lake Wetland Management District is located in the U.S. state of South Dakota and is administered by the U.S. Fish and Wildlife Service.  This is the largest Wetland Management District in the U.S., with 45,000 acres (182 km) of area directly under federal protection and another 550,000 acres (2,225 km) managed in partnership with private landowners as conservation easements.  A total of 162 Waterfowl Production areas are located on the federally owned lands and the conservation easements are generally adjacent to these areas and act as buffer zones to increase habitat protection.\n\nQuestion: What can be found in the Northwest Montana Wetland Management District? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"district_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the wetland management district.\"\n    },\n    \"location_state\": {\n      \"type\": \"string\",\n      \"description\": \"The U.S. state where the district is located.\"\n    },\n    \"primary_purpose\": {\n      \"type\": \"string\",\n      \"description\": \"The main objective or purpose of the district.\"\n    },\n    \"administered_by\": {\n      \"type\": \"string\",\n      \"description\": \"The agency responsible for administering the district.\"\n    },\n    \"land_holdings\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the land areas managed by the district.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"type\": {\n            \"type\": \"string\",\n            \"enum\": [\n              \"Waterfowl Production Areas\",\n              \"conservation easement\"\n            ]\n          },\n          \"count\": {\n            \"type\": \"integer\",\n            \"description\": \"The number of areas of this type.\"\n          },\n          \"total_acreage\": {\n            \"type\": \"integer\",\n            \"description\": \"The total acreage for this type of land holding.\"\n          },\n          \"description\": {\n            \"type\": \"string\",\n            \"description\": \"Additional descriptive information for the land holding, if available.\"\n          }\n        },\n        \"required\": [\n          \"type\",\n          \"total_acreage\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"associated_complex\": {\n      \"type\": \"object\",\n      \"description\": \"Information about the larger complex the district is part of, and other entities within that complex.\",\n      \"properties\": {\n        \"complex_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the complex.\"\n        },\n        \"other_integral_parts\": {\n          \"type\": \"array\",\n          \"description\": \"Other entities that are integral parts of the same complex as the district.\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"complex_name\",\n        \"other_integral_parts\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"district_name\",\n    \"location_state\",\n    \"primary_purpose\",\n    \"administered_by\",\n    \"land_holdings\",\n    \"associated_complex\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "district_name": {
        "type": "string",
        "description": "The name of the wetland management district."
      },
      "location_state": {
        "type": "string",
        "description": "The U.S. state where the district is located."
      },
      "primary_purpose": {
        "type": "string",
        "description": "The main objective or purpose of the district."
      },
      "administered_by": {
        "type": "string",
        "description": "The agency responsible for administering the district."
      },
      "land_holdings": {
        "type": "array",
        "description": "Details about the land areas managed by the district.",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "Waterfowl Production Areas",
                "conservation easement"
              ]
            },
            "count": {
              "type": "integer",
              "description": "The number of areas of this type."
            },
            "total_acreage": {
              "type": "integer",
              "description": "The total acreage for this type of land holding."
            },
            "description": {
              "type": "string",
              "description": "Additional descriptive information for the land holding, if available."
            }
          },
          "required": [
            "type",
            "total_acreage"
          ],
          "additionalProperties": false
        }
      },
      "associated_complex": {
        "type": "object",
        "description": "Information about the larger complex the district is part of, and other entities within that complex.",
        "properties": {
          "complex_name": {
            "type": "string",
            "description": "The name of the complex."
          },
          "other_integral_parts": {
            "type": "array",
            "description": "Other entities that are integral parts of the same complex as the district.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "complex_name",
          "other_integral_parts"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "district_name",
      "location_state",
      "primary_purpose",
      "administered_by",
      "land_holdings",
      "associated_complex"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
