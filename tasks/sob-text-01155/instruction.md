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
Martin Jol: Maarten Cornelis "Martin" Jol (born 16 January 1956) is a Dutch football manager and former midfielder.

Kim Nam-il: Kim Nam-Il (Korean: 김남일 ; born 14 March 1977) is a retired South Korean footballer who played as defensive midfielder.  He was virtually unknown before he became a superstar for his impressive defensive displays in the 2002 FIFA World Cup.

Kim Tae-wan: Kim Tae-wan (; born 13 August 1991) is a retired South Korean footballer and currently manager.  He is a manager of Sangju Sangmu in K League Classic.

Dang Seong-jeung: Dang Seong-jeung (; born 4 January 1966) is a retired South Korean footballer and coach. On 29 November 2012, he was appointed manager of Daegu FC.

Lee Young-pyo: Lee Young-pyo (Korean: 이영표 ; ] ; born 23 April 1977) is a retired South Korean footballer.  Lee was recognized for his speed and dribbling skills.  His former manager Martin Jol once called him "the best left-back in Holland".

Johan Neeskens: Johannes Jacobus "Johan" Neeskens (] ; born 15 September 1951) is a Dutch football manager and former midfielder.  As a player, he was an important member of the Dutch national team that finished as runners-up in the 1974 and 1978 FIFA World Cups and is considered to be one of the greatest Dutch midfielders of all time.  In 2004, he was named one of the 125 Greatest Living Footballers at a FIFA Awards Ceremony., while in 2017 he has been included in the "FourFourTwo" list of the 100 all-time greatest players, at the 64th position.

Kim Bum-soo (footballer, born 1968): Kim Bum-Soo (; born 29 August 1968) is a retired South Korean footballer and football goalkeeper coach.

Son Jong-hyun: Son Jong-hyun (born 30 November 1991) is a retired South Korean footballer who last played as a midfielder for Louisville City of the USL in 2016.

Arnold Mühren: Arnold Johannes Hyacinthus Mühren (born 2 June 1951 in Volendam, North Holland) is a Dutch football manager and former midfielder.  His older brother Gerrie, also a midfield player, won three European Cup titles with Ajax in the early 1970s.  Mühren is among the few players to have won all three major UEFA-organised club competitions, the European Cup (1972–73), the Cup Winners' Cup (1986–87) and the UEFA Cup (1980–81).  The last of these was won with Ipswich Town, while the other titles were won while playing for Ajax.  He is also one of the two Dutch players, together with Danny Blind, to have won all UEFA club competitions and the Intercontinental Cup.

Park Jong-chan: Park Jong-chan (Hangul: 박종찬 ; born 2 October 1981) is a retired South Korean footballer who played as midfielder.

Question: The retired South Korean footballer worked under which Dutch football manager and former midfielder born in 1956?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "manager": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Dutch football manager."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the manager."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the manager."
        },
        "former_playing_position": {
          "type": "string",
          "description": "The former playing position of the manager."
        }
      },
      "required": [
        "name",
        "nationality",
        "birth_year",
        "former_playing_position"
      ],
      "additionalProperties": false
    },
    "managed_player": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the retired South Korean footballer managed by the manager."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the player."
        },
        "status": {
          "type": "string",
          "description": "The current status of the player (e.g., 'retired footballer')."
        }
      },
      "required": [
        "name",
        "nationality",
        "status"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "A description of the relationship between the manager and the player."
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the Dutch football manager who fits the criteria."
    }
  },
  "required": [
    "manager",
    "managed_player",
    "relationship_description",
    "final_answer"
  ],
  "additionalProperties": false
}
