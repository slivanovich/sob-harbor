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
Larry Johnson (American football coach): Larry Johnson (born c. 1952) is an American football coach, currently the defensive line and assistant head coach at Ohio State University.  He served as an assistant football coach at Pennsylvania State University from 1996 to 2013.  Johnson was a high school football coach in the Washington, D.C. area from 1983 to 1993.  He is the father of former National Football League running back Larry Johnson and former Penn State wide receiver Tony Johnson.

Larry Johnson (running back): Larry Alphonso Johnson Jr. (born November 19, 1979) is a former American football running back in the National Football League (NFL).  He played college football for Penn State University, and was recognized as a unanimous All-American.  He was drafted by the Kansas City Chiefs in the first round of the 2003 NFL Draft, and also played for the Cincinnati Bengals, Washington Redskins and Miami Dolphins of the NFL.

Rickey Young: Rickey Young (born December 7, 1953 in Mobile, Alabama) is a former American football running back who played nine seasons in the NFL.  Young played college football at Jackson State and was a teammate of Walter Payton.  Rickey was drafted in 1975 (7th round, 164th overall pick) by the San Diego Chargers.  After playing three years for the Chargers (1975–1977) he was traded to the Minnesota Vikings for All-Pro guard Ed White.  In his first season with the Vikings (1978) he led the NFL with 88 receptions, breaking Chuck Foreman's record for receptions by a running back in a season.  He played in six seasons with the Vikings, but retired after seeing limited action in 1982 and 1983.  He retired with 1,011 rushes for 3,666 yards and 23 touchdowns, along with 408 catches (then an NFL record for running backs) for 3,285 and 16 touchdowns.

Peyton Hillis: Peyton Derek Hillis (born January 21, 1986) is a former American football running back who played in the National Football League (NFL).  Hillis attended Conway High School in Conway, Arkansas and was a highly touted recruit.  Hillis attended the University of Arkansas in Fayetteville, Arkansas where he was primarily used as a fullback.  After being drafted in the 7th round of the 2008 NFL Draft, Hillis rose to the top of the depth chart as the starting fullback for the Denver Broncos.  Due to injuries to the running back corps, he became the starting running back.  After spending two years in Denver, Hillis was traded to the Cleveland Browns in 2010.  In 2011, Hillis won a nationwide vote which put him on the cover of EA Sports' "Madden NFL 12" video game.

Avon Cobourne: Avon Cobourne (born March 6, 1979) is a former American professional Canadian football running back who was most recently a running back coach for the Winnipeg Blue Bombers of the Canadian Football League (CFL).  He was a running back for West Virginia University from 1999 to 2002 before entering the NFL.

Ron Sayers: Ronald Sayers (born August 29, 1947) is a former American football running back who played in the American Football League (AFL) for the San Diego Chargers in 1969.  He played college football for the University of Nebraska Omaha.  He is the younger brother of Pro Football Hall of Fame running back Gale Sayers.

Walter Mendenhall: Walter Mendenhall (born January 22, 1986) is a former American football running back.  He played college football at Illinois from 2005 to 2007 before transferring to Illinois State University where he played in 2008.  He was signed by the Philadelphia Eagles as an undrafted free agent in 2009 and has also been a member of the Indianapolis Colts, Buffalo Bills and Cincinnati Bengals.  He is the brother of former Arizona Cardinals running back Rashard Mendenhall.

Tony Johnson (wide receiver): Tony Johnson (born March 12, 1982) is a former American football wide receiver.  He played collegiately at Penn State from 2000 to 2003.  Entering the 2008 season, he was ranked 10th all time in receptions for the Nittany Lions with 107, and 9th in receiving yards with 1,702.  Johnson was listed at 5'11, 209 lbs.  and wore number 11.  His older brother is former NFL running back Larry Johnson.  Tony was also Larry's manager.

Barry Redden: Barry Redden (born July 21, 1960) is a former American football running back who played for the Los Angeles Rams, the San Diego Chargers, and the Cleveland Browns of the National Football League (NFL).  He spent much of his career playing in the shadow of Pro Football Hall of Fame running back Eric Dickerson.

John David Washington: John David Washington (born July 28, 1984) is an American actor and former American football running back.  He played college football at Morehouse and signed with the St. Louis Rams as an undrafted free agent in 2006.  Professionally, Washington spent four years as the running back for the United Football League's California franchise, staying with the team through its entire history.

Question: When was the former American football running back which Larry Johnson was his father born 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the former American football running back."
    },
    "person_profession": {
      "type": "string",
      "description": "The profession of the person."
    },
    "father_name": {
      "type": "string",
      "description": "The name of the person's father."
    },
    "birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the former American football running back."
    }
  },
  "required": [
    "person_name",
    "person_profession",
    "father_name",
    "birth_date"
  ],
  "additionalProperties": false
}
