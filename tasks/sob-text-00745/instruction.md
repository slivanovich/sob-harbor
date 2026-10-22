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
Janko Tipsarević: Janko Tipsarević (, ] ; born 22 June 1984) is a Serbian professional tennis player.  His career-high singles ranking is world No. 8, achieved on 2 April 2012.  In his career, he has won four ATP World Tour titles, one ATP doubles title, three Futures, and 15 Challenger titles.  Tipsarević also won the 2001 Australian Open Junior title.  Tipsarević has achieved two victories over a World No. 1 player, having defeated compatriot Novak Djokovic twice.  He also has thirteen victories against other players in the top 10: four wins against Tomáš Berdych, and one each against Fernando González, Mikhail Youzhny, David Ferrer, James Blake, Gaël Monfils, Andy Murray and Juan Mónaco.  He holds victories over former World No. 1 players Carlos Moyá, Marat Safin, Lleyton Hewitt, Juan Carlos Ferrero and Andy Roddick.  His best results at a Grand Slam have been reaching the quarterfinals at the US Open in 2011 and 2012.  He is only the second Serb to reach the final 16 at all four different grand slams.

Mirjana Lučić-Baroni: Mirjana Lučić-Baroni (née Lučić; born 9 March 1982) is a Croatian professional tennis player.  She enjoyed a promising career on the WTA Tour in the late 1990s, during which she set several "youngest-ever" records.  She captured the women's doubles title at the 1998 Australian Open when she was 15-years-old, partnered with Martina Hingis.  She also won the first ever professional tournament she entered, the 1997 Croatian Bol Ladies Open, and defended it the following year at age 16, making her the youngest player in history to successfully defend a title.  She then reached the semifinals of the 1999 Wimbledon Championships, beating world No. 4 Monica Seles en route before she lost to Steffi Graf in 3 sets.  Following a series of personal problems from 2000 onwards, she faded from the scene.

Fred Perry: Frederick John "Fred" Perry (18 May 1909 – 2 February 1995) was a British tennis and table tennis player from England and former World No. 1 who won 10 Majors including eight Grand Slams and two Pro Slams single titles, as well as six Major doubles titles.  Perry won three consecutive Wimbledon Championships from 1934 to 1936 and was World Amateur number one tennis player during those three years.  Prior to Andy Murray in 2013, Perry was the last British player to win the men's Wimbledon championship, in 1936, and the last British player to win a men's singles Grand Slam title until Andy Murray won the 2012 US Open.

2012 US Open – Men's singles final: The 2012 US Open Men's Singles final was the championship tennis match of the Men's Singles tournament at the 2012 US Open.  In the final, Andy Murray defeated defending champion Novak Djokovic 7–6, 7–5, 2–6, 3–6, 6–2 to win the match.  It was the equal-longest US Open men's final in history, lasting 4 hours and 54 minutes (equalling the 1988 US Open final played by Ivan Lendl and Mats Wilander), and the equal second-longest men's final in the Open era, only behind the 2012 Australian Open final.  By winning the 2012 US Open, Murray became the first British man since Fred Perry in 1936 to win a Grand Slam singles title, and the first British man in the Open Era to do so.  The match is a significant part of the rivalry between the two players.  This match also marked a milestone for Murray, as it was his 100th match win at a grand slam tournament.

2010 Rogers Cup – Men's Singles: Andy Murray became the first player since Andre Agassi in 1995 to successfully defend the title.  He beat Roger Federer 7-5, 7-5 in the final.  It was also the first time in the tournament's history that the top four seeds reached the semifinals.

Andre Agassi: Andre Kirk Agassi ( ; born April 29, 1970) is an American retired professional tennis player and former World No. 1 who was one of the sport's most dominant players from the early 1990s to the mid-2000s.  Generally considered by critics and fellow players to be one of the greatest tennis players of all time, Agassi has been called the greatest service returner in the history of the game.  Described by the BBC upon his retirement as "perhaps the biggest worldwide star in the sport's history", Agassi compiled performances that, along with his unorthodox apparel and attitude, saw him cited as one of the most charismatic players in history.  As a result, he is credited for helping to revive the popularity of tennis during the 1990s.

2013 Andy Murray tennis season: The 2013 Andy Murray tennis season officially began at the Brisbane International where he was the defending champion.  He successfully defended that title, defeating Grigor Dimitrov in straight sets in the final.  After a quarterfinal showing at Indian Wells, where he lost to Juan Martín del Potro in 3 sets, Murray recovered to win the Miami Masters for the second time, defeating David Ferrer in the final.  Winning in Miami meant that Murray overtook Roger Federer as World No. 2, the first time Murray had held the ranking since September 2009, meaning that neither Federer nor Rafael Nadal were ranked in the top 2 for the first time since the end of 2003.  During the summer Murray won his first Wimbledon title, defeating Novak Djokovic in the final in straight sets to end Britain's 77-year wait for a home grown men's champion.  It was Murray's second major title, and third consecutive title on grass, after winning at the Olympics the previous year, meaning he extended his winning streak on grass to 18 matches.  In the summer hard court season, Murray failed to defend his US Open title, losing to Stanislas Wawrinka in the quarterfinals.  Following the Davis Cup World Group Play-offs, during which Murray won both his singles and the doubles rubber, he ended his season prematurely in order to undergo surgery on a long-standing back problem that had caused him trouble for over a year and a half.  He ended the season ranked number 4 in the world, behind Nadal, Djokovic and Ferrer.

Àlex Corretja: Àlex Corretja i Verdegay (] ; born 11 April 1974) is a former professional tennis player from Spain.  During his career, he finished runner-up twice at the French Open (in 1998 and 2001).  He won the ATP Tour World Championships in 1998 and reached his career-high singles ranking of World No. 2 in 1999.  He also played a key role in helping Spain win its first-ever Davis Cup title in 2000.  He became a temporary coach of British tennis player Andy Murray in April 2008 for the duration of the clay-court season and resumed the role in 2009.  On 29 March 2011, Corretja and Murray parted company by mutual agreement.

Jamie Murray: Jamie Robert Murray, {'1': ", '2': ", '3': ", '4': "} (born 13 February 1986) is a British professional tennis player from Scotland.  He is a five-time Grand Slam doubles winner and a Davis Cup champion, currently the world No. 11 doubles player, and a former doubles world No. 1.  Murray is the elder brother of Britain's world No. 3 singles tennis player Andy Murray.

2016 Andy Murray tennis season: Andy Murray's 2016 tennis season began at the Australian Open.  The 2016 season was a stand out year for Murray, ultimately resulting in finishing as the year-end No.1 player in the world as well as clinching the year-end money title.  Andy and his brother, Jamie Murray, also became the first brothers to finish as year-end No.1 ranked players in singles and doubles team, respectively.  He won an ATP-best 9 Tour titles (new career high) from 13 finals (he only played 17 tournaments this season), including his second Wimbledon crown and second successive Olympic gold medal in singles, thus becoming the first person, man or woman, to defend the Olympic singles title.  In the 2016 season, Andy became the first man to win singles titles at (1) a grand slam, (2) the Olympics, (3) a Masters 1000 event, and (4) the ATP World Tour Finals in the same calendar year (Serena Williams, in 2012, is the only other person to accomplish this feat).

Question: Andy Murray became the first player, since which American retired professional tennis player and former World No. 1 who was one of the sport's most dominant players from the early 1990s to the mid-2000s, in 1995 to successfully defend the title?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the tennis player."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "career_status": {
      "type": "string",
      "description": "The career status of the player (e.g., 'retired professional')."
    },
    "highest_ranking": {
      "type": "string",
      "description": "The highest singles ranking achieved by the player."
    },
    "year_of_achievement": {
      "type": "integer",
      "description": "The year the player successfully defended a title."
    },
    "achievement_description": {
      "type": "string",
      "description": "A description of the specific achievement."
    }
  },
  "required": [
    "player_name",
    "nationality",
    "career_status",
    "highest_ranking",
    "year_of_achievement",
    "achievement_description"
  ],
  "additionalProperties": false
}
