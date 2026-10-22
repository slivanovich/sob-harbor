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
Pendle Hill High School: Pendle Hill High School is a comprehensive, co-educational high school with over 300 students located in Pendle Hill, a suburb in the west of Sydney, Australia.  The school enjoys a prominent position in extensive, elevated and park-like grounds, with views east to Sydney and west to the Blue Mountains.  Established in 1965, the school has a long tradition of academic, cultural and sporting achievements especially in rugby league.

Padiham: Padiham is a small town and civil parish on the River Calder, about 3 mi west of Burnley and south of Pendle Hill, in Lancashire, England.  It is part of the Borough of Burnley, but has its own town council with varied powers.  Padiham was originally a rural village lying by the River Calder.  It is still surrounded by attractive countryside on an arc running from the north-west to the north-east in the foothills of Pendle Hill.

Pendle Hill: Pendle Hill is located in the east of Lancashire, England, near the towns of Burnley, Nelson, Colne, Clitheroe and Padiham.  Its summit is 557 m above mean sea level.  It gives its name to the Borough of Pendle.  It is an isolated hill, separated from the Pennines to the east, the Bowland Fells to the northwest, and the West Pennine Moors to the south.  It is included in detached part of the Forest of Bowland Area of Outstanding Natural Beauty (AONB).

Higham, Lancashire: Higham is a village in the Borough of Pendle in Lancashire, England, south of Pendle Hill.  The civil parish is named Higham with West Close Booth.  The village is 2 mi north-east of Padiham and about 4 mi south west of Nelson along the A6068 road.

Sabden: Sabden is a medium to large village and civil parish in the Ribble Valley, Lancashire.  Sabden is located south of Pendle Hill, in a valley about three miles north west of Padiham.  The parish is 2,451 acres.  It lies in the Forest of Pendle section of the Forest of Bowland Area of Outstanding Natural Beauty.

Pendle Hill railway station: Pendle Hill railway station is located on the Main Western line, serving the Sydney suburb of Pendle Hill.  It is served by Sydney Trains T1 Western and T5 Cumberland line services.

Forest of Pendle: The Forest of Pendle is the name given to an area of hilly landscape to the east of Pendle Hill in eastern Lancashire, roughly defining the watershed between the River Ribble and its tributary the River Calder.  The forest is not identical to the modern local government district of Pendle, which is larger.  And in fact the modern version of the forest has come to contain areas to the north and east of Pendle Hill which are partly in the district of Ribble Valley.

Pendle College, Lancaster: Pendle College is one of the constituent colleges of the University of Lancaster.  Founded in 1974, the college is named after the Pendle region of the east of Lancashire, which is dominated by Pendle Hill.  The term "Pendle" is associated with a great deal of fantasy and legend.  Although named after Pendle Hill, the area is perhaps more well known for its association with the infamous Pendle Witches.

Roughlee: Roughlee is a village in Pendle, Lancashire, England, in the civil parish of Roughlee Booth.  It is close to Nelson, Barrowford and Blacko.  The village lies at the foot of Pendle Hill, well known for the Pendle Witches, and includes the hamlet of Crowtrees.  The parish adjoins the Pendle parishes of Blacko, Barrowford, Old Laund Booth, Goldshaw Booth and Barley-with-Wheatley Booth.  It is part of the Forest of Bowland Area of Outstanding Natural Beauty (AONB).

Pendle Hill, New South Wales: Pendle Hill is a suburb of Sydney, in the state of New South Wales, Australia.  Pendle Hill is located 30 kilometres west of the Sydney central business district, in the local government areas of Cumberland Council and City of Parramatta and is part of the Greater Western Sydney region.

Question: In which direction is Padiham located to Pendle Hill?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "source_location": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the source location."
        },
        "type": {
          "type": "string",
          "description": "The type of the source location (e.g., town, village)."
        }
      },
      "required": [
        "name",
        "type"
      ],
      "additionalProperties": false
    },
    "target_location": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the target location."
        },
        "type": {
          "type": "string",
          "description": "The type of the target location (e.g., hill, mountain)."
        }
      },
      "required": [
        "name",
        "type"
      ],
      "additionalProperties": false
    },
    "relative_direction": {
      "type": "string",
      "description": "The cardinal or intercardinal direction of the source location relative to the target location."
    }
  },
  "required": [
    "source_location",
    "target_location",
    "relative_direction"
  ],
  "additionalProperties": false
}
