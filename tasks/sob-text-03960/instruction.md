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
Breaking In (2018 film): Breaking In is an upcoming thriller film directed by James McTeigue and starring Gabrielle Union.  Union is also set to produce the film alongside Will Packer, James Lopez, Craig Perry and Sheila Taylor.

ITV at the Movies: ITV at the Movies was a weekly British television film review show broadcast on ITV2, originally presented by Giles Vickers-Jones.  The final series was presented by James King and was produced and directed by Richard Leyland.  The show was replaced in 2011 by "The Movie Show on ITV2".

Ninja Assassin: Ninja Assassin is a 2009 German-American neo-noir martial arts thriller film directed by James McTeigue.  The story was written by Matthew Sand, with a screenplay by J. Michael Straczynski.  The film stars South Korean pop musician Rain as a disillusioned assassin looking for retribution against his former mentor, played by ninja film legend Sho Kosugi.  "Ninja Assassin" explores political corruption, child endangerment and the impact of violence.  Known for their previous work on the "Matrix Trilogy" and "V for Vendetta", Lana and Lilly Wachowski, Joel Silver, and Grant Hill produced the film.  A collective effort to commit to the film's production was made by Legendary Pictures, Dark Castle Entertainment and Silver Pictures.  It was distributed by Warner Bros.  Pictures.

Assistant director: The role of an assistant director on a film includes tracking daily progress against the filming production schedule, arranging logistics, preparing daily call sheets, checking cast and crew, and maintaining order on the set.  They also have to take care of the health and safety of the crew.  The role of an assistant to the director is often confused with assistant director but the responsibilities are entirely different.  The assistant to the director manages all of the Director's in development, pre-production, while on set, through post-production and is often involved in both personal management as well as creative aspects of the production process.  Historically, assistant to director was a stepping stone to directing work; Alfred Hitchcock was an AD, as was James McTeigue.  This transition into film directing is no longer common in feature films.  It is more common now for an assistant to the director to transition to a production management or producer role than to directing.

Survivor (film): Survivor is a 2015 British-American spy thriller film directed by James McTeigue and written by Philip Shelby.  The film stars Milla Jovovich, Pierce Brosnan and Dylan McDermott.

James McTeigue: James McTeigue (born 29 December 1967) is an Australian film director.  He has been an assistant director on many films, including "Dark City" (1998), the "Matrix trilogy" (1999–2003) and "" (2002), and made his directorial debut with the 2006 film "V for Vendetta" to critical acclaim.  Since "Vendetta" he has collaborated with the Wachowskis an additional three times as director on "The Invasion" (albeit uncredited), "Ninja Assassin" and "Sense8".

The Invasion (film): The Invasion is a 2007 science fiction horror thriller film starring Nicole Kidman and Daniel Craig, directed by Oliver Hirschbiegel, with additional scenes written by The Wachowskis and directed by James McTeigue.

V for Vendetta (film): V for Vendetta is a 2005 dystopian political thriller film directed by James McTeigue and written by The Wachowskis, based on the 1988 DC/Vertigo Comics limited series of the same name by Alan Moore and David Lloyd.  The film is set in an alternative future where a neo-fascist regime has subjugated the United Kingdom.  Hugo Weaving portrays V, an anarchist freedom fighter who attempts to ignite a revolution through elaborate terrorist acts and Natalie Portman plays Evey, a young, working-class woman caught up in V's mission, while Stephen Rea portrays the detective leading a desperate quest to stop V.

The Raven (2012 film): The Raven is a 2012 American psychological crime thriller film directed by James McTeigue, produced by Marc D. Evans, Trevor Macy and Aaron Ryder and written by Ben Livingston and Hannah Shakespeare.  It stars John Cusack, Alice Eve, Brendan Gleeson and Luke Evans.

Selina Giles: Selina Giles (born March 5, 1972) is an English actress and writer.  She is best known for playing Valerie Stowe in "Until Death" with Jean-Claude Van Damme and Stephen Rea and Evey's mother in the Wachowskis "V for Vendetta (film)"

Question: What movie was Salina Giles in that was directed by James McTeigue?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "director": {
      "type": "string",
      "description": "The director of the movie."
    },
    "actor": {
      "type": "string",
      "description": "The actor in the movie."
    },
    "role_played": {
      "type": "string",
      "description": "The role played by the actor in the movie."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    }
  },
  "required": [
    "movie_title",
    "director",
    "actor",
    "role_played",
    "film_year"
  ],
  "additionalProperties": false
}
