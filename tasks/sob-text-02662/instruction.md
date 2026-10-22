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
2009 Korea Open Super Series: The 2009 Korea Open Super Series was held from January 13, 2009 to January 18, 2009.  It was a part of the 2009 BWF Super Series badminton tournament.

2009 Singapore Super Series: The 2009 Singapore Open Super Series was the fifth tournament of 2009 BWF Super Series badminton tournament.  It was held from June 9 to June 14, 2009 in Singapore.

P. V. Sindhu: Pusarla Venkata Sindhu (born 5 July 1995) is an Indian professional badminton player, who is currently world no 2 in the BWF World Ranking.  At the 2016 Summer Olympics, she became the first Indian woman to win an Olympic silver medal.  She is one of the two Indian badminton players to ever win an Olympic medal – other being Saina Nehwal.  She was also a silver medalist at the 2017 BWF World Championships and, in 2017, became first Indian ever to win Korea Open Super Series.

2014 Korea Open Super Series: The 2014 Korea Open Super Series was the first super series tournament of the 2014 BWF Super Series.  The tournament took place in Seoul, South Korea from January 7–12, 2014 and had a total purse of $600,000.  A qualification was held to fill four places in four of the five disciplines of the main draws.

2008 Swiss Open Super Series: The 2008 Swiss Open Super Series was the fourth tournament of 2008 BWF Super Series badminton tournament.  It was held from March 11 to March 16, 2008 in Basel, Switzerland.

Kim Hyo-min: Kim Hyo-min (born 8 December 1995 in Ulsan) is a South Korean female badminton player.  Although she now specializes in singles, Kim's first big result in a major international junior event came when she and fellow singles specialist Lee Min-ji reached the girls' doubles semi-finals at the 2012 World Junior Championships.  The following year, she was undefeated in South Korea's run to winning the Suhandinata Cup at the 2013 World Junior Championships.  In 2014, Kim beat Sun Yu to reach the final of the 2014 Macau Open Grand Prix Gold, and she became the runner-up after defeated by P. V. Sindhu in the final round.

2009 Swiss Open Super Series: The 2009 Swiss Open Super Series was the fourth tournament of 2009 BWF Super Series badminton tournament.  It was held from March 10 to March 15, 2009 in Basel, Switzerland.

2010 Korea Open Super Series: The 2010 Korea Open Super Series is the first tournament of the 2010 BWF Super Series in badminton.  It was held in Seoul, South Korea from January 12 to January 17, 2010.

Korea Open (badminton): The Korea Open is an annual badminton event that is commonly held in Seoul, South Korea.  The tournament is now known as Korea Open Super Series because it became one of the BWF Super Series tournaments beginning with 2007.

2011 Korea Open Super Series Premier: The 2011 Korea Open Super Series Premier was the second tournament of the 2011 BWF Super Series.  It was the first competition under the new format where a select group of Super Series events were elevated to premier status.  The tournament was held in Seoul, South Korea from 25–30 January 2011 and had a total purse of $1,200,000.

Question: In which badminton tournament did Pusarla Venkata Sindhu, the first Indian to win Korea Open Super Series, defeat Kim Hyo-min?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tournament_name": {
      "type": "string",
      "description": "The full name of the badminton tournament."
    },
    "tournament_year": {
      "type": "integer",
      "description": "The year the tournament was held."
    },
    "tournament_category": {
      "type": "string",
      "description": "The category or series type of the tournament (e.g., 'Grand Prix Gold', 'Super Series')."
    },
    "match_details": {
      "type": "object",
      "properties": {
        "winner": {
          "type": "object",
          "properties": {
            "player_name": {
              "type": "string",
              "description": "The name of the winning player."
            },
            "player_nationality": {
              "type": "string",
              "description": "The nationality of the winning player."
            }
          },
          "required": [
            "player_name",
            "player_nationality"
          ],
          "additionalProperties": false
        },
        "runner_up": {
          "type": "object",
          "properties": {
            "player_name": {
              "type": "string",
              "description": "The name of the runner-up player."
            },
            "player_nationality": {
              "type": "string",
              "description": "The nationality of the runner-up player."
            }
          },
          "required": [
            "player_name",
            "player_nationality"
          ],
          "additionalProperties": false
        },
        "round": {
          "type": "string",
          "description": "The round of the tournament in which the match took place."
        }
      },
      "required": [
        "winner",
        "runner_up",
        "round"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tournament_name",
    "tournament_year",
    "tournament_category",
    "match_details"
  ],
  "additionalProperties": false
}
