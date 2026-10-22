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
Joe Carbone: Joe Carbone is a teacher at The Equity Project 'TEP' charter school in Manhattan.  He is most known as NBA Head Strength and Conditioning Coach of The Los Angeles Lakers (2004–2008) and the Personal Strength Coach and Trainer to Kobe Bryant (1996–2004).  He is a Strength & Conditioning Specialist (CSCS) through the National Strength & Conditioning Association.  Prior to 1996, Carbone was the Head Strength & Conditioning Coach of the Philadelphia 76ers.

Martin Clawson: Martin Clawson is the Head Strength and Conditioning Coach at the club.  He is himself a former player with Bradford Northern and comes from a famous Rugby League family.  He has a background in sports fitness and was formerly a masseur at the club before assuming his present role.  He is a former body building competitor and his personality makes him the ideal person for his job at the Bulls.  Martin was employed as a business consultant for corporate communications giants Wish Communications with Garry Schofield OBE and John Stankevitch but has since taken up the role of Strength and Conditioning Coach at Wakefield Trinity Wildcats in the Super League.

Jerry Palmieri: Gerard Anthony Palmieri (born October 30, 1958) is an American football strength & conditioning coach.  Palmieri most recently served on Tom Coughlin’s staff for the New York Giants, a position he served in for 12 seasons.  During those years, the Giants won Super Bowl XLII and Super Bowl XLVI.  Palmieri was also on Tom Coughlin’s staff with the Jacksonville Jaguars from 1995 to 2002 when their teams competed in two AFC Championship Games.  Palmieri spent 2003 as an assistant strength & conditioning coach for the New Orleans Saints.  Prior to his NFL career he held head strength coach positions at Boston College from 1993 to 1994, where he served under Tom Coughlin and Dan Henning respectively, and at Kansas State from 1987 to 1992 where he was a part of the Bill Snyder transformation of Kansas State Football.  Palmieri began his strength & conditioning career as a part-time strength coach while he earned his master's degree at the University of North Carolina at Chapel Hill from 1982 to 1983, and then an assistant strength & conditioning coach at Oklahoma State University from 1984 to 1986.

Nuʻu Tafisi: Nu'u Tafisi ( ; born June 30, 1981 in Samoa) is a former American football defensive end for the Seattle Seahawks of the National Football League and current head strength and conditioning coach at Brigham Young University.  He was originally signed by the Seahawks as an undrafted free agent in 2007.  He played college football at California & Mt. San Antonio College (Mt. SAC).

Bob King (speed coach): Bob King (born August 20, 1954) is an American Strength and Conditioning coach with a focus on speed training.  He played college football at Texas Tech University.  He was the Strength and Conditioning coach for the Dallas Mavericks, Dallas Burn (now FC Dallas), Assistant Strength and conditioning coach for the Dallas Cowboys and Push Coach for the US Skeleton team.

Istvan Javorek: István Javorek (born January 6, 1943) is a sports conditioning coach.  Coach Javorek is the retired head strength and conditioning coach at Johnson County Community College.  He supervised the strength and conditioning program for

Johnson County Community College: Johnson County Community College (JCCC) is a 245 acre community college located in Overland Park, Kansas at College Boulevard and Quivira Road.  With more than 19,400 credit and continuing education students, JCCC is the largest undergraduate institution of higher education in the state of Kansas.

Johnnie Morant: Johnnie Morant, Jr. (born December 7, 1981) is a former gridiron football wide receiver.  He was drafted by the Oakland Raiders in the fifth round of the 2004 NFL Draft.  He played college football at Syracuse.  He is currently the Head Strength and Conditioning Coach and Wide Receivers coach at East Carter High School.  While at Kentucky Christian University, Coach Morant help mentor an All-American Wide Receiver who was invited to an All Star game and an All Mid-South Academic Wide Receiver.

Thibault Giroud: Thibault Giroud (born 9 March 1974 in Grenoble, France) is a French rugby union strength and condiitioning coach with Toulon.  He was previously a strength and conditioning coach for Glasgow Warriors.  He previously played for NFL Europe (American football) as a Running Back; trained as a Sprinter; as an Olympic Bob Sleigher; then a rugby union player and now strength & conditioning coach with various rugby teams.

Chris Doyle (American football): Chris Doyle (born June 30, 1968) is an American football coach and former player.  He is currently the Head strength and conditioning coach at The University of Iowa he has held since 1999.  Doyle recently added the title of Executive Director of the Football program in 2015.  Doyle played college football on the offensive line at Boston University from 1986 to 1988.

Question: István Javorek is a retired head strength and conditioning coach at college located in what city and state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string"
    },
    "college_name": {
      "type": "string"
    },
    "college_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "coach_role": {
      "type": "string"
    }
  },
  "required": [
    "coach_name",
    "college_name",
    "college_location",
    "coach_role"
  ],
  "additionalProperties": false
}
