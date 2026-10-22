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
Adam Saad: Adam Saad (born 23 July 1994) is an Australian rules footballer who plays for the Gold Coast Football Club in the Australian Football League (AFL).  Saad made his debut for the Suns in Round 1 of the 2015 season and kicked one goal.  Renowned for his precise ball use by foot and ability to break the lines and cut angles to evade opponents, he was chosen at pick #25 in the 2015 Rookie draft from the Coburg Football Club in the Victorian Football League (VFL).  In Round 5, 2015 Saad was nominated for the Rising Star after his teams win over the Brisbane Lions where he had 26 touches.

2007 AFL season: The 2007 Australian Football League season was the 111th season of the elite Australian rules football competition.  The regular season commenced on 30 March 2007, and concluded with the 2007 AFL Grand Final on 29 September 2007, with Geelong defeating Port Adelaide by 119 points, the highest winning-margin in an AFL Grand Final, to claim the 2007 AFL premiership.

2008 AFL season: The 2008 Australian Football League season was the 112th season of the elite Australian rules football competition.  This season commenced on 20 March 2008 and concluded on 27 September 2008.  The season consisted of twenty-two rounds of home-and-away matches, and four rounds of finals.  The premiership was won by Hawthorn , who beat minor premiers Geelong by 26 points in the 2008 AFL Grand Final.

2016 AFL season: The 2016 Australian Football League season was the 120th season of the elite Australian rules football competition.  There were 18 teams competing in the league, the same as the previous four seasons.  The first game was played on Thursday, 24 March, and the 2016 AFL Grand Final was played on Saturday, 1 October with the Western Bulldogs defeating Sydney by 22 points to win its second premiership and first in 62 years, breaking the then-longest active drought in VFL/AFL history.

2017 AFL season: The 2017 Australian Football League season was the 121st season of the elite Australian rules football competition.  There are 18 teams competing in the league, the same as the previous five seasons.  The first game was played on Thursday, 23 March, and the season concluded with the 2017 AFL Grand Final on Saturday, 30 September.

1952 VFL Grand Final: The 1952 VFL Grand Final was an Australian rules football game contested between the Geelong Football Club and Collingwood Football Club, held at the Melbourne Cricket Ground on 27 September 1952.  It was the 56th annual Grand Final of the Victorian Football League, staged to determine the premiers for the 1952 VFL season.  The match, attended by 81,304 spectators, was won by Geelong by 46 points, marking that club's fifth premiership victory and second in succession.

International Rules Series: The International Rules Series is a senior men's international rules football competition between the Australia international rules football team (selected by the Australian Football League) and the Ireland international rules football team (selected by the Gaelic Athletic Association).  The series is played close to annually in October or November after the completion of the AFL Grand Final and the All-Ireland Football Final which are both traditionally played in late September.  The matches are played using a set of compromise rules decided upon by both the two governing bodies; known formally as international rules football.  While the International Rules Series matches use some rules from Australian rules football, the field, ball and uniforms of both teams are all from Gaelic football.

2015 AFL season: The 2015 Australian Football League season was the 119th season of the elite Australian rules football competition.  There were 18 teams competing in the league, the same as the previous year.  The first game was played on Thursday, 2 April, and the Grand Final was played on Saturday, 3 October, with Hawthorn defeating by 46 points to win its 13th premiership and its third in successive years.

2015 AFL Grand Final: The 2015 AFL Grand Final was an Australian rules football match contested between the Hawthorn Football Club and the West Coast Eagles at the Melbourne Cricket Ground on 3 October 2015.  It was the 119th annual Grand Final of the Australian Football League (formerly the Victorian Football League), staged to determine the premiers for the 2015 AFL season.  The match, attended by 98,632 spectators, was won by Hawthorn by a margin of 46 points, marking the club's third consecutive premiership and thirteenth VFL/AFL premiership victory overall.  Hawthorn's Cyril Rioli was awarded the Norm Smith Medal as the best player on the ground.

1992 AFL season: The 1992 Australian Football League season was the 96th season of the elite Australian rules football competition.  The AFL Grand Final this year was won by the West Coast Eagles, who became the first non-Victorian club to win a Premiership.

Question: Who won the Grand Final of the elite Australian rules football competition by 46 points in the same year that saw Adam Saad nominated for the Rising Star?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "grand_final_year": {
      "type": "integer",
      "description": "The year of the AFL Grand Final in question, which is also the year the player was nominated for the Rising Star."
    },
    "player_rising_star_nomination": {
      "type": "object",
      "properties": {
        "player_name": {
          "type": "string",
          "description": "The name of the player nominated for the Rising Star award."
        },
        "nomination_round": {
          "type": "integer",
          "description": "The round in which the player was nominated for the Rising Star."
        }
      },
      "required": [
        "player_name",
        "nomination_round"
      ],
      "additionalProperties": false
    },
    "grand_final_outcome": {
      "type": "object",
      "properties": {
        "winning_team": {
          "type": "string",
          "description": "The team that won the Grand Final."
        },
        "losing_team": {
          "type": "string",
          "description": "The team that lost the Grand Final."
        },
        "winning_margin_points": {
          "type": "integer",
          "description": "The points difference by which the winning team defeated the losing team."
        },
        "winner_premiership_details": {
          "type": "object",
          "properties": {
            "total_premierships": {
              "type": "integer",
              "description": "The total number of premierships won by the winning team, including this one."
            },
            "consecutive_premierships": {
              "type": "integer",
              "description": "The number of consecutive premierships won by the winning team, including this one."
            }
          },
          "required": [
            "total_premierships",
            "consecutive_premierships"
          ],
          "additionalProperties": false
        },
        "norm_smith_medalist": {
          "type": "string",
          "description": "The player awarded the Norm Smith Medal for best on ground in the Grand Final."
        },
        "spectator_count": {
          "type": "integer",
          "description": "The number of spectators who attended the Grand Final."
        }
      },
      "required": [
        "winning_team",
        "losing_team",
        "winning_margin_points",
        "winner_premiership_details",
        "norm_smith_medalist",
        "spectator_count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "grand_final_year",
    "player_rising_star_nomination",
    "grand_final_outcome"
  ],
  "additionalProperties": false
}
