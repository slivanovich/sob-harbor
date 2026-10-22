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
Lost in Panic Room: Lost in Panic Room is a 2010 Chinese suspense thriller film directed by Zhang Fanfan and written by Xiao Yu.  The film stars Alec Su, Pace Wu, Hu Ming, and Jerry Yuan.  It was followed by sequel "Lost in Panic Cruise".  The film was released in China on October 30, 2010.

Jared Leto: Jared Joseph Leto ( ; born December 26, 1971) is an American actor, singer, songwriter, and director.  After starting his career with television appearances in the early 1990s, Leto achieved recognition for his role as Jordan Catalano on the television series "My So-Called Life" (1994).  He made his film debut in "How to Make an American Quilt" (1995) and received critical praise for his performance in "Prefontaine" (1997).  Leto played supporting roles in "The Thin Red Line" (1998), "Fight Club" (1999) and "American Psycho" (2000), as well as the lead role in "Urban Legend" (1998), and earned critical acclaim after portraying heroin addict Harry Goldfarb in "Requiem for a Dream" (2000).  He later began focusing increasingly on his music career, returning to acting with "Panic Room" (2002), "Alexander" (2004), "Lord of War" (2005), "Lonely Hearts" (2006), "Chapter 27" (2007), and "Mr. Nobody" (2009).  In 2012, he directed the documentary film "Artifact".  In 2016, he played the DC Comics supervillain Joker in the DC Extended Universe film "Suicide Squad".

Panic Room: Panic Room is a 2002 American thriller film directed by David Fincher and written by David Koepp.  The film stars Jodie Foster and Kristen Stewart as a mother and daughter whose new home is invaded by burglars, played by Forest Whitaker, Jared Leto, and Dwight Yoakam.

Safe room: A safe room or panic room is a fortified room that is installed in a private residence or business to provide a safe shelter, or hiding place, for the inhabitants in the event of a break in, home invasion, tornado, terror attack, or other threat.  Safe rooms usually contain communications equipment, so that law enforcement authorities can be contacted.

Adventureland (film): Adventureland is a 2009 American romantic comedy-drama film written and directed by Greg Mottola, starring Jesse Eisenberg and Kristen Stewart and co-starring Ryan Reynolds, Kristen Wiig, Bill Hader, Martin Starr, and Margarita Levieva.  The film is set in the summer of 1987 when recent college grad James Brennan (Jesse Eisenberg) is making big plans to tour Europe and attend graduate school in pursuit of a career in journalism.  However, financial problems force him to look for a summer job instead of traveling abroad, which places him at Adventureland, a run-down amusement park in western Pennsylvania.  There he meets Emily Lewin (Kristen Stewart), a co-worker with whom he develops a quick rapport and relationship.

Kristen Stewart: Kristen Jaymes Stewart (born (1990--) 9, 1990 ) is an American actress and model.  Born in Los Angeles to parents working in show business, Stewart began her acting career in 1999 with uncredited roles and a minor character appearance in several films.  She gained notice in 2002 for playing Jodie Foster's daughter in the thriller "Panic Room", which garnered her a Young Artist Award nomination for Best Leading Actress in a Feature Film.  She went on to star in "Speak" (2004), "Catch That Kid" (2004), "Zathura" (2005), and "Into The Wild" (2007), for which she was nominated for a Screen Actors Guild Award.  She received widespread recognition in 2008 for playing Bella Swan in "The Twilight Saga" film series (2008–12), which grossed over $3.3 billion worldwide.

The Cake Eaters: The Cake Eaters is a 2007 American independent drama film about two small town families who must confront old issues with the return of one family's son.  The film was directed by Mary Stuart Masterson (in her feature film directorial debut) and stars Kristen Stewart, Aaron Stanford, Bruce Dern, and Jayce Bartok.  Kristen Stewart is featured as Georgia, a young girl with Friedreich's ataxia, a rare disease for which there is no cure.

Lost in Panic Cruise: Lost in Panic Cruise is a 2011 Chinese suspense thriller and sequel to "Lost in Panic Room".  The film was directed by Zhang Fanfan and written by Xiao Yu, starring Alec Su, Annie Wu, Cica Zhou, Yang Kun, and Ni Hongjie.  The film was released in China on 27 October 2011.  It is the sequel to the 2010 film "Lost in Panic Room."

Arthur Max: Arthur Max (born May 1, 1946) is an American production designer.  He has been nominated for three Academy Awards: once for his Production Design work on "Gladiator" (2000), "American Gangster" (2007), and "The Martian" (2015).  In addition to his Oscar nominations, Max won several other honors for his production design on the film, including the BAFTA, the National Board of Review prize and the Broadcast Film Critics honor.  He also collected two "Excellence in Production Design" Award2 from the Art Directors Guild, the first for Gladiator and the second for The Martian.  He was also nominated for "Black Hawk Down", "Robin Hood", "American Gangster", "Prometheus" and "Panic Room".  After "[[The Martian (film), Max worked on [[All The Money In The World]] (2017) marking Max's twelfth project for filmmaker Scott, a list of achievements which includes "[[Exodus: Gods and Kings]]", "[[The Counselor]]", "[[Kingdom of Heaven (film)|Kingdom of Heaven]]", "Robin Hood" and the aforementioned "Black Hawk Down" and "[[Body of Lies (film)|Body of Lies]]".  He designed Fincher's 1995 thriller, "[[Seven (1995 film)|Seven"]]".

Hui Bu Hui: Hui Bu Hui (Will We) is a song written by Roxanne Seeman, Fredrik Samsson and Tobias Forsberg.  It is the theme song and promo music video for the Mainland China hit thriller Lost in Panic Cruise, the sequel to Lost in Panic Room.  "Hui Bu Hui (Will We)" was recorded by Yang Kun in Mandarin and produced by Zhang Ya Dong.  Chinese lyrics are by Cui Shu.  Hui Bu Hui (Will We) and released on October 13, 2011.  The movie premiered on Mainland China October 27, 2011.

Question: Which film did Kristen Stewart star in first, Adventureland or Panic Room?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress being queried."
    },
    "films_compared": {
      "type": "array",
      "description": "A list of films involved in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "film_title",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "first_film_by_release": {
      "type": "string",
      "description": "The title of the film the actress starred in first, based on release year."
    },
    "first_film_release_year": {
      "type": "integer",
      "description": "The release year of the film the actress starred in first."
    }
  },
  "required": [
    "actress_name",
    "films_compared",
    "first_film_by_release",
    "first_film_release_year"
  ],
  "additionalProperties": false
}
