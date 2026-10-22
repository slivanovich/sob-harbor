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
Geof Motley: Geof Motley OAM is a former Australian rules footballer and coach who played for South Australian National Football League (SANFL) side Port Adelaide.  Motley was born near Alberton Oval, the home ground of the Port Adelaide Football Club, and grew up supporting Port Adelaide.

Norwood–Port Adelaide rivalry: The Norwood–Port Adelaide rivalry is Australian rules football's oldest and one of its most intense rivalries.  It is contested between the Norwood Football Club and the Port Adelaide Football Club.  Together Port Adelaide (36) and Norwood (30) have won 66 South Australian National Football League (SANFL) premierships since the founding of the competition in 1878.  As the SANFL competition has been suspended due to war, only 132 seasons have been played, therefore together Norwood and Port Adelaide have won exactly half of all SANFL premierships awarded.  The two clubs have met in finals 50 times with 17 of those grand finals including 2 war-time grand finals.

Jacob Surjan: Jacob Adam Surjan (born 15 August 1985 in Perth, Australia) is an Australian rules footballer of Croatian descent and former player of the Port Adelaide Football Club.  He currently serves as the development coach of the Port Adelaide Football Club at AFL level, and as the midfield coach of Port Adelaide at SANFL level.

Port Adelaide Football Club: The Port Adelaide Football Club is a professional Australian rules football club based in Alberton, Port Adelaide, South Australia.  The club's senior team plays in the Australian Football League (AFL) under the nickname Power, whilst its reserves and development teams compete in the South Australian National Football League (SANFL) under the nickname Magpies.  Port Adelaide is the oldest professional sporting club in South Australia and the fifth-oldest club in the AFL.  Since the club's first game on 24 May 1870, the club has won 36 South Australian league premierships, including six in a row.  The club also won the Champions of Australia competition on a record four occasions.  In 1997, the club joined the Australian Football League as the only pre-existing non-Victorian club—and subsequently added the 2004 AFL premiership to its achievements.

Jesse Palmer (Australian footballer): Jesse Palmer (born 17 October 1996) is an Australian rules footballer playing for the Port Adelaide Football Club in the Australian Football League (AFL).  He was drafted by the Port Adelaide Football Club with their third selection and seventy-eighth overall in the 2014 national draft.  He made his debut in the forty point loss against Melbourne in round 21, 2016 at the Adelaide Oval.

Dan Houston: Daniel "Dan" Houston (born 12 May 1997) is an Australian rules footballer playing for the Port Adelaide Football Club in the Australian Football League (AFL).  He was drafted by the Port Adelaide Football Club with their third selection and forty-fifth overall in the 2016 rookie draft.  Prior to the start of the 2017 season, he was promoted to the senior list and subsequently made his debut in the twenty-eight point win against Sydney in the opening round of the season at the Sydney Cricket Ground.

Chad Cornes: Chad Studley Cornes (born 12 November 1979) is a former professional Australian rules footballer who played for the Port Adelaide Football Club and Greater Western Sydney Giants in the Australian Football League (AFL).  He was a member of the Port Adelaide side which won the premiership in 2004.  On 3 July 2013, he retired from AFL football due to a troublesome knee.  Cornes is currently serving as the SANFL coach of Port Adelaide.

Gavin Wanganeen: Gavin Adrian Wanganeen (born 18 June 1973) is a former Australian rules footballer who played for Essendon in the Australian Football League (AFL) and Port Adelaide in both the AFL and the South Australian National Football League (SANFL).  Wanganeen won the 1993 Brownlow Medal.  Wanganeen is a descendant of the Kokatha Mula people.  He is the first cousin of brothers Aaron and Alwyn Davey.

John Butcher (Australian footballer): John Butcher (born 3 July 1991) is a former professional Australian rules footballer who played for the Port Adelaide Football Club in the Australian Football League (AFL).  He was the earliest of the three Port Adelaide players drafted in the first round in the 2009 AFL Draft (he went at pick #8).  Butcher's younger brother Danny was drafted to Port Adelaide as part of the Rookie Draft in 2011 at pick 21.

Ashley Fernee: Ashley Fernee (born 24 June 1977) is a former Australian rules footballer who played in the Australian Football League (AFL).  He was selected for the Adelaide Football Club in the 1995 draft, having previously played with the Calder Cannons.  Fernee only played two games for the Adelaide Football Club in 1996, debuting against Fitzroy Football Club in round 17.  In spite of those two games, he was not selected to play in 1997, and in 1998 things were not looking promising, with Michelangelo Rucci stating that the "wait will go on unless a long injury list strikes again".  Fernee did not play in 1998, and he was delisted by the Adelaide Football Club in October of that year.  He played for the SANFL team, South Adelaide Football Club, in 1999, and nominated for the AFL draft at the end of the season.  Unsuccessful, Fernee left Adelaide to return to Victoria, where he played for the East Keilor Football Club.

Question: Gavin Adrian Wanganeen played for The Port Adelaide Football Club that is located where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "club_name": {
      "type": "string",
      "description": "The name of the football club."
    },
    "player_name": {
      "type": "string",
      "description": "The name of the player associated with the club."
    },
    "club_location": {
      "type": "object",
      "properties": {
        "suburb": {
          "type": "string",
          "description": "The suburb where the club is based."
        },
        "city": {
          "type": "string",
          "description": "The city where the club is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the club is located."
        }
      },
      "required": [
        "suburb",
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "club_name",
    "player_name",
    "club_location"
  ],
  "additionalProperties": false
}
