{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGiuliano de Paula: Giuliano Victor de Paula (born 31 May 1990), simply known as Giuliano, is a Brazilian professional footballer who plays for Turkish Süper Lig team Fenerbahçe and the Brazilian national team as an attacking midfielder.\n\nMarcelo Leite Pereira: Marcelo Leite Pereira known as Marcelinho (born 22 June 1987) is a Brazilian professional footballer who last played for Avaí as a forward.  He is known for his great skills with excellent pace and ball control.  He has a brilliant vision for goal and capable of scoring with both feet.  He has dominated third edition of Hero Indian Super League by delivering 10 goals and 5 assists and winning Golden Boot for Delhi Dynamos alongside former Chelsea player Florent Molouda who has won golden ball for his team.  Marcelino goal has been named as Best International week goal for club Delhi Dynamos vs Goa FC.\n\nPhilippe Coutinho: Philippe Coutinho Correia (] ; born 12 June 1992) is a Brazilian professional footballer who plays as an attacking midfielder for Premier League club Liverpool and the Brazil national team.\n\nFernandinho (footballer): Fernando Luiz Roza (born 4 May 1985), or simply Fernandinho (] ; meaning \"Little Fernando\"), is a Brazilian professional footballer who plays as a midfielder for Premier League club Manchester City and the Brazil national team.  He has also captained both sides on many occasions.\n\nRonaldinho: Ronaldo de Assis Moreira (born 21 March 1980), commonly known as Ronaldinho (] ) or Ronaldinho Gaúcho, is a Brazilian professional footballer and ambassador for Spanish club FC Barcelona.  He played mostly as an attacking midfielder, but was also deployed as a forward or a winger.  He played the bulk of his career at European clubs Paris Saint-Germain, Barcelona and Milan as well as playing for the Brazilian national team.  Often considered one of the best players of his generation and regarded by many as one of the greatest of all time, Ronaldinho won two FIFA World Player of the Year awards and a Ballon d'Or.  He was renowned for his technical skills and creativity; due to his agility, pace and\n\nFabinho (footballer, born 1993): Fábio Henrique Tavares (born 23 October 1993), commonly known as Fabinho, is a Brazilian professional footballer who plays as a right back or as a defensive midfielder for Monaco in Ligue 1, and for the Brazilian national team.\n\nNike Mercurial Vapor: The Mercurial Vapor is a football boot manufactured by Nike.  The boot is known for being lightweight.  Because of this, the boot is endorsed by many players for whom speed is part of their game, notably wingers or strikers, such as Cristiano Ronaldo, Franck Ribéry, Luiz Adriano, Zlatan Ibrahimović, Didier Drogba, Jesús Navas, Luka Modrić, Arturo Vidal, Douglas Costa, Xherdan Shaqiri, Raheem Sterling, Stephan El Shaarawy, Eden Hazard, Alexis Sánchez, Carlos Bacca and Philippe Coutinho, among others.\n\nCraig Johnston: Craig Peter Johnston (born 25 June 1960) is a South African-born Australian former footballer.  He played in the English Football League between 1977 and 1988, winning five league titles with Liverpool.  After retiring, he designed and created the prototype for Adidas' Predator football boot, worn by many footballers and rugby players.  He was eligible for the Australian and South African national teams, but only ever made an appearance for the England U-21 youth team.\n\nDiego Cavalieri: Diego Cavalieri (born 1 December 1982) is a Brazilian professional footballer who plays for Fluminense as a goalkeeper in the Campeonato Brasileiro Série A.  He is of Italian ancestry and holds both an Italian and Brazilian passport.  He elected to represent Brazil at international level and has thus far made 3 appearances for the national team.\n\nRamires: Ramires Santos do Nascimento (] ; born 24 March 1987), known simply as Ramires, is a Brazilian professional footballer who plays for Chinese club Jiangsu Suning and the Brazil national team.  A midfielder, he is comfortable playing in either the centre or right midfielder position.  He normally plays as a box-to-box midfielder role because of his energy in supporting defensive and offensive play.\n\nQuestion: The Mercurial Vapor is a football boot  endorsed by many players such as a Brazilian professional footballer who plays for what national team? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"boot_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football boot mentioned in the question.\"\n    },\n    \"endorsing_players\": {\n      \"type\": \"array\",\n      \"description\": \"A list of players who endorse the specified boot and match the criteria (Brazilian professional footballer).\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"player_name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the endorsing player.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the player.\"\n          },\n          \"national_team\": {\n            \"type\": \"string\",\n            \"description\": \"The national team the player plays for.\"\n          }\n        },\n        \"required\": [\n          \"player_name\",\n          \"nationality\",\n          \"national_team\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"target_national_team\": {\n      \"type\": \"string\",\n      \"description\": \"The national team that answers the question 'who plays for what national team?'\"\n    }\n  },\n  \"required\": [\n    \"boot_name\",\n    \"endorsing_players\",\n    \"target_national_team\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "boot_name": {
        "type": "string",
        "description": "The name of the football boot mentioned in the question."
      },
      "endorsing_players": {
        "type": "array",
        "description": "A list of players who endorse the specified boot and match the criteria (Brazilian professional footballer).",
        "items": {
          "type": "object",
          "properties": {
            "player_name": {
              "type": "string",
              "description": "The full name of the endorsing player."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the player."
            },
            "national_team": {
              "type": "string",
              "description": "The national team the player plays for."
            }
          },
          "required": [
            "player_name",
            "nationality",
            "national_team"
          ],
          "additionalProperties": false
        }
      },
      "target_national_team": {
        "type": "string",
        "description": "The national team that answers the question 'who plays for what national team?'"
      }
    },
    "required": [
      "boot_name",
      "endorsing_players",
      "target_national_team"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
