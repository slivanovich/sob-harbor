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
Joe Jonas: Joseph Adam "Joe" Jonas (born August 15, 1989) is an American singer and actor.  Jonas first rose to fame as a member of the pop-rock band Jonas Brothers, along with his brothers Kevin and Nick.  The band's debut album, "It's About Time" (2006), was a commercial failure following a limited release.  The group signed with Hollywood Records, and in 2007 released their eponymous second studio album.  The album went on to be a commercial success for the group, selling over two million copies in the United States alone.  The group became heavily involved with the Disney Channel and later made their film debut in the Disney Channel Original Movie "Camp Rock" (2008).  The film and its soundtrack became a major hit for the network and helped propel the brothers into further commercial success.  Their third studio album, "A Little Bit Longer" (2008), became their first to top the "Billboard" 200 and went on to become their highest selling album to date.  The album's lead single became a top five hit in the United States.  Their fourth studio album, "Lines, Vines and Trying Times" (2009) became their second to top the charts in the United States.  The brothers also starred in two of their Disney Channel series from 2009 to 2010, being "JONAS L.A." and "".  In 2010, the group starred in "", reprising their roles from the original film.

Piper Curda: Piper Joy Curda (born August 16, 1997) is an American actress and singer.  She is known for her roles as Jasmine in the Disney Channel series "I Didn't Do It", and as Alyssa in the Disney Channel Original Movie "Teen Beach 2".  Previously Curda appeared in a recurring role in the third season of the Disney Channel series "A.N.T. Farm".

Laura Marano: Laura Marie Marano (born November 29, 1995) is an American actress and singer.  She starred in the Disney Channel series "Austin & Ally" as Ally Dawson.  Marano was one of the five original classmates in "Are You Smarter than a 5th Grader? ".  She starred in "Without a Trace" for three seasons and also "Back to You", in both instances playing the daughter of the main characters.  Marano starred in the indie film "A Sort of Homecoming".  Marano also starred in the 2015 Disney Channel Original Movie "Bad Hair Day" along with "Good Luck Charlie" actress Leigh-Allyn Baker.  In 2015, she signed with Big Machine Records and released her debut single "Boombox" on March 11, 2016.  At the end of 2016, Big Machine Records made the decision to drop all of their pop artists.  Marano then signed to Warner Bros.  Records in 2017 and plans to release her debut album with the label.  She is also the younger sister of actress Vanessa Marano who starred in Freeform's "Switched at Birth".

Jonas Brothers: The Jonas Brothers were an American rock and pop rock band.  Formed in 2005, they gained popularity from their appearances on the Disney Channel television network.  They consist of three brothers: Paul Kevin Jonas II, Joseph Adam Jonas, and Nicholas Jerry Jonas.  Raised in Wyckoff, New Jersey, the Jonas Brothers moved to Little Falls, New Jersey in 2005, where they wrote their first record that made its Hollywood release.  In the summer of 2008, they starred in the Disney Channel Original Movie "Camp Rock" and its sequel, "".  They also starred as Kevin, Joe, and Nick Lucas, the band JONAS, in their own Disney Channel series "JONAS", which was later re-branded for its second season as "Jonas L.A." The show was eventually cancelled after two seasons.  The band released four albums: "It's About Time" (2006), "Jonas Brothers" (2007), "A Little Bit Longer" (2008), and "Lines, Vines and Trying Times" (2009).

The Clapping Song: "The Clapping Song" is an American song, written by Lincoln Chase, originally arranged by Charles Callello and recorded by Shirley Ellis in 1965.  The song was released shortly after Ellis had released "The Name Game".  The lyrics of "The Clapping Song" were borrowed from the song "Little Rubber Dolly", a 1930s song recorded by the Light Crust Doughboys, and also feature instructions for a clapping game.  The song sold over a million copies, and peaked at number eight in the United States and number six in the UK.

Down Down Baby: "Down Down Baby" is a clapping game played by children in English-speaking countries.  In the game, two or more children stand in a circle, and clap hands in tune to a rhyming song.  As with most hand-clapping games, there are many variations.  Modified versions of the song have appeared in Little Anthony and the Imperials's "Shimmy Shimmy Ko-Ko Bop", Nelly's "Country Grammar", Simian Mobile Disco's "Hotdog", The Damned's "New Rose", The Drums' "Let's Go Surfing", Usher's "OMG", Carter USM's "Turn On, Tune In, And Switch Off", Bella Thorne and Zendaya's "Contagious Love", the film "Big" and EXO's "Ko Ko Bop".

Shake It Up: I Love Dance: Shake It Up: I Love Dance (stylized as Shake It Up: I <3 Dance, also known as Shake It Up: I ♥ Dance) is the third and final soundtrack for the Disney Channel Original Series "Shake It Up".  It was released on March 5, 2013.  The soundtrack is based on songs featuring on the show's third (and final) season (2012-2013).  The album features musical artists associated with or popularized by Disney Channel stars Bella Thorne, Zendaya, Bridgit Mendler, McClain Sisters, Caroline Sunshine, Roshon Fegan, Selena Gomez, Coco Jones, Olivia Holt and Dove Cameron, as well as non-Disney Channel stars Young L.A. (BG5), Drew Seeley, TKO, SOS and Nevermind.

G Hannelius: Genevieve Knight "G" Hannelius (born December 22, 1998) is an American actress and singer.  She starred as Avery Jennings in the Disney Channel sitcom "Dog with a Blog".  Prior to this, she had recurring roles in the Disney Channel series "Sonny with a Chance" and "Good Luck Charlie".  She has also starred in "Leo Little's Big Show" and has done voice work as Rosebud in the "Air Buddies" films.  She also guest starred in Disney Channel's series "Jessie".

Bella Thorne: Annabella Avery Thorne (born October 8, 1997) is an American actress and singer.  She played Ruthy Spivey in the television series "My Own Worst Enemy", Tancy Henrickson in the fourth season of "Big Love", and CeCe Jones on the Disney Channel series "Shake It Up".  She also appeared as Hilary/"Larry" in "Blended" and as Celia in "Alexander and the Terrible, Horrible, No Good, Very Bad Day".  In 2015, she played Madison in "The DUFF", Amanda in "Perfect High" and Hazel in "Big Sky".  Thorne currently stars as Paige on the Freeform series, "Famous in Love".

Miss Lucy had a baby: "Miss Lucy had a baby...", also known by various other names, is an American schoolyard rhyme.  Originally used as a jump-rope chant, it is now more often sung alone or as part of a clapping game.  It has many variations, possibly originating from it, or from its predecessors.

Question: Which actress starred in the Disney Channel series "Shake It Up" and released a modified version of the "Down Down Baby" clapping game?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The full name of the actress."
    },
    "disney_channel_series_starred_in": {
      "type": "string",
      "description": "The Disney Channel series the actress starred in."
    },
    "modified_clapping_game_song": {
      "type": "string",
      "description": "The title of the song that is a modified version of the clapping game."
    },
    "original_clapping_game": {
      "type": "string",
      "description": "The name of the original clapping game."
    },
    "actress_birth_date": {
      "type": "string",
      "description": "The birth date of the actress in YYYY-MM-DD format."
    }
  },
  "required": [
    "actress_name",
    "disney_channel_series_starred_in",
    "modified_clapping_game_song",
    "original_clapping_game",
    "actress_birth_date"
  ],
  "additionalProperties": false
}
