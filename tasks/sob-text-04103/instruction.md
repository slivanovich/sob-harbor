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
Faith Off: "Faith Off" is the eleventh episode of the eleventh season of the American animated sitcom "The Simpsons".  It originally aired on the Fox network in the United States on January 16, 2000.  In the episode, Bart believes he has the power to heal others through faith after removing a bucket glued to Homer's head.  Meanwhile, Homer creates a homecoming game float for Springfield University.  The episode, which features guest appearances from Don Cheadle and Joe Mantegna, received generally positive reviews from critics following its release on home video in the season 11 DVD.

Bart's New Friend: "Bart's New Friend" is the eleventh episode of the 26th season of the American animated sitcom "The Simpsons", and the 563rd episode of the series.  It originally aired on the Fox network in the United States on January 11, 2015.  The episode focuses on Bart's new friendship with his father Homer, who has been hypnotized in order to think he is a young boy.

Going Native: "Going Native" is the eleventh episode of the sixteenth season of the American animated sitcom "South Park", and the 234th episode of the series overall.  It premiered on Comedy Central in the United States on October 17, 2012.  In the episode, when Butters starts acting out at school, he learns that he wasn't born in South Park.  He and Kenny journey to Butters' homeland for his coming of age ceremony.

E-I-E-I-(Annoyed Grunt): "E-I-E-I-(Annoyed Grunt)" is the fifth episode of the eleventh season of the American animated sitcom "The Simpsons".  It originally aired on the Fox network in the United States on November 7, 1999.  In the episode, inspired by a "Zorro" movie, Homer begins slapping people with a glove and challenging them to duels.  However, when a real Southern gentleman accepts Homer's request for a duel, the Simpsons run off to the old farm Homer lived in with his parents and breed a dangerously addictive but successful tobacco/tomato hybrid called "tomacco".  Just when they are about to gain a hundred and fifty million dollars from the hybrid, dangerously addicted animals ruin their plan.

South Park (season 15): The fifteenth season of the American animated sitcom "South Park" began airing on Comedy Central on April 27, 2011 and ended on November 16, 2011.  In response to reactions to the mid-season finale episode "You're Getting Old", which seemed to insinuate that creators Trey Parker and Matt Stone were wrapping up the series, Comedy Central proclaimed through the media that "South Park" was renewed for two more seasons, and the duo were signed through 2013.  Shortly before the airing of the season finale episode "The Poor Kid", "South Park" was extended again until 2016, taking the show to 20 seasons.  Parker was the director and writer for all episodes, and Robert Lopez was the writer in this eleventh episode for the fifteenth season.

The Blind Side (Family Guy): "The Blind Side" is the eleventh episode of the tenth season of the American animated sitcom "Family Guy".  The episode originally aired on Fox in the United States on January 15, 2012.  In the episode, Peter meets Stella, the new worker who replaces Opie and is deaf.  Quagmire falls for her and decides to have a party for disabled women at the bar, where Brian meets a blind girl named Kate and decides to date her.  Meanwhile, Lois replaces the stairs after Stewie gets a splinter, but Peter constantly slips and falls down them and eventually decides to stay upstairs for good.

Insane in the Mainframe: "Insane in the Mainframe" is the eleventh episode of the third season of the American animated sitcom "Futurama".  It originally aired on the Fox network in the United States on April 8, 2001.  The episode was written by Bill Odenkirk and directed by Peter Avanzino.  In the episode, Fry and Bender are admitted to an insane asylum for robots after being charged for their roles in holding up a bank.  Fry's attempts to convince the asylum's staff that he is a human fail; he is eventually made to believe that he is a robot, and is deemed "cured" and released from the asylum.  After being released, the Planet Express crew try to make him rediscover his humanity; these attempts fail, until Fry bleeds and realizes he is in fact, human.

The Simpsons (season 11): "The Simpsons"' eleventh season originally aired between September 1999 and May 2000, beginning on Sunday, September 26, 1999, with "Beyond Blunderdome".  The showrunner for the 11th production season was Mike Scully.  The season contained four hold-over episodes from the season 10 (AABF) production line.

Specs and the City: "Specs and the City" is the eleventh episode of the 25th season of the American animated sitcom "The Simpsons", and the 541st episode of the series.  It premiered on the Fox network in the United States on January 26, 2014.  The episode was written by Brian Kelley and directed by Lance Kramer.  The original title of the episode was intended to be "I Only Have My Eyes for You", a take on "I Only Have Eyes for You", but was changed to "Specs and the City", a take on "Sex and the City".  The Oogle goggles were originally known as "MyEyes".

The D'oh-cial Network: "The D'oh-cial Network" is the eleventh episode of the twenty-third season of the American animated sitcom "The Simpsons".  It originally aired on the Fox network in the United States on January 15, 2012.  In the episode, Lisa is sad that she has no real friends.  She discovers that it is easier to make friends on the Internet and therefore creates a social networking website called SpringFace.  It becomes incredibly popular in Springfield and Lisa gets many online friends.  However, they still ignore her in real life, and the website starts to cause trouble in the town when people use it while driving and cause accidents.  Lisa is put on trial and the court orders her to close down SpringFace.

Question: "Faith Off" is the eleventh episode of which season of the American animated sitcom, "The Simpsons"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "episode_title": {
      "type": "string",
      "description": "The title of the episode."
    },
    "series_title": {
      "type": "string",
      "description": "The title of the animated sitcom."
    },
    "season_number": {
      "type": "integer",
      "description": "The season number of the episode."
    },
    "episode_number_in_season": {
      "type": "integer",
      "description": "The episode number within its season."
    },
    "network": {
      "type": "string",
      "description": "The network on which the episode originally aired."
    },
    "original_air_date": {
      "type": "string",
      "format": "date",
      "description": "The original air date of the episode."
    }
  },
  "required": [
    "episode_title",
    "series_title",
    "season_number",
    "episode_number_in_season",
    "network",
    "original_air_date"
  ],
  "additionalProperties": false
}
