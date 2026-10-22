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
Rafael Dumas: Rafael Dumas (born 13 March 1995) is a Brazilian professional footballer who plays as a defender for Paysandu, on loan from Brazilian Série A club Flamengo.  He previously had a six-month loan spell at FC Goa in the Indian Super League in 2016 and at Global.

2009 FIFA Confederations Cup Final: The 2009 FIFA Confederations Cup Final was a football match to determine the winners of the 2009 FIFA Confederations Cup.  The match was held at Coca-Cola Park, Johannesburg, South Africa, on 28 June 2009 and was contested by the United States and Brazil.  Despite being two goals down at half-time, Brazil won the match 3–2, with Lúcio scoring the winning goal six minutes from full-time.

Nicolau Colaco: Nicolau Colaco (born 16 May 1984) is an Indian footballer who plays as a defender for FC Goa in the Indian Super League, on loan from I-League club Salgaocar.

Lúcio: Lucimar Ferreira da Silva (born 8 May 1978), commonly known as Lúcio, is a Brazilian footballer who last played for FC Goa of the Indian Super League as a central defender.

2015 Indian Super League season: The 2015 Indian Super League Season was the second season of the Indian Super League, a professional football league played in India since 2014.  The season features eight teams.  The regular season kicked-off on 3 October and ended on 6 December, while the finals began on 11 December, which will conclude with the final match on 20 December.  The defending champions Atlético de Kolkata were eliminated in the semi-finals by Chennaiyin.  The final was played between Goa and Chennayin on 20 December 2015 at the Fatorda Stadium in Goa.  Chennayin were crowned as champions defeating Goa 3-2 in the final.

FC Goa: FC Goa (also known as The Gaurs) is an Indian professional football franchise based in Goa that competes in the Indian Super League.  The club was launched on 26 August 2014.  The team is owned by Goan Football Club Pvt. Ltd. which consists of "Jaydev Mody", Venugopal Dhoot and Virat Kohli.  It represents Goa, the only state or union territory to declare football as its official sport.  The logo represents Goa's state animal the Gaur while the colours blue and orange symbolizes the Goan coastline and sunrise.

2015 Indian Super League Final: The 2015 Indian Super League Final was a football match between Goa and Chennaiyin who reached the final of 2015 Indian Super League played on 20 December 2015 at the Fatorda Stadium in Goa.  Chennayin defeated Goa 3-2 in the match to win the season.

2016 Indian Super League Final: The 2016 Indian Super League Final was a football match between Atlético de Kolkata and Kerala Blasters on 18 December 2016 at the Jawaharlal Nehru Stadium in Kochi, Kerala.  It was the final match of the 2016 Indian Super League season, the third season of the Indian Super League.  The match was the second time these two teams played each other in the Indian Super League final after both sides met in the inaugural 2014 final.  Atlético de Kolkata won that final 1–0.

Victor Simões: Victor Simões, full name Victor Simões de Oliveira (born March 23, 1981, in Rio de Janeiro) is a Brazilian footballer who last played for FC Goa in the Indian Super League.

Richarlyson: Richarlyson Barbosa Felisbino, simply Richarlyson, (born 27 December 1982) is a Brazilian footballer who plays for FC Goa in the Indian Super League.  Mainly a defensive midfielder, he can also play as a left back or central defender.

Question: What was the final score of the 2009 football match against the United States which was won by a Brazilian footballer who last played as central defender for FC Goa of the Indian Super League?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "match_name": {
      "type": "string",
      "description": "The name of the football match."
    },
    "match_year": {
      "type": "integer",
      "description": "The year the match took place."
    },
    "teams_contested": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The teams that contested the match."
    },
    "winning_team": {
      "type": "string",
      "description": "The team that won the match."
    },
    "final_score": {
      "type": "string",
      "description": "The final score of the match."
    },
    "winning_goal_scorer_details": {
      "type": "object",
      "properties": {
        "player_name": {
          "type": "string",
          "description": "The name of the player who scored the winning goal."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the player."
        },
        "last_club": {
          "type": "string",
          "description": "The last club the player played for."
        },
        "position": {
          "type": "string",
          "description": "The primary playing position of the player."
        }
      },
      "required": [
        "player_name",
        "nationality",
        "last_club",
        "position"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "match_name",
    "match_year",
    "teams_contested",
    "winning_team",
    "final_score",
    "winning_goal_scorer_details"
  ],
  "additionalProperties": false
}
