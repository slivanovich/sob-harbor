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
Simon Goodwin: Simon Goodwin (born 26 December 1976 in Adelaide, South Australia) is the senior coach of the Melbourne Football Club.  He is a retired professional Australian rules footballer, a former dual premiership player for the Adelaide Crows, a multi-times All-Australian player and a former captain of the Adelaide Crows.  Goodwin played a total of 275 senior games in his AFL career, all for the Adelaide Crows.

Matthew Powell (Australian footballer): Matthew Powell (born 27 September 1973) is a former Australian rules footballer who played with Adelaide in the Australian Football League (AFL).

Chris Powell: Christopher George Robin "Chris" Powell (born 8 September 1969) is an English professional football player and coach.  A left back, Powell played for clubs including Southend United, Derby County, Charlton Athletic – where he had three spells as a player over eight seasons – West Ham United and Leicester City.  He also made five appearances for the England national team.

Sunshine Football Club (VFA): Sunshine Football Club, nicknamed The Crows, was an Australian rules football club which played in the Victorian Football Association (VFA) from 1959 until 1989.  The club colours were navy blue and white.

Matt Powell: Matthew Powell (born 8 May 1978 in Abergavenny, Wales) is a Welsh rugby union footballer, who played for Worcester Warriors at scrum-half.

Jack Powell (rugby union): John "Jack" Anderson Powell (14 September 1882 – 20 March 1941) was a Welsh international rugby union forward who played club rugby for Cardiff and London Welsh.  Powell played a single international game for Wales, in 1906, and faced the Original All Blacks as part of the Glamorgan county team in 1905 and the South African team as a member of the Cardiff team in 1907.

Jeff Powell (American football): Jeffrey O'Neal "Jeff" Powell (born May 27, 1963) is a retired American football player who was a running back in the National Football League (NFL).  Powell also won recognition as an elite hurdler in track and field.  Powell played college football for the University of Tennessee and is famous for his 60-yard touchdown in the third quarter during the 1986 Sugar Bowl.  He was drafted by the Chicago Bears in the sixth round of the 1986 NFL Draft, and after his football career, Powell earned a law degree from Vanderbilt University Law School.  He currently practices law in Tennessee.

Adelaide Football Club: The Adelaide Football Club, nicknamed the Crows, is a professional Australian rules football club that competes in the Australian Football League (AFL).  The club is based in Adelaide, South Australia, playing its home matches at Adelaide Oval.  The club has its training and administration base at Football Park in West Lakes, where it previously played home matches between 1991 and 2013.  The club song is "The Pride of South Australia", to the tune of the Marines' Hymn.

Hope Powell: Hope Patricia Powell CBE (born 8 December 1966) is an English former international footballer and women's first-team manager of Brighton & Hove Albion.  She was the coach of the England women's national football team and the Great Britain women's Olympic football team until August 2013.  As a player, Powell won 66 caps for England, mainly as an attacking midfielder, scoring 35 goals.  She made her England debut at the age of 16, and went on to play in the 1995 FIFA Women's World Cup, England's first World Cup appearance.  She was also vice-captain of her country.  At club level Powell played in four FA Women's Cup finals and captained Croydon to a League and Cup double in 1996.

John Meesen: John Meesen (born 20 June 1986) is a former Australian rules football player who played for the Melbourne Football Club and Adelaide Football Club in the Australian Football League (AFL).  Drafted with the 8th selection in the 2004 Draft, Meesen had a long wait to play his first senior game for the Adelaide Crows.  Playing for Norwood in the South Australian National Football League, Meesen was a leading ruckman in the senior side, but was incapable of surpassing Rhett Biglands, Ben Hudson and Matthew Clarke for a spot in the Crows team.  Following Biglands' 2007 season-ending injury in the 2006 preliminary final and Clarke's move to St Kilda, it was thought that Meesen would begin season 2007 as back-up ruckman to Hudson.  However an injury-plagued pre-season saw Jonathon Griffin and Ivan Maric move ahead of him in the pecking order.

Question: Which football club that Matthew Powell played with is nicknamed the Crows?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the player."
    },
    "club_played_for": {
      "type": "string",
      "description": "The name of the football club the player played for."
    },
    "club_nickname": {
      "type": "string",
      "description": "The nickname of the football club."
    },
    "sport_type": {
      "type": "string",
      "description": "The type of football played by the club (e.g., Australian rules football, rugby union)."
    },
    "is_nickname_crows": {
      "type": "boolean",
      "description": "True if the club's nickname is 'Crows', false otherwise."
    }
  },
  "required": [
    "player_name",
    "club_played_for",
    "club_nickname",
    "sport_type",
    "is_nickname_crows"
  ],
  "additionalProperties": false
}
