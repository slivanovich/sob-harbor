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
SFWA Young Player of the Year: The Scottish Football Writers' Association Young Player of the Year (often called the SFWA Young Player of the Year, or simply the Scottish Young Player of the Year) award is given to the footballer in the Scottish football league system, who is seen to have been the best young (under 23) player of the previous season.  The shortlist is compiled by the members of the Scottish Football Writers' Association (the SFWA), who also vote for the winner.  The prize is seen as the highest awarded to a young player as it names the "Young Player of the Year"; the footballer who is seen to have been "the" best young player over the previous season.  The award was first made in 2002, and was won by Motherwell forward James McFadden.

Dave Mackay: David Craig Mackay (14 November 1934 – 2 March 2015) was a Scottish football player and manager.  Mackay was best known for a highly successful playing career with Heart of Midlothian, the Double-winning Tottenham Hotspur side of 1961, and winning the league with Derby County as a manager.  He also represented Scotland 22 times, and was selected for their 1958 FIFA World Cup squad.  Mackay tied with Tony Book of Manchester City for the Football Writers' Association's Footballer of the Year award in 1969 and was later listed by the Football League in their "100 Legends", as well as being an inaugural inductee to both the English and Scottish Football Halls of Fame.  He was described, by Tottenham Hotspur, as one of their greatest players and was known as 'the hearbeat' of their most successful ever team.

Rex Kingsley Footballer of the Year: The Rex Kingsley Footballer of the Year was an award given annually to the Scottish footballer who was adjudged to have been the best of that year (calendar year and not season) in Scottish football between 1951–1964.  The award was handed out by Rex Kingsley of the "Sunday Mail".  As there were no Football Writers' awards (until the SWFA awards in 1965) or Players' Association awards (until the PFA Scotland awards in 1978), the Rex Kingsley Footballer of the Year award was generally considered to be the most prestigious of its type at the time.

Sandy Jardine: William "Sandy" Pullar Jardine (31 December 1948 – 24 April 2014) was a Scottish professional footballer, who played for Rangers, Hearts and represented Scotland.  He twice won the Scottish Football Writers Association Player of the Year award and was part of the Rangers team that won the European Cup Winners' Cup in 1972.  Jardine was also co-manager of Hearts with Alex MacDonald and later worked for Rangers.  He died in April 2014, 18 months after being diagnosed with liver cancer.

SFWA Manager of the Year: The Scottish Football Writers' Association Manager of the Year (often called the SFWA Manager of the Year, or simply the Scottish Manager of the Year) award is given to the manager in Scottish football who is seen to have been the best manager of the previous season.  The award is voted for by the members of the Scottish Football Writers' Association.

FWA Footballer of the Year: The Football Writers' Association Footballer of the Year (often called the FWA Footballer of the Year, or in England simply the Footballer of the Year) is an annual award given to the player who is adjudged to have been the best of the season in English football.  The award has been presented since the 1947–48 season, when the inaugural winner was Blackpool winger Stanley Matthews.  The latest winner of the award as of 2016–17 is N'Golo Kante of Chelsea.  Eight players have won the award on more than one occasion, the most recent being Cristiano Ronaldo, who won his second award in the 2007–08 season.  Thierry Henry has won the award on the most occasions, having won three times in four seasons.

Leigh Griffiths: Leigh Griffiths (born 20 August 1990) is a Scottish professional footballer who plays as a striker for Scottish Premiership club Celtic and the Scotland national team.

Scottish Football Writers' Association: The Scottish Football Writers' Association (SFWA) is an association of Scottish football journalists and correspondents writing for newspapers and agencies, founded in 1965.  The most prestigious awards in Scottish football is The Official Scottish Football Awards 2010.

SFWA Footballer of the Year: The Scottish Football Writers' Association Footballer of the Year (often called the SFWA Footballer of the Year, or simply the Scottish Footballer of the Year) is an annual award given to the player who is adjudged to have been the best of the season in Scottish football.  The award has been presented since the 1964–65 season, and the winner is selected by a vote amongst the members of the Scottish Football Writers' Association (SFWA), which comprises over 100 football journalists based throughout Scotland.  The first winner was Celtic's Billy McNeill, and the first non-Scottish winner was Mark Hateley of Rangers in 1994.  Six players have won the award on more than one occasion, the most recent being Leigh Griffiths, who won his second award in the 2015–16 season.

Celtic F.C. league record by opponent: Celtic Football Club is a professional association football club based Glasgow, Scotland.  The club was founded in 1887 and began playing league football in 1890 as founder members of the Scottish Football League.  Since their first season Celtic have remained in the top division of the Scottish football league system: the Scottish Football League (1890–93), Scottish Football League Division One (1893–1975), Scottish Football League Premier Division (1975–98), Scottish Premier League (1998–2013) and Scottish Premiership (2013–present).  As of 2015–16 the club has completed 127 seasons of competitive football and have been Scottish football champions 47 times.

Question: Who is both a winner of the Scottish Football Writers' Association Footballer of the Year award, and plays as a striker?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the footballer."
    },
    "award_name": {
      "type": "string",
      "description": "The name of the award won by the player."
    },
    "playing_position": {
      "type": "string",
      "description": "The primary playing position of the footballer."
    },
    "club": {
      "type": "string",
      "description": "The club the player plays for."
    },
    "award_years": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The season(s) in which the player won the award."
    }
  },
  "required": [
    "player_name",
    "award_name",
    "playing_position",
    "club",
    "award_years"
  ],
  "additionalProperties": false
}
