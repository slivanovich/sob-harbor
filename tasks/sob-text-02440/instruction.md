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
The Black Panthers: Vanguard of the Revolution: The Black Panthers: Vanguard of the Revolution is a 2015 American documentary film directed and written by Stanley Nelson Jr. The film combines archival footage and interviews with surviving Panthers and FBI agents to tell the story of the revolutionary black organization Black Panther Party.  It is Nelson Jr.'s eighth film to premiere at Sundance.  The film was pitched at Sheffield Doc/Fest's MeetMarket in 2014 and is the first of a three-part series of documentary films about African-American history "America Revisited".  It will be followed by "Tell Them We Are Rising: The Story of Historically Black Colleges and Universities" and "The Slave Trade: Creating a New World".

They Were Not Silent: They Were Not Silent is a documentary about the Jewish Labor Committee's anti-Nazi movement in America before, during and after World War II.  The film features rare archival footage and photographs along with interviews with labor veterans, Holocaust survivors and scholars.  It explores how international Jewry worked to help Jews and non-Jews in Germany, Poland, and elsewhere in Europe.  The JLC's role has changed over the years.  A trade unionist who has focused on JLC history, Kenneth Burt, says he hopes that the documentary will encourage new interest in the organization.

The Sixth Battalion: The Sixth Battalion is a 1998 documentary film that examines the history of Jewish soldiers who fought for the Slovak Republic, which was closely aligned with Nazi Germany during World War II.  The documentary combines interviews with archival footage and photographs of the Slovak Republic in order to provide a brief history of the state, exploring the rise of antisemitism and how it affected these Jewish soldiers.

Nancy Kates: Nancy Kates is an independent filmmaker based in the San Francisco Bay Area.  She directed "Regarding Susan Sontag", a feature documentary about the late essayist, novelist, director and activist.  Through archival footage, interviews, still photographs and images from popular culture, the film reflects the boldness of Sontag’s work and the cultural importance of her thought, and received funding from the National Endowment for the Humanities, the National Endowment for the Arts, the Foundation for Jewish Culture and the Sundance Documentary Film Program.

Roots of the Cuban Missile Crisis: Roots of the Cuban Missile Crisis is a 48-minute 2001 Cold War documentary by New Line Home Video with "film footage from the era [and] newly created interviews covering U.S./Soviet relations from post-WWII Europe through the end of the crisis".  The documentary is a ""Beyond the Movie" feature" on the infinifilm DVD for the movie "Thirteen Days" and synthesizes archival footage and still photography, interviews, "Trinity and Beyond" documentary scenes, and "Thirteen Days" movie scenes and sequences (many with archival footage).

Patrick Montgomery: Patrick Montgomery is an American documentary producer/director and film and photo archivist.  He has specialized in making films using archival materials, most notably "The Man You Loved to Hate" (1979) about the legendary actor/director Erich Von Stroheim and "The Compleat Beatles" (1982) a two-hour documentary about the rise and fall of the world's most famous rock group.  He also founded and ran Archive Films/Archive Photos, the largest independent commercial film and photo archive in the U.S. until its acquisition by The Image Bank, a division of Eastman Kodak, in 1997.

Ken Burns: Kenneth Lauren "Ken" Burns (born July 29, 1953) is an American filmmaker, known for his style of using archival footage and photographs in documentary films.  His most widely known documentaries are "The Civil War" (1990), "Baseball" (1994), "Jazz" (2001), "The War" (2007), "" (2009), "Prohibition" (2011), "The Central Park Five" (2012), "The Roosevelts" (2014), and "The Vietnam War" (2017).  He was also executive producer of both "The West" (1996, directed by Stephen Ives), and "Cancer: The Emperor of All Maladies" (2015, directed by Barak Goodman).

The First Measured Century: The First Measured Century: The Other Way of Looking at American History is a three-hour PBS documentary film hosted by Ben J. Wattenberg.  The film was produced for PBS by BJW, Inc. and New River Media, Inc. and was first broadcast in December 2000.  The film traces American history during the 20th century through a sequence of vignettes of pioneering social scientists who used numerical tools to examine America.  The film mixes archival footage, archival still photography and artwork, interviews with contemporary experts, graphical animations of statistical trends, and on-camera narrative appearances by the host.  Information from Middletown IV, a 1999 replication of Middletown studies of Muncie, Indiana first begun by Robert and Helen Lynd in 1924, is included in the film and companion volume.

Jazz (TV series): Jazz is a 2000 documentary miniseries, directed by Ken Burns.  It was broadcast on PBS in 2001, and was released on DVD and VHS on January 2, 2001 by the same company.  Its chronological and thematic episodes provided a history of jazz, emphasizing innovative composers and musicians and American history.  Swing musicians Louis Armstrong and Duke Ellington are the central figures.  Several episodes discussed the later contributions of Charlie Parker and Dizzy Gillespie to bebop, and of Miles Davis, Ornette Coleman, and John Coltrane to free and cool jazz.  Nine episodes surveyed forty-five years (1917–1961), leaving the final episode to cover forty years (1961–2001).  The documentary examines the impacts of racial segregation and drugs on jazz.

Dial H-I-S-T-O-R-Y: Dial H-I-S-T-O-R-Y, a 68-minute-long film by director Johan Grimonprez, traces the history of airplane hijacking as portrayed by mainstream television media.  The film premiered in 1997 at the Musée National d'Art Moderne (Centre Georges Pompidou (Paris); and at Catherine David's curated Documenta X(Kassel).  "This study in pre-Sept.  11 terrorism" is composed of archival footage material — interspersing reportage shots, clips from science fiction films, found footage, home video and reconstituted scenes.  The work is interspersed with passages from Don DeLillo's novels "Mao II" and "White Noise", "providing a literary and philosophic anchor to the film".  According to the director, "Dial H-I-S-T-O-R-Y's narrative is based on an imagined dialogue between a terrorist and a novelist where the writer contends that the terrorist has hijacked his role within society."  The film's opening line, taken from "Mao II", introduces the skyjacker as protagonist.  Interspersing fact and fiction, Grimonprez said that the use of archival footage to create "short-circuits in order to critique a situation" may be understood as a form of a Situationist Détournement.

Question: Jazz is a 2000 documentary miniseries, directed by which American filmmaker, known for his style of using archival footage and photographs in documentary films?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentary_title": {
      "type": "string",
      "description": "The title of the documentary miniseries."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the director."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the director."
        },
        "known_for_style": {
          "type": "string",
          "description": "A description of the director's known filmmaking style."
        }
      },
      "required": [
        "name",
        "nationality",
        "known_for_style"
      ],
      "additionalProperties": false
    },
    "release_year": {
      "type": "integer",
      "description": "The year the documentary miniseries was released."
    }
  },
  "required": [
    "documentary_title",
    "director",
    "release_year"
  ],
  "additionalProperties": false
}
