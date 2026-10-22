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
Normahl: Normahl is a German punk band formed in 1978 in Winnenden near Stuttgart by four high school students.  Their first major entry into the U.S. was with the song Keine Überdosis Deutschland featured in the hit movie Euro Trip.

Jacob Pitts: Jacob Pitts (born November 20, 1979) is an American actor.  His most notable performance was in the 2004 film "EuroTrip" as Cooper Harris and as Bill "Hoosier" Smith in HBO's 2010 miniseries "The Pacific".  He appeared in the play "Where Do We Live" at the Vineyard Theatre in May 2004.  Pitts has also appeared in TV shows such as "Law & Order" in 2000 where he played John Telford, "Sex & The City" (2000) where he played Sam Jones, and "Ed" where he played Johnny Malone.  Pitts also had a starring role on the FX television drama "Justified" as Tim Gutterson.

EuroTrip: EuroTrip is a 2004 American teen comedy adventure film written by Alec Berg, David Mandel, and Jeff Schaffer, and directed by Schaffer.  The film stars Scott Mechlowicz, Jacob Pitts, Michelle Trachtenberg, Travis Wester, and Jessica Boehrs.  Mechlowicz portrays Scott "Scotty" Thomas, an American teenager who travels across Europe in search of his German pen pal, Mieke (Boehrs).  Accompanied by his friend Cooper (Pitts) and siblings Jenny and Jamie (Trachtenberg and Wester), Scott's quest takes him to London, Paris, Amsterdam, Bratislava, Berlin, and Rome, encountering awkward and embarrassing situations along the way.  The film received a 2004 Teen Choice Award nomination for "Choice Movie Your Parents Didn't Want You to See".

21 (2008 film): 21 is a 2008 American heist drama film directed by Robert Luketic and starring Jim Sturgess, Kevin Spacey, Laurence Fishburne, Kate Bosworth, Liza Lapira, Jacob Pitts, Aaron Yoo, and Kieu Chinh.  The film is inspired by the true story of the MIT Blackjack Team as told in "Bringing Down the House", the best-selling book by Ben Mezrich.  Despite its largely mixed reviews and controversy over the film's casting choices, "21" was a box office success, and was the number one film in the United States and Canada during its first and second weekends of release.

ZaSu Pitts: ZaSu Pitts ( ; born Eliza Susan Pitts; January 3, 1894 – June 7, 1963) was an American actress who starred in many silent dramas and comedies, transitioning successfully to mostly comedy films with the advent of sound films.  She may be best known for her performance in Erich von Stroheim's epic silent film "Greed".

Captain Euro: Captain Euro is a fictional comic book-style superhero character, created in 1999 as a way to promote the European Union, and specifically the Euro, the single European currency that arrived in 2002.  The character has been featured on a website (first at captaineuro.com, later at captaineuro.eu) since 1999, but has not appeared in any actual comic books.  The website's contents are available only in English.

Destry Rides Again (1932 film): Destry Rides Again is a 1932 American pre-Code Western movie starring Tom Mix and directed by Benjamin Stoloff, about a man framed for a crime he didn't commit, who returns to wreak havoc following his release from prison.  The movie was based on a novel by Max Brand.  The supporting cast includes Claudia Dell, ZaSu Pitts, and Francis Ford.

Benjamin Levy (musician): Double bassist Benjamin Levy was born in Cooperstown, New York in 1980 and grew up in Pennsylvania and Colorado.  He attended Cherry Creek High School in Greenwood Village, Colorado during which time he studied with David Potter, and spent two summers studying with Stuart Sankey at the Aspen Music Festival.  Mr. Levy has appeared in performance with soprano Dawn Upshaw, the Borromeo String Quartet, and the Hawthorne String Quartet.  In 2002, while a Fellow at the Tanglewood Music Center, Mr. Levy was the recipient of the Maurice Schwartz Prize and was reviewed in The New York Times for his performance of Jacob Druckman's "Valentine" for solo double bass.  A 2002 graduate of the New England Conservatory, Mr. Levy joined the bass section of the Boston Symphony Orchestra at the start of the 2003 Tanglewood season.  He is also the Coordinator, Double Bass Seminar at the Boston Conservatory.  Mr. Levy's teachers have included David Potter, Todd Seeber, Timothy Pitts, Paul Ellison, and Stuart Sankey.

Jake Pitts: Jacob Mark "Jake" Pitts (born August 21, 1985) is an American musician and record producer best known as the lead guitarist of the rock band Black Veil Brides.

Glenn-Fowler Expedition: The Glenn-Fowler Expedition was an expedition to Santa Fe, New Mexico led by Hugh Glenn and Jacob Fowler to see if trading with the Spanish in that region was feasible.  The expedition was made up of 21 men.  They left their establishment on the Verdigris River in present-day Oklahoma on September 25, 1821 and arrived in Santa Fe in January 1822, and found that the Spanish authority in the region had been ended by the Mexican War of Independence.  The new Mexican government was quite happy to promote trade between Mexico and the United States.  The authorities gave the expedition to trap and hunt in the formerly Spanish lands.  The expedition members obtained nearly 1100 lbs of furs before they left the area on their return trip.  They returned home successfully, proving that trade with the Santa Fe area was feasible.  The profitable trip, along with the earlier trip of William Becknell, led to the establishment of the Santa Fe trail.

Question: Jacob Pitts starred in the movie Euro Trip as which character?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "movie_title": {
      "type": "string",
      "description": "The title of the movie the actor starred in."
    },
    "movie_release_year": {
      "type": "integer",
      "description": "The release year of the movie."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor in the movie."
    }
  },
  "required": [
    "actor_name",
    "movie_title",
    "movie_release_year",
    "character_name"
  ],
  "additionalProperties": false
}
