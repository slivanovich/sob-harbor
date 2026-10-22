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
Club Atlético Acassuso: Club Atlético Acassuso is an Argentine football club from the Boulogne Sur Mer district of San Isidro Partido in Greater Buenos Aires.  The squad currently plays in Primera B Metropolitana, the regionalised third division of the Argentine football league system.

Club Atlético San Isidro: The Club Atlético de San Isidro is an Argentine sports club based in San Isidro in Greater Buenos Aires.  Originally established as an association football club, San Isidro has gained recognition for its rugby union team, holding a record of 33 Torneo de la URBA championships.  The senior squad currently competes at Grupo I, the top division of Unión de Rugby de Buenos Aires (URBA).

Club Pueyrredón: Club Pueyrredón, also nicknamed Puey, is an Argentine rugby union and field hockey club from the Boulogne Sur Mer district of San Isidro Partido in Greater Buenos Aires.  The rugby team currently plays in the Torneo de la URBA Grupo I, the first division of the Unión de Rugby de Buenos Aires league system.

Isidro Ros Ríos: Isidro Ros Ríos (born 6 November 1995), commonly known as Isi, is a Spanish footballer who plays for UCAM Murcia CF as a winger.

Andrés Kogovsek: Andrés Kogovsek (born 1974) is an Argentine handball player.  He was born in San Isidro, Argentina and plays for the club Villa Ballester.  He competed for the Argentine national team at the 2012 Summer Olympics in London.  Andrés won the gold medal at the 2011 Pan American Games.

Christian Sánchez (Salvadoran footballer): Christian Alexander Sánchez Viscarra (born May 15, 1983 in Sonsonate, El Salvador) is a Salvadoran footballer who currently plays as a midfielder for Isidro Metapán in the Salvadoran Premier Division.

UCAM Murcia CF: Universidad Católica de Murcia Club de Fútbol, commonly known as UCAM Murcia or simply UCAM, is a Spanish football club based in Murcia.  Founded in 1999 it plays in Segunda División B – Group 4, holding home games at "Estadio de La Condomina", with a capacity of 6,500 spectators.

Yonathan Cabral: Yonathan Cabral (Isidro Casanova, Buenos Aires, Argentina, May 10, 1992) is an Argentine footballer who plays as defender in the Racing Club of Primera Division Argentina .  In his personal life is brother of the current champion of Celta de Vigo, Gustavo Cabral .

C.D. Águila San Isidro: Club Deportivo Águila San Isidro is a Salvadoran football club, which currently plays in the Salvadoran Third Division.

CD San Isidro: Club Deportivo San Isidro is a Spanish football team based in San Isidro, in the autonomous community of Canary Islands.  Founded in 1970 it plays in Tercera División – Group 12, holding home matches at "Estadio La Palmera", with a 2,500-seat capacity.  In Tenerife, the club are commonly known as Raqui San Isidro.

Question: Isidro Ros Ríos plays for a team that plays in which division ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player."
    },
    "team_info": {
      "type": "object",
      "properties": {
        "team_name": {
          "type": "string",
          "description": "The name of the team the player plays for."
        },
        "division": {
          "type": "string",
          "description": "The division the team plays in."
        }
      },
      "required": [
        "team_name",
        "division"
      ],
      "additionalProperties": false
    },
    "sport": {
      "type": "string",
      "description": "The sport the player plays."
    }
  },
  "required": [
    "player_name",
    "team_info",
    "sport"
  ],
  "additionalProperties": false
}
