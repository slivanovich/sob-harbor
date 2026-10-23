{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSquare Schoolhouse: The Square Schoolhouse is a historic schoolhouse at the junction of New Hampshire Route 156 and Ledge Hill Road in Nottingham, New Hampshire.  The two-story wood frame building was built in 1850 as the first schoolhouse in the town, a purpose it served until 1920.  The schoolhouse is now owned by the Else Cilley Chapter of the Daughters of the American Revolution It is named not for its shape, but for its location in Nottingham Square.\n\nNew Hampshire Route 97: New Hampshire Route 97 (abbreviated NH 97) is a 2.563 mi east–west state highway in Salem, Rockingham County, New Hampshire.  The western terminus of the route is in the center of Salem at New Hampshire Route 28 (Broadway).  The eastern terminus is at the Massachusetts state line, where the road continues east as Massachusetts Route 97 and continues on to Haverhill.  NH 97 is named Main Street along its entire length.\n\nNew Hampshire Route 156: New Hampshire Route 156 (NH 156) is a 6.424 mi secondary north–south highway in Rockingham County in southeastern New Hampshire.  The road runs from Raymond to Nottingham.\n\nNew Hampshire Route 153: New Hampshire Route 153 is a 50.566 mi secondary north–south highway in Strafford and Carroll counties in eastern New Hampshire.  The southern terminus is in Farmington at New Hampshire Route 11.  The northern terminus is in Conway village (town of Conway) at New Hampshire Route 16 and New Hampshire Route 113.\n\nWest Nottingham, New Hampshire: West Nottingham is an unincorporated community in the town of Nottingham in Rockingham County, New Hampshire, United States.  It is located along New Hampshire Route 152, 1 mi south of U.S. Route 4 and 5 mi north of the town center of Nottingham.\n\nNew Hampshire Route 108: New Hampshire Route 108 is a 42.430 mi north–south state highway in Rockingham and Strafford counties in southeastern New Hampshire.  The southern terminus of NH 108 is at the Massachusetts state line in Plaistow.  The northern terminus is at an intersection with New Hampshire Route 125 and New Hampshire Route 202A in downtown Rochester.\n\nRaymond, New Hampshire: Raymond is a town in Rockingham County, New Hampshire, United States.  The population was 10,138 at the 2010 census, and the estimated population in 2016 was 10,285.  Part of Pawtuckaway State Park is in the north.\n\nNew Hampshire Route 84: New Hampshire Route 84 is a 4.184 mi secondary east–west state highway in Rockingham County in southeastern New Hampshire.  The eastern terminus of NH 84 is in Hampton Falls at U.S. Route 1.  The western terminus is in Kensington at New Hampshire Route 150.\n\nNew Hampshire Route 202A: New Hampshire Route 202A (abbreviated NH 202A) is a 14.639 mi east–west state highway in Strafford and Rockingham counties in southeastern New Hampshire.  The western terminus is in Northwood at U.S. Route 202 and New Hampshire 9, near their intersection with U.S. Route 4.  Its eastern terminus is in downtown Rochester at New Hampshire Route 108 and New Hampshire Route 125.\n\nNew Hampshire Route 87: New Hampshire Route 87 is a 6.317 mi east–west highway in Rockingham County in southeastern New Hampshire connecting Newfields to Epping.  The eastern terminus of NH 87 is in Newfields at its junction with New Hampshire Route 85.  The western terminus is in Epping at its junction with New Hampshire Route 125.\n\nQuestion: New Hampshire Route 156 runs from Nottingham to which New Hampshire town in Rockingham County?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"route_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of the New Hampshire Route.\"\n    },\n    \"start_town\": {\n      \"type\": \"string\",\n      \"description\": \"One of the towns the route connects.\"\n    },\n    \"end_town\": {\n      \"type\": \"string\",\n      \"description\": \"The other town the route connects, which is the answer to the question.\"\n    },\n    \"end_town_county\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the end_town is located.\"\n    }\n  },\n  \"required\": [\n    \"route_number\",\n    \"start_town\",\n    \"end_town\",\n    \"end_town_county\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "route_number": {
        "type": "integer",
        "description": "The number of the New Hampshire Route."
      },
      "start_town": {
        "type": "string",
        "description": "One of the towns the route connects."
      },
      "end_town": {
        "type": "string",
        "description": "The other town the route connects, which is the answer to the question."
      },
      "end_town_county": {
        "type": "string",
        "description": "The county where the end_town is located."
      }
    },
    "required": [
      "route_number",
      "start_town",
      "end_town",
      "end_town_county"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
