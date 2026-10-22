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
For The Gambia Our Homeland: "For The Gambia Our Homeland" is the national anthem of the Gambia, written by Virginia Julia Howe and composed by Jeremy Frederic Howe (based on the traditional Mandinka song Foday Kaba Dumbuya).  It was adopted after an international competition to produce an anthem (and flag) before independence in 1965.

Union (Yes album): Union is the thirteenth studio album by the English rock band Yes, released on 30 April 1991 by Arista Records.  Production began in 1990 following the amalgamation of two bands featuring current and previous members of Yes at the time: Yes, consisting of Chris Squire, Trevor Rabin, Tony Kaye, and Alan White; and Anderson Bruford Wakeman Howe (ABWH), consisting of Jon Anderson, Steve Howe, Rick Wakeman, and Bill Bruford.  The album is a collection of tracks written and performed by each group separately.  Recording was met with differences from the beginning, including the merger of the two groups, internal relations, and the decision by producer Jonathan Elias to have session musicians play parts already put down by Wakeman and Howe.

2017 AFL Mark of the Year: The Australian Football League celebrates the best mark of the season through the annual Mark of the Year competition.  In 2017, this is officially known as the Woolworths AFL Mark of the Year Each round three marks are nominated and fans are able to vote online for their favourite.  The winner was Essendon 's Joe Daniher, which surprised many fans and media personal who expected Jeremy Howe of Collingwood to win the award for his screamer against Melbourne in round 12.  Following the shock win, Collingwood's president Eddie McGuire said that the voting system for Mark of the Year needs an overhaul.

Through a Naked Lens: Through a Naked Lens is a 2005 American play by author George Barthel.  It received its world premiere Off-Broadway at the Wings Theatre in New York City.  The play itself uses historical evidence and imagined circumstances to depict the rise of early Hollywood film star Ramón Novarro.  While a celebration of Novarro’s life, the drama is told largely through the perspective of reporter Herbert Howe.  While Barthel places Howe and Novarro in a romantic relationship, it is unknown if such a connection actually existed.  Howe did, however, spend a great deal of time with Novarro as his publicist.  The play also features Alice Terry, Rex Ingram, Irving G. Thalberg, Jim Quirk, Adela Rogers St. Johns, and Louis B. Mayer as characters.

Gordie Howe: Gordon "Gordie" Howe, OC (March 31, 1928 – June 10, 2016) was a Canadian professional ice hockey player.  From 1946 to 1980, he played twenty-six seasons in the National Hockey League (NHL) and six seasons in the World Hockey Association (WHA); his first 25 seasons were spent with the Detroit Red Wings.  Nicknamed "Mr. Hockey", Howe is considered the most complete player to ever play the game and one of the greatest ice hockey players of all time.  A 23-time NHL All-Star, he held many of the sport's career scoring records until they were broken in the 1980s by Wayne Gretzky, who himself has been a major champion of Howe's legacy.  He continues to hold NHL records for most games and seasons played.  In 2017, Howe was named one of the "100 Greatest NHL Players".

Saskatoon Minor Football Field: The Saskatoon Minor Football Field at Gordon Howe Park (formerly known as Gordie Howe Bowl) is a football stadium located in Saskatoon, Saskatchewan, Canada.  It was opened September 30, 1960, built on land repossessed by the city in 1931 for unpaid taxes.  It is the home of the Saskatoon Hilltops, who play in the Prairie Football Conference of the Canadian Junior Football League and is also used for high school football.  It is located on the southwest corner of the city.  The park is named after Gordie Howe, a Saskatoon native and member of the Hockey Hall of Fame.

Jeremy Howe: Jeremy Howe (born 29 June 1990) is a professional Australian rules footballer playing for the Collingwood Football Club in the Australian Football League (AFL).  He previously played for the Melbourne Football Club from 2011 to 2015.

No Apologies (Alanis Morissette song): "No Apologies" is a pop-ballad song co-written by Alanis Morissette, Leslie Howe and Serge Côté, and produced by Howe for Morissette's second album "Now Is the Time" (1992).  Its protagonist says her feelings for someone have "turn[ed] to stone", but that "[her] heart makes no apologies".  It was released as the album's second single in 1993 (see 1993 in music) and was Morissette's first ballad to be released as a single.  It received radio and video play but was not given a commercial release, and it did not cause sales of "Now Is the Time" to significantly increase.  Leslie Howe engineered and mixed the song, and a promotional single for it includes the album version and a radio edit.  It did reach number 14 on the Canadian pop chart.

Colleen Howe: Colleen Joffa Howe (February 17, 1933 – March 6, 2009) was a sports agent who founded Power Play International and Power Play Publications to manage the business interests of her husband, Hall of Fame hockey player Gordie Howe, as well as those of their sons Marty and Mark.  She was married to Gordie for 55 years, until her death.  As a civic leader, she brought the first Junior A hockey team to the United States, built the first indoor rink for public use in Michigan, and ran for Congress.  In 2000, as "Mrs. Hockey", Howe received the Wayne Gretzky International Award—presented to individuals "who have made major contributions to the growth and advancement of hockey in the United States"—from the United States Hockey Hall of Fame, along with her husband (known as "Mr. Hockey") and their two sons Mark and Marty.

Birth and After Birth: Birth and After Birth is an absurdest play written by Tina Howe.  It was written in 1972 but it wasn’t produced until 2006.  Howe was originally met with backlash and was quoted saying "The absurdists can shake up our preconceptions about power and identity but for a woman to take on the sanctity of motherhood, even my agent at the time dismissed me.”  Its first performance was with the Atlantic Theatre Company and it was directed by Christian Parker.  Howe has been compared to many of the great absurdest writers of the 20th century due to her loose structure and nonsense plot.

Question: What sport did Jeremy Howe play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the player."
    },
    "sport_played": {
      "type": "string",
      "description": "The sport the player is known for playing."
    },
    "current_team": {
      "type": "string",
      "description": "The current team the player plays for."
    },
    "league": {
      "type": "string",
      "description": "The league the player participates in."
    }
  },
  "required": [
    "player_name",
    "sport_played",
    "current_team",
    "league"
  ],
  "additionalProperties": false
}
