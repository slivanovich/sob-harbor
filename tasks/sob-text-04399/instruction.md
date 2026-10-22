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
1997–98 WCHL season: The 1997-98 West Coast Hockey League season was the third season of the West Coast Hockey League, a North American minor professional league.  Nine teams participated in the regular season, and the San Diego Gulls were the league champions.  In addition to league play, WCHL teams played regular season games against the Russian Superleague team CKA-Amur (now Amur Khabarovsk).

1959–60 EPHL season: The 1959-60 Eastern Professional Hockey League season was the first season of the Eastern Professional Hockey League, a North American minor professional league.  Six teams participated in the regular season, and the Montreal Royals were the league champions.

1960–61 EPHL season: The 1960-61 Eastern Professional Hockey League season was the second season of the Eastern Professional Hockey League, a North American minor professional league.  Six teams participated in the regular season, and the Hull-Ottawa Canadians were the league champions.

Sherbrooke Saint-François: The Sherbrooke Saint-François was a minor league professional ice hockey team based in Sherbrooke, Quebec.  The team was part of the minor professional league Ligue Nord-Américaine de Hockey (LNAH).  The Saint-Francois played at the Palais des Sports.

Dennis McCauley: Dennis McCauley (born August 15, 1985) is an American professional ice hockey player who is currently playing for the Portland Pirates in the American Hockey League.

Bakersfield Oilers: The Bakersfield Oilers was a semi-pro hockey team in the Pacific Southwest Hockey League that played in Bakersfield, California in 1994-95.  The Oilers played out of the 4,100 seat Bakersfield Convention Center.  The Oilers were the predecessor to the Bakersfield Fog of the West Coast Hockey League.  They made the transition along with the Alaska Gold Kings (Fairbanks, Alaska), Anchorage Aces (Anchorage, Alaska), and Fresno Falcons (Fresno, California) to a minor professional league in 1995-96.  The players had college, major junior, junior A and minor pro experience.  Many of the players spent their off season playing roller hockey Roller Hockey International and were living in southern California.

1961–62 EPHL season: The 1961-62 Eastern Professional Hockey League season was the third season of the Eastern Professional Hockey League, a North American minor professional league.  Six teams participated in the regular season, and the Hull-Ottawa Canadians were the league champions.

1998–99 WCHL season: The 1998–99 West Coast Hockey League season was the fourth season of the West Coast Hockey League, a North American minor professional league.  Nine teams began the regular season, although the Tucson Gila Monsters folded after 21 games.  Tucson's unexpected mid-season exit created schedule irregularities, causing some teams to play 70 regular season games while others played 71.

1962–63 EPHL season: The 1962-63 Eastern Professional Hockey League season was the fourth and final season of the Eastern Professional Hockey League, a North American minor professional league.  Four teams participated in the regular season, and the Kingston Frontenacs were the league champions.

Portland Pirates: The Portland Pirates were a minor league professional ice hockey team in the American Hockey League (AHL).  Their home arena was the Cross Insurance Arena in downtown Portland, Maine.  The franchise was previously known as the Baltimore Skipjacks from 1982 to 1993.

Question: What minor professional league did Dennis McCauley play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the ice hockey player."
    },
    "league_name": {
      "type": "string",
      "description": "The name of the minor professional league the player is associated with."
    },
    "league_type": {
      "type": "string",
      "description": "The type of the league, e.g., 'minor professional'."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the player is currently playing for."
    }
  },
  "required": [
    "player_name",
    "league_name",
    "league_type",
    "team_name"
  ],
  "additionalProperties": false
}
