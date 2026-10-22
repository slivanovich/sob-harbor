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
Community (TV series): Community is an American television sitcom created by Dan Harmon that aired on NBC and Yahoo! Screen from September 17, 2009 to June 2, 2015.  The series follows an ensemble cast of characters played by Joel McHale, Gillian Jacobs, Danny Pudi, Yvette Nicole Brown, Alison Brie, Donald Glover, Ken Jeong, Chevy Chase, and Jim Rash at a community college in the fictional town of Greendale, Colorado.  It makes heavy use of meta-humor and pop culture references, often parodying film and television clichés and tropes.

Scream 4: Scream 4 (stylized as SCRE4M) is a 2011 American slasher film and the fourth and most recent installment in the "Scream" series.  Directed by Wes Craven, his final feature film before his death in 2015, and written by Kevin Williamson (who returned to the series after writing the first two films), the film stars an ensemble cast which includes David Arquette, Neve Campbell, Courteney Cox, Emma Roberts, Hayden Panettiere, Anthony Anderson, Alison Brie, Adam Brody, Rory Culkin, Marielle Jaffe, Erik Knudsen, Mary McDonnell, Marley Shelton and Nico Tortorella.  The plot involves Sidney Prescott returning to Woodsboro after ten years, as part of her book tour.  As soon as she arrives, Ghostface once again begins killing students from Woodsboro High.

Advanced Criminal Law: "Advanced Criminal Law" is the fifth episode of the first season of the American comedy television series "Community".  It aired in the United States on NBC on October 15, 2009.  The episode centers on three main story lines.  First, Jeff (Joel McHale) defends Britta (Gillian Jacobs) when she is accused of cheating on a Spanish test.  Meanwhile, Pierce (Chevy Chase) tries to help Annie (Alison Brie) write Greendale a school song.  Finally, Troy (Donald Glover) and Abed (Danny Pudi) test each other's gullibility.

GLOW (TV series): GLOW is an American comedy-drama television series created by Liz Flahive and Carly Mensch.  The series revolves around a fictionalization of the characters and gimmicks of the 1980s syndicated women's professional wrestling circuit, the Gorgeous Ladies of Wrestling (or GLOW) originally created by David McLane.  The first season consists of 10 episodes and was released via Netflix on June 23, 2017.  On August 10, 2017, Netflix renewed the series for a second season of 10 episodes.

Introduction to Statistics (Community): "Introduction to Statistics" is the seventh episode of the first season of the American comedy television series "Community", airing on NBC on October 29, 2009.  Annie (Alison Brie) hosts a Dia de los Muertos party, the success of which depends on Jeff (Joel McHale) attending.  At the party, Pierce gets high, causing trouble for the other characters.  Jeff pursues their statistics professor, Professor Michelle Slater (Lauren Stamile).  Finally, Shirley (Yvette Nicole Brown) is distressed due to her ex-husband's behavior.

List of BoJack Horseman episodes: "BoJack Horseman" is an American animated sitcom created by Raphael Bob-Waksberg.  The series stars Will Arnett as the eponymous character, BoJack Horseman, the washed-up star of the 1990s sitcom "Horsin' Around", who plans his big return to celebrity relevance with a tell-all autobiography that he dictates to his ghostwriter Diane Nguyen (Alison Brie).  BoJack also has to contend with the demands of his agent and on-again-off-again girlfriend, Princess Carolyn (Amy Sedaris); the misguided antics of his freeloading roommate, Todd Chavez (Aaron Paul); and his frenemy, Mr. Peanutbutter (Paul F. Tompkins), who is also Nguyen's boyfriend.  The series satirizes Hollywood, celebrity culture, and the film industry.

BoJack Horseman: BoJack Horseman is an American adult animated comedy-drama created by Raphael Bob-Waksberg.  The series stars Will Arnett as the title character.  The supporting cast includes Amy Sedaris, Alison Brie, Paul F. Tompkins, and Aaron Paul.  The series' first season premiered on August 22, 2014, on Netflix, with a Christmas special premiering on December 19.  The show is designed by the cartoonist Lisa Hanawalt, who had previously worked with Bob-Waksberg on the webcomic "Tip Me Over, Pour Me Out".

List of BoJack Horseman characters: "BoJack Horseman" is an American adult animated sitcom created by Raphael Bob-Waksberg.  The series stars Will Arnett as the title character, BoJack Horseman.  The supporting cast includes Amy Sedaris, Alison Brie, Paul F. Tompkins, and Aaron Paul.  The series' first season premiered on August 22, 2014, on Netflix, with a Christmas special premiering on December 19.  The show is designed by the cartoonist Lisa Hanawalt, who had previously worked with Bob-Waksberg on the webcomic "Tip Me Over, Pour Me Out".

The Disaster Artist (film): The Disaster Artist is a 2017 American biographical comedy-drama film produced and directed by James Franco.  Written by Scott Neustadter and Michael H. Weber, based on Greg Sestero's non-fiction book of the same name, the film chronicles the making of Tommy Wiseau's 2003 cult film "The Room".  The film stars James and Dave Franco as Wiseau and Sestero, alongside a supporting cast featuring Seth Rogen, Alison Brie, Ari Graynor, Josh Hutcherson and Jacki Weaver.

Alison Brie: Alison Brie Schermerhorn (born December 29, 1982 ) is an American actress and producer.  She portrayed Annie Edison in the NBC/Yahoo! sitcom "Community" (2009–2015) and Trudy Campbell in the AMC drama "Mad Men" (2007–2015).  Brie currently voices Diane Nguyen on the Netflix animated series "BoJack Horseman" (2014–present) and portrays Ruth Wilder on the Netflix comedy-drama series "GLOW" (2017).  She has starred in several films, such as "Scream 4" (2011), "The Five-Year Engagement" (2012), "The Lego Movie" (2014), "Get Hard" (2015), "Sleeping with Other People" (2015), and "How to Be Single" (2016).

Question: Who created the American comedy-drama television series in which Alison Brie portrays Ruth Wilder?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "alison_brie_role": {
      "type": "string",
      "description": "The character Alison Brie portrays in the series."
    },
    "series_genre": {
      "type": "string",
      "description": "The genre of the television series."
    },
    "creators": {
      "type": "array",
      "description": "A list of individuals who created the series.",
      "items": {
        "type": "string"
      }
    },
    "network_or_platform": {
      "type": "string",
      "description": "The network or streaming platform where the series was released."
    }
  },
  "required": [
    "series_name",
    "alison_brie_role",
    "series_genre",
    "creators",
    "network_or_platform"
  ],
  "additionalProperties": false
}
