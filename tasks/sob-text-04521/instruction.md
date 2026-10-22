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
2012–13 New York Rangers season: The 2012–13 New York Rangers season was the National Hockey League franchise's 86th season of play and their 87th season overall.  The regular season was reduced from its usual 82 games to 48 due to a lockout.  The lockout ended on January 5 when the NHL and NHL Players' Association (NHLPA) reached an agreement.  The Rangers were defeated by the Boston Bruins in the Eastern Conference Semi-finals.  After the Rangers season was ended, they relieved Head Coach John Tortorella of his duties.

Dick Todd (ice hockey): Richard "Dick" Todd is a retired former ice hockey coach.  He has the second most wins by a coach in Ontario Hockey League history.  Todd got his start as a coach with the Peterborough Petes in the 1970s as a trainer and worked his way up, becoming the team's head coach in 1982.  Unlike the vast majority of hockey coaches, Todd never played the game at a high level.  He led the team for the next eleven years, winning the J. Ross Robertson Cup in 1989 and 1993.  Todd was awarded the Matt Leyden Trophy as OHL Coach of the Year in 1987–88.  He also led Canada to a gold medal at the 1991 World Junior Ice Hockey Championships.  In 1993 Todd took a job as an assistant coach with the New York Rangers, winning a Stanley Cup with them in 1994.  He retired in 1998, but came back as coach of the Petes in 2004.  In his final two years with the team Todd recorded his 500th career victory.  He did this faster than any other coach in Major Junior A hockey history, accomplishing the milestone in just 813 games.  He also led the Petes to another OHL title before retiring again at the close of the 2005–06 OHL season.

Tom Anastos: Thomas A. "Tom" Anastos (born July 5, 1963 in Dearborn, Michigan) is an American ice hockey coach, former player, and former league administrator.  He was most recently the head coach of the Michigan State Spartans men's ice hockey team (MSU), a member of the Big Ten Conference (Big Ten) in Division I of the National Collegiate Athletic Association (NCAA).  He played junior hockey for the Paddock Pool Saints, college hockey for the Michigan State University Spartans and professional hockey for the Sherbrooke Canadiens.  He was an ice hockey league administrator most recently serving as commissioner of the Central Collegiate Hockey Association (CCHA), a now defunct NCAA Division I conference, from 1998-2012.  Anastos is a member of the Dearborn (Michigan) Sports Hall of Fame, inducted in 2000.

Ted Sator: Ted Sator (born November 18, 1949) is an American professional ice hockey coach.  He has twelve seasons of NHL coaching experience, serving as an assistant coach for various teams and head coach of the New York Rangers and Buffalo Sabres.  He has also spent time coaching in the AHL and ECHL along with coaching in Europe including stints as the Slovenian and Hungarian national ice hockey teams.  He is a current assistant men's ice hockey coach at Lindenwood University.

Peter Laviolette: Peter Philip Laviolette Jr. (born December 7, 1964) is an American professional ice hockey coach and former player.  He is the current head coach for the Nashville Predators of the National Hockey League (NHL).  He has previously held this position with the New York Islanders, Carolina Hurricanes, and Philadelphia Flyers.  He coached the Hurricanes to a Stanley Cup win in 2006, and later coached the Philadelphia Flyers to the Stanley Cup Finals in 2010, and the Nashville Predators in 2017.  Laviolette is the fourth coach in NHL history to lead three different teams to the Stanley Cup Finals.  Despite this, he only played twelve NHL games himself, all with the New York Rangers.

Shawn McEachern: Shawn K. McEachern (born February 28, 1969) is an American ice hockey coach and former professional ice hockey player.  He is the current head boys' varsity ice hockey coach at The Rivers School, an independent 6–12 school in Weston, Massachusetts.

John Tortorella: John Robert Tortorella (born June 24, 1958) is an American ice hockey coach and former player.  He is the head coach for the Columbus Blue Jackets of the National Hockey League (NHL).  Tortorella has held the position of head coach of the Vancouver Canucks (2013–2014), the New York Rangers (2009–2013) and the Tampa Bay Lightning (2001–2008).  He led Tampa Bay to the 2004 Stanley Cup championship.

John Vanbiesbrouck: John Vanbiesbrouck (born September 4, 1963), nicknamed "the Beezer" and "VBK", is an American professional ice hockey executive and former player.  A goaltender as a player, he was inducted into the United States Hockey Hall of Fame in 2007.  Vanbiesbrouck played in the National Hockey League (NHL) for the New York Rangers, Florida Panthers, Philadelphia Flyers, New York Islanders, and New Jersey Devils.  He began his career playing major junior hockey for the Sault Ste. Marie Greyhounds of the Ontario Hockey League (OHL).  Following a successful season with the Greyhounds, he was drafted by the New York Rangers in the fourth round, 72nd overall, in the 1981 NHL Draft.  After his junior career ended, he played for the Rangers minor league affiliate, the Tulsa Oilers of the Central Hockey League.  Despite the team's near collapses due to financial concerns, Vanbiesbrouck led the Oilers to a league championship and shared the league's MVP honors.

Gilles Leger: Gilles Leger (born July 16, 1941 in Cornwall, Ontario) is a Pro Scout with the New York Rangers and a former professional ice hockey coach.  Although a talented Canadian football player, Leger chose to dedicate his life to hockey.  From 1967-72, he coached the St. Francis Xavier University squad before he was hired as an assistant coach with the Ottawa Nationals.  He had brief head coaching stints Toronto Toros and Birmingham Bulls, then moving on to serve as general manager of the latter club.  Leger has since held a series of front office jobs.  From 1979 until 1983, he was the director of player development for the Quebec Nordiques.  He then became president of the Fredericton Express and Halifax Citadels American Hockey League teams and the QMJHL Quebec Ramparts.  He later severed as a scout for several NHL clubs, including the Edmonton Oilers and most recently the New York Rangers.

Doug Weight: Douglas Daniel Weight (born January 21, 1971) is an American professional ice hockey coach, executive and former player.  He is currently the head coach and assistant general manager for the New York Islanders.  During his 19-year National Hockey League career, he played for the New York Rangers, Edmonton Oilers, Carolina Hurricanes, Anaheim Ducks, St. Louis Blues and the New York Islanders.

Question: When was the American ice hockey coach and former player which was released after 2012–13 New York Rangers season born ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The full name of the ice hockey coach."
    },
    "coach_nationality": {
      "type": "string",
      "description": "The nationality of the coach."
    },
    "coach_profession_types": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions held by the individual."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the coach in 'Month Day, Year' format."
    },
    "release_context": {
      "type": "object",
      "properties": {
        "team": {
          "type": "string",
          "description": "The team from which the coach was released."
        },
        "role": {
          "type": "string",
          "description": "The role the coach held at the time of release."
        },
        "season": {
          "type": "string",
          "description": "The season after which the coach was released."
        }
      },
      "required": [
        "team",
        "role",
        "season"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_name",
    "coach_nationality",
    "coach_profession_types",
    "birth_date",
    "release_context"
  ],
  "additionalProperties": false
}
