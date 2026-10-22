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
Christopher Denham: Christopher Denham , born Armando Alberto, is an American actor, film director, writer, and producer.  He directed "Home Movie" (2008) and is best known for his role in "Argo" (2012).

Home Movie (film): Home Movie is a 2008 horror film and is the directorial debut of actor Christopher Denham.

Highlander (franchise): Highlander is a film and television franchise that began with a 1986 fantasy movie starring Christopher Lambert, who played Connor MacLeod, the Highlander.  Born in Glenfinnan, in the Scottish Highlands in the 16th century, MacLeod is one of a number of Immortals.  There have been five "Highlander" movies, two television series, an animated series, an animated movie, an animated flash-movie series, ten original novels, nineteen comic book issues, and various licensed merchandise.

List of accolades received by Argo (2012 film): "Argo" is a 2012 political thriller directed by Ben Affleck, and produced by Grant Heslov, Affleck and George Clooney.  The screenplay by Chris Terrio was adapted from sections of the Central Intelligence Agency (CIA) operative Tony Mendez's memoir "The Master of Disguise: My Secret Life in the CIA", and the 2007 "Wired" article "The Great Escape" by Joshuah Bearman on the Canadian Caper.  The film stars Affleck as Mendez, who attempts to rescue six United States diplomats from Tehran, Iran, during the 1979–81 Iran hostage crisis by pretending that they are part of a film crew scouting the country for the filming of a fictitious science-fiction film, "Argo".  Bryan Cranston, Alan Arkin, and John Goodman feature in supporting roles.

Argo (2012 film): Argo is a 2012 American historical drama film directed by Ben Affleck.  Screenwriter Chris Terrio adapted the screenplay from the book by the U.S. Central Intelligence Agency operative Tony Mendez, "The Master of Disguise", and the

Gone Baby Gone: Gone Baby Gone is a 2007 American neo-noir mystery drama film directed by Ben Affleck.  In his feature-length directorial debut, Affleck cowrote the screenplay with Aaron Stockard based on the novel "Gone, Baby, Gone" by Dennis Lehane.  The film stars Casey Affleck and Michelle Monaghan as two private investigators hunting for a little girl who was abducted from the Boston neighborhood of Dorchester.  The supporting cast includes Morgan Freeman, Ed Harris and Amy Ryan.

Live by Night (film): Live by Night is a 2016 American crime drama film written, directed, co-produced by and starring Ben Affleck.  Based on the 2012 novel of the same name by Dennis Lehane, the film follows an Ybor City bootlegger (Affleck) who becomes a notorious gangster.  The film also stars Elle Fanning, Brendan Gleeson, Chris Messina, Sienna Miller, Zoe Saldana and Chris Cooper.

Sound of My Voice: Sound of My Voice is a 2011 American psychological thriller film directed by Zal Batmanglij and starring Christopher Denham, Nicole Vicius and Brit Marling.  The plot focuses on two documentary filmmakers who attempt to expose a cult led by a charismatic leader (Marling) who claims to be from the future.  The film was written by Batmanglij and Marling.  It premiered at the 2011 Sundance Film Festival.  It was also selected to close the 2011 SXSW Film Festival.  The film was released by Fox Searchlight Pictures on April 27, 2012.

Boiler Room (film): Boiler Room is a 2000 American crime drama film written and directed by Ben Younger, and starring Giovanni Ribisi, Vin Diesel, Nia Long, Ben Affleck, Nicky Katt, Scott Caan, Tom Everett Scott, Ron Rifkin and Jamie Kennedy.  Screenwriter Ben Younger interviewed for a job at brokerage firm Sterling Foster.  Younger said, "I walked in and immediately realized, 'This is my movie.'  I mean, you see these kids and know something is going on."

Preservation (2014 film): Preservation is a 2014 horror thriller film that was directed by Christopher Denham.  It had its world premiere on April 17, 2014 at the Tribeca Film Festival and stars Wrenn Schmidt as a woman trapped in a forest preserve, stalked by maniacs.

Question: Which movie starring Christopher Denham was directed by Ben Affleck in 2012?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the movie was released."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the movie's director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "starring_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor who starred in the movie."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres the movie belongs to."
    }
  },
  "required": [
    "movie_title",
    "release_year",
    "director",
    "starring_actor",
    "genres"
  ],
  "additionalProperties": false
}
