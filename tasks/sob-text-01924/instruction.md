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
1996 Porsche Tennis Grand Prix – Doubles: Gigi Fernández and Natasha Zvereva were the defending champions but only Zvereva competed that year with Lisa Raymond.

Raúl Ramírez: Raúl Ramírez (born 20 June 1953) is a retired Mexican professional tennis player.  He was active during the 1970s and 1980s, and is regarded as one of the great all-around players of the modern era.  Ramírez was also the first player to finish first in both singles and doubles Grand Prix point standings, accomplishing the feat in 1976.  He attended and played tennis at the University of Southern California in Los Angeles.

1997 Toray Pan Pacific Open – Doubles: Gigi Fernández and Natasha Zvereva were the defending champions but they competed with different partners that year, Fernández with Martina Hingis and Zvereva with Lindsay Davenport.

Natasha Zvereva: Natasha Zvereva, or Zverava, (born Natallya Maratawna Zverava; Belarusian: Наталля Маратаўна Зверава; 16 April 1971) is a former tennis player from Belarus.  Zvereva was the first major athlete in the Soviet Union to demand publicly that she should be able to keep her tournament earnings.  The team of Zvereva and Gigi Fernández won more women's doubles titles and Grand Slam women's doubles championships than any other team since that of Martina Navratilova and Pam Shriver.

1992 US Open – Women's Doubles: Pam Shriver and Natasha Zvereva were the defending champions but they competed with different partners that year, Shriver with Martina Navratilova and Zvereva with Gigi Fernández.

1995 Ameritech Cup – Doubles: Gigi Fernández and Natasha Zvereva were the defending champions but only Zvereva competed that year with Lori McNeil.

1996 Acura Classic – Doubles: Gigi Fernández and Natasha Zvereva were the defending champions but only Zvereva competed that year with Lindsay Davenport.

1996 US Open – Women's Doubles: Gigi Fernández and Natasha Zvereva were the defending champions and successfully defended their title, defeating Jana Novotná and Arantxa Sánchez Vicario 1–6, 6–1, 6–4 in the final.  It was the 5th US Open, 15th Grand Slam and 66th overall title for Fernández, and the 4th US Open, 15th Grand Slam and 60th overall title, in their respective careers.

1997 Acura Classic – Doubles: Lindsay Davenport and Natasha Zvereva were the defending champions but they competed with different partners that year, Davenport with Chanda Rubin and Zvereva with Gigi Fernández.

1996 French Open – Women's Doubles: Gigi Fernández and Natasha Zvereva were the defending champions, but lost 6–2, 6–1 in the final to Lindsay Davenport and Mary Joe Fernández.  It was the 1st Grand Slam doubles title and the 8th title overall for Davenport, and the 2nd Grand Slam doubles title and the 14th title overall for Fernández, in their respective careers.

Question: Whom between  Natasha Zvereva and Raúl Ramírez did Gigi Fernández win the most Grand Slam double's championships with?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "main_player_name": {
      "type": "string",
      "description": "The name of the player whose Grand Slam doubles championships are being evaluated."
    },
    "compared_partners": {
      "type": "array",
      "description": "A list of partners being compared for Grand Slam doubles championships with the main player.",
      "items": {
        "type": "object",
        "properties": {
          "partner_name": {
            "type": "string",
            "description": "The name of the partner."
          },
          "grand_slam_doubles_championships_won_with_main_player": {
            "type": "integer",
            "description": "The number of Grand Slam doubles championships won by the main player with this specific partner."
          }
        },
        "required": [
          "partner_name",
          "grand_slam_doubles_championships_won_with_main_player"
        ],
        "additionalProperties": false
      }
    },
    "partner_with_most_grand_slam_doubles_championships": {
      "type": "string",
      "description": "The name of the partner with whom the main player won the most Grand Slam doubles championships."
    },
    "number_of_titles_with_winning_partner": {
      "type": "integer",
      "description": "The total number of Grand Slam doubles championships won with the identified winning partner."
    }
  },
  "required": [
    "main_player_name",
    "compared_partners",
    "partner_with_most_grand_slam_doubles_championships",
    "number_of_titles_with_winning_partner"
  ],
  "additionalProperties": false
}
