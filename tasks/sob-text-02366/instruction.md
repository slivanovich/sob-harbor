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
Darren Minchington: Darren Minchington is an Australian rules footballer who plays for the St Kilda Football Club in the Australian Football League (AFL).  He made his debut on 9 August 2013 against Hawthorn Football Club in Round 20 of the 2013 AFL season.  He started his senior football career at St Kilda's VFL affiliate club Sandringham in 2012, but suffered a hip injury after playing nine games, ending his season.  He has kicked two goals in two games for the St Kilda Football Club and will look to retain his place in the side in the 2014 AFL season.  He was dropped after his second game against the Sydney Swans even though he contributed with a goal.

2016 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2016, this is officially known as the Coates Hire AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite at the league's website.  Eddie Betts of the Adelaide Football Club was the winner with his goal kicked in round ten against the Greater Western Sydney Giants.

2014 AFL Goal of the Year: The Australian Football League celebrated the best goal of the season through the annual Goal of the Year competition.  In 2014, it was officially known as the Hungry Jacks AFL Goal of the Year.  Each round three goals were nominated and fans were able to vote online for their favourite at the league's website.

Jay Kennedy-Harris: Jay Kennedy-Harris (born 21 March 1995) is a professional Australian rules footballer playing for the Melbourne Football Club in the Australian Football League (AFL).  A small forward, 1.73 m tall and weighing 75 kg , Kennedy-Harris has the ability to play in both the forward line and the midfield.  He entered top level football early when he played for the Oakleigh Chargers in the TAC Cup as a bottom-aged player, in addition to representing Vic Metro in the 2013 AFL Under 18 Championships.  His achievements as a junior include being the first indigenous player to captain a TAC Cup side and he was named in the TAC Cup team of the year.  He was recruited by the Melbourne Football Club with the fortieth overall selection in the 2013 AFL draft and made his debut in the 2014 season.

Rhys Mathieson: Rhys Mathieson (born 10 January 1997) is a professional Australian rules footballer with the Brisbane Lions in the Australian Football League (AFL).  He was recruited by the Brisbane Lions with the 39th selection in the 2015 national draft.  At 1.87 metres (6 ft 2 in) tall and weighing 84 kilograms (185 lb), he plays as a Midfielder and is known for his ability to win contested ball.  He played his first senior game in round 9 of the 2016 season against Melbourne.  In his time at the Lions he has been known for his on-field antics, in particular his goal celebrations.  Upon kicking his first AFL goal, Rhys celebrated with a 'shotgun' move made famous by Hawthorn's Mark WIlliams and faced some criticism for this showboating, while the Lions were losing to GWS in round 17, 2016.

2013 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2013, this is officially known as the British Paints AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite at the league's website.  At the end of the home and away season, three finalists were selected for a final public vote, which was won by Lance Franklin for his long-range goal after hurdling over a teammate in the middle of the ground.

2013 AFL Grand Final: The 2013 AFL Grand Final was an Australian rules football game contested between Hawthorn Football Club and Fremantle Football Club at the Melbourne Cricket Ground on 28 September 2013.  It was the 117th annual Grand Final of the Australian Football League (formerly the Victorian Football League), staged to determine the premiers for the 2013 AFL season.  The match, attended by 100,007 spectators, was won by Hawthorn by a margin of 15 points, marking the club's eleventh VFL/AFL premiership victory.  Hawthorn's Brian Lake was awarded the Norm Smith Medal as the best player on the ground.

2017 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2017, this is officially known as the Coates Hire AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite at the league's website.  Daniel Rioli of Richmond was the winner with his banana goal kicked in round 3 against West Coast .  His selection as a finalist was controversial due to him not even winning the vote for Goal of the Week in round 3.

2007 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual AFL Goal of the Year competition.  In 2007, this is officially known as the Toyota AFL Mark of the Year

Lance Franklin: Lance "Buddy" Franklin (born 30 January 1987) is a professional Australian rules footballer playing for the Sydney Swans in the Australian Football League (AFL).  He previously played for the Hawthorn Football Club between 2005 and 2013.  Franklin is the tenth-highest goalkicker in VFL/AFL history with 860 career goals, which is the most of any current player, and has led his clubs' goalkicking ten times.  He has won a total of seven All-Australian selections (three at full forward and four at centre half-forward) and four Coleman Medals throughout his career.

Question: How many Coleman Medals did the winner of the 2013 AFL Goal of the Year win?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "goal_of_the_year_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year of the AFL Goal of the Year competition."
        },
        "winner_name": {
          "type": "string",
          "description": "The name of the player who won the Goal of the Year for that season."
        }
      },
      "required": [
        "year",
        "winner_name"
      ],
      "additionalProperties": false
    },
    "winner_career_achievements": {
      "type": "object",
      "properties": {
        "coleman_medals_won": {
          "type": "integer",
          "description": "The total number of Coleman Medals won by the player."
        }
      },
      "required": [
        "coleman_medals_won"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "integer",
      "description": "The answer to the question: how many Coleman Medals did the winner of the 2013 AFL Goal of the Year win?"
    }
  },
  "required": [
    "goal_of_the_year_details",
    "winner_career_achievements",
    "question_answer"
  ],
  "additionalProperties": false
}
