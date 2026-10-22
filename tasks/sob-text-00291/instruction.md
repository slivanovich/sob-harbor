Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
1964 Minnesota Golden Gophers baseball team: The 1964 Minnesota Golden Gophers baseball team represented the University of Minnesota in the 1964 NCAA University Division baseball season.  The Golden Gophers played their home games at Delta Field.  The team was coached by Dick Siebert in his 17th season at Minnesota.

2003 Minnesota Golden Gophers football team: The 2003 Minnesota Golden Gophers football team represented the University of Minnesota in the 2003 NCAA Division I-A football season.  In their seventh year under head coach Glen Mason, the Golden Gophers compiled a 10–3 record and outscored their opponents by a combined total of 503 to 285.  The team made an appearance in the Sun Bowl.  The 2003 Minnesota Golden Gophers football team was ranked 17th in the final USA Today/AFCA Coaches poll and 20th in the final Associated Press poll.

1988 Minnesota Golden Gophers football team: The 1988 Minnesota Golden Gophers football team represented the University of Minnesota in the 1988 NCAA Division I-A football season.  In their third year under head coach John Gutekunst, the Golden Gophers compiled a 2–7–2 record and were outscored by their opponents by a combined total of 246 to 195.  The tie against Illinois was the last tie for the Golden Gophers and under current NCAA rules, it will be the last in Golden Gophers history.

1960 Minnesota Golden Gophers baseball team: The 1960 Minnesota Golden Gophers baseball team represented the University of Minnesota in the 1960 NCAA University Division baseball season.  The Golden Gophers played their home games at Delta Field.  The team was coached by Dick Siebert in his 13th season at Minnesota.

2002 Minnesota Golden Gophers football team: The 2002 Minnesota Golden Gophers football team represented the University of Minnesota in the 2002 NCAA Division I-A football season.  In their sixth year under head coach Glen Mason, the Golden Gophers compiled an 4–7 record and outscored their opponents by a combined total of 376 to 319.  The 2001 Minnesota Golden Gophers football team was not ranked in either the final USA Today/AFCA Coaches poll or Associated Press poll.

2001 Minnesota Golden Gophers football team: The 2001 Minnesota Golden Gophers football team represented the University of Minnesota in the 2001 NCAA Division I-A football season.  In their fifth year under head coach Glen Mason, the Golden Gophers compiled an 4–7 record and outscored their opponents by a combined total of 308 to 299.  The 2001 Minnesota Golden Gophers football team was not ranked in either the final USA Today/AFCA Coaches poll or Associated Press poll.

1956 Minnesota Golden Gophers baseball team: The 1956 Minnesota Golden Gophers baseball team represented the University of Minnesota in the 1956 NCAA baseball season.  The Golden Gophers played their home games at Delta Field.  The team was coached by Dick Siebert in his 9th season at Minnesota.

Northstar Line: The Northstar Line (reporting mark MNRX) is a commuter rail route in the US state of Minnesota.  Northstar runs 40 mi from Big Lake to downtown Minneapolis at Target Field using existing track and right-of-way owned by the BNSF Railway.  Passenger service began on November 16, 2009.  The rail line serves part of the Northstar Corridor between Minneapolis and St. Cloud.  Planning for the line began in 1997 when the Northstar Corridor Development Authority (NCDA) was formed.  The corridor is mostly served by Interstate 94 and U.S. Highway 10.

John Anderson (baseball coach): John Anderson (born May 16, 1955 in Hibbing, Minnesota) is the head coach of the University of Minnesota Golden Gophers baseball team.  In 35 seasons (as of the end of the 2016 season), Anderson has led the Golden Gophers to a record of 1,092 wins, 726 losses and three ties.  In the Big Ten he has led Golden Gophers to a record of 493 wins and 289 losses, as of the end of the 2012 season.

Target Field: Target Field is a baseball park in the historic warehouse (or North Loop) district of downtown Minneapolis.  It is the home ballpark of the Minnesota Twins, the state's Major League Baseball (MLB) franchise.  It also has served as the occasional home of Minnesota Golden Gophers baseball, and other local and regional baseball events.

Question: What is the occasional home of Minnesota Golden Gophers baseball, has a commuter rail route that runs to it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "location_name": {
      "type": "string",
      "description": "The name of the baseball park."
    },
    "primary_tenant": {
      "type": "string",
      "description": "The primary Major League Baseball team that calls this park home."
    },
    "occasional_tenant": {
      "type": "string",
      "description": "The team that occasionally uses this park as a home."
    },
    "commuter_rail_service": {
      "type": "object",
      "properties": {
        "line_name": {
          "type": "string",
          "description": "The name of the commuter rail line."
        },
        "destination_location": {
          "type": "string",
          "description": "The destination of the commuter rail line, which is the baseball park."
        },
        "service_start_date": {
          "type": "string",
          "description": "The date when passenger service began on the rail line."
        }
      },
      "required": [
        "line_name",
        "destination_location",
        "service_start_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "location_name",
    "primary_tenant",
    "occasional_tenant",
    "commuter_rail_service"
  ],
  "additionalProperties": false
}
