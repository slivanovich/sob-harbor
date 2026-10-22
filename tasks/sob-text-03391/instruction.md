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
2015 Buffalo Bills season: The 2015 Buffalo Bills season was the franchise’s 56th overall season as a football team, 46th in the National Football League, third under leadership of general manager Doug Whaley and first under new head coach Rex Ryan, who signed a five-year, $27.5 million contract on January 12, 2015 after having previously spent the past six seasons coaching the division-rival New York Jets, leading them to two straight AFC Championship games in 2009 and 2010, becoming the franchise’s 18th head coach and the fifth in the past seven years in the process.  Ryan replaced Doug Marrone, who opted out of his contract on December 31, 2014 to take advantage of a contract loophole, fearing the Pegulas were going to fire him, hence the reason the Bills entered the 2015 season looking for a new head coach.  Despite the bold prediction made by Ryan at his introductory press conference, where he stated, “I’m not going to let our fans down.  I am not going to do that.  I know it’s been 15 years since the Bills made the playoffs.  Well, get ready, man, we’re going.  We are going,” the Bills were unable to make the playoffs in their first season with Ryan as head coach, finishing with a record of 8-8 (the team’s first since 2002), making it the 16th straight season without a playoff appearance, which became the longest active in major professional sports after Major League Baseball’s Toronto Blue Jays broke their 22-year playoff drought on September 25, 2015.  It was also the first full season under the ownership of Terry and Kim Pegula (whom also own the Buffalo Sabres), having purchased the Bills partway through 2014 after the death of longtime owner Ralph Wilson in March at the age of 95.  The Bills began their season with an open competition for the starting quarterback position after Kyle Orton, the starter for most of the 2014 campaign, retired during the offseason, so the team acquired free agent Tyrod Taylor, a former backup quarterback of the Baltimore Ravens, who won the competition over incumbent second-string quarterback EJ Manuel and trade acquisition Matt Cassel, the latter of whom the team later traded along with a seventh-round pick in 2017 to the Dallas Cowboys, in exchange for a fifth-round draft pick in 2017.

Jeffrey J. Miller: Jeffrey J. Miller (born 1961) is an American author and historian, best known for his work focusing on the history of professional football.  His books include "Pop Warner: A Life on the Gridiron", "100 Things Bills Fans Should Know & Do Before They Die", "Game Changers: The Greatest Plays in Buffalo Bills Football History" (co-written with Hall-of-Fame coach Marv Levy), "Rockin' the Rockpile: The Buffalo Bills of the American Football League,""Buffalo's Forgotten Champions: The Story of Buffalo's First Professional Football Team and the Lost 1921 Title," and "The Icemen Cameth: The History of the Natural Ice Industry at Lime Lake, New York, 1880–1925".  He is a member of the Professional Football Researchers Association, and was the 2004 recipient of the PFRA's Ralph E. Hay Award, presented for "Lifetime achievement in professional football research and historiography."  He lives in Western New York with his wife and son.

2000 Buffalo Bills season: The 2000 Buffalo Bills season was the team's 41st and 31st as part of the National Football League.  The Bills total offense ranked 9th in the league and their total defense ranked 3rd in the league.  The 2000 season was the first since the 1987 season that long-time Bills players Bruce Smith, Andre Reed and Thurman Thomas were not on the team together, as all were released just days after the Bills were eliminated from the 1999 playoffs.  Smith and Reed signed with the Redskins, while Thomas signed with the Dolphins.  The Buffalo Bills finished in fourth place in the AFC East and finished the National Football League's 2000 season with a record of 8 wins and 8 losses.  Though the Bills were 7-4 after eleven games, they lost their next four in a row, only avoiding a losing season in the final game of the year.  The 2000 season marked a turning point in Buffalo's history.  From 2000 to present, the Bills have failed to make the playoffs.  After the 2000 season ended, general manager John Butler left the team to take the same position with the San Diego Chargers.

Ed Rutkowski: Edward John Anthony Rutkowski (born March 21, 1941) is a former American football player, and a former politician in Buffalo, New York.  Rutkowksi was a noted college and professional American football player.  A wide receiver, he was an American Football League All-Star in 1965, playing for the AFL's Buffalo Bills as a receiver, defensive back, punt and kickoff return man and backup quarterback from 1963 to 1968.  In a famous Topps football card mixup, Rutkowski was shown on two Buffalo Bills' football cards, his own, and mistakenly on the card for Ray Abruzzese.  Rutkowski closed out his Pro Football career by playing seven games as a backup quarterback with the Montreal Alouettes of the Canadian Football League in 1969.  From 1972-78 and again in 1990, Rutkowski served as a color commentator on the Bills' radio broadcasts.  In 1979, he became the County Executive of Erie County, New York, succeeding Edward Regan, who stepped down to become New York State Comptroller.  Rutkowski was elected to full terms in 1979 and 1983, following his one year unexpired term, for a total of nine years in office.  In 1987, Rutkowski was defeated for reelection by Assemblyman Dennis Gorski.

Buffalo Bills (quartet): The Buffalo Bills were a barbershop quartet formed in Buffalo, New York, on September 20, 1947.  The original members were tenor Vern Reed, an executive for the Tonawanda Boys' Club; lead Al Shea, who was a City of Buffalo policeman; baritone Herschel Smith, a corporate executive; and bass Bill Spangenberg, a truck driver for a steel company.  They started out as an unnamed foursome, singing for community groups.  During an appearance at the Buffalo Quarterback Club, they were introduced as the "Buffalo Bills", which was meant to be just for that day, but the name stuck from that point on.  Coincidentally, a football team known formerly as the Buffalo Bisons also changed its name to the Bills at about the same time; the name proved popular enough that the current Buffalo Bills also picked up the name when they debuted thirteen years later.

Tyrod Taylor: Tyrod Di'allo Taylor (born August 3, 1989) is an American football quarterback for the Buffalo Bills of the National Football League (NFL).  He was the starting quarterback for the Virginia Tech Hokies football team from the start of the 2008 college football season through the 2011 Orange Bowl, the final game of the 2010 college football season for Virginia Tech.  He was drafted by the Baltimore Ravens in the sixth round of the 2011 NFL Draft and served as the backup to starting quarterback Joe Flacco, including during the Ravens' Super Bowl XLVII victory over the San Francisco 49ers.  Signed by Buffalo as a free agent in 2015, Taylor was named the starting quarterback for the Bills at the beginning of the 2015 NFL season.

Dick Cunningham (American football): Richard Karekin Cunningham (born October 12, 1944) is a former American football linebacker.  He played in the American Football League for the Buffalo Bills and in the National Football League for the Buffalo Bills, the Houston Oilers, and the Philadelphia Eagles from 1967 to 1973.  Cunningham played college football at the University of Arkansas and was drafted in the eighth round of the 1966 NFL Draft by the Detroit Lions and the fourth round of the Red Shirt portion of the 1966 AFL Draft by the Buffalo Bills.

1984 Buffalo Bills season: The 1984 Buffalo Bills season was the 25th season for the club and its 15th in the National Football League (NFL).  The team started the season with eleven consecutive losses before an upset home win over Dallas in Week 12.  The 1984 Bills gave up a team-record 454 points on defense, an average of more than 28 per game.  The Bills gave up 30+ points eight times and allowed fewer than 20 points in a game only three times all season.  The Bills also allowed 60 quarterback sacks, for a total of 554 yards, the most-ever at the time.  The Bills' 4,341 total yards gained was second-worst in the league in 1984 (only the Colts had fewer total yards gained).  The 1984 Bills are one of only two NFL teams to have been outscored by 25 points six different times during the season.

Frank Reich: Frank Michael Reich, Jr. (born December 4, 1961) is an American football coach and former player who is the offensive coordinator for the Philadelphia Eagles of the National Football League (NFL).  Reich was a quarterback who played college football for the University of Maryland.  He was chosen by the Buffalo Bills in the third round of the 1985 NFL draft, and also played for the Carolina Panthers, New York Jets and Detroit Lions of the NFL.  Reich and Buffalo Bills starting quarterback Jim Kelly formed one of the longest-tenured backup-and-starter tandems, playing together for nine seasons from 1986 to 1994.  For a time, he had the distinction of having led his team to the biggest comeback victory ever in both the college and NFL ranks.

Matt Cassel: Matthew Brennan Cassel (born May 17, 1982) is an American football quarterback for the Tennessee Titans of the National Football League (NFL).  He was drafted by the New England Patriots in the seventh round of the 2005 NFL draft, and has also played for the Kansas City Chiefs, Minnesota Vikings, Buffalo Bills, and Dallas Cowboys.  He played college football at USC.

Question: What quarterback, born in 1082, was acquired by the Buffalo Bills in 2015?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "quarterback_name": {
      "type": "string",
      "description": "The full name of the quarterback."
    },
    "acquisition_year": {
      "type": "integer",
      "description": "The year the quarterback was acquired by the Buffalo Bills."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the quarterback."
    },
    "acquisition_method": {
      "type": "string",
      "description": "The method by which the quarterback was acquired (e.g., 'trade acquisition', 'free agent')."
    }
  },
  "required": [
    "quarterback_name",
    "acquisition_year",
    "birth_year",
    "acquisition_method"
  ],
  "additionalProperties": false
}
