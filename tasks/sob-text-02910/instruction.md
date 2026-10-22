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
The Best of Times (film): The Best of Times is a 1986 American comedy-drama film directed by Roger Spottiswoode and written by Ron Shelton.  It stars Robin Williams and Kurt Russell as two friends attempting to relive a high school football game.

Hollywood Homicide: Hollywood Homicide is a 2003 American action comedy film starring Harrison Ford, Josh Hartnett, Lena Olin, Bruce Greenwood, Isaiah Washington, Lolita Davidovich, Keith David, Gladys Knight, Master P, Dwight Yoakam, Martin Landau, and André Benjamin.  It was directed by Ron Shelton, written by Shelton and Robert Souza, and produced by Lou Pitt.  The film is based on the true experiences of Souza, who was a homicide detective in the LAPD Hollywood Division and moonlighted as a real estate broker in his final ten years on the job.

Bull Durham: Bull Durham is a 1988 American romantic comedy sports film.  It is partly based upon the minor-league baseball experiences of writer/director Ron Shelton and depicts the players and fans of the Durham Bulls, a minor-league baseball team in Durham, North Carolina.

Just Getting Started (film): Just Getting Started is an upcoming American action comedy film directed and written by Ron Shelton.  The film stars Morgan Freeman, Tommy Lee Jones, Rene Russo and Elizabeth Ashley.  It is scheduled for release by Broad Green Pictures on December 8, 2017.  This will mark the final film appearance of Glenne Headly, who died on June 8, 2017.

Blaze (1989 film): Blaze is a 1989 film written and directed by Ron Shelton.  Based on the 1974 memoir "Blaze Starr: My Life as Told to Huey Perry" by Blaze Starr and Huey Perry, the film stars Paul Newman as Earl Long and Lolita Davidovich as Blaze Starr, with Starr herself in a cameo appearance.

White Men Can't Jump: White Men Can't Jump is a 1992 American sports comedy film written and directed by Ron Shelton, starring Wesley Snipes and Woody Harrelson as streetball hustlers.  The film was released in the United States on March 27, 1992, by 20th Century Fox.

Ron Shelton: Ronald Wayne "Ron" Shelton (born September 15, 1945) is an American Oscar-nominated film director and screenwriter and former minor league baseball infielder.  Shelton is known for the many films he has made about sports.

Blue Chips: Blue Chips is a 1994 basketball drama film, directed by William Friedkin, written by Ron Shelton and starring Nick Nolte as a college coach and real-life basketball stars Shaquille O'Neal and Anfernee "Penny" Hardaway as talented finds.  It features cameos from noted basketball figures Bob Knight, Rick Pitino, Nolan Richardson, Bob Cousy, Larry Bird, Jerry Tarkanian, Matt Painter, Allan Houston, Dick Vitale, Jim Boeheim, Dan Dakich and Bobby Hurley, as well as actor Louis Gossett, Jr.

Khady Sylla: Khady Sylla (Dakar, March 27, 1963 – Dakar, October 8, 2013) was a Senegalese writer of two novels, short work, and film.

Dark Blue (film): Dark Blue is a 2002 film directed by Ron Shelton and starring Kurt Russell with Ving Rhames and Brendan Gleeson in supporting roles.  The film is based on a story written for film by crime novelist James Ellroy and takes place during the days leading up to and including the Rodney King trial verdict.

Question: While Ron Shelton is a film director, what is Khady Sylla?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "primary_profession": {
      "type": "string",
      "description": "The main profession of the person."
    },
    "number_of_novels_written": {
      "type": "integer",
      "description": "The number of novels written by the person."
    },
    "has_written_short_work": {
      "type": "boolean",
      "description": "Indicates if the person has written short work."
    },
    "has_worked_on_film": {
      "type": "boolean",
      "description": "Indicates if the person has worked on film."
    }
  },
  "required": [
    "person_name",
    "primary_profession",
    "number_of_novels_written",
    "has_written_short_work",
    "has_worked_on_film"
  ],
  "additionalProperties": false
}
