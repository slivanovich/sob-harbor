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
Stefan Noesen: Stefan Noesen (born February 12, 1993) is an American professional ice hockey player.  He is currently playing for the New Jersey Devils of the National Hockey League (NHL).  Noesen was selected in the first round (21st overall) of the 2011 NHL Entry Draft by the Ottawa Senators.

1999 NHL Entry Draft: The 1999 NHL Entry Draft was held on June 26 at the FleetCenter in Boston, Massachusetts.  According to "Sports Illustrated" and other sports news agencies, at the time the 1999 draft was considered one of the deepest in talent in years, headed by Patrik Stefan and the Sedin twins.  However, the overall impact in the NHL hasn't matched those of the neighboring drafts.  An example of this one is how many first round picks have played the equivalent of an entire regular season ten seasons after the 1999 draft; only 16 out of 28 first round picks in 1999 have played 82 NHL games, while the same statistic applies to 23 out of 27 players in 1998 and 21 out of 30 players in 2000.  In addition, while the Sedin twins have excelled in the NHL, only Barret Jackman and Martin Havlat were still active players of the other 26 first-round picks in the NHL 15 years after the draft.  The team that originally held the first overall pick, the Tampa Bay Lightning, traded out of the first round altogether in the trading carousel used to select the Sedins.

Paul Houck: Paul Houck (born August 12, 1963 in Vancouver, British Columbia) is a former ice hockey player.  He had a successful college career with the University of Wisconsin between 1981 and 1985, and was named a Western Collegiate Hockey Association Second Team All-Star in 1983, as well as earning a spot on the National Collegiate Athletic Association Championship All-Tournament team.  He was selected 71st overall by the Edmonton Oilers in the 1981 NHL Entry Draft, and traded to the Minnesota North Stars in 1985.  Houck played 16 National Hockey League games for the North Stars between 1985 and 1988, scoring one goal and two assists while spending most of his career in the minor leagues.  He played two seasons in the Nederlands between 1989 and 1991 before retiring.  His son, Jackson Houck, was drafted 94th overall by the Edmonton Oilers in the 2013 NHL Entry Draft.  Paul, of the 1981 NHL Entry Draft, and his son, of the 2013 NHL Entry Draft, become the first father-and-son tandem drafted by the Edmonton Oilers in the team's history.

Nick Merkley: Nicholas Merkley (born May 23, 1997) is a Canadian professional ice hockey player.  He is currently playing with the Tucson Roadrunners of the American Hockey League (AHL) as a prospect for the Arizona Coyotes of the National Hockey League (NHL).  Merkley was rated as a top prospect who was widely projected to be a first round selection in the 2015 NHL Entry Draft.  In the said Draft, he was selected 30th overall by the Arizona Coyotes, the final pick of the opening round.

Jay Bouwmeester: Jay Daniel Bouwmeester (born September 27, 1983) is a Canadian professional ice hockey defenceman playing for the St. Louis Blues of the National Hockey League (NHL).  He was a first round selection, third overall, of the Florida Panthers at the 2002 NHL Entry Draft.  He was named to the NHL All-Rookie Team in 2003 and played seven seasons in the Panthers organization before being traded to the Calgary Flames in 2009, with whom he played four seasons.  He held one of the longest iron man streaks in NHL history as he appeared in 737 consecutive regular season games between 2004 and 2014.  Bouwmeester played in the 2007 and 2009 NHL All-Star Games.

Frédérik Gauthier: Frédérik Gauthier (born April 26, 1995) is a Canadian professional ice hockey player.  He is currently playing in the Toronto Maple Leafs organization of the National Hockey League (NHL).  He was selected by the Maple Leafs in the 1st round (21st overall) of the 2013 NHL Entry Draft.  Gauthier is a top prospect who was ranked number eight on the NHL Central Scouting Bureau's final ranking of North American skaters.  He fulfilled the expectation to be a first round selection at the 2013 NHL Entry Draft.  He was born in Laval, Quebec, a suburb of Montreal.

Paul Bittner: Paul Bittner (born November 4, 1996) is an American professional ice hockey Winger who is currently assigned to the Cleveland Monsters of the American Hockey League (AHL) as a prospect of the Columbus Blue Jackets in the National Hockey League (NHL).  Bittner has played major junior hockey with the Portland Winterhawks of the Western Hockey League (WHL).  Bittner was rated as a top prospect who was widely projected to be a first round selection in the 2015 NHL Entry Draft.  He was, however, selected 38th overall, in the second round by the Blue Jackets in the 2015 NHL Entry Draft.

2010 NHL Entry Draft: The 2010 NHL Entry Draft was the 48th NHL Entry Draft, held on June 25–26, 2010 at the Staples Center in Los Angeles, California, home arena of the Los Angeles Kings.  This was the first time Los Angeles hosted the NHL Entry Draft.  An unofficial record of 11 American-trained players were selected in the first round, starting with Jack Campbell and ending with Brock Nelson.  The record was set in the 2006 and 2007 drafts, where 10 U.S.-trained players were selected in the first round.

2011 NHL Entry Draft: The 2011 NHL Entry Draft was the 49th NHL Entry Draft.  It was held on June 24–25, 2011, at the Xcel Energy Center in St. Paul, Minnesota.  It was the first time the Draft was held in the state of Minnesota since the Minnesota North Stars hosted the 1989 NHL Entry Draft.

1987–88 Quebec Nordiques season: Quebec made a huge trade during the 1987 NHL Entry Draft, as the Nordiques traded away Dale Hunter and Clint Malarchuk to the Washington Capitals for Gaetan Duchesne, Alan Haworth, and the Capitals first round draft pick in the 1987 NHL Entry Draft, in which the Nordiques selected Joe Sakic.  Haworth had an injury plagued season in 1986–87, appearing in only 50 games, however, he scored 25 goals and 41 points.  In 1985–86, Haworth had a career high 34 goals and 73 points for the Capitals.  Duchesne had a career high 52 points with Washington in 1986–87, as he scored 17 goals and had 35 assists.  Joe Sakic was the Nordiques second selection in the 1987 NHL Entry Draft, as he scored 60 goals and 133 points in 72 games with the Swift Current Broncos of the Western Hockey League (WHL), as Quebec selected Bryan Fogarty with their first pick.  Fogarty had 70 points in 56 games with the Kingston Canadians of the Ontario Hockey League (OHL).

Question: In which city was NHL Entry Draft held when Stefan Noesen was a first round selection ?  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the ice hockey player."
    },
    "draft_year": {
      "type": "integer",
      "description": "The year the player was selected in the NHL Entry Draft."
    },
    "draft_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the NHL Entry Draft was held."
        },
        "state": {
          "type": "string",
          "description": "The state where the NHL Entry Draft was held."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "draft_year",
    "draft_location"
  ],
  "additionalProperties": false
}
