{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBilly Wilson (footballer, born 1936): William \"Billy\" Wilson (born 23 September 1936) is a former professional footballer from Northern Ireland.  He played as a wing half.  He started his career with his hometown club, Portadown, and made his debut for the club at the age of 16.  In 1955, Wilson moved to England to join Football League First Division side Burnley and initially played in the reserves.  He made his first appearance for the senior team in the 0–1 defeat to Blackpool on 1 May 1957, alongside fellow debutant Jim Appleby.  Wilson played only one more match for Burnley, deputising for regular right-half Bobby Seith for the 0–7 loss against Nottingham Forest on 18 September 1957.  He was released from his contract in May 1958 and despite interest from Crewe Alexandra and Notts County, he returned to Northern Ireland and signed for Linfield\n\nList of Linfield F.C. players: Linfield F.C. is a semi-professional association football club based in Belfast, Northern Ireland.  The club plays in the NIFL Premiership, the highest level of the Northern Ireland Football League.  They have played at their current home ground, Windsor Park, since 1905.  Previous to this they had played at Ulsterville Avenue from 1889 until 1905 and The Meadow from their foundation in 1886 to 1889.  They were one of the founding clubs of the league in 1890, and since that time the club has competed in numerous nationally and internationally organised competitions.\n\nKillyleagh Youth F.C.: Killyleagh Youth Football Club (also known as Killyleagh YC) is a Northern Irish, intermediate-level football club based in Killyleagh, near Downpatrick, playing in Division 1A of the Northern Amateur Football League.  The club was formed in 1960, playing in the South Belfast Youth League for one season before joining the Amateur League in 1961.  Intermediate status was achieved in 1963.  They play their home matches at the Showgrounds in Killyleagh.  Perhaps their biggest achievement of recent times was when they reached the semi-final of the Irish Cup in 2002, losing 4–0 to Linfield.  .\n\nLinfield F.C.: Linfield Football Club is a semi-professional football club based in Belfast, Northern Ireland.  The club was founded in 1886 as Linfield Athletic Club and in 1905 moved into the current home of Windsor Park, which is also the home of the Northern Ireland national team.  The club plays in the NIFL Premiership – the highest level of the Northern Ireland Football League.  Linfield's main rival is Glentoran – the other half of Belfast's Big Two.  This rivalry traditionally includes a league derby played on Boxing Day each year, which usually attracts the largest league attendance of the season.  Linfield's average league home attendance is approximately 2,500 the highest in the division and more than double the league's overall average of about 1,000.\n\nQuestion: Where is linfield football club based?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"club_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football club.\"\n    },\n    \"club_type\": {\n      \"type\": \"string\",\n      \"description\": \"The professional status of the club (e.g., semi-professional).\"\n    },\n    \"base_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the club is based.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the club is based.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"league_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the league the club plays in.\"\n    }\n  },\n  \"required\": [\n    \"club_name\",\n    \"club_type\",\n    \"base_location\",\n    \"league_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "club_name": {
        "type": "string",
        "description": "The name of the football club."
      },
      "club_type": {
        "type": "string",
        "description": "The professional status of the club (e.g., semi-professional)."
      },
      "base_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the club is based."
          },
          "country": {
            "type": "string",
            "description": "The country where the club is based."
          }
        },
        "required": [
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "league_name": {
        "type": "string",
        "description": "The name of the league the club plays in."
      }
    },
    "required": [
      "club_name",
      "club_type",
      "base_location",
      "league_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
