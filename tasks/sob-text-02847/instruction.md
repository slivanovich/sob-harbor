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
Patriots Day (film): Patriots Day is a 2016 American action-drama film about the 2013 Boston Marathon bombing and the subsequent terrorist manhunt.  Directed by Peter Berg and written by Berg, Matt Cook and Joshua Zetumer, the film is based on the book "Boston Strong" by Casey Sherman and Dave Wedge.  It stars Mark Wahlberg, J. K. Simmons, John Goodman, Kevin Bacon and Michelle Monaghan.

The Fighter: The Fighter is a 2010 American biographical sports drama film directed by David O. Russell, and starring Mark Wahlberg (who also co-produced), Christian Bale, Amy Adams and Melissa Leo.  The film centers on the lives of professional boxer Micky Ward (Wahlberg) and his older half-brother Dicky Eklund (Bale).  Adams plays as Micky's girlfriend Charlene Fleming and Leo portrays Micky and Dicky's mother, Alice Eklund-Ward.  The film was inspired by the 1995 documentary that features the Eklund-Ward family, titled "".

Transformers: The Last Knight: Transformers: The Last Knight is a 2017 American science fiction action film based on the "Transformers" toy line created by Hasbro.  It is the fifth installment of the live-action "Transformers" film series, the second film in the sequel trilogy and the sequel to 2014's "".  Like its predecessors, the film is directed by Michael Bay, featuring Mark Wahlberg returning from "Age of Extinction", with Josh Duhamel, John Turturro, and Glenn Morshower all reprising their roles from the first , with Laura Haddock and Anthony Hopkins both joining the cast.  Bay and Wahlberg have stated they will not return for another sequel.

Mark Wahlberg: Mark Robert Michael Wahlberg (born June 5, 1971) is an American actor, producer, businessman, former model, and former rapper.  Wahlberg was known as Marky Mark in his early career as frontman for the group Marky Mark and the Funky Bunch, releasing the albums "Music for the People" and "You Gotta Believe".  Wahlberg later transitioned to acting, appearing in films such as the drama "Boogie Nights" and the satirical war comedy-drama "Three Kings" during the 1990s.  In the 2000s, he starred in the biographical disaster drama "The Perfect Storm", the science fiction film "Planet of the Apes", the heist film "The Italian Job", and the Martin Scorsese-directed neo-noir crime drama "The Departed", for which he received an Academy Award nomination for Best Supporting Actor.  In the 2010s, he starred in the action comedy "The Other Guys" alongside Will Ferrell, the biographical sports drama "The Fighter" (for which he earned an Academy Award nomination as a producer for Best Picture), the comedy "Ted", the war film "Lone Survivor", the crime comedy "Pain & Gain", the science fiction action film "" and the sequel "", the comedy "Daddy's Home", the disaster film "Deepwater Horizon", and the thriller "Patriots Day".

Daniel Van Kirk: Daniel Van Kirk (born Daniel Nall) is an American comedian, podcast personality, and writer from Rochelle, Illinois.  He earned his Bachelor of Fine Arts in theater performance from Roosevelt University.  He appears as himself and as comedic caricatures on several podcasts such as "Sklarbro Country" with Randy and Jason Sklar as a regular, "The Bear Down Podcast" and "The Todd Glass Show" as well as hosting "Hindsight with Daniel Van Kirk" on the Steve Dahl Network.  Van Kirk has appeared on Doug Benson's podcast, "Doug Loves Movies", in character as Mark Wahlberg.  A mini-game on the podcast is "Doing Lines with Mark", in which Van Kirk - either in person or via recording - will recite a film quote as Wahlberg; and a contestant must name the film where the quote is taken from.  Van Kirk has also appeared on the podcast in character as Steven Seagal.

Stop It Girl: "Stop It Girl" is a 1986 single from New Kids on the Block, with lead vocals by Donnie Wahlberg, Joey McIntyre, and an intro rap by who some believe to be Donnie Wahlberg's younger brother Mark Wahlberg.  Others believe it to be Joey, but no one is quite sure.  Written and produced by Maurice Starr, it was the second release from their debut album "New Kids on the Block".  The songs hook is inspired by, and interpolates, "One Bad Apple" by The Osmonds.

Paul Thomas Anderson filmography: American director, screenwriter, and producer Paul Thomas Anderson has directed seven feature-length films, five short films, twelve music videos, one documentary, one television episode as a guest segment director, and one theatrical play.  He made his directorial debut with the mockumentary short film "The Dirk Diggler Story" (1988), at the age of 18, about a pornographic actor in the 1970s.  Anderson followed it five years later with another short film, "Cigarettes & Coffee" in 1993.  In 1996, Anderson wrote and directed the neo-noir crime thriller "Hard Eight", starring Philip Baker Hall, John C. Reilly, Gwyneth Paltrow, and Samuel L. Jackson.  The film was well received, with film critic Roger Ebert saying of it in his review, "Movies like "Hard Eight" remind me of what original, compelling characters the movies can sometimes give us."  Using the basis of "The Dirk Diggler Story", Anderson wrote and directed an expansion of the film entitled "Boogie Nights" in 1997.  The film starred Mark Wahlberg as Eddie Adams/"Dirk Diggler" during the Golden Age of Porn in the 1970s and his eventual downfall in the 1980s.  "Boogie Nights" received acclaim from critics and was a commercial success; at the 70th Academy Awards ceremony, the film was nominated for three Academy Awards, including for Best Supporting Actor (Burt Reynolds), Best Supporting Actress (Julianne Moore) and Best Original Screenplay.

We Own the Night (film): We Own the Night is a 2007 American crime drama film written and directed by James Gray and starring Joaquin Phoenix, Mark Wahlberg, Eva Mendes and Robert Duvall.  It is the third film directed by Gray, and the second to feature Phoenix and Wahlberg together, the first being "The Yards".  The title comes from the motto of the NYPD's Street Crimes Unit, which disbanded in 2002.

Contraband (2012 film): Contraband is a 2012 American crime thriller film directed by Baltasar Kormákur, starring Mark Wahlberg, Kate Beckinsale, Ben Foster, Caleb Landry Jones, Giovanni Ribisi, Lukas Haas, Diego Luna and J. K. Simmons.  The film is a remake of the 2008 Icelandic film "Reykjavík-Rotterdam" which Baltasar Kormákur starred in.  It was released on January 13, 2012 in the United States by Universal Pictures.

Marky Mark and the Funky Bunch: Marky Mark and the Funky Bunch was an American hip-hop group led by Mark Wahlberg.  The Funky Bunch consisted of Wahlberg (alias Marky Mark), Scott Ross (alias Scottie Gee), Hector Barros (alias Hector the Booty Inspector), Terry Yancey (alias DJ-T), and Anthony Thomas (alias Ashey Ace).  The group's best known song is "Good Vibrations", which made it to number one on the "Billboard" Hot 100 in 1991.

Question: Mark Wahlberg starred in a thriller about what event in American history?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film Mark Wahlberg starred in."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "historical_event": {
      "type": "string",
      "description": "The American historical event the film is about."
    },
    "event_year": {
      "type": "integer",
      "description": "The year the historical event took place."
    }
  },
  "required": [
    "film_title",
    "film_genre",
    "historical_event",
    "event_year"
  ],
  "additionalProperties": false
}
