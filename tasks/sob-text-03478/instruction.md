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
Two-Faced Woman: Two-Faced Woman is a 1941 American romantic comedy film from Metro-Goldwyn-Mayer, directed by George Cukor and starring Greta Garbo in her final film role, Melvyn Douglas, and Constance Bennett.  Garbo plays a wife who pretends to be her own fictitious twin sister in order to recapture the affections of her estranged husband (Douglas), who has left her for a former girlfriend (Bennett).  The film is generally regarded as a box-office bomb and an unsuccessful attempt to "Americanize" Garbo in order to increase her United States fan base.  By mutual agreement, Garbo's contract with MGM was terminated shortly after "Two-Faced Woman" was released, and it became her last film.

Susan Lenox (Her Fall and Rise): Susan Lenox (Her Fall and Rise) is a 1931 American Pre-Code film starring Greta Garbo and Clark Gable, based on the novel by David Graham Phillips.  The film was made by Metro-Goldwyn-Mayer and was directed and produced by Robert Z. Leonard.  This was the only film in which Greta Garbo was paired with Clark Gable.  The notoriety of the novel alone was enough for British censors to ban it from release.  With a few cuts, it was finally approved in the UK with a new title: "The Rise of Helga".

A Woman's Secret: A Woman's Secret is a 1949 film noir directed by Nicholas Ray, and starred Maureen O'Hara, Gloria Grahame and Melvyn Douglas.  The film was based on the novel "Mortgage on Life" by Vicki Baum.

The Kiss (1929 film): The Kiss is a 1929 American silent drama film from Metro-Goldwyn-Mayer directed by Jacques Feyder and starring Greta Garbo, Conrad Nagel and Lew Ayres in his first feature film.  The film is known for being both MGM's and Greta Garbo's last silent film.  It was also the last such film for Conrad Nagel.  That said, the film did take advantage of the new sound technology, and was released with an orchestral score and sound effects.  It was based on an 1896 film.

A Woman of Affairs: A Woman of Affairs is a 1928 Metro-Goldwyn-Mayer drama film directed by Clarence Brown and starring Greta Garbo, John Gilbert, Douglas Fairbanks Jr. and Lewis Stone.  The film, released with a synchronized score and sound effects, was based on a 1924 best-selling novel by Michael Arlen, "The Green Hat", which he adapted as a four-act stage play in 1925.  "The Green Hat" was considered so daring in the United States that the movie did not allow any associations with it and was renamed "A Woman of Affairs", with the characters also renamed to mollify the censors.  In particular the film script eliminated all references to heroin use, homosexuality and syphilis that were at the core of the tragedies involved.

Mata Hari (1931 film): Mata Hari is a 1931 American Pre-Code Metro-Goldwyn-Mayer film loosely based on the life of Mata Hari, an exotic dancer and courtesan executed for espionage during World War I.  The film stars Greta Garbo in the title role.  It was Garbo's most commercially successful vehicle.  Only a censored version of the film is currently available.

Greta Garbo: Greta Garbo (born Greta Lovisa Gustafsson; ] ; 18 September 1905 – 15 April 1990), was a Swedish-born American film actress during the 1920s and 1930s.  Garbo was nominated three times for the Academy Award for Best Actress and received an Academy Honorary Award in 1954 for her "luminous and unforgettable screen performances."  In 1999, the American Film Institute ranked Garbo fifth on their list of the greatest female stars of classic Hollywood cinema, after Katharine Hepburn, Bette Davis, Audrey Hepburn, and Ingrid Bergman.

Ninotchka: Ninotchka is a 1939 American film made for Metro-Goldwyn-Mayer by producer and director Ernst Lubitsch which stars Greta Garbo and Melvyn Douglas.  It is written by Billy Wilder, Charles Brackett, and Walter Reisch, based on a screen story by Melchior Lengyel.  "Ninotchka" is Greta Garbo's first full comedy, and her penultimate film.  It is one of the first American movies which, under the cover of a satirical, light romance, depicted the Soviet Union under Joseph Stalin as being rigid and gray, in this instance comparing it with the free and sunny Parisian society of pre-war years.

Nils Asther: Nils Anton Alfhild Asther (17 January 1897 – 19 October 1981) was a Swedish actor active in Hollywood from 1926 to the mid-1950s, known for his beautiful face and often called "the male Greta Garbo".  Between 1916 and 1963 he appeared in over 70 feature films, 16 of which were produced in the silent era.  He didn't seek publicity, choosing instead to be alone.  He is mainly remembered today for two silent films he made with his fellow Swede, Greta Garbo, and the pre-code interracial love affair in "The Bitter Tea of General Yen".

Melvyn Douglas: Melvyn Douglas (born Melvyn Edouard Hesselberg, April 5, 1901 – August 4, 1981) was an American actor.  Douglas came to prominence in the 1930s as a suave leading man, perhaps best typified by his performance in the 1939 romantic comedy "Ninotchka" with Greta Garbo.  Douglas later played mature and fatherly characters, as in his Academy Award–winning performances in "Hud" (1963) and "Being There" (1979) and his Academy Award–nominated performance in "I Never Sang for My Father" (1970).

Question: A Woman's Secret co-starred the actor who played in which movie alongside Greta Garbo?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_from_womans_secret": {
      "type": "string",
      "description": "The actor who co-starred in 'A Woman's Secret' and also appeared in a film with Greta Garbo."
    },
    "garbo_co_star_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film where the identified actor co-starred with Greta Garbo."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "other_notable_co_star": {
          "type": "string",
          "description": "Another notable co-star in the film besides Greta Garbo and the identified actor."
        }
      },
      "required": [
        "title",
        "year",
        "director"
      ],
      "additionalProperties": false
    },
    "garbo_film_genre": {
      "type": "string",
      "description": "The genre of the Greta Garbo film, if specified."
    }
  },
  "required": [
    "actor_from_womans_secret",
    "garbo_co_star_film"
  ],
  "additionalProperties": false
}
