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
Howie Stange: Howard 'Howie' Erwin Stange (March 3, 1924 – December 4, 1990) was an American musician, singer and pianist who played Rockabilly and Country music, possessing a distinctive vocal and playing style.  Howie was a musical virtuoso who had the ability to pick up any instrument and play with a high degree of technical proficiency, despite the fact that he never learned how to read music.  Howie was born of four sisters and two brothers who include: Gertrude 'Kiki' Stange, Doris Stange, Frank Anthony Stange, Raymond Christopher Stange, Esther Madelyn Stange and Kathleen Leona Stange.  Among the six siblings, only his youngest sister, Kathleen, lives to date, age 85.  Howie achieved both national and international fame recognition, for his hit 45 record, "Real Gone Daddy/This Old Bomb of Mine," released in 1957.  Regarded as one of the most significant and influential Rockabilly musicians of his era, Howie's music currently resides on over 100 record compilations of the best rockabilly music ever produced.  Howie's song "Real Gone Daddy" has achieved "Maybelline" status among fans.  Additionally, in 1958 he went on to record "Are You Lonesome To-Night?"  which was subsequently picked up by Elvis Presley Are You Lonesome Tonight?  (song) who later went on to chart this song at number 1 on the Billboard Charts in 1960.  Howie Stange did not achieve significant fame or fortune during his lifetime: however, his music left a lasting impression on a generation of young listeners who where first being introduced to rock and roll music in the 1950's.

Ashly Lorenzana: Ashly Lorenzana (born 1987) is a female sex worker, freelance writer and author of the autobiographical memoir titled "Sex, Drugs & Being an Escort".  Lorenzana currently resides in Portland, Oregon where she was born.

Don Read: Don Read (born December 15, 1933) is a former American football player, coach, and college athletics administrator.  He served as the head football coach at Portland State University (1968–1971, 1981–1985), the University of Oregon (1974–1976), the Oregon Institute of Technology (1977–1980), and the University of Montana (1986–1995), compiling a career college football record of 154–127–1.  From 1968 to 1971 and from 1981 to 1985, he led the Portland State Vikings to a 39–52–1 record.  From 1974 to 1976, he guided the Oregon Ducks to a 9–24 record with a 3–18 mark in conference.  His best success came at Montana, where he went 85–36, including three 11-win seasons and an NCAA Division I-AA National Championship in his final year of coaching, 1995.  Read currently resides in Corvallis, Oregon, where he participates in scouting and game planning for the Oregon State Beavers.

Darren Treasure: Darren Treasure (born 1965) is a high performance sport consultant.  Treasure’s past and present clients include sport governing bodies and professional athletes in a variety of sports and in the entertainment field.  He has worked as a sport psychology consultant with Olympic, World and NCAA national champions and all-American athletes at a number of different Universities.  Treasure currently resides in Portland, Oregon, and serves as the High Performance Director for the Nike Oregon Project.  In 2010, Treasure was featured in a Runner's World magazine article for his work with Kara Goucher and Alberto Salazar.  He's also been featured in a number of running periodicals for his work with, among others, the American record holder in the mile Alan Webb, and American long distance runner Galen Rupp, both of whom are members of the Oregon Project.

Dave Atchison: Dave Atchison (born 1979) is an American drummer/musician based in Portland, Oregon.  Atchison, a Nashville, Tennessee native is a founding member of the hardcore punk band From Ashes Rise, a band in which he played from 1997–2005, and again from 2009 to the present.  During the hiatus of From Ashes Rise from 2005 to 2009, he played drums in Smoke or Fire, recording and touring with the band until his departure in 2009.  Atchison currently resides in Portland, Oregon.

Eric Pollard (skier): Eric Pollard is an American snow freeskier and film editor from Welches, Oregon and currently resides in the Hood River region of Oregon.  He has been a professional skier for Line Skis for over 15 years and also designs skis for Line Skis.  He has had his own line of clothing at Causwell and K2 which never reached the market due to failures by the brands attempting to manufacture the goods.  He will be debuting a line of outerwear with Dakine in Fall 2015.

Wally Amos: Wallace "Wally" Amos, Jr. (born July 1, 1936) is an American TV personality, entrepreneur and author from Tallahassee, Florida.  He is the founder of the "Famous Amos" chocolate chip cookie brand.  He also was the host of the adult reading program, "Learn to Read".  He currently resides in Kailua, Hawaii where he runs The Cookie Kahuna gourmet cookie brand.

Eddie Martinez: Eddie Martinez is an American guitarist, born and raised in New York City and of Puerto Rican ancestry, who mainly functions as a session musician.  He has worked with David Lee Roth (on "Crazy from the Heat"), Run-D.M.C.  (on "Run-D.M.C. " and "King of Rock"), Robert Palmer (most notably "Simply Irresistible"), Meat Loaf (""), several Jim Steinman projects, and many others.  He also played jazz guitar during Blondie's Farewell Concert in 1982 in Toronto and he accompanied Mick Jagger at the first Live Aid concert in 1985.  He has recorded one solo album, "No Lies", on Cotillion Records which was produced by Bernard Edwards.  He currently resides in the Portland, Oregon area.

Stick Against Stone: Stick Against Stone is a Post-punk / No Wave band from Pittsburgh, Pennsylvania; that later resided in Brooklyn, New York; Eugene, Oregon and San Francisco, California and remained active (in no less than six incarnations) between 1981 and 1990.  The group returned to performing in 2011 and currently resides in the New York City area.

Corvallis, Oregon: Corvallis is a city in central western Oregon, United States.  It is the county seat of Benton County and the principal city of the Corvallis, Oregon Metropolitan Statistical Area, which encompasses all of Benton County.  As of the 2010 United States Census, the population was 54,462.  Its population was estimated by the Portland Research Center to be 55,298 in 2013.  Corvallis is the location of Oregon State University, a large Hewlett-Packard research campus, and Good Samaritan Regional Medical Center.

Question: Don Read currently resides in a city that is located in what county of Oregon?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person whose residence is being queried."
    },
    "residence_city": {
      "type": "string",
      "description": "The city where the person currently resides."
    },
    "residence_state": {
      "type": "string",
      "description": "The state where the person currently resides."
    },
    "residence_county": {
      "type": "string",
      "description": "The county of the city where the person currently resides."
    }
  },
  "required": [
    "person_name",
    "residence_city",
    "residence_state",
    "residence_county"
  ],
  "additionalProperties": false
}
