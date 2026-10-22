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
Johnny Green: John Waldo Green (10 October 1908 – 15 May 1989) was an American songwriter, composer, musical arranger, conductor and pianist.  He was given the nickname "Beulah" by colleague Conrad Salinger.  His most famous song was one of his earliest, "Body and Soul".  Green won four Academy Awards for his film scores and a fifth for producing a short musical film, and he was inducted into the Songwriters Hall of Fame in 1972.

Hamilton (album): Hamilton is the cast album to the 2015 musical "Hamilton".  The musical is based on the 2004 biography of Alexander Hamilton written by Ron Chernow, with music, lyrics, and book by Lin-Manuel Miranda.  The recording stars Lin-Manuel Miranda, Leslie Odom Jr., Phillipa Soo, Renée Elise Goldsberry, Christopher Jackson, Daveed Diggs, Anthony Ramos, Okieriete Onaodowan, Jasmine Cephas Jones, and Jonathan Groff.  It also features Jon Rua, Thayne Jasperson, Sydney James Harcourt, Ariana DeBose, and Sasha Hutchings.  It achieved the largest first week sales for a digital cast album and is the highest-charting cast album since 1963.  It was the highest-selling Broadway cast album of 2015 and peaked at number one on the Rap Album chart, the first cast album to ever do so.

Anthony Ramos (artist): Anthony Ramos is an American video artist, performance artist and painter.  He was born in 1944 in Providence, Rhode Island, and lives in the South of France.

Anthony Ramos (actor): Anthony Ramos Martinez (born November 1, 1991) is an American actor.  In 2015, he originated the roles of John Laurens and Philip Hamilton, Alexander Hamilton's eldest son, in the Broadway musical "Hamilton".  Prior to that, he originated the role of Justin Laboy in Lin-Manuel Miranda's short musical "21 Chump Street".  He has been cast in the upcoming comedy-drama series "She's Gotta Have It" as Mars Blackmon.

White Girl (2016 film): White Girl is a 2016 American film written and directed by Elizabeth Wood in her directorial debut.  It stars Morgan Saylor, Brian Marc, India Menuez, Adrian Martinez, Anthony Ramos, Ralph Rodriguez, Annabelle Dexter-Jones, Chris Noth and Justin Bartha.

Thomas and Sally: Thomas and Sally (also known as "The Sailor's Return") is a dramatic pastoral opera in two acts by the composer Thomas Arne with an English libretto by Isaac Bickerstaff.  The opera was meant to be performed as an "after piece", which is a short musical work to be performed after a spoken play.

21 Chump Street: 21 Chump Street is a fifteen-minute musical written by composer Lin-Manuel Miranda, who most notably created the Broadway musicals "In the Heights", "Bring It On the Musical" and "Hamilton".  The show was based on an episode of "This American Life," where a high school student fell in love with an undercover police officer, and ultimately was arrested for selling drugs to the officer in an attempt to impress her.  The musical premiered in a showcase put on by "This American Life", held at the Brooklyn Academy of Music on June 7, 2014.

Lin-Manuel Miranda: Lin-Manuel Miranda ( ; born January 16, 1980) is an American composer, lyricist, playwright, and actor best known for creating and starring in the Broadway musicals "Hamilton" and "In the Heights".  He co-wrote the songs for Disney's "Moana" soundtrack (2016) and is set to star in their upcoming film "Mary Poppins Returns".  Miranda's awards include a Pulitzer Prize, two Grammy Awards, an Emmy Award, a MacArthur Fellowship, and three Tony Awards.

The Musical of Musicals (The Musical!): The Musical of Musicals (The Musical!)  is a musical by Joanne Bogart and Eric Rockwell.  It is structured into five acts, each of which is a short musical parodying (and paying homage to) the style of an American or British musical theatre composer or composer/lyricist team, all dealing with roughly the same classic melodrama plot: "I can't pay the rent!"

Art Thief Musical!: Art Thief Musical!  is a 2004 American short musical film by Linus Lau.  It stars Autumn Reeser, Benjamin Sprunger, Matt O'Toole and Sean Smith.  It premiered at the Palm Springs International Festival of Short Films in September 2004.  Inspired by Jacques Demy's The Umbrellas of Cherbourg, all of the "dialogue" throughout the entire film is sung, except for the last two lines.

Question: which American composer did Anthony Ramos originated the role of Justin Laboy in his short musical "21 Chump Street"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musical_title": {
      "type": "string",
      "description": "The title of the short musical."
    },
    "composer_name": {
      "type": "string",
      "description": "The name of the American composer."
    },
    "composer_nationality": {
      "type": "string",
      "description": "The nationality of the composer."
    },
    "role_originated": {
      "type": "string",
      "description": "The role originated by Anthony Ramos in the musical."
    }
  },
  "required": [
    "musical_title",
    "composer_name",
    "composer_nationality",
    "role_originated"
  ],
  "additionalProperties": false
}
