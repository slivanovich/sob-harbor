{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNewichawannock Canal: The Newichawannock Canal is a man-made canal which drains Great East Lake into Horn Pond at the border between Wakefield, New Hampshire, and Acton, Maine, in the northeastern United States.  It is at the head of the Salmon Falls River, which the Abenaki called \"Newichawannock\", meaning \"river with many falls\".  Begun in 1850 by the Great Falls Company to increase the water available for its mills in Somersworth, New Hampshire, the 0.75 mi canal is unusual as it was built for strictly industrial purposes in an area remote from the actual industrial site.  The canal forms the boundary between the states of New Hampshire and Maine, and is spanned by a stone bridge built at the same time.  The canal and bridge, along with related artifacts, were listed on the National Register of Historic Places in 2014.\n\nVaughan Woods State Park: Vaughan Woods State Park is a public recreation area located along the Salmon Falls River on the western edge of South Berwick, Maine, at the New Hampshire border.  The state park includes the restored Hamilton House, stands of old-growth forest, and 3 mi of hiking trails.  The lands were bequeathed to the state by Elizabeth Vaughan in 1949.\n\nPortland &amp; Rochester Railroad: The Portland and Rochester Railroad, established in 1867, was an important predecessor railway of the Rochester to Portland branch line of the Boston and Maine Railroad.  It was founded in the merger of several smaller shortline rail transport companies, the oldest being the shortline York and Cumberland Railroad which was formed in 1846 to connect the seaport facilities of Portland, Maine, to the water powered manufacturing and textile industries along the Quampheagan Falls on the Salmon Falls River in the twin towns of South Berwick, Maine, and Rollinsford, New Hampshire (ca 1850).\n\nSalmon Falls River: The Salmon Falls River is a tributary of the Piscataqua River in the U.S. states of Maine and New Hampshire.  It rises at Great East Lake, Newichawannock Canal, and Horn Pond and flows south-southeast for approximately 38 mi , forming the border between York County, Maine, and Strafford County, New Hampshire.\n\nGreat East Lake: Great East Lake is an 1825 acre water body located in Carroll County, New Hampshire, and York County, Maine, in the United States.  The lake is shared by the towns of Wakefield, New Hampshire, and Acton, Maine, with 45% of its surface area in Acton and 55% in Wakefield.  The lake is the farthest upstream of the five headwater lakes of the Salmon Falls River, a tributary of the Piscataqua River.  Water from Great East Lake flows out its dam and through the 800 ft Newichawannock Canal into Horn Pond, then into the Salmon Falls River below Horn Pond.\n\nLovell Lake: Lovell Lake is a 538 acre water body in Carroll County in eastern New Hampshire, United States, in the town of Wakefield.  The lake is both spring-fed and fed by small streams including Horse Brook.  The outlet of the lake, located at the village of Sanbornville, is the beginning of the Branch River.  From here, the Branch River flows through Milton where it joins the Salmon Falls River on the Maine-New Hampshire border.  The Salmon Falls River empties into the tidal waters of the Piscataqua River northwest of Portsmouth, New Hampshire, then into the Gulf of Maine.\n\nBerwick Academy (Maine): Berwick Academy is a college preparatory school located in South Berwick, Maine.  Founded in 1791, it is the oldest educational institution in Maine and one of the oldest private schools in North America.  The school sits on a 72-acre, 11-building campus on a hill overlooking the Salmon Falls River, near the border between Maine and New Hampshire.  Approximately 565 students in grades Pre-K through 12 (and Post-Grad) attend this coeducational day school, from approximately 60 communities in the surrounding regions of southern Maine, southeastern New Hampshire and northeastern Massachusetts.\n\nSalmon Falls Mill Historic District: The Salmon Falls Mill Historic District encompasses a historic mill complex on Front Street in Rollinsford, New Hampshire.  The complex includes four major structures and seven smaller ones, on about 14 acre of land along the Salmon Falls River.  They were built between about 1840 and the mid-1860s, and have an unusual architectural unity, for additions made to the buildings were done with attention to matching elements of the existing structures.  The Number 2 Mill, built in 1848, was an early location where a turbine was used instead of a waterwheel to provide power to the mill machinery.  The district was listed on the National Register of Historic Places in 1980.\n\nLittle River (Salmon Falls River): The Little River is a 21.3 mi tributary of the Salmon Falls River in the U.S. state of Maine.  It rises from streams in York County, flows southwest through Lebanon, and reaches its confluence with the Salmon Falls River in Berwick.\n\nHorn Pond: Horn Pond is a 227 acre water body located on the border of Acton, Maine, and Wakefield, New Hampshire, in the United States.  The lake is both spring-fed and fed by the outflows of Great East Lake to the north and Wilson Lake to the east.  Horn Pond's outlet is the Salmon Falls River which forms a natural border between Maine and New Hampshire and empties into the Piscataqua River east of Dover, New Hampshire, and ultimately the Gulf of Maine.\n\nQuestion: This U.S. state's oldest school, Berwick Academy, overlooks the Salmon Falls River which forms part of the state border with New Hampshire. Name the state.\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"state_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the U.S. state.\"\n    },\n    \"school_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"school_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the school.\"\n        },\n        \"location_town\": {\n          \"type\": \"string\",\n          \"description\": \"The town where the school is located.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the school was founded.\"\n        },\n        \"oldest_in_state\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the school is the oldest educational institution in the state.\"\n        }\n      },\n      \"required\": [\n        \"school_name\",\n        \"location_town\",\n        \"founding_year\",\n        \"oldest_in_state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"river_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"river_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the river.\"\n        },\n        \"forms_state_border\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the river forms part of a state border.\"\n        }\n      },\n      \"required\": [\n        \"river_name\",\n        \"forms_state_border\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"state_name\",\n    \"school_information\",\n    \"river_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "state_name": {
        "type": "string",
        "description": "The name of the U.S. state."
      },
      "school_information": {
        "type": "object",
        "properties": {
          "school_name": {
            "type": "string",
            "description": "The name of the school."
          },
          "location_town": {
            "type": "string",
            "description": "The town where the school is located."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the school was founded."
          },
          "oldest_in_state": {
            "type": "boolean",
            "description": "Indicates if the school is the oldest educational institution in the state."
          }
        },
        "required": [
          "school_name",
          "location_town",
          "founding_year",
          "oldest_in_state"
        ],
        "additionalProperties": false
      },
      "river_information": {
        "type": "object",
        "properties": {
          "river_name": {
            "type": "string",
            "description": "The name of the river."
          },
          "forms_state_border": {
            "type": "boolean",
            "description": "Indicates if the river forms part of a state border."
          }
        },
        "required": [
          "river_name",
          "forms_state_border"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "state_name",
      "school_information",
      "river_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
