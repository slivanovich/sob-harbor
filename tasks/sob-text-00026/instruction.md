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
Canary Islands derby: The Canary Islands derby is the name given to football matches contesting Spanish sides UD Las Palmas and C.D. Tenerife, who are generally regarded as the top two sides in the Canary Islands.  The Canary Islands derby is a match with a lot of rivalry and intensity that has always faced the islands of Gran Canaria and Tenerife and its inhabitants.  According to World Soccer Magazine, the Canary Islands derby is on the list of the 50 greatest rivalries in the world and is considered one of the most important and spectacular derbies in Spain.  Las Palmas have generally been more successful in derby matches.

SD Tenisca: Sociedad Deportiva Tenisca is a Spanish football team club from the city of Santa Cruz de La Palma, on the island of La Palma (Canary Islands).  It was founded in 1922 and currently plays in the Canary group of the Tercera División – Group 12 of Spain.

Canary Islands autonomous football team: The Canary Islands national football team is the regional football team for the Canary Islands, Spain.  They are not affiliated with FIFA or UEFA/CAF, because the Canary Islands are represented internationally by the Spanish national football team.  The team only plays friendly matches.

CD Orientación Marítima: Club Deportivo Orientación Marítima is a Spanish football team based in Arrecife, Lanzarote, in the autonomous community of the Canary Islands.  Founded in 1954, it plays in Divisiones Regionales de Fútbol in Canary Islands, holding home games at "Ciudad Deportiva de Lanzarote", with a capacity of 7,000 spectators.

Rally Islas Canarias: The Rally Islas Canarias, known originally as the Rally El Corte Inglés is an international rally racing event based on the Spanish island of Gran Canaria in the Canary Islands.  The event has been a long running round of the European Rally Championship, the Spanish Rally Championship and the Canary Islands Rally Championship.  It has also in the recent past been a round of the Intercontinental Rally Challenge, the European Rally Cup South and the European Rally Cup West.  The rally is a tarmac rally event and has been since inception.

UD Las Zocas: Unión Deportiva Las Zocas is a Spanish football team based in Las Zocas, San Miguel de Abona, in the autonomous community of the Canary Islands.  Founded in 1986 it plays in Tercera División – Group 12, holding home games at "Estadio Juanito Marrero", with a capacity of 3,000 seats.

UD Las Palmas: Unión Deportiva Las Palmas, S.A.D. is a Spanish football team based in Las Palmas, in the autonomous community of Canary Islands.  Founded on 22 August 1949, it plays in La Liga, holding home games at the Estadio Gran Canaria, with a capacity of 33,111 seats.

Hernán Santana: Hernán Daniel Santana Trujillo (born 26 August 1990), simply known as Hernán, is a Spanish professional footballer who plays for UD Las Palmas as a midfielder.

CD Marino: Club Deportivo Marino is a Spanish football team based in Playa de las Américas, in the autonomous community of the Canary Islands.  Founded in 1936 it plays in Tercera División – Group 12, holding home games at "Estadio Antonio Domínguez", with a capacity of 7,500 seats.

Bentor: Bentor ( 1463 – February 1495), sometimes also called Ventor, Bentore, Benytomo, or Bentorey, was the last mencey or king of Taoro from November 1494 until his suicide in February 1495.  A native Guanche prince in the Canary Islands during the second half of the 15th century, Bentor was the eldest grandson (in some sources, son) of Bencomo, the penultimate mencey (or king) of Taoro.  Taoro was one of nine menceyatos, or kingdoms, on the island of Tenerife in the Canary Islands before the Spanish conquest of the islands.  Bentor's mother was probably named Hañagua, although this is unclear.  He succeeded his grandfather as mencey upon his father's death in November 1494, and led the kingdom until his own death by suicide four months later in February 1495.  Bentor had five siblings: one sister (Dácil) and four brothers (Ruiman, Rosalva, Chachiñama, and Tiñate).

Question: What Spanish football team has a midfielder named Hernan and is based in the Canary Islands?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "football_team_name": {
      "type": "string",
      "description": "The name of the Spanish football team."
    },
    "team_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the team is based."
        },
        "autonomous_community": {
          "type": "string",
          "description": "The autonomous community where the team is located."
        }
      },
      "required": [
        "city",
        "autonomous_community"
      ],
      "additionalProperties": false
    },
    "midfielder_details": {
      "type": "object",
      "properties": {
        "player_name": {
          "type": "string",
          "description": "The name of the midfielder."
        },
        "player_position": {
          "type": "string",
          "description": "The playing position of the player."
        }
      },
      "required": [
        "player_name",
        "player_position"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "football_team_name",
    "team_location",
    "midfielder_details"
  ],
  "additionalProperties": false
}
