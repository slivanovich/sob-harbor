{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1973–74 Seattle SuperSonics season: The 1973–74 Seattle SuperSonics season was the 7th season of the Seattle SuperSonics in the National Basketball Association (NBA).  Following the resignation of Lenny Wilkens as a head coach after the 1971–72 season and a poor campaign in the 1972–73 season that saw the departure of general manager Bob Houbregs, the Sonics hired Boston Celtics' stalwart Bill Russell as head coach and general manager.  With Russell at the helm, the team finished in 6th place in the Western Conference with a 36–46 record.  The Sonics' home court, Seattle Center Coliseum, was the venue for the 1974 NBA All-Star Game.\n\n1986–87 Seattle SuperSonics season: The 1986–87 Seattle SuperSonics season was the 20th season of the Seattle SuperSonics in the National Basketball Association.  Bernie Bickerstaff returned for his second season as head coach of the franchise and, despite little improvement over their previous season's 31–51 record, managed to clinch a spot in the playoffs and reach the Western Conference Finals, losing in four games to the Los Angeles Lakers.\n\nP. J. Carlesimo: Peter John \"P. J.\" Carlesimo (born May 30, 1949) is an American basketball coach, who coached in both the NBA and college basketball for nearly 40 years.  He is also a television broadcaster, having worked with \"ESPN, The NBA on TNT, Westwood One, Fox Sports Southwest\" and \"CSN New England\".\n\n1972–73 Seattle SuperSonics season: The 1972–73 Seattle SuperSonics season was the 8th season of the Seattle SuperSonics in the National Basketball Association (NBA).  The team finished the regular season in 6th place in the Western Conference with a 26–56 record, 21 wins behind the one obtained in their previous season.  Head coach Tom Nissalke was fired by the team in January after a 13–32 start and was replaced by his assistant Bucky Buckwalter.\n\n1991–92 Seattle SuperSonics season: The 1991–92 NBA season was the 24th season for the Seattle SuperSonics in the National Basketball Association.  After a 7–3 start to the season, head coach K. C. Jones was fired with the team holding an 18–18 record.  After splitting four games under interim coach Bob Kloppenburg, the Sonics hired George Karl, who returned after a four-year absence from coaching in the NBA.  Under Karl, the SuperSonics finished the season fourth in the Pacific Division with a 47–35 record, reaching the playoffs as the number 6 seed in the Western Conference.  Ricky Pierce led the team in scoring averaging 21.7 points per game in his first full season with the Sonics.  In the first round, they defeated the 3rd-seeded Golden State Warriors in four games, winning the final two games by just four points.  However, they lost the conference semifinals to the Utah Jazz in five games.\n\n1971–72 Seattle SuperSonics season: The 1971–72 Seattle SuperSonics season was the 5th season of the Seattle SuperSonics in the National Basketball Association (NBA).  In their third season with Lenny Wilkens as head coach, the Sonics finished the regular season in sixth place in the Western Conference with a 47–35 record, their first winning record in franchise history.  Wilkens quit as head coach at the end of the season and was replaced by former Dallas Chaparrals coach Tom Nissalke.\n\n2007–08 Seattle SuperSonics season: The 2007–08 Seattle SuperSonics season was the 41st season of the Seattle SuperSonics in the National Basketball Association (NBA) and the franchise's final season of play in Seattle before relocating to Oklahoma City to play as the Thunder.  With head coach P. J. Carlesimo as replacement of Bob Hill, who was fired at the end of the previous season, the SuperSonics finished in 15th place in the Western Conference with a franchise worst 20–62 record.  Seattle's first round draft pick and no. 2 overall Kevin Durant was chosen as the Rookie of the Year at the end of the season.\n\nBob Kloppenburg: Bob Kloppenburg (born July 28, 1927) is an American professional basketball coach, who served as an interim head coach of the Cleveland Cavaliers in the early 1980s.  Kloppenburg later served as an assistant coach for the Seattle SuperSonics, Denver Nuggets and Toronto Raptors.  While with the Seattle SuperSonics (1985–1996), Kloppenburg was the assistant coach for the NBA West All-Star team in 1994.  He contributed to Seattle's three 60 win seasons in the 90's.  His NAIA small college coaching career saw him win five district championships in twenty years for an overall record of 369-161.  Widely regarded as the innovator of the SOS Defensive System, a system known for its ability to create turnovers because of \"contact switching\" on every screen and intense ball pressure with trapping principles.  Kloppenburg is, together with Ernie Woods, the co-founder of basketball coaching website \"HoopTactics.com\".\n\n1970–71 Seattle SuperSonics season: The 1970–71 Seattle SuperSonics season was the Seattle SuperSonics 4th season in the National Basketball Association (NBA).  In their second season with Lenny Wilkens as head coach, the Sonics finished in 8th place in the Western Conference with a 38–44 record.  Trouble arose with the injury of top scorer Bob Rule, who tore his Achilles tendon three games into the season during a match against the Portland Trail Blazers and lost him for the remainder of the season.\n\n1974–75 Seattle SuperSonics season: The 1974–75 Seattle SuperSonics season was the 8th season of the Seattle SuperSonics in the National Basketball Association (NBA).  In their second season with Bill Russell as head coach and with rookies comprising half the roster, the SuperSonics finished the regular season in 4th place in the Western Conference with a 43–39 record and reached the playoffs for the first time in franchise history.  After defeating the Detroit Pistons in 3 games in the first round in a best-of-three series, the team fell to the future champions Golden State Warriors in six games.\n\nQuestion: Who did a television broadcaster replace as head coach of the Seattle SuperSonics?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"replacing_coach\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the coach who was replaced.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"new_coach\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the new coach who was also a television broadcaster.\"\n        },\n        \"is_broadcaster\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the new coach was also a television broadcaster.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_broadcaster\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"season_of_replacement\": {\n      \"type\": \"string\",\n      \"description\": \"The season in which the replacement occurred.\"\n    }\n  },\n  \"required\": [\n    \"replacing_coach\",\n    \"new_coach\",\n    \"season_of_replacement\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "replacing_coach": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the coach who was replaced."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "new_coach": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the new coach who was also a television broadcaster."
          },
          "is_broadcaster": {
            "type": "boolean",
            "description": "Indicates if the new coach was also a television broadcaster."
          }
        },
        "required": [
          "name",
          "is_broadcaster"
        ],
        "additionalProperties": false
      },
      "season_of_replacement": {
        "type": "string",
        "description": "The season in which the replacement occurred."
      }
    },
    "required": [
      "replacing_coach",
      "new_coach",
      "season_of_replacement"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
