{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUSS Asheville (PG-21): USS \"Asheville\" (Gunboat No. 21/PG-21), the lead ship in her class of two United States Navy gunboats, was the first ship of the United States Navy named for the city of Asheville, North Carolina.  The ship was built at the Charleston Naval Shipyard of North Charleston, South Carolina, from her keel laying in June 1918, her launching in July 1918, and her commissioning in July 1920.\n\nUSS Hyman: USS \"Hyman\" (DD-732), an \"Allen M. Sumner\"-class destroyer , was a ship of the United States Navy named for Lieutenant Commander Willford Milton Hyman, who commanded the destroyer USS \"Sims\" during the Battle of the Coral Sea.  During the battle, \"Sims\" was lost and Hyman went down with his ship on 7 May 1942.  He was posthumously awarded the Navy Cross.  \"Hyman\" was laid down by Bath Iron Works, Bath, Maine on 22 November 1943, was launched on 8 April 1944 and commissioned on 16 June 1944.\n\nWaldo Canyon Fire: The Waldo Canyon fire was a forest fire that started approximately 4 mi northwest of Colorado Springs, Colorado on June 23, 2012 and was declared 100 percent contained on July 10, 2012 after no smoke plumes were visible on a small portion of the containment line on Blodgett Peak.  The fire was active in the Pike National Forest and adjoining areas, covering a total of 18247 acre .  The fire had caused the evacuation of over 32,000 residents of Colorado Springs, Manitou Springs and Woodland Park, several small mountain communities along the southwestern side of Highway 24, and partial evacuation of the United States Air Force Academy.  There were 346 homes destroyed by the fire.  U.S. Highway 24, a major east-west road, was closed in both directions.  The Waldo Canyon Fire resulted in insurance claims totaling more than US $453.7 million.  It was the most destructive fire in Colorado state history, as measured by the number of homes destroyed, until the Black Forest Fire surpassed it almost a year later when it consumed 486 homes and damaged 28 others.\n\nUSS Kearsarge (LHD-3): USS \"Kearsarge\" (LHD-3) is the third \"Wasp\"-class amphibious assault ship of the United States Navy.  She is the fifth ship to be named (the fourth actually commissioned) in honor of USS \"Kearsarge\" , a sloop-of-war that gained fame during the American Civil War, which was in turn named for Mount Kearsarge in New Hampshire.\n\nUSS Kearsarge (1861): USS \"Kearsarge\", a \"Mohican\"-class sloop-of-war, is best known for her defeat of the Confederate commerce raider  during the American Civil War.  \"Kearsarge\" was the only ship of the United States Navy named for Mount Kearsarge in New Hampshire.  Subsequent ships were later named \"Kearsarge\" in honor of the ship.\n\nDesolation Peak (Washington): Desolation Peak is in the North Cascade Mountains of Washington state, about 6.2 mi south of the Canada–United States border and in the Ross Lake National Recreation Area.  It was first climbed in 1926 by Lage Wernstedt, who named it for the destruction caused by a forest fire that swept the slopes bare that same year.  At the summit stands a small, wooden, one room fire lookout belonging to the National Park Service.  The lookout is 15 mi from the nearest road and overlooks miles of forest and numerous other peaks.\n\nMount Kearsarge (Merrimack County, New Hampshire): Mount Kearsarge is a mountain located in Wilmot, New Hampshire, and Warner, New Hampshire.  Two state parks are located on the mountain: Winslow State Park and Rollins State Park.  On a very clear day, skyscrapers in the city of Boston, Massachusetts 80 mi away are visible from the fire tower on the summit.  The summit has remained bare since a 1796 forest fire.\n\nUSS Kearsarge (BB-5): USS \"Kearsarge\" (BB-5), the lead ship of her class of pre-dreadnought battleships, was a United States Navy ship, named after the sloop-of-war \"Kearsarge\" .  Her keel was laid down by the Newport News Shipbuilding Company of Virginia, on 30 June 1896.  She was launched on 24 March 1898, sponsored by the wife of Rear Admiral Herbert Winslow, and commissioned on 20 February 1900.\n\nKearsarge-class battleship: The \"Kearsarge\"-class battleships were two pre-dreadnought battleships built for the United States Navy at the beginning of the 20th century.  They were designed to be used for coastal defense.  Both of the ships, USS \"Kearsarge\" and USS \"Kentucky\" , were authorized in 1895 and commissioned in 1900.  Neither ship participated in a major battle, although they participated in the Great White Fleet, the oldest ships on the cruise.  \"Kentucky\" was decommissioned in 1920 and sold for scrap in 1923.  \"Kearsarge\" was also decommissioned in 1920, although it was then converted into a crane ship, and served in that capacity until scrapping in 1955.\n\nUSS Kearsarge (CV-33): USS \"Kearsarge\" (CV/CVA/CVS-33) was one of 24 \"Essex\"-class aircraft carrier s completed during or shortly after World War II for the United States Navy.  The ship was the third US Navy ship to bear the name, and was named for a Civil War-era steam sloop.  \"Kearsarge\" was commissioned in March 1946.  Modernized in the early 1950s as an attack carrier (CVA), she served in the Korean War, for which she earned two battle stars.  In the late 1950s she was further modified to become an anti-submarine carrier (CVS).  \"Kearsarge\" was the recovery ship for the last two manned Project Mercury space missions in 1962–1963.  She completed her career serving in the Vietnam War, earning five battle stars.\n\nQuestion: USS \"Kearsarge\" was the only ship of the United States Navy named for a mountain whose summit has remained bare since a forest fire in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ship_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the ship.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type or class of the ship.\"\n        },\n        \"naming_reason\": {\n          \"type\": \"string\",\n          \"description\": \"The reason or entity the ship was named after.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"naming_reason\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mountain_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the mountain.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the mountain is located.\"\n        },\n        \"summit_condition\": {\n          \"type\": \"string\",\n          \"description\": \"The current condition of the mountain's summit.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\",\n        \"summit_condition\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of event that caused the summit condition.\"\n        },\n        \"event_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the event occurred.\"\n        }\n      },\n      \"required\": [\n        \"event_type\",\n        \"event_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"ship_details\",\n    \"mountain_details\",\n    \"event_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ship_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the ship."
          },
          "type": {
            "type": "string",
            "description": "The type or class of the ship."
          },
          "naming_reason": {
            "type": "string",
            "description": "The reason or entity the ship was named after."
          }
        },
        "required": [
          "name",
          "type",
          "naming_reason"
        ],
        "additionalProperties": false
      },
      "mountain_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the mountain."
          },
          "location": {
            "type": "string",
            "description": "The state where the mountain is located."
          },
          "summit_condition": {
            "type": "string",
            "description": "The current condition of the mountain's summit."
          }
        },
        "required": [
          "name",
          "location",
          "summit_condition"
        ],
        "additionalProperties": false
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_type": {
            "type": "string",
            "description": "The type of event that caused the summit condition."
          },
          "event_year": {
            "type": "integer",
            "description": "The year the event occurred."
          }
        },
        "required": [
          "event_type",
          "event_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "ship_details",
      "mountain_details",
      "event_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
