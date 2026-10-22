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
Alfie Clarke: Alfred William Clarke (1914–1953) was a Welsh amateur football inside left who played in the Football League for Newport County.  He was capped by Wales at amateur level.

George Wheeler (footballer): George Harold Wheeler (19 February 1910 – 1995) was a Welsh amateur football left back who played in the Football League for Newport County.  He was capped by Wales at amateur level.

Alan McIntosh: Alan McIntosh (born 19 July 1939) was a Welsh amateur football outside forward who played in the Football League for Cardiff City.  He was capped by Wales at amateur level.

Roy McDonald (footballer): Robert William McDonald (11 July 1896 – 1970) was a Welsh amateur football inside left who played in the Football League for Newport County.  He was capped by Wales at amateur level.

Reg Callender: Reginald Henry Callender (1892 – 5 October 1915) was an English amateur football outside left who played in the Football League for Derby County and Glossop.  He represented the England amateur national team.

Glyn Davies (footballer, born 1909): Glyn Ivor Davies (24 November 1909 – 1985) was a Welsh amateur football outside left who played in the Football League for Swansea Town and Norwich City.  He was capped by Wales at amateur level.

Doug Orr: Douglas McDonald Orr (born 8 November 1937) was a Scottish amateur football outside left who played in the Scottish League for Queen's Park.  He was capped by Scotland at amateur level and also played in the Football League for Queens Park Rangers.

Sam Jones (Welsh footballer): Samuel E. Jones was a Welsh amateur football outside left who played in the Football League for Newport County.  He was capped by Wales at amateur level.

Keith Huntley: Keith Stanley Murray Huntley (12 February 1931 – December 1995) was a Welsh amateur football outside left who played in the Football League for Swansea Town.  He was capped by Wales at amateur level.

Newport County A.F.C.: Newport County Association Football Club (Welsh: "Clwb Pêl-droed Sir Casnewydd" ) is a professional association football club based in the city of Newport, South Wales.  The team play in League Two, the fourth tier of the English football league system.  Most recently reformed in 1989, the club is a continuation of the Newport County club which was founded in 1912 and was a founder member of the Football League's new Third Division in 1920.

Question: What Welsh amateur football outside left played for a football club in Newport, South Wales?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the football player."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the player."
        },
        "position": {
          "type": "string",
          "description": "The primary playing position of the player."
        },
        "is_amateur": {
          "type": "boolean",
          "description": "Indicates if the player was an amateur footballer."
        }
      },
      "required": [
        "name",
        "nationality",
        "position",
        "is_amateur"
      ],
      "additionalProperties": false
    },
    "club_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the football club the player played for."
        },
        "location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the club is based."
            },
            "region": {
              "type": "string",
              "description": "The region or country subdivision where the club is located."
            }
          },
          "required": [
            "city",
            "region"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "question_match": {
      "type": "boolean",
      "description": "True if the player and club details match all criteria in the question."
    }
  },
  "required": [
    "player_details",
    "club_details",
    "question_match"
  ],
  "additionalProperties": false
}
