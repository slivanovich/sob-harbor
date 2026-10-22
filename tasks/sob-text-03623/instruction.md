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
1979–80 Vancouver Canucks season: The 1979–80 Vancouver Canucks season was the team's 10th in the NHL.  Stan Smyl led the team in goals, assists, points, and penalty minutes, the last time one player has led his team in all four categories.  On October 14, 1979, Wayne Gretzky scored his first NHL goal against Glen Hanlon.

1984–85 Pittsburgh Penguins season: The 1984–85 Pittsburgh Penguins season was the team's 18th in the National Hockey League.  It marked the debut of Mario Lemieux for the Penguins.  Lemieux debuted on October 11, 1984, against the Boston Bruins and scored a goal with his very first NHL shot, on his first shift.  Later that season, Lemieux played in the NHL All-Star Game and became the first rookie to be named the All-Star Game's Most Valuable Player.  Despite missing seven games during the season, Lemieux scored 100 points and won the Calder Memorial Trophy as the rookie of the year.

Mike Backman: Michael Charles Backman (born January 2, 1955 in Halifax, Nova Scotia) is a former professional ice hockey right winger.  He was drafted by the World Hockey Association's Quebec Nordiques in the seventh round, one-hundredth overall, of the 1975 WHA Amateur Draft; however, he never played in that league.  Despite being un-drafted in the National Hockey League, he played eighteen regular-season and ten playoff games in the NHL with the New York Rangers over three seasons.  Backman first played NHL hockey with the Rangers in the 1981-82 season, playing three games.  He registered two assists that first year and the following year scored his first NHL goal.

David Hale (ice hockey): David M. Hale (born June 18, 1981) is a former American professional ice hockey player.  He played for the New Jersey Devils, Calgary Flames, Phoenix Coyotes, Tampa Bay Lightning and Ottawa Senators over an eight-year National Hockey League (NHL) career.  Hale is noteworthy for holding the record for most games needed to score his first NHL goal, with it taking him 231 games, scoring it in his 6th professional season.

Joe Pavelski: Joseph James Pavelski (born July 11, 1984) is an American professional ice hockey player and captain for the San Jose Sharks of the National Hockey League (NHL).  He scored a goal in his first NHL game, making him the 11th Sharks player in the history of the team to do so.  He won a silver medal as a member of the United States national men's ice hockey team at the 2010 Winter Olympics in Vancouver.  He also served as captain of Team USA at the 2016 World Cup of Hockey in Toronto.

Morris Stefaniw: Morris Alexander Stefaniw (born January 10, 1948 in North Battleford, Saskatchewan) is a retired professional ice hockey centreman.  During the 1972–73 season, he appeared in 13 games for the NHL's Atlanta Flames.  His lone NHL goal was the first goal in Flames' history and the first goal in the history of the Nassau Veterans Memorial Coliseum, during a 3–2 victory over the New York Islanders on October 7, 1972.

Taylor Leier: Taylor Leier (born February 15, 1994) is a Canadian professional ice hockey player who currently plays for the Lehigh Valley Phantoms of the American Hockey League (AHL).  He was drafted in the fourth round, 117th overall, at the 2012 NHL Entry Draft by the Philadelphia Flyers.  Leier scored his first NHL goal on December 17, 2016 against the Dallas Stars.

Jarkko Varvio: Jarkko Varvio (April 28, 1972 in Tampere, Finland) is a retired Finnish ice hockey player who had a very brief stint in the NHL.  Varvio was drafted by Minnesota North Stars in the 1992 NHL Entry Draft.  He was the top scorer at the 1992 Men's World Ice Hockey Championships in Czechoslovakia.  However, his only two active seasons in the NHL were in 1993-94 and 1994-95 with the Dallas Stars.  In 13 career games, he notched three goals, four assists (for seven points), and had four penalty minutes.  Jarkko scored his first NHL goal in his first NHL game, which was also the first game Dallas Stars played as the Stars since leaving Minnesota.  After his time with the Stars Varvio bounced around Europe playing in various leagues.  Varvio last played for Ravensburg EV in Germany's GerObL before retiring in 2005.

Brandon Kozun: Brandon Scott Kozun (born March 8, 1990) is an American-born Canadian professional ice hockey player currently playing with Lokomotiv Yaroslavl of the Kontinental Hockey League (KHL).  He was a drafted in the sixth round, 179th overall, in the 2009 NHL Entry Draft by the Los Angeles Kings.  He scored his first NHL career goal on February 20, 2015, against the Carolina Hurricanes.

Wayne Gretzky: Wayne Douglas Gretzky {'1': ", '2': ", '3': ", '4': "} ( ; born January 26, 1961) is a Canadian former professional ice hockey player and former head coach.  He played twenty seasons in the National Hockey League (NHL) for four teams from 1979 to 1999.  Nicknamed "The Great One", he has been called "the greatest hockey player ever" by many sportswriters, players, and the league itself.  He is the leading scorer in NHL history, with more goals and assists than any other player.  He garnered more assists than any other player scored total points, and is the only NHL player to total over 200 points in one season – a feat he accomplished four times.  In addition, he tallied over 100 points in 16 professional seasons, 14 of them consecutive.  At the time of his retirement in 1999, he held 61 NHL records: 40 regular-season records, 15 playoff records, and six All-Star records.  As of 2015, he still holds 60 NHL records.

Question: The player who scored his first NHL goal against Glen Hanlon in 1979 was born on which day ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player who scored the goal."
    },
    "first_nhl_goal_event": {
      "type": "object",
      "properties": {
        "opponent_goalie": {
          "type": "string",
          "description": "The name of the opposing goalie against whom the first NHL goal was scored."
        },
        "event_year": {
          "type": "integer",
          "description": "The year the first NHL goal was scored."
        }
      },
      "required": [
        "opponent_goalie",
        "event_year"
      ],
      "additionalProperties": false
    },
    "player_birth_details": {
      "type": "object",
      "properties": {
        "birth_date": {
          "type": "string",
          "description": "The full birth date of the player."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the player."
        }
      },
      "required": [
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "first_nhl_goal_event",
    "player_birth_details"
  ],
  "additionalProperties": false
}
