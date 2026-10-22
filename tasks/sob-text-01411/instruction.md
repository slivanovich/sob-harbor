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
Sam Freed: Sam Freed (born August 29, 1948) is an American actor who has performed on Broadway and television and in movies.  His first major regular role on television was as Bob Barsky in the last three seasons of "Kate & Allie".  In the short-lived series "Ferris Bueller", he played Bill Bueller, the father of the title character.  He also portrayed James C. Whiting III, the executive editor of "The Baltimore Sun", in the fifth and final season of "The Wire".  He is married to actress Barrie Youngfellow, who co-starred in the 1980s ABC-TV/syndicated sitcom series "It's a Living".

Parker Lewis Can't Lose: Parker Lewis Can't Lose is an American teen sitcom that originally aired on FOX from September 1990 to June 1993.  During the last season, the series sported the simpler title Parker Lewis.  The series was produced by Columbia Pictures Television and was strongly influenced by the feature film "Ferris Bueller's Day Off".  In competition, NBC debuted the film's TV spinoff "Ferris Bueller", but it only lasted 13 episodes, even though it aired during the same month as "Parker Lewis".

Alan Ruck: Alan Douglas Ruck (born July 1, 1956) is an American actor.  He played Cameron Frye, Ferris Bueller's hypochondriac best friend in John Hughes' "Ferris Bueller's Day Off" (1986), and Stuart Bondek, the lecherous, power-hungry member of the mayor's staff in the ABC sitcom "Spin City".  His other notable films include "Bad Boys" (1983), "Three Fugitives" (1989), "Young Guns II" (1990), "Speed" (1994), "Twister" (1996), and "Kickin' It Old Skool" (2007).  In 2016, he co-starred with Geena Davis in an updated Fox TV adaptation of William Peter Blatty's best-selling novel "The Exorcist."

Ferris Bueller (TV series): Ferris Bueller is an American sitcom based on the 1986 John Hughes film "Ferris Bueller's Day Off".  The show stars Charlie Schlatter in the title role.  The series debuted on August 23, 1990, on NBC and was cancelled within its first season, a few months after its debut.  The show was produced by Paramount Television.  Hughes was not involved in the show's production.

Stephanie Blake: Stephanie Blake is an American burlesque performer and actress.  She is known for playing the role of the nurse who came to Ferris' house in "Ferris Bueller's Day Off".

John Hughes (filmmaker): John Wilden Hughes Jr. (February 18, 1950 – August 6, 2009) was an American film director, producer, and screenwriter.  He directed and/or scripted some of the most successful comedy films of the 1980s and early 1990s including the comedy "National Lampoon's Vacation" (1983), the coming-of-age comedy "Sixteen Candles" (1984), the teen sci-fi comedy "Weird Science" (1985), the coming-of-age comedy-drama "The Breakfast Club" (1985), the coming-of-age comedy "Ferris Bueller's Day Off" (1986), the romantic comedy-drama "Pretty in Pink" (1986), the romance "Some Kind of Wonderful" (1987), the comedies "Planes, Trains and Automobiles" (1987) and "Uncle Buck" (1989), the Christmas family comedy "Home Alone" (1990) and its sequel, "" (1992).

Ferris Bueller's Day Off: Ferris Bueller's Day Off is a 1986 American teen comedy film written, co-produced and directed by John Hughes, and co-produced by Tom Jacobson.  The film stars Matthew Broderick as Ferris Bueller, a high-school slacker who spends a day off from school, with Mia Sara and Alan Ruck.  Ferris regularly "breaks the fourth wall" to explain techniques and inner thoughts.

Matthew Broderick: Matthew Broderick (born March 21, 1962) is an American actor and singer.  His roles include the title character in "Ferris Bueller's Day Off" (1986) for which he earned a Golden Globe nomination for Best Actor – Motion Picture Musical or Comedy, the adult voice of Simba in Disney's "The Lion King" trilogy (1994–2004), David Lightman in the Cold War thriller "WarGames" (1983), and Leo Bloom in the Broadway production of "The Producers".

Brandon Douglas: Brandon Douglas (born June 21, 1968) is an American actor.  He first came to prominence in the television series "Falcon Crest", in which he played Ben Agretti during the 1988–1989 season.  He is best known for playing Wayne Jones in the hit CBS TV series Northern Exposure.  He is also well known for playing Dr. Andrew Cook in the popular CBS series "Dr. Quinn, Medicine Woman".  Other credits include: "21 Jump Street", "Northern Exposure", "Matlock", "Murder, She Wrote", and "JAG".  He also costarred as Cameron Frye in the short-lived sitcom "Ferris Bueller".

Danke Schoen: "Danke Schoen" is a 1962 song first recorded by Bert Kaempfert.  It gained its fame in 1963 when American singer Wayne Newton recorded his version of it.  It regained fame when it was featured in the 1986 American comedy film "Ferris Bueller's Day Off", lip synced by the main character, Ferris Bueller (Matthew Broderick).  The music was composed by Bert Kaempfert, with the German lyrics written by Kurt Schwabach and the English lyrics by Milt Gabler.  The melody was originally released without lyrics under the title "Candlelight Cafe".

Question: Alan Douglas Ruck, is an American actor, he played Cameron Frye, Bueller's hypochondriac best friend in John Hughes' "Ferris Bueller's Day Off", released in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    }
  },
  "required": [
    "actor_name",
    "character_played",
    "film_title",
    "release_year"
  ],
  "additionalProperties": false
}
