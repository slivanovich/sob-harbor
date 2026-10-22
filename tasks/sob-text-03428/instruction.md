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
Peter Crouch: Peter James Crouch (born 30 January 1981) is an English professional footballer who plays as a striker for Premier League club Stoke City.  He was capped 42 times by the England national team between 2005 and 2010, scoring 22 goals for his country in that time, and appearing at two World Cups.

Jan Jönsson: Jan Jönsson (born 24 May 1960) is a former Swedish football player and manager.  He is the manager of Sanfrecce Hiroshima.

IFK Hässleholm: IFK Hässleholm is a Swedish football club from Hässleholm that was established in 1905.  The team is currently playing in Division 2 Östra Götaland.  Several well known players have played at the club including England international striker Peter Crouch as well as Swedish footballers Jon Jönsson, Andreas Dahl, and Tobias Linderoth.  In recent years the club has played in Division 2, which is the fourth tier of the Swedish football league system.  However, the club has played in second tier football (Division 1 Södra and Division 2 Södra) in 1972–1974, 1975–81, 1987–1988, and 1992–1998.

Andreas Hermansson: Andreas Hermansson (born January 8, 1973) is a former Swedish football player, who played as a forward for allsvenskan clubs such as Trelleborgs FF, IFK Göteborg, Hammarby IF, Enköpings SK and GIF Sundsvall.  Along with two stints at his hometown club Umeå FC.

Jon Jönsson: Jon Jönsson (born July 8, 1983) is a Swedish football player who plays for IF Elfsborg in the Swedish Allsvenskan.  Jönsson made his first team debut in IFK Hässleholm aged 15, and his talent was recognised by Tottenham Hotspur who brought him to London.  In return IFK Hässleholm received roughly £70,000 and two players to play one season on loan, Alton Thelwell and Peter Crouch.

Roger Gustafsson: Roger Gustafsson (born 29 February 1952 in Gothenburg) is a former Swedish football player and manager.  He has played in the highest Swedish league, Allsvenskan, with GAIS, but is better known as the best performing manager in Allsvenskan ever, having won five Swedish championships with IFK Göteborg.  He also took the club to the Champions League group stage twice and the quarter-finals of the same tournament once.  He is still active in the club as leader of the youth section.

Andreas Dahl: Andreas Dahl (born June 6, 1984 in Hässleholm) is a Swedish former football player.  He has previously spent one season at Coventry City F.C. Prior to that, he represented his home town club IFK Hässleholm.  Dahl has made 15 matches for the Swedish under-21 national team.

Jörgen Jönsson: Ulf Peter Jörgen Jönsson (born 29 September 1972) is a retired Swedish professional ice hockey player who last played for Färjestads BK of the Swedish Elitserien.  He has represented the Team Sweden 285 times, making him the record holder for most games played in the national team.  Jörgen Jönsson is also the older brother of former NHL-star Kenny Jönsson, and the two played 68 games in North America together as teammates.

Tommy Jönsson: Tommy Jönsson (born March 4, 1976) is a former Swedish football player, who played as defender and retired in 2010.

Hamilton Thorp: Hamilton Thorp (born 21 August 1973) is an Australian former professional football player who played for IFK Norrköping in 2003.

Question: Which former IFK Hässleholm football player is older, Jon Jönsson or Peter Crouch?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_one_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first player being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first player."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "player_two_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second player being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second player."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "older_player_name": {
      "type": "string",
      "description": "The name of the player who is older."
    },
    "older_player_birth_year": {
      "type": "integer",
      "description": "The birth year of the older player."
    },
    "younger_player_birth_year": {
      "type": "integer",
      "description": "The birth year of the younger player."
    }
  },
  "required": [
    "player_one_details",
    "player_two_details",
    "older_player_name",
    "older_player_birth_year",
    "younger_player_birth_year"
  ],
  "additionalProperties": false
}
