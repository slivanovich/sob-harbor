{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNorberto Menéndez: Norberto Menéndez (14 December 1936 – 26 May 1994) was an Argentine footballer striker.  He was born in 1936 in the city of Buenos Aires, Argentina.  He played for the Argentine national team at the 1958 World Cup in Sweden, where he scored once against Northern Ireland, adding to the 3–1 only Argentine victory in that tournament.  Menéndez won six Primera Division Argentina titles during his career.  He has the distinction of being the only footballer who, having played for the two giants of the Argentine league (Boca Juniors and River Plate), won three league championships with each of them.  He was also the first player of Argentina's National Team to have scored a goal at the qualification standings of a World Cup, on 13 October 1957 against Chile.\n\nLa barra del Rojo: La Barra Del Rojo is the barra brava of the Club Atlético Independiente.  They are unusual in Argentina in that they don’t have a nickname.  It is considered as the largest and strongest barra brava in Argentina.  The existence of this group has been publicly known since the 1950s.  Besides attending Independiente matches, since 1982, the core members of the group attend the national team's World Cups.  They also attended some times the Copa América.\n\nJulio Musimessi: Julio Elías Musimessi (July 9, 1924 in Resistencia, Chaco – August 27, 1997 in Morón) was an Argentine football goalkeeper who played for Newell's Old Boys, Boca Juniors and the Argentina national team.\n\nBasketball in Argentina: Basketball was introduced in Argentina in 1912 by the \"Asociación Cristiana de Jóvenes\" (Young Men's Christians Association – YCMA), with the first Federation created in 1921 to organise the competitions.  In 1929, the Argentine Basketball Federation (\"Confederación Argentina de Basketball\") was established.  The body currently controls the Argentina national team.\n\nHendro Kartiko: Hendro Kartiko (born 24 April 1973 in Banyuwangi, East Java) is a retired Indonesian footballer who last played with Mitra Kukar.  He normally plays as a goalkeeper and is 178 cm in height.  He also played for the Indonesia national football team.  His first appearance in the senior national team was in the Asian Cup 1996 for Indonesia against Kuwait, Indonesia draw 2-2, his substitution Kurnia Sandy was injured.  In Asian Cup 2000 Asian people mention him \"Fabian Barthez Asia\", in this event Indonesia had one draw and two losses in the first round, drew 0-0 with Kuwait, loss 0-4 from China PR and loss 0-3 from South Korea.  In Asian Cup 2004 he was chosen as a \"Man of The Match\" for Indonesia against Qatar, Indonesia won 2-1.  He has 60 caps in the senior national team since his debut in 1996 and became one of football players in his country with the most appearances in the senior national team squad.  Since 2007, he has not been chosen again as the number one goalkeeper in the senior national team.  He was replaced by other younger players in Indonesia.  Currently, his place in the national team is occupied by Markus Horison.\n\nItaly national football team: The Italian national football team (Italian: \"Nazionale di calcio italiana\" ) represents Italy in association football and is controlled by the Italian Football Federation (FIGC), the governing body for football in Italy.\n\nGabriel Calderón: Gabriel Humberto Calderón (born 7 February 1960) is a former Argentine football midfielder and coach who currently manages Qatar SC .  Calderón played in several teams including Argentine Racing Club de Avellaneda and Club Atlético Independiente, Spanish Real Betis and French Paris Saint-Germain.  He was part of the Argentina Under-20 team that won the 1979 FIFA World Youth Championship, and also played in the 1982 FIFA World Cup in Spain and in the 1990 FIFA World Cup in Italy.  After his retirement, he managed Caen, Lausanne Sports and several teams in the Middle East including the Saudi Arabian national team, Omani national team, Al-Ittihad, Al-Hilal, Baniyas and Bahraini national team.  He also managed La Liga side Real Betis.\n\nRobert Braet: Robert Braet (11 February 1912 in Bruges – 23 February 1987 in Bruges) was a tall Belgian goalkeeper.  He never played for any other football team besides Cercle Brugge.  Braet is seen as one of the biggest monuments in the team's history.  He was also part of the Belgian national team that took part in the 1938 FIFA World Cup.\n\nJulio Lamas: Julio César Lamas (born June 9, 1964) is an Argentina professional basketball coach.  He is currently the head coach of Obras Sanitarias of the Argentine League.  He has also been the head coach of the senior men's Argentina national team.\n\nJulio Libonatti: Julio Libonatti (5 July 1901 – 9 October 1981) was a football manager and former footballer who played as a forward for the Argentina national team and Italy national team.\n\nQuestion: Who controls the national team besides the Argentina one who Julio Libonatti played for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"national_team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the national team.\"\n    },\n    \"controlling_body_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the organization that controls the national team.\"\n    },\n    \"controlling_body_acronym\": {\n      \"type\": \"string\",\n      \"description\": \"The acronym of the controlling body, if available.\"\n    },\n    \"sport\": {\n      \"type\": \"string\",\n      \"description\": \"The sport the national team plays.\"\n    }\n  },\n  \"required\": [\n    \"national_team_name\",\n    \"controlling_body_name\",\n    \"controlling_body_acronym\",\n    \"sport\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "national_team_name": {
        "type": "string",
        "description": "The name of the national team."
      },
      "controlling_body_name": {
        "type": "string",
        "description": "The name of the organization that controls the national team."
      },
      "controlling_body_acronym": {
        "type": "string",
        "description": "The acronym of the controlling body, if available."
      },
      "sport": {
        "type": "string",
        "description": "The sport the national team plays."
      }
    },
    "required": [
      "national_team_name",
      "controlling_body_name",
      "controlling_body_acronym",
      "sport"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
