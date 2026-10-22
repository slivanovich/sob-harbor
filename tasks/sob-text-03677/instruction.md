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
Ron Singleton: Ronald Lee Singleton (born April 15, 1952 in New Orleans, Louisiana) is a former American football offensive tackle in the National Football League.  He was drafted by the San Diego Chargers in the fourth round of the 1976 NFL Draft.  He played college football at Grambling State.  He is mentioned in The Blind Side, by Michael Lewis.

The Blind Side: Evolution of a Game: The Blind Side: Evolution of a Game is a book by Michael Lewis released in 2006 by W. W. Norton & Company.  It focuses on American football.

The Blind Side (film): The Blind Side is a 2009 American biographical sports drama film written and directed by John Lee Hancock, based on the 2006 book "" by Michael Lewis.  The storyline features Michael Oher, an offensive lineman who was drafted by the Baltimore Ravens of the NFL.  The film follows Oher from his impoverished upbringing, through his years at Wingate Christian School (a fictional representation of Briarcrest Christian School in Memphis, Tennessee), his adoption by Sean and Leigh Anne Tuohy, to his position as one of the most highly coveted prospects in college football, then finally becoming a first-round pick of the Ravens.

Michael Oher: Michael Jerome Oher ( ; born Michael Jerome Williams, Jr.; May 28, 1986) is an American football offensive tackle who is currently a free agent.  He played college football for the University of Mississippi, and was drafted by the Baltimore Ravens in the first round of the 2009 NFL Draft.  He has also played for the Tennessee Titans and Carolina Panthers.

Chances (Five for Fighting song): "Chances" is a song written by Gregg Wattenberg and John Ondrasik, and recorded by Ondrasik under his stage name Five for Fighting.  The song was released on July 21, 2009, as the first single from the band's 2009 album "Slice".  The song was the band's fourth single to chart on the "Billboard" Hot 100 chart.  "Chances" is the second track of the official Superleague Formula soundtrack "A Beautiful Race: The Superleague Formula album", which was re-released from Sony Music Entertainment Philippines on April 4, 2010.  It was also featured in the end credits to "The Blind Side", the end montage of scenes in "The Vampire Diaries" season 1, episode 10, "The Turning Point" and in promos for professional wrestler Shawn Michaels' induction into the WWE Hall of Fame of 2011.

Mark Livolsi: Mark Livolsi is an American film editor.  He is primarily known for his work on the hit comedies "Wedding Crashers" (2005) and "The Devil Wears Prada" (2006); for each film, Livolsi was nominated for an ACE Eddie Award.  His most recent film as editor is the hugely successful football drama "The Blind Side".

Neil R. Barrett: Neil Richard Joseph Barrett (born 27 July 1992 in Dublin) is an Irish rugby union player.  He is a back-row forward who can play either blind side flanker or at number 8, and has occasionally played at centre.  He plays club rugby for Leinster in the Pro14 and Heineken Cup.  Barrett, still not 20 years old, is seen as a great prospect for the future, and is a current member of the Irish national u-20 team, having also played for his country at u-18 (schools) and u-19 level.  He is renowned for his ball carrying ability and strength, as well as crowd-pleasing "big hits", or impact tackles.  He also represents a solid line-out option and is near the complete back-rower due to combativeness at the breakdown.  He is yet to establish himself as a starter for the senior Leinster team, but has made five appearances, as well as playing regularly for both the "A" and u-20 sides.  While attending Blackrock College he helped the school to win both the Senior and Junior cup.  He was on the same cup-winning teams as fellow Leinster Rugby academy member and Ireland u-20 team-mate Simon Hillary.

Playfair Cricket Annual: Playfair Cricket Annual is a compact annual about cricket that is published in the United Kingdom each April, just before the English cricket season is due to begin.  It has been published every year since 1948.  Its main purposes are to review the previous English season and to provide detailed career records and potted biographies of current players.  It is produced in a "pocket-sized" format, being approximately 5×4 in (i.e., about 13×10 cm), so that it is a convenient size for carrying to cricket matches.  The front cover of each edition has featured a photograph of a prominent current cricketer.  There is a popular myth that this "honour" has a "hex" or "curse" associated with it, as the player featured then invariably has a poor season.

Hugh Freeze: Danny Hugh Freeze Jr. (born September 27, 1969) is an American football coach.  He is the former head coach at the University of Mississippi, and is widely known for being portrayed as the head coach from the 2009 motion picture "The Blind Side" starring Sandra Bullock.  Freeze served as the head football coach at Lambuth University from 2008 to 2009 and at Arkansas State University in 2011.  He was previously a successful high school football coach at Briarcrest Christian School in Memphis, Tennessee, where he coached Michael Oher and Greg Hardy.  He would later follow both of them to the University of Mississippi.

Leigh Anne Tuohy: Leigh Anne Tuohy (née Roberts; born August 9, 1960) is an American interior designer.  She is best known for being the legal guardian of Michael Oher.  Their story was featured in Michael Lewis' 2006 book, "", and its 2009 feature film adaptation "The Blind Side".  In the film, Tuohy was portrayed by actress Sandra Bullock, who won the Academy Award for Best Actress for the performance.

Question: In what year was the football player featured in The Blind Side drafted into the NFL?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the football player featured in 'The Blind Side'."
    },
    "nfl_draft_year": {
      "type": "integer",
      "description": "The year the player was drafted into the NFL."
    },
    "nfl_team_drafted_by": {
      "type": "string",
      "description": "The NFL team that drafted the player."
    },
    "draft_round": {
      "type": "string",
      "description": "The round in which the player was drafted."
    },
    "featured_in_media": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of media where the player is featured."
    }
  },
  "required": [
    "player_name",
    "nfl_draft_year",
    "nfl_team_drafted_by",
    "draft_round",
    "featured_in_media"
  ],
  "additionalProperties": false
}
