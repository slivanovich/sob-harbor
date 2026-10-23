{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMount Vernon: Mount Vernon was the plantation house of George Washington, the first President of the United States, and his wife, Martha Dandridge Custis Washington.  The estate is situated on the banks of the Potomac River in Fairfax County, Virginia, near Alexandria, across from Prince George's County, Maryland.  The Washington family had owned land in the area since the time of Washington's great-grandfather in 1674.  In 1739 they embarked on an expansion of the estate that continued under George Washington, who came into possession of the estate in 1754, but did not become its sole owner until 1761.\n\nGeorge Washington's Gristmill: George Washington’s Gristmill was part of the original Mount Vernon plantation, constructed during the lifetime of the United States' first president.  The original structure was destroyed about 1850.  The Commonwealth of Virginia and the Mount Vernon Ladies’ Association have reconstructed the gristmill and the adjacent distillery.  The reconstructed buildings are located at their original site three miles (5 km) west of Mount Vernon proper near Woodlawn Plantation in Alexandria, Virginia.  Because the reconstructed buildings embody the distinctive characteristics of late eighteenth century methods of production and are of importance to the history of Virginia, the site is listed on the National Register of Historic Places despite the fact that the buildings are not original.\n\nCedar Crest (Faunsdale, Alabama): Cedar Crest, also known as Cedar Crest Farms, is a Greek Revival plantation house located near Faunsdale, Alabama.  It was built for Kimbrough Cassels Dubose in 1850 by Albert Prince, a slave.  Dubose, born in Darlington District, South Carolina was educated at the preparatory school of Prof. Stafford who later was of the faculty of the University of Alabama.  His wife was Miss Elizabeth Boykin Witherspoon also of Darlington District, South Carolina, and they had seven sons and four daughters: John Witherspoon, James Henry, Jr., Eugene, Nicholas William, Francis Marion, Lemuel Benton and Edwin Dargan-the daughters Louisa, Rosalie, Augusta and Adele.  The house is one-and-a-half stories with side gables, but has been simplified.  It originally had side wings, with adjoining porches across the front.  These were removed in 1939, leaving the small central front portico.  Another historic plantation house, Altwood, was moved from a nearby location to the Cedar Crest grounds in 1988.  The house was added to the National Register of Historic Places on August 5, 1993 as a part of the Plantation Houses of the Alabama Canebrake and Their Associated Outbuildings Multiple Property Submission.\n\nMount Vernon High School (Ohio): Mount Vernon High School is a public four-year high school located in Mount Vernon, Ohio, United States.  It is the only high school in the Mount Vernon City Schools district.  The school's mascot is the Yellow Jacket, and its official colors are orange and black.  The mascot is actually orange and black rather than yellow and black, due to copyright reasons.  It is located at 300 Martinsburg Road, near State Route 586.  Near the high school is Mount Vernon Middle School, the only one in the district.  Also nearby is Mount Vernon Nazarene University, MVNU.\n\nAnn Pamela Cunningham: Ann Pamela Cunningham (August 15, 1816 Rosemont Plantation, South Carolina - May 1, 1875) is credited with saving George Washington's beloved home Mount Vernon from ruin and neglect.  In a letter to Ann Pamela, Cunningham's mother described the crumbling condition of the estate as she saw it in 1853 while on a steamship heading down the Potomac River.  Cunningham was in her 30s and, having been crippled in a riding accident as a teenager, decided she would initiate a campaign to save the estate.  She raised funds to purchase Mount Vernon by launching an unprecedented appeal for donations through newspaper articles directed toward \"the Ladies of the South\" and founded The Mount Vernon Ladies' Association of the Union, the group that still owns and manages Washington's estate, and served as its first regent.  The group purchased Mount Vernon for $200,000 The Mount Vernon Ladies' Association is the oldest private preservation organization in the United States.\n\nNottoway Plantation: Nottoway Plantation, also known as Nottoway Plantation House is located in White Castle, Louisiana, United States.  The plantation house is a Greek Revival and Italianate-styled mansion built by John Hampden Randolph in 1859, and is the largest extant antebellum plantation house in the South with 53000 sqft of floor space.\n\nRosemont Plantation: Rosemont Plantation is a historic archaeological site located near Waterloo, Laurens County, South Carolina.  Development of the plantation was begun sometime between 1750 and 1790, and reached its zenith during the second quarter of the 19th century.  The main house burned in 1930.  Architectural remains may provide information on intra-site patterning, subsistence data, refuse disposal patterns, architecture and organization of the plantation, and the display of wealth by the plantation owner.  It was the home of Ann Pamela Cunningham, who worked to save George Washington’s Mount Vernon Plantation and served as the first Regent of the Mount Vernon Ladies' Association of the Union.\n\nHampton Plantation: Hampton Plantation, also known as Hampton Plantation House and Hampton Plantation State Historic Site, is a historic plantation, now a state historic site, north of McClellanville, South Carolina.  The plantation was established in 1735, and its main house exhibits one of the earliest known examples in the United States of a temple front in domestic architecture.  It is also one of the state's finest examples of a wood frame Georgian plantation house.  It was declared a National Historic Landmark in 1970.\n\nMount Vernon (Woodleaf, North Carolina): Mount Vernon is a historic plantation house, farm complex, and national historic district located near Woodleaf, Rowan County, North Carolina.  The house was built about 1822, and is a two-story, three bay, Federal style frame dwelling.  It is sheathed in weatherboard and has a full-width, one-story shed roofed porch.  The house was designated a post office in 1822.  Also on the property are the contributing log smokehouse, large barn (c. 1898), \"lighthouse\" or Delco house (c. 1917), corn crib (c. 1917), gear house (c. 1917), woodhouse (c. 1917), spring house, mill site, shop, and plantation office.\n\nHercules (chef): Hercules – also known as \"Herculas\" or \"Uncle Harkless\" – was a slave who worked at Mount Vernon, George Washington's Virginia plantation on the Potomac River.  He was the head cook at the mansion in the 1780s, cooking for the Washington family and their guests.  In 1790 President Washington brought him to Philadelphia, Pennsylvania (then the temporary national capital) to cook in the kitchen of the President's House.  Hercules escaped to freedom from Mount Vernon in 1797, and later was legally manumitted under the terms of Washington's will.\n\nQuestion: Hercules, also known as \"Herculas\" or \"Uncle Harkless\", was a slave who worked at Mount Vernon, the plantation house of who, the first President of the United States?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"plantation_owner\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the owner of the plantation.\"\n        },\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The official title or role of the owner.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"plantation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the plantation.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The county and state where the plantation is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"worker_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the worker.\"\n        },\n        \"status\": {\n          \"type\": \"string\",\n          \"description\": \"The status of the worker (e.g., slave).\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The primary role or occupation of the worker at the plantation.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"status\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"plantation_owner\",\n    \"plantation_details\",\n    \"worker_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "plantation_owner": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the owner of the plantation."
          },
          "title": {
            "type": "string",
            "description": "The official title or role of the owner."
          }
        },
        "required": [
          "name",
          "title"
        ],
        "additionalProperties": false
      },
      "plantation_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the plantation."
          },
          "location": {
            "type": "string",
            "description": "The county and state where the plantation is located."
          }
        },
        "required": [
          "name",
          "location"
        ],
        "additionalProperties": false
      },
      "worker_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the worker."
          },
          "status": {
            "type": "string",
            "description": "The status of the worker (e.g., slave)."
          },
          "role": {
            "type": "string",
            "description": "The primary role or occupation of the worker at the plantation."
          }
        },
        "required": [
          "name",
          "status",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "plantation_owner",
      "plantation_details",
      "worker_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
