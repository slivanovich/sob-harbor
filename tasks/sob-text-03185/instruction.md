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
Hertford: Hertford (/ˈhɑːfəd/, /ˈhɑːtfəd/) is the county town of Hertfordshire, England, and is also a civil parish in the East Hertfordshire district of the county.  Forming a civil parish, the 2011 census put the population of Hertford at about 26,000.

Norton Mandeville: Norton Mandeville is a small village near the A414 road, in the Epping Forest District, in the English county of Essex.  Norton Mandeville has an Anglican parish church dedicated to All Saints.

Norton Heath: Norton Heath is a small village near the A414 road, in the Epping Forest District, in the English county of Essex.

Nine Ashes: Nine Ashes is a hamlet near the A414 road, in the Epping Forest District, in the English county of Essex.  Nearby settlements include the village of Norton Heath and the hamlet of King Street.

Bobbingworth: Bobbingworth is a village and civil parish in the Epping Forest district of Essex, England.  The village is situated approximately 3 mi north-west from Chipping Ongar, 10 mi west from the county town of Chelmsford, and lies off the A414 road.  Bobbingworth is in the parliamentary constituency of Brentwood & Ongar.

Double road race: The Double Road Race is a long-distance road running competition consisting of two segments or "legs" – a 10-kilometer road run, followed by a five-kilometer road run, with a short rest break in between.  The Double Road Race Federation added additional distances in August 2014.  Other official distances for Double Racing® include Double 5k (3+2), Double 8k (5+3), and Double 21k (15+6).  The race was created by Runner's World magazine founder Bob Anderson.

Highwood, Essex: Highwood is a village and civil parish in the Chelmsford District of Essex, England.  The village is approximately a mile south from the A414 road and four miles west from the centre of the county town of Chelmsford.  Loves Green is part of the village at its north.  The hamlet of Edney Common is at the east of the parish.

King Street, Essex: King Street is a hamlet near the A414 road, in the Epping Forest District, in the English county of Essex.  Nearby settlements include the village of Norton Mandeville and the hamlet of Nine Ashes.

A414 road: The A414 is a major road in England.  It runs from the A41 at a junction west of Hemel Hempstead in Hertfordshire, through the town to junction 8 of the M1 motorway at Buncefield, and running parallel to the M1 until junction 7, heading south of St Albans, east through Hatfield, Hertford, then across the A10 and into Essex through Harlow, Chipping Ongar and Chelmsford before terminating at Maldon.

Cooksmill Green: Cooksmill Green is a hamlet in the Chelmsford District of Essex, England.  It is situated approximately four miles west from the centre of the county town of Chelmsford.  The A414 road is less than one mile to the south.

Question: What county town of 26,000 does the A414 road run through?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "county_town_name": {
      "type": "string",
      "description": "The name of the county town."
    },
    "county": {
      "type": "string",
      "description": "The county to which the town belongs."
    },
    "population": {
      "type": "integer",
      "description": "The approximate population of the town."
    },
    "road_information": {
      "type": "object",
      "properties": {
        "road_name": {
          "type": "string",
          "description": "The name of the road running through the town."
        },
        "road_type": {
          "type": "string",
          "description": "The classification or type of the road."
        }
      },
      "required": [
        "road_name",
        "road_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "county_town_name",
    "county",
    "population",
    "road_information"
  ],
  "additionalProperties": false
}
