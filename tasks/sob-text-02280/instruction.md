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
Nicola Sutter: Nicola Sutter (born 5 May 1995) is a Swiss professional footballer who currently plays as a midfielder for FC Thun.

Dennis Hediger: Dennis Hediger (born 22 September 1986, in Switzerland) is a Swiss professional footballer who currently plays as a midfielder for FC Thun in the Swiss Super League.

FC Thun: FC Thun ("Fussballclub Thun 1898") is a Swiss football team from the Bernese Oberland town of Thun.  The club currently plays in the Swiss Super League after being promoted in the 2009/10 season.  The club plays at the Stockhorn Arena which accommodates a total of 10,000 supporters, both seated and standing.  The club's colours are red and white.

FC Dürrenast: FC Dürrenast is a football team from Thun, Switzerland.  The team currently plays in the Bern/Jura regional competition of the Swiss football pyramid.

Nicolas Schindelholz: Nicolas Schindelholz (born 12 February 1988 Switzerland) is a Swiss professional footballer who currently plays as a defender for FC Thun in the Swiss Super League.

Edmond Lekaj: Edmond Lekaj (born 25 August 1994) is an Albanian, Swiss professional footballer who currently plays as a midfielder for FC Thun in the Swiss Super League.

Mickaël Facchinetti: Mickaël Facchinetti (born 15 February 1991) is a Swiss professional footballer who currently plays for FC Thun as a left full back.

Silvan Aegerter: Silvan Aegerter (born 5 May 1980, in Grenchen) is a Swiss football midfielder who currently plays as midfielder for FC Lugano in the Swiss Challenge League.  Before he played for FC Thun and FC Zürich.  He played in the youth team for his local team FC Grenchen and also for FC Basel.

Roland Bättig: Roland Bättig (born 28 July 1979 Switzerland) is a former Swiss professional footballer who last played as a midfielder for FC Thun in the Swiss Super League.

Tranquillo Barnetta: Tranquillo Barnetta (] ; born 22 May 1985) is a Swiss professional footballer who plays as a midfielder for St. Gallen.  He usually plays out wide as a left winger but can also play in the centre as an attacking midfielder, or even in a more withdrawn role as a central midfielder.  Barnetta is known for his "extreme pace, mobility and creativity".  Prior to moving to the MLS, Barnetta played football for several Swiss and German clubs.  At international level, he has amassed 75 caps for the Swiss national team, representing his nation in three FIFA World Cups, and two UEFA European Football Championships.

Question: Who is a Swiss professional footballer who currently plays as a midfielder for a Swiss football team from the Bernese Oberland town of Thun ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the football team."
        },
        "location": {
          "type": "string",
          "description": "The town and region where the team is located."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the football team."
        }
      },
      "required": [
        "name",
        "location",
        "nationality"
      ],
      "additionalProperties": false
    },
    "player_criteria": {
      "type": "object",
      "properties": {
        "position": {
          "type": "string",
          "description": "The required playing position for the footballer."
        },
        "nationality": {
          "type": "string",
          "description": "The required nationality for the footballer."
        },
        "current_status": {
          "type": "string",
          "description": "Indicates if the player is currently active."
        }
      },
      "required": [
        "position",
        "nationality",
        "current_status"
      ],
      "additionalProperties": false
    },
    "matching_players": {
      "type": "array",
      "description": "A list of players who match all the specified criteria.",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The full name of the player."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the player as stated in the context."
          },
          "current_position": {
            "type": "string",
            "description": "The current playing position of the player."
          }
        },
        "required": [
          "player_name",
          "nationality",
          "current_position"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "team_details",
    "player_criteria",
    "matching_players"
  ],
  "additionalProperties": false
}
