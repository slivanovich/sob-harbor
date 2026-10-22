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
Pakistani cricket team in Australia in 1972–73: The Pakistan national cricket team toured Australia in the 1972–73 season and played three Test matches against the Australian national cricket team.  After an inadequate preparation against weak teams, Pakistan lost by an innings in the first Test in Adelaide.  While Australia won the series 3–0, the last two tests were competitive, with Pakistan seeming the likely winner on the second last days.  The 2nd test in Melbourne was attended by 115,721.  Pakistan also visited Sri Lanka and played a match against the Sri Lankan national cricket team and followed the tour with a series against New Zealand, where both teams played their first ODI.

List of Pakistan Test cricket records: Test cricket is the oldest form of cricket played at international level.  A Test match is scheduled to take place over a period of five days, and is played by teams representing Full Member nations of the International Cricket Council (ICC).  Pakistan obtained Full Member status of the ICC in 1952, becoming the seventh nation eligible to play Test cricket.  The Pakistan national cricket team played their first Test match on 16 October 1952 against India which they lost by an innings and 70 runs.  They recorded their first victory in their second ever match against India on 23 October 1952.  Since then, they have played 410 matches, against every other Test-playing nation.  s of 2017 , Pakistan is fourth most successful team in Test cricket with an overall winning percentage of 32.19, ahead of Australia (47.00), South Africa (36.86) and England (35.89).

William West (umpire): William Arthur John West was a first class cricketer and Test match umpire.  Born in Birmingham in 1863 he played five first class matches for Marylebone Cricket Club, scoring 182 runs at 26 with a highest score of 74 against Lancashire.  A right arm quick bowler, he also took five wickets at just 20 apiece.  He stood in the match between North and South in 1890 and continued to umpire for the next 45 years, until his final season in 1935.  He officiated in nine Test matches, from his first England v Australia test in 1896 to the 1912 Triangular Tournament featuring England, Australia and South Africa.  He died in Northampton in 1938.

Pakistan national cricket team record by opponent: The Pakistan national cricket team represents Pakistan in international cricket and is a full member of the International Cricket Council (ICC) with Test and One Day International (ODI) status.  Pakistan first competed in international cricket in 1952, when they played against India in a four-day Test match; India won the match by an innings and 70 runs at the Feroz Shah Kotla Ground, Delhi.  In the same series, Pakistan recorded their first Test win, the second match by an innings and 43 runs at the University Ground, Lucknow.  s of 2017 , Pakistan have played 410 Test matches; they have won 132 matches, lost 120 matches, and 158 matches were drawn.  They have also won the 1998–99 Asian Test Championship, defeating Sri Lanka in the final by an innings and 175 runs.  Pakistan played their first ODI match against New Zealand in February 1973 at the Lancaster Park, Christchurch, but registered their first win against England at Trent Bridge, Nottingham, in August 1974.  s of 2017 , Pakistan have played 879 ODI matches, winning 464 matches and losing 389; they also tied 8 matches, whilst 18 had no result.  They also won the 1992 Cricket World Cup, the 2000 and 2012 Asia Cups, and the 2017 ICC Champions Trophy.  Pakistan played their first Twenty20 International (T20I) match at the County Cricket Ground, Bristol, on 28 August 2006, against England, winning the match by five wickets.  In 2009, they won the 2009 ICC World Twenty20, defeating Sri Lanka by eight wickets.  s of 2017 , Pakistan have played 115 T20I matches and won 68 of them; 44 were lost and three were tied.

Pakistani cricket team in Australia in 1978–79: The Pakistan national cricket team, captained by Majid Khan, toured Australia in March 1979 and played two Test matches against the Australia national cricket team.  The series was drawn 1–1.  Pakistan visited Sri Lanka "en route" for home and played a match against the Sri Lankan national cricket team.

Thomas Bartley (cricket umpire): Thomas Bartley (1908–1964) was a Test match umpire.  Bartley represented Cheshire in the Minor Counties and played in the Lancashire League but made his most notable contribution to cricket as an umpire.  He stood in first class cricket from 1948 to 1960 and officiated in 6 home tests against Pakistan, South Africa and Australia from 1954 to 1956.

Steve Andrew: Steve Andrew ( born 27 January 1966 ) is an English first class and List A cricketer who played First class cricket for Hampshire County Cricket Club and Essex County Cricket Club.  He also played for these teams in List A games and he also played List A games for Hertfordshire.  His highest score in First class cricket of 35 came when playing for Essex in the match against Northamptonshire County Cricket Club.  His best bowling in First class cricket of 7/47 came when playing for Essex in the match against Lancashire County Cricket Club.

Frank Farrands: Frank Henry Farrands was a first class cricketer and test match umpire.  A right-handed roundarm fast bowler, he took 128 wickets for Marylebone Cricket Club (1868–1880), Nottinghamshire (1871) and others in just 30 matches at an average of 15.  He umpired in first class cricket from 1868 to 1900, standing in 7 Ashes tests on the Australian tours of 1884, 1886 and 1888.  He would die in 1916 in Sutton-in-Ashfield, Nottinghamshire, the town of his 1835 birth.

Pakistan A cricket team: The Pakistan A cricket team is a national cricket team representing Pakistan.  It is the 'second-tier' of international Pakistan cricket, below the full Pakistan national cricket team.  Matches played by Pakistan A are not considered to be Test matches or One Day Internationals, instead receiving first-class and List A classification respectively.  Pakistan A played their first match in August 1964, a three-day first-class contest against Ceylon Board President's XI.

Pakistan national cricket team: The Pakistan national cricket team (Urdu: ‎ ), popularly referred to as the Shaheens ("lit: Falcons") Men in Green and the Cornered Tigers, represents Pakistan in international cricket and is administered by the Pakistan Cricket Board (PCB).  The team is a full member of the International Cricket Council, and participates in Test, ODI and Twenty20 International cricket matches.

Question: Thomas Bartley (1908–1964) was a Test match umpire, He stood in first class cricket from 1948 to 1960 and officiated in 6 home tests against Pakistan, The Pakistan national cricket team, are popularly referred to as what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_name": {
      "type": "string",
      "description": "The official name of the cricket team."
    },
    "popular_names": {
      "type": "array",
      "description": "A list of popular names or nicknames for the team.",
      "items": {
        "type": "string"
      }
    },
    "number_of_popular_names": {
      "type": "integer",
      "description": "The total count of popular names identified for the team."
    }
  },
  "required": [
    "team_name",
    "popular_names",
    "number_of_popular_names"
  ],
  "additionalProperties": false
}
