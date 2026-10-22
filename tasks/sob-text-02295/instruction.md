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
IZombie (TV series): iZombie (stylized as iZOMBiE) is an American television series developed by Rob Thomas and Diane Ruggiero-Wright for The CW.  It is a loose adaptation of the comic book series of the same name created by Chris Roberson and Michael Allred, and published by DC Comics under their Vertigo imprint.  The series premiered on March 17, 2015.

Veronica Mars: Veronica Mars is an American teen noir mystery drama television series created by screenwriter Rob Thomas.  The series is set in the fictional town of Neptune, California, and stars Kristen Bell as the eponymous character.  The series premiered on September 22, 2004, during television network UPN's final two years, and ended on May 22, 2007, after a season on UPN's successor, The CW, airing for three seasons total.  "Veronica Mars" was produced by Warner Bros.  Television, Silver Pictures Television, Stu Segall Productions, and Rob Thomas Productions.  Joel Silver and Rob Thomas were executive producers for the entire run of the series, while Diane Ruggiero was promoted in the third season.

Veronica Mars (season 3): The third and final season of "Veronica Mars", an American drama television series created by Rob Thomas, began airing on The CW in the United States on October 3, 2006.  The season was produced by Warner Bros.  Television, Silver Pictures Television, Stu Segall Productions, Inc and Rob Thomas Productions, and Joel Silver, Diane Ruggiero and Thomas served as executive producers.  The third season comprises 20 episodes and concluded its initial airing on May 22, 2007.

List of iZombie episodes: "iZombie" (stylized as "iZOMBiE") is an American television series developed by Rob Thomas and Diane Ruggiero-Wright for The CW, and is a loose adaptation of the comic book series of the same name created by Chris Roberson and Michael Allred, and published by DC Comics under their Vertigo imprint.  The series was officially picked up on May 8, 2014, for the 2014–15 season and premiered on March 17, 2015.

List of iZombie characters: "iZombie" (stylized as "iZOMBiE") is an American television series developed by Rob Thomas and Diane Ruggiero-Wright for The CW.  It is a loose adaptation of the comic book series of the same name created by Chris Roberson and Michael Allred, and published by DC Comics under their Vertigo imprint.  The series premiered on March 17, 2015.

Mercy Malick: Mercy Malick is an American actor, singer/songwriter, writer, director, choreographer and aerialist.  She is best known for Mission Control, Major Crimes, Circle, and iZombie.

Veronica Mars (season 2): The second season of "Veronica Mars", an American drama television series created by Rob Thomas, premiered on UPN in the United States on September 28, 2005.  The series was produced by Warner Bros.  Television, Silver Pictures Television and Rob Thomas Productions, and Joel Silver and Thomas served as the executive producers.

Diane Ruggiero: Diane Ruggiero-Wright is an American television writer and producer.  Her credits include "That's Life", "Veronica Mars", "Free Agents", "Dirty Sexy Money", "Big Shots", the "Mythological X" remake "The Ex List" and "iZombie", which she co-created with Rob Thomas.  With Thomas, she also co-wrote the script for the "Veronica Mars" film.

Veronica Mars (character): Veronica Mars is the fictional protagonist, occasional narrator (through voiceovers), and antiheroine of the American television series "Veronica Mars", which aired on UPN from 2004 to 2006 and on The CW from 2006 to 2007.  The character was portrayed by Kristen Bell through the duration of the series.  Following the show's cancellation, Bell reprised the role in the 2014 film continuation.  The character, created by Rob Thomas, was originally male and the protagonist of his unproduced novel "Untitled Rob Thomas Teen Detective Novel", which eventually became the basis of the series.  After the work's transition from novel to television series, Thomas changed the character's gender from male to female as he believed a noir piece told from a female point of view would be more interesting.

Circle (2015 film): Circle is a 2015 American psychological thriller film written and directed by Aaron Hann and Mario Miscione.  It stars an ensemble cast that includes Carter Jenkins, Lawrence Kao, Allegra Masters, Michael Nardelli, Julie Benz, Mercy Malick, Lisa Pelikan, and Cesar Garcia.  It was inspired by the 1957 drama "12 Angry Men" and was shot in 2014.  It premiered at the Seattle International Film Festival on May 28, 2015, before being released to video-on-demand on October 16, 2015.  In the film, fifty people wake up in a darkened room, only to find that one of them is killed every two minutes or when they attempt to leave.  When they realize that they can control which person is selected to die, blocs emerge based on personal values.

Question:  Mercy Malick is best known for Mission Control, Major Crimes, Circle, and iZombie, an American television series developed by Rob Thomas and Diane Ruggiero-Wright for what television network?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_title": {
      "type": "string",
      "description": "The title of the television series."
    },
    "developers": {
      "type": "array",
      "description": "A list of individuals who developed the series.",
      "items": {
        "type": "string"
      }
    },
    "television_network": {
      "type": "string",
      "description": "The television network for which the series was developed."
    }
  },
  "required": [
    "series_title",
    "developers",
    "television_network"
  ],
  "additionalProperties": false
}
