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
Under Fire (film): Under Fire is a 1983 American political thriller film set during the last days of the Nicaraguan Revolution that ended the Somoza regime in 1979 Nicaragua.  It stars Nick Nolte, Gene Hackman and Joanna Cassidy.  The musical score by Jerry Goldsmith, which featured well-known jazz guitarist Pat Metheny, was nominated for an Academy Award.  The editing by Mark Conte and John Bloom was nominated for a BAFTA Award for Best Editing. The Film was shot in the Mexican states of Chiapas and Oaxaca.

Who Framed Roger Rabbit: Who Framed Roger Rabbit is a 1988 American live-action/animated fantasy film directed by Robert Zemeckis, produced by Frank Marshall and Robert Watts, and written by Jeffrey Price and Peter S. Seaman.  The film is based on Gary K. Wolf's 1981 novel "Who Censored Roger Rabbit? " The film stars Bob Hoskins, Christopher Lloyd, Charles Fleischer, Stubby Kaye, and Joanna Cassidy.  Combining live-action and animation, the film is set in Hollywood during the late 1940s, where animated characters and people co-exist.  The story follows Eddie Valiant, a private detective who must exonerate "Toon" Roger Rabbit, who is accused of murdering a wealthy businessman.

Vampire in Brooklyn: Vampire in Brooklyn (also known as Wes Craven's Vampire in Brooklyn) is a 1995 American comedy horror film directed by Wes Craven.  Eddie Murphy, who also produced and stars in the film, wrote the film's script, alongside Vernon Lynch and Murphy's older brother Charles Q. Murphy.  "Vampire in Brooklyn" co-stars Angela Bassett, Allen Payne, Kadeem Hardison, John Witherspoon, Zakes Mokae, and Joanna Cassidy.  Murphy also plays an alcoholic preacher and a foul-mouthed Italian gangster.  The film was released in the United States on October 27, 1995.  Despite negative reviews, the film became a cult film among fans.

Buffalo Bill (TV series): Buffalo Bill is an American television sitcom that featured the misadventures of an egotistical talk show host, played by Dabney Coleman and his staff (including Geena Davis and Joanna Cassidy) at WBFL-TV, a small TV station in Buffalo, New York.  It premiered June 1, 1983 on NBC and ran for two seasons (1983–84).  It was also shown on the then-new UK fourth TV channel Channel 4.

The Package (1989 film): The Package is a 1989 political thriller film directed by Andrew Davis and starring Gene Hackman, Joanna Cassidy and Tommy Lee Jones.  Set during the Cold War, the film portrays an assassination conspiracy within both the U.S. and Soviet militaries.  The Americans and Soviets are about to sign a disarmament treaty to completely eliminate nuclear weapons, but elements within each country's military are vehemently opposed to such a plan and determined to stop it at all costs.  Roger Ebert awarded the film three stars out of four, calling it "smarter than most thrillers".

Kathaa Animations: Kathaa Animations, is an Indian Animation Studio, aimed at developing original content for the Indian as well as Global audiences.  It is best known for the creation of the Animated Characters Hum Tum for the film Hum Tum.  Hum Tum was one of the most successful animated characters to be used in mainstream Bollywood film. 

Ghosts of Mars: Ghosts of Mars is a 2001 American science fiction action horror film written, directed and with music by John Carpenter.  The film stars Ice Cube, Natasha Henstridge, Jason Statham, Pam Grier, Clea DuVall, and Joanna Cassidy.  The film received negative reviews and was a box office bomb, scoring just a 21% rating on Rotten Tomatoes and earning $14 million at the box office, against a $28 million production budget.

The Late Show (film): The Late Show is a 1977 American neo-noir mystery film written and directed by Robert Benton and produced by Robert Altman.  It stars Art Carney, Lily Tomlin, Bill Macy, Eugene Roche, and Joanna Cassidy.

Minna Haapkylä: Minna-Maria Erika Haapkylä (born 10 June 1973 in Helsinki) is a Finnish actress.  She has won two Jussi Awards; one for the best actress in a supporting role for a 1999 Veikko Aaltonen film "Rakkaudella Maire", and another in 2009 for the best actress in a leading role for "Kuulustelu", directed by Jörn Donner.  Haapkylä was married to actor Hannu-Pekka Björkman from 2002 to 2014.  They have two sons.She is now in a relationship with actress Joanna Haartti having come out as gay.

Joanna Cassidy: Joanna Cassidy (born August 2, 1945) is an American actress.  She is best known for her roles as the replicant Zhora Salome in Ridley Scott's film "Blade Runner" (1982) and Dolores in "Who Framed Roger Rabbit" (1988).  She has won a Golden Globe Award, was nominated for three Emmy Awards and also was nominated for a Saturn Award and Screen Actors Guild Awards.

Question: Who did the actress Joanna Cassidy play in the film that featured Hollywood during the late 1940s, where animated characters and people co-exist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_setting_description": {
      "type": "string",
      "description": "A description of the film's setting."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actress in the film."
    }
  },
  "required": [
    "actress_name",
    "film_title",
    "film_release_year",
    "film_setting_description",
    "character_played"
  ],
  "additionalProperties": false
}
