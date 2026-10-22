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
J. Wellington Wimpy: J. Wellington Wimpy, generally referred to as Wimpy, is one of the characters in the long-running comic strip "Popeye", created by E. C. Segar in 1934 and originally called "Thimble Theatre", and in the "Popeye" cartoons based upon the strip.  Wimpy was one of the dominant characters in the newspaper strip, but when "Popeye" was adapted as an animated cartoon series by Fleischer Studios, Wimpy became a minor character; Dave Fleischer said that the character in the Segar strip was "too intellectual" to be used in film cartoons.  Wimpy did appear in Robert Altman's 1980 live-action musical film "Popeye," played by veteran character actor Paul Dooley.

Happy Feet Two: Happy Feet Two is a 2011 Australian-American 3D computer-animated family musical comedy film directed, produced and co-written by George Miller.  It is the sequel to Miller's 2006 film "Happy Feet".  It features Elijah Wood, Robin Williams, Hugo Weaving, Magda Szubanski and Anthony LaPaglia reprising their roles from the first film.  Pink voiced Gloria due to Brittany Murphy's death in 2009, and Richard Carter who portrayed a human character and voiced Barry in the first film, voices Bryan the beachmaster in this one, respectively.  Common also replaced Fat Joe as Seymour.  The original cast is joined by new characters voiced by Hank Azaria, Brad Pitt, Matt Damon, and Sofía Vergara.

Paul L. Smith: Paul Lawrence Smith (June 24, 1936 – April 25, 2012), most frequently credited as Paul Smith or Paul L. Smith, was an American actor.  Burly, bearded and imposing, he appeared in films and occasionally on television since the 1970s, generally playing "heavies" and bad guys.  His most notable roles include Hamidou, the vicious prison guard in "Midnight Express" (1978), Bluto in Robert Altman's "Popeye" (1980), Gideon in the ABC miniseries "Masada" (1981) and Glossu Rabban in David Lynch's "Dune" (1984).

Red Sonja (film): Red Sonja is a 1985 Dutch-American sword and sorcery action film directed by Richard Fleischer.  The film introduces Brigitte Nielsen as the title character with Arnold Schwarzenegger, Sandahl Bergman, Ronald Lacey, Ernie Reyes, Jr., Paul L. Smith and Pat Roach in supporting roles.  The film features the sword-wielding Marvel Comics character Red Sonja, created by Roy Thomas, who first appeared in Marvel's "Conan the Barbarian" series (#23) in 1973.  The film's character of Red Sonja was based on Red Sonya of Rogatino, a character created by Robert E. Howard appearing in his short story "The Shadow of the Vulture" (1934).  The film acknowledges that it was "based on the character created by Robert E. Howard" in the introductory credits.

A Wedding: A Wedding is a 1978 American comedy film directed by Robert Altman, with an ensemble cast that included Desi Arnaz, Jr., Carol Burnett, Paul Dooley, Vittorio Gassman, Mia Farrow, Lillian Gish, Geraldine Chaplin, Howard Duff, Nina Van Pallandt, Amy Stryker, and Pat McCormick.  The story is told in the trademark Altman style, with multiple plots and overlapping humorous dialogue.

Popeye (film): Popeye is a 1980 American musical comedy film directed by Robert Altman.  It is a live-action film adaptation of E. C. Segar's "Popeye" comic strip and stars Robin Williams as Popeye the Sailor Man and Shelley Duvall as Olive Oyl.

Can't Stop the Music: Can't Stop the Music is a 1980 American musical comedy film directed by Nancy Walker.  Written by Allan Carr and Bronté Woodard, the film is a pseudo-biography of disco's Village People which bears only a vague resemblance to the actual story of the group's formation.  It was produced by Thorn EMI Screen Entertainment (formerly EMI Films), and distributed by independent distributor Associated Film Distribution (AFD).

Health (film): HealtH (also known as Health and H.E.A.L.T.H.) is a 1980 American ensemble comedy film, the fifteenth feature project from director Robert Altman.  It stars Carol Burnett, Glenda Jackson, James Garner, Lauren Bacall, and Paul Dooley, and was written by Altman, Dooley and Frank Barhydt.  The film's title is an acronym for "Happiness, Energy, and Longevity through Health".

J. Karen Thomas: J. Karen Thomas (1965 – March 26, 2015) was an American actress, singer, and voice artist.  Her numerous television credits included her role as Audrey Carlisle on the dramatic television series, "Nashville".  Other television roles included recurring roles and guest appearances on "Drop Dead Diva", "The Ellen Show" and "Criminal Minds".  Thomas' cinematic credits included "The Identical" (2014), "Captive" (2015), and a co-starring role in the 2014 film, "Boulevard", which was shot in her native Nashville, opposite Robin Williams.

Roberto Aguire: Roberto Aguire (born 1988) is an actor and producer.  His first major film role was in the 2012 film "Struck by Lightning", in which he played the character of Emillio.  In 2014, he starred opposite Robin Williams as a troubled young street hustler named Leo in the film "Boulevard".

Question: What character did actor Paul L. Smith play opposite Robin Williams in the 1980 American musical comedy film directed by Robert Altman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor in question."
    },
    "co_star_name": {
      "type": "string",
      "description": "The name of the co-star mentioned in the question."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_director": {
      "type": "string",
      "description": "The director of the film."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actor in the specified film."
    }
  },
  "required": [
    "actor_name",
    "co_star_name",
    "film_title",
    "film_year",
    "film_director",
    "character_played"
  ],
  "additionalProperties": false
}
