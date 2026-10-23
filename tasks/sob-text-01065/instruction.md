{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAmargosa, Texas: Amargosa is an unincorporated community and census-designated place in Jim Wells County, Texas, United States.  Its population was 291 as of the 2010 census.  Prior to 2010, the community was grouped with nearby Owl Ranch as part of the Owl Ranch-Amargosa census-designated place.  The community is named for the Amargosa Creek that runs nearby.  The word \"amargosa\" means \"bitter\" in Spanish.\n\nElmont, New York: Elmont is an unincorporated community and census-designated place (CDP) located in northwestern Hempstead in Nassau County, New York, United States, along its border with the borough of Queens in New York City.  It is a suburban bedroom community located on Long Island.  The population was 33,198 at the 2010 census.\n\nGreenbrae, California: Greenbrae is a small unincorporated community in Marin County, California.  It is located 1.5 mi south-southeast of downtown San Rafael, at an elevation of 33 feet (10 m), located adjacent to U.S. Route 101 at the opening of the Ross Valley.  Part of Greenbrae is an unincorporated community of the county while the remaining area is inside the city limits of Larkspur.  The ZIP code is 94904, and is shared with the neighboring Census-designated place (CDP) of Kentfield.  The community is in area codes 415 and 628.\n\nNew York Stakes: The New York Stakes is an American Thoroughbred horse race held annually at Belmont Park in Elmont, Long Island, New York.  A Grade II event open to fillies and mares age four and older, it is contested on turf at a distance of one and one-quarter miles (10 furlongs).  In 2015, the date for the race was moved to the Friday before the Belmont Stakes as part of the Belmont Racing Festival.  For 2016, the purse was increased to $500,000.\n\nTantallon, Maryland: Tantallon is an unincorporated community in Prince George's County, Maryland, United States.  Although a separate community, it is a part of the census-designated place (CDP) of Fort Washington.  The ZIP code for the community is 20744.  Tantallon reported as an census-designated place by the U.S. Census Bureau in 1980, which included much of the northern half of Fort Washington's census area.  The population recorded was 9,945.\n\nEnhaut, Pennsylvania: Enhaut is an unincorporated community and census-designated place (CDP) located in Dauphin County in the state of Pennsylvania.  The community was formerly part of the census-designated place of Bressler-Enhaut-Oberlin, before splitting into three separate CDPs for the 2010 census.  As of the 2010 census the population in Enhaut was 1,007.\n\nOberlin, Pennsylvania: Oberlin is an unincorporated community and census-designated place (CDP) located in Dauphin County, Pennsylvania, United States.  The community was part of the census-designated place of Bressler-Enhaut-Oberlin, before it was split into three separate CDPs for the 2010 census.  As of the 2010 census the population was 588.\n\nAbram, Texas: Abram is an unincorporated community and census-designated place in Hidalgo County, Texas, United States.  Its population was 2,067 as of the 2010 census.  Prior to 2010, the community was part of the Abram-Perezville census-designated place with nearby Perezville.  The community was named after Texas Ranger Abram Dillard, who was a resident of the area.\n\nMatron Stakes (Belmont Park): The Matron Stakes is an American Thoroughbred horse race held annually during the Fall at Belmont Park in Elmont, Long Island, New York (but was just lately a Spring/Summer event along with the Futurity Stakes).  Open to two-year-old fillies, it is contested on dirt at a distance at seven furlongs.  It is a former Grade I stakes but since 2007 has been a Grade II event.  In effect, it is a filly counterpart to the Belmont Futurity Stakes.  It is now a Grade III event.\n\nBull Mountain, Oregon: Bull Mountain is an unincorporated community and census-designated place in Washington County, Oregon, United States.  Bull Mountain is located mostly on a hill for which the community is named.  It is bordered on the east by Tigard, on the south by King City, and Beaverton lies to the north.  The north-eastern part of the Bull Mountain hill is now within the Tigard city limits, as the city has steadily annexed portions of the unincorporated region on its boundary.  In 2010, the community became a census-designated place with a population of 9,133.  Fire protection and EMS services are provided through Tualatin Valley Fire and Rescue.\n\nQuestion: Where is the unincorporated community and census-designated place which The New York Stakes is been held annually located\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the horse racing event.\"\n    },\n    \"venue_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the venue where the event is held.\"\n    },\n    \"community_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"community_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the community where the venue is located.\"\n        },\n        \"is_unincorporated\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the community is unincorporated.\"\n        },\n        \"is_cdp\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the community is a census-designated place (CDP).\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the community is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the community is located.\"\n        },\n        \"located_within\": {\n          \"type\": \"string\",\n          \"description\": \"The specific area or larger entity within which the community is located.\"\n        }\n      },\n      \"required\": [\n        \"community_name\",\n        \"is_unincorporated\",\n        \"is_cdp\",\n        \"county\",\n        \"state\",\n        \"located_within\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The specific location of the unincorporated community and CDP where the event is held.\"\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"venue_name\",\n    \"community_details\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the horse racing event."
      },
      "venue_name": {
        "type": "string",
        "description": "The name of the venue where the event is held."
      },
      "community_details": {
        "type": "object",
        "properties": {
          "community_name": {
            "type": "string",
            "description": "The name of the community where the venue is located."
          },
          "is_unincorporated": {
            "type": "boolean",
            "description": "Indicates if the community is unincorporated."
          },
          "is_cdp": {
            "type": "boolean",
            "description": "Indicates if the community is a census-designated place (CDP)."
          },
          "county": {
            "type": "string",
            "description": "The county where the community is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the community is located."
          },
          "located_within": {
            "type": "string",
            "description": "The specific area or larger entity within which the community is located."
          }
        },
        "required": [
          "community_name",
          "is_unincorporated",
          "is_cdp",
          "county",
          "state",
          "located_within"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The specific location of the unincorporated community and CDP where the event is held."
      }
    },
    "required": [
      "event_name",
      "venue_name",
      "community_details",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
