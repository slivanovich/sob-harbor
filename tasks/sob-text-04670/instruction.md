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
Superman Returns: Superman Returns is a 2006 American superhero film directed and produced by Bryan Singer.  It is based on the DC Comics character Superman and serves as an homage sequel to the motion pictures "Superman" (1978) and "Superman II" (1980), while ignoring the events of "Superman III" (1983) and "" (1987).  The film stars Brandon Routh as Clark Kent/Superman, Kate Bosworth as Lois Lane, Kevin Spacey as Lex Luthor, with James Marsden, Frank Langella, and Parker Posey.  The film tells the story of the title character returning to Earth after a five-year absence.  He finds that his love interest Lois Lane has moved on with her life, and that his archenemy Lex Luthor is plotting a scheme that will destroy Superman and the world.

Man of Steel (film): Man of Steel is a 2013 superhero film featuring the DC Comics character Superman.  It is a British-American venture produced by Legendary Pictures, DC Entertainment, Syncopy Inc., and Cruel and Unusual Films, and distributed by Warner Bros.  Pictures.  It is the first installment in the DC Extended Universe (DCEU).  The film is directed by Zack Snyder, written by David S. Goyer, and stars Henry Cavill, Amy Adams, Michael Shannon, Kevin Costner, Diane Lane, Laurence Fishburne, Antje Traue, Ayelet Zurer, Christopher Meloni, and Russell Crowe.  "Man of Steel" is a reboot of the "Superman" film series that retells the character's origin story.  In the film, Clark Kent learns that he is a superpowered alien from the planet Krypton and assumes the role of mankind's protector as Superman, but finds himself having to prevent General Zod from destroying humanity.

Superman II: Superman II is a 1980 British-American superhero film directed by Richard Lester, based on the DC Comics character Superman.  It is a sequel to the 1978 film "Superman" and stars Gene Hackman, Christopher Reeve, Terence Stamp, Ned Beatty, Sarah Douglas, Margot Kidder, and Jack O'Halloran.  The film was released in Australia and mainland Europe on December 4, 1980, and in other countries throughout 1981.  Selected premiere engagements of "Superman II" were presented in Megasound, a high-impact surround sound system similar to Sensurround.

Last Son (comics): "Last Son" is a five-issue comic book story arc featuring Superman in the monthly "Action Comics".  It is written by Geoff Johns and Richard Donner, the director of the well-known 1978 film "Superman: The Movie" and a portion of "", with pencils by Adam Kubert.  This story introduces the original character, Christopher Kent and adapts the classic Superman film villains, General Zod, Ursa and Non into the regular DC Universe continuity.

Superman (1978 film): Superman (informally titled Superman: The Movie in some listings and reference sources) is a 1978 superhero film directed by Richard Donner and based on the DC Comics character of the same name.  The film is a British, Swiss, Panamanian and American joint venture, produced by Warner Bros., Film Export A.G., Dovemead Limited and International Film Productions.  "Superman" features an ensemble cast of Marlon Brando, Gene Hackman, Christopher Reeve, Jeff East, Margot Kidder, Glenn Ford, Phyllis Thaxter, Jackie Cooper, Trevor Howard, Marc McClure, Terence Stamp, Valerie Perrine, Ned Beatty, Jack O'Halloran, Maria Schell, and Sarah Douglas.  The film depicts Superman's origin, including his infancy as Kal-El of Krypton and his youthful years in the rural town of Smallville.  Disguised as reporter Clark Kent, he adopts a mild-mannered disposition in Metropolis and develops a romance with Lois Lane, while battling the villainous Lex Luthor.

Superman IV: The Quest for Peace: Superman IV: The Quest for Peace is a 1987 American superhero film directed by Sidney J. Furie, based on the DC Comics character Superman.  It is the fourth and final film in the original "Superman" film series, and the first film in that series not to be produced by Alexander and Ilya Salkind, but rather by Golan-Globus' Cannon Films, in association with Warner Bros. Gene Hackman returned as Lex Luthor, who creates an evil solar-powered version of Superman called Nuclear Man.

Superman and the Legion of Super-Heroes: "Superman and the Legion of Super-Heroes" is a comic book story arc from DC Comics by Geoff Johns and Gary Frank, featuring the Superman character and the return of the pre-"Crisis on Infinite Earths" Legion of Super-Heroes.  Presented in "Action Comics" #858–863 (Late December 2007 – May 2008), this arc marked Geoff Johns' debut as a solo writer on "Action", having previously written alongside Kurt Busiek and Richard Donner.

Superman III: Superman III is a British-American 1983 superhero film directed by Richard Lester, based on the DC Comics character Superman.  It is the third film in the "Superman" film series and the last "Superman" film to be produced by Alexander Salkind and Ilya Salkind.  The film features a cast of Christopher Reeve, Richard Pryor, Annette O'Toole, Annie Ross, Pamela Stephenson, Robert Vaughn, Marc McClure, and Gavan O'Herlihy.  This film is followed by "", released on July 24, 1987.

Geoffrey Unsworth: Geoffrey Gilyard Unsworth, OBE, BSC (26 May 1914 – 28 October 1978) was a British cinematographer who worked on nearly 90 feature films spanning over more than 40 years.  He is best known for his work on films such as Stanley Kubrick's "", Bob Fosse's "Cabaret" and Richard Donner's "Superman".

Geoffrey Faithfull: Geoffrey Faithfull B.S.C., (28 January 1893 – 1 December 1979) was a British cinematographer who worked on more than 180 feature films from starting in the industry in the 1910s.  Faithfull also directed two films: "For You Alone" (1945) and "I'll Turn to You" (1946).  He worked on several films with Michael Powell and among his later work was responsible for the 1960 SF classic "Village of the Damned".

Question: Geoffrey Gilyard Unsworth, was a British cinematographer who worked on nearly 90 feature films spanning over more than 40 years, and is best known for his work on films such as Superman, released in which year, a film directed by Richard Donner and based on the DC Comics character of the same name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "cinematographer": {
      "type": "string",
      "description": "The cinematographer known for their work on the film."
    },
    "based_on_character_source": {
      "type": "string",
      "description": "The comic book publisher the character is based on."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "cinematographer",
    "based_on_character_source"
  ],
  "additionalProperties": false
}
