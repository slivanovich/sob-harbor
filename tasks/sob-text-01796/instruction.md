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
Jonathan Cross: Jonathan Neil Cross (born 2 March 1975) is a footballer who played as a full back in the Football League for Wrexham, Hereford United and Chester City.

Ian Dalziel (footballer): Ian Dalziel (born 24 October 1962 in South Shields) is an English former footballer who played as a full back in the Football League for Derby County, Hereford United and Carlisle United.  He later played for Gateshead.

Chester City F.C.: Chester City Football Club was an English football team from Chester which played in a variety of leagues between 1885 and 2010.  The club, which was founded as Chester F.C., joined the Football League in 1931.  Over the next eight decades, the club spent most of its time competing in the lower divisions playing its home games at Sealand Road (1906–1990).  In 1983 it was renamed Chester City.  The club moved to the Deva Stadium in 1992 after playing two seasons of home games at Macclesfield Town's Moss Rose.  In 2004 Chester won the Conference National, their only league title.

Craig Jones (footballer, born 1989): Craig Nicholas Jones (born 19 December 1989) is an English football midfield player, currently playing for Westfields.  He started his career at Lads Club, a football club in Hereford.  He was then scouted by Cardiff City, where he remained for several years before joining the Hereford United youth set up.  Due to injuries to several other players Jones featured on the bench in two League matches at the beginning of December.  He made his debut for Hereford in the 2–0 home defeat against Colchester United when he came on as a substitute for Stephen O'Leary in a game that relegated the club back into Football League Two.

John Trewick: John Trewick (born 3 June 1957) is an English football coach and former midfielder.  He was first team coach at Hereford United from 2004 to 2009.  After the relegation of Hereford United to League Two, Trewick assumed the role of manager from Graham Turner, but he was dismissed from the Hereford manager's post on 8 March 2010.

Kings Langley F.C.: Kings Langley Football Club are a semi-professional association football club in the village and civil parish of Kings Langley, Hertfordshire, England.  The club have spent the majority of their history in the Hertfordshire County League, they joined the Spartan South Midlands Football League in 2001, winning the Premier Division in the 2015-16 season and are currently members of the Southern League Premier Division - the seventh tier of the English football league system, following a third consecutive promotion in 2016 when they became champions of the Southern League Division One South.  In doing so, Kings Langley join Truro F.C., Chester F.C., F.C. United of Manchester and Gretna F.C. as the only clubs in the United Kingdom with three or more successive promotions.  They are also unofficially the highest-ranked village football club in England.

James Pugh (footballer): James Pugh (born July 1891, date of death unknown) was an English footballer.  His regular position was at full back.  He was born in Hereford, Herefordshire.  He played for Manchester United, Clapton Orient, Coventry City, Luton Town, Brighton & Hove Albion, Hereford United, Bridgend Town, Abertillery and Wrexham.

Roger Preece: Preece began his playing career as an apprentice with Coventry City, but in August 1986 he moved to Wrexham.  He made more than 100 Football League appearances over the next four years but had from a poor disciplinary record, as he was sent off five times.  In summer 1990, he was released by Wrexham and moved to local rivals Chester City, which was a division higher in the Football League Third Division.  He began at Chester as a full back but went on to make his greatest mark as a Midfielder.

John Galley: John Edward Galley (born 7 May 1944 in Clowne, Derbyshire) is an English former footballer who scored 149 goals from 409 games in the Football League playing as a striker for Wolverhampton Wanderers, Rotherham United, Bristol City, Nottingham Forest, Peterborough United and Hereford United during the 1960s and 1970s.  He was part of the Hereford United side that won the Third Division title in 1976.  After 14 seasons in the Football League, he dropped down into non-league football to play for Telford United.

Steve Davey: Stephen Gilbert Richard "Steve" Davey (born 5 September 1948 in Plymouth) is an English former footballer who played in the Football League for Plymouth Argyle, Hereford United, Portsmouth and Exeter City.  For Plymouth he played either as a striker or at full back.  He played a key role in Portsmouth's promotion from the Fourth Division in 1979–80, playing mainly at centre-back.

Question: Jonathan Neil Cross, is a footballer who played as a full back in the Football League for Wrexham, Hereford United and which English football team from Chester which played in a variety of leagues between 1885 and 2010, and was founded as Chester F.C., joined the Football League in 1931?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "club_name": {
      "type": "string",
      "description": "The full name of the football club."
    },
    "club_location": {
      "type": "string",
      "description": "The city where the football club is located."
    },
    "founded_as_name": {
      "type": "string",
      "description": "The original name of the football club when it was founded."
    },
    "football_league_entry_year": {
      "type": "integer",
      "description": "The year the club joined the Football League."
    },
    "club_active_period": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The start year of the club's active period mentioned in the context."
        },
        "end_year": {
          "type": "integer",
          "description": "The end year of the club's active period mentioned in the context."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    },
    "player_who_played_for_club": {
      "type": "string",
      "description": "The name of the footballer mentioned in the question who played for this club."
    },
    "player_position": {
      "type": "string",
      "description": "The primary playing position of the footballer."
    }
  },
  "required": [
    "club_name",
    "club_location",
    "founded_as_name",
    "football_league_entry_year",
    "club_active_period",
    "player_who_played_for_club",
    "player_position"
  ],
  "additionalProperties": false
}
