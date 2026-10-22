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
Peter Pan (1953 film): Peter Pan is a 1953 American animated adventure film produced by Walt Disney and based on the play "Peter Pan, or The Boy Who Wouldn't Grow Up" by J. M. Barrie.  It is the 14th Disney animated feature film and was originally released on February 5, 1953, by RKO Radio Pictures.  "Peter Pan" is the final Disney animated feature released through RKO before Walt Disney's founding of his own distribution company, Buena Vista Distribution, later in 1953 after the film was released.  "Peter Pan" is also the final Disney film in which all nine members of Disney's Nine Old Men worked together as directing animators.  It is also the second Disney animated film starring Kathryn Beaumont, Heather Angel, and Bill Thompson after their roles in the animated feature "Alice in Wonderland".

Hercules (1997 film): Hercules is a 1997 American animated musical fantasy comedy film produced by Walt Disney Feature Animation for Walt Disney Pictures.  The 35th Disney animated feature film, the film was directed by Ron Clements and John Musker.  The film is loosely based on the legendary hero Heracles (known in the film by his Roman name, Hercules), the son of Zeus, in Greek mythology.  The film also featured the first positive portrayal of African American women in a Disney animated film.

The Sword in the Stone (film): The Sword in the Stone is a 1963 American animated musical fantasy comedy film produced by Walt Disney and released by Buena Vista Distribution.  The 18th Disney animated feature film, it was the final Disney animated film to be released before Walt Disney's death.  The songs in the film were written and composed by the Sherman Brothers, who later wrote music for other Disney films like "Mary Poppins" (1964), "The Jungle Book" (1967), "The Aristocats" (1970), and "Bedknobs and Broomsticks" (1971).

Lady and the Tramp: Lady and the Tramp is a 1955 American animated romantic musical comedy-drama film produced by Walt Disney and released to theaters on June 22, 1955 by Buena Vista Distribution.  The 15th Disney animated feature film, it was the first animated feature filmed in the CinemaScope widescreen film process.  Based on "Happy Dan, The Whistling Dog" by Ward Greene, "Lady and the Tramp" tells the story of a female American Cocker Spaniel named Lady who lives with a refined, upper-middle-class family, and a male stray mongrel called the Tramp.  When the two dogs meet, they embark on many romantic adventures.  A direct-to-video sequel, "", was released in 2001.

Interrupting Chicken: "Interrupting Chicken’s" plot has a repetitive nature, with a humorous story line and a good underlying message.  The story begins with little red chicken’s bedtime.  Little red chicken’s calm, patient father is referred to as “Papa.”  Papa is getting little red chicken settled for bed.  Little red chicken eagerly suggests reading a bedtime story.  Papa often refers to how little red chicken regularly interrupts bedtime stories before they are finished.  Papa informs little red chicken that she should not interrupt the story like past experiences, little red chicken promises to “be good tonight”(4).  "Interrupting chicken" includes other classic children’s books such as: "Hansel and Gretel"," Little Red Riding Hood" and "Chicken Little".  Papa begins by kindly reading "Hansel and Gretel" to little red chicken.  Before reaching the end of the story little red chicken interrupts the story!  The images show little red chicken in the story of "Hansel and Gretel" and she is yelling, “don’t go in she’s a witch!”  which results to a sudden end to the story(18).  Little Red chicken appears to be absolutely delighted with her decision to step in and save the day while her father was not so impressed.  Papa addresses little red chicken's behavior and she promises not to engage in such activity for the next story.  Papa begins by reading "Little Red Riding Hood".  Before Papa could get through the story little Red chicken jumps in once again and informs Little Red Riding Hood that she is not to talk to strangers.  Papa begins to become tired and informs little red chicken that she should not be interrupting because the purpose of bedtime stories is to make her sleepy.  Little red chicken defends herself by saying “he was a mean old wolf.” (18).  Little red chicken convinces Papa to read another story, this time, "Chicken Little".  Little red chicken once again jumps into to solve the problem.  Papa is becoming exhausted and little red chicken is upset because there are no more stories to read.  Little red chicken believes she cannot go to bed without a story.  Papa suggests that little red chicken tell him a story.  Little red chicken loves the idea and climbs into bed, yawning and tired.  Little red chicken then writes a story about reading stories for bedtime until she realizes papa has fallen asleep!  The story ends with little red chicken saying “good night, Papa” and the last picture shows both of them cuddled up happily in bed(40).

Home on the Range (2004 film): Home on the Range is a 2004 American animated musical western comedy film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  The 45th Disney animated feature film, it was the last 2D animated Disney film released until "The Princess and the Frog" in 2009.  Named after the popular country song of the same name, "Home on the Range" features the voices of Roseanne Barr, Judi Dench, Jennifer Tilly, Cuba Gooding Jr., Randy Quaid, and Steve Buscemi.  The film is set in the Old West, and centers on a mismatched trio of dairy cows—brash, adventurous Maggie; prim, proper Mrs. Caloway; and ditzy, happy-go-lucky Grace.  The three cows must capture an infamous cattle rustler named Alameda Slim for his bounty in order to save their idyllic farm from foreclosure.  Aiding them in their quest is Lucky Jack, a feisty, peg-legged rabbit, but a selfish horse named Buck, eagerly working in the service of Rico, a famous bounty hunter, seeks the glory for himself.

Dinosaur (film): Dinosaur is a 2000 American CGI animated adventure film produced by Walt Disney Feature Animation and The Secret Lab and released by Walt Disney Pictures.  It is the 39th Disney animated feature film and Disney's The Secret Lab computer animated feature, though it is not officially labeled as one of the animated classics in the United Kingdom, where "The Wild" (2006) is included in the canon instead.

Oliver &amp; Company: Oliver & Company is a 1988 American animated musical comedy-drama film produced by Walt Disney Feature Animation and released on November 18, 1988, by Walt Disney Pictures.  The 27th Disney animated feature film, the film is inspired by the classic Charles Dickens novel "Oliver Twist", which has been adapted many other times for the screen.  In the film, Oliver is a homeless kitten who joins a gang of dogs to survive in the streets.  Among other changes, the setting of the film was relocated from 19th century London to late 1980s New York City, Fagin's gang is made up of dogs (one of which is Dodger), and Sykes is a loan shark.

Chicken Little (2005 film): Chicken Little is a 2005 American 3D computer-animated science fiction comedy film, produced by Walt Disney Feature Animation and loosely based on the original fable of the same name.  The 46th Disney animated feature film, it was directed by Mark Dindal from a screenplay by Steve Bencich, Ron J. Friedman, and Ron Anderson, based on a story by Mark Kennedy and Dindal.  The film is dedicated to Disney artist and writer Joe Grant, who died before the film's release.

Old Dogs (film): Old Dogs is a 2009 American ensemble comedy film directed by "Wild Hogs"'s Walt Becker and starring John Travolta and Robin Williams with an ensemble supporting cast played by Kelly Preston, Matt Dillon, Justin Long, Seth Green, Rita Wilson, Dax Shepard, Lori Loughlin, and Bernie Mac.  It was released in theaters on November 25, 2009 and was released on DVD March 9, 2010.

Question: What was the 46th Disney animated feature film, Old Dogs or Chicken Little ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the Disney animated feature film."
    },
    "feature_film_number": {
      "type": "integer",
      "description": "The sequential number of the film in the Disney animated feature film canon."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "production_company": {
      "type": "string",
      "description": "The company that produced the film."
    }
  },
  "required": [
    "film_title",
    "feature_film_number",
    "release_year",
    "production_company"
  ],
  "additionalProperties": false
}
