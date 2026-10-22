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
What we've got here is failure to communicate: The phrase "What we've got here is failure to communicate" is a quotation from the 1967 film "Cool Hand Luke", spoken in the movie first by Strother Martin (as the Captain, a prison warden) and later, abridged, by Paul Newman (as Luke, a stubborn prisoner).

Ed Lukowich: Edward R. "Ed" Lukowich (born March 1, 1946; nicknamed "Cool Hand Luke") is a former champion curler.  Lukowich is a two-time Brier champion, having won the Brier Tankard for Alberta as skip of both the 1978 and 1986 Canadian championship teams.  In 1986 his team also won the World Curling Championship.  In 1988, representing Canada at the Olympic Games while curling was a demonstration sport, his team placed third.

Strother Martin: Strother Douglas Martin, Jr. (March 26, 1919 – August 1, 1980) was an American character actor who often appeared in support of superstars John Wayne and Paul Newman and was memorable in western films directed by John Ford and Sam Peckinpah.  Martin perhaps is best known as the prison "captain" in the 1967 film "Cool Hand Luke", in which he uttered the famous line, "What we've got here is failure to communicate."  The line is number 11 on the American Film Institute list of AFI's 100 Years...100 Movie Quotes.

Lou Antonio: Lou Antonio (born January 23, 1934) is an American actor and TV director best known for performing in the films "Cool Hand Luke" and "America America".  He also starred in two short-lived TV series, "Dog and Cat", and "Makin' It".

Luke (French band): Luke is a French rock band.  The group was formed in Aquitaine in 1998 when Thomas Boulard joined the group "Spring", consisting of Christophe Plantier and François Jugé.  The band's name is derived from the American movie Cool Hand Luke.  In 1999, Luke composed a number of demos and a seven track CD.  That same year they signed with "Village Vert".  They released an EP titled "Je n'éclaire que moi".

The Flight of the Phoenix (1965 film): The Flight of the Phoenix is a 1965 American drama film starring James Stewart, produced and directed by Robert Aldrich, and based on the 1964 novel "The Flight of the Phoenix" by Elleston Trevor.  The story describes several men struggling to survive their aircraft's emergency landing in the Sahara Desert, and stars Richard Attenborough, Peter Finch, Hardy Krüger and Ernest Borgnine.  The ensemble cast includes Ian Bannen, Ronald Fraser, Christian Marquand, Dan Duryea and George Kennedy as other passengers on the aircraft.

Stuart Rosenberg: Stuart Rosenberg (August 11, 1927 – March 15, 2007) was an American film and television director whose motion pictures include "Cool Hand Luke" (1967), "Voyage of the Damned" (1976), "The Amityville Horror" (1979), and "The Pope of Greenwich Village" (1984).  He was noted for his work with actor Paul Newman.

George Kennedy: George Harris Kennedy Jr. (February 18, 1925 – February 28, 2016) was an American actor who appeared in more than 200 film and television productions.  He is best remembered for portraying "Dragline" opposite Paul Newman in "Cool Hand Luke" (1967), for which he won the Academy Award for Best Supporting Actor and was nominated for the corresponding Golden Globe.  He received a second Golden Globe nomination for portraying Joe Patroni in "Airport" (1970).

Paul Newman: Paul Leonard Newman (January 26, 1925 – September 26, 2008) was an American actor, film director, producer, race car driver, IndyCar owner, entrepreneur, activist, and philanthropist.  He won and was nominated for numerous awards, winning an Academy Award for his performance in the 1986 film "The Color of Money", a BAFTA Award, a Screen Actors Guild Award, a Cannes Film Festival Award, an Emmy Award, and many others.  Newman's other roles include the title characters in "The Hustler" (1961) and "Cool Hand Luke" (1967), as well as "Butch Cassidy and the Sundance Kid" (1969), as Butch Cassidy, "The Sting" (1973), and "The Verdict" (1982).  He also voiced Doc Hudson in the first installment of Disney-Pixar's "Cars", and received a posthumous credit for his voice recordings in "Cars 3" (2017).

Cool Hand Luke: Cool Hand Luke is a 1967 American prison drama film directed by Stuart Rosenberg, starring Paul Newman and featuring George Kennedy in an Oscar-winning performance.  Newman stars in the title role as Luke, a prisoner in a Florida prison camp who refuses to submit to the system.

Question: What actor, who starred in The Flight of the Phoenix, also starred in Cool Hand Luke?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in both films."
    },
    "films_starred_in": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the film titles the actor starred in, relevant to the question."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award won by the actor for one of the films."
        },
        "film_for_award": {
          "type": "string",
          "description": "The title of the film for which the award was received."
        },
        "award_category": {
          "type": "string",
          "description": "The category of the award (e.g., Best Supporting Actor)."
        }
      },
      "required": [
        "award_name",
        "film_for_award",
        "award_category"
      ],
      "additionalProperties": false,
      "description": "Details about an award won by the actor for one of the specified films."
    }
  },
  "required": [
    "actor_name",
    "films_starred_in"
  ],
  "additionalProperties": false
}
