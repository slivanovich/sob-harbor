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
Robert Roy Pool: Robert Roy Pool (born 1953) is an American screenwriter, best known for his authorship of the motion pictures "Outbreak" (1995), starring Dustin Hoffman, and "The Big Town" (1987), starring Matt Dillon.  He also received a "story by" credit on the motion picture "Armageddon" (1998), which starred Bruce Willis and Billy Bob Thornton.  Pool has collaborated with Laurence Dworet, a former emergency room doctor.

A Good Day to Die Hard: A Good Day to Die Hard is a 2013 American action thriller film and the fifth installment in the "Die Hard" film series.  The film was directed by John Moore and written by Skip Woods, and stars Bruce Willis as John McClane.  The main plot finds McClane travelling to Russia to get his estranged son, Jack, an undercover CIA agent, out of prison.  He is soon caught in the crossfire of a global terrorist plot.  Alongside Willis, the film also stars Jai Courtney, Cole Hauser, Yuliya Snigir and Sebastian Koch as the film's villain.

Jimmy Bennett: James Michael Bennett (born February 9, 1996) is an American actor and musician.  He is known for his roles as a child actor in "Daddy Day Care", "Hostage", "Poseidon", "Evan Almighty", "Orphan", Shorts, and as young James T. Kirk in the 2009 film "Star Trek".  He also starred on the ABC series "No Ordinary Family" as JJ Powell, a teenager gifted with vast intelligence after a plane crash.

Hostage (2005 film): Hostage is a 2005 American action thriller drama film produced by and starring Bruce Willis and directed by Florent Emilio Siri.  The film was based on a novel by Robert Crais, and was adapted for the screen by Doug Richardson.

Moonlighting (theme song): "Moonlighting" is the theme song to the ABC comedy-crime drama of the same name, which ran from 1985 to 1989 and starred Bruce Willis and Cybill Shepherd.  The theme song was performed by Al Jarreau, who wrote the song with Lee Holdridge; it was produced by Nile Rodgers.  Included on the soundtrack album for the series and released as a single in 1987, the song reached number 23 on the "Billboard" Hot 100 and spent one week at number one on the Adult Contemporary chart.  In 1988 the song earned two Grammy Award nominations for Best Pop Vocal Performance, Male and for Best Song Written Specifically for a Motion Picture or Television.

Michael Budd: Michael Hamish Budd (born 2 July 1974) is an award winning Australian film Actor, Director and Producer.  He is an active member of the Australian Directors Guild.  And best known for playing Esmael, alongside Henry Cavill (Man of Steel) and Sigourney Weaver in The Cold Light of Day The film also starred Bruce Willis.

First Kill (2017 film): First Kill is an American action thriller film directed by Steven C. Miller and written by Nick Gordon.  The film stars Hayden Christensen and Bruce Willis.

Last Man Standing (1996 film): Last Man Standing is a 1996 American action thriller film written and directed by Walter Hill and starring Bruce Willis, Christopher Walken and Bruce Dern.  It is a credited remake of Akira Kurosawa's "Yojimbo".

Red (2010 film): Red is a 2010 American action comedy film inspired by the limited comic book series of the same name created by Warren Ellis and Cully Hamner and published by the DC Comics imprint Homage.  The film stars Bruce Willis, Morgan Freeman, John Malkovich, Mary-Louise Parker, Helen Mirren and Karl Urban, with German film director Robert Schwentke directing a screenplay by Jon Hoeber and Erich Hoeber.  In the film version, the title is derived from the designation of former CIA Agent Frank Moses (Bruce Willis), meaning "Retired, Extremely Dangerous".

Wake (cancelled film): Wake is a cancelled American action thriller film written by Christopher Borrelli.  The film had Ben Kingsley, Piper Perabo, Cameron Monaghan and Ellen Burstyn set to star.  Filming began on February 16, 2015 in Cleveland, which halted on February 26 due to financial issues.  It was then expected to resume production in 2-3 weeks, but it was postponed for an indefinite time after actor Bruce Willis and director John Pogue left the film due to financing and scheduling issues.

Question: Jimmy Bennett is known for a role in what 2005 American action thriller that was produced by and starred Bruce Willis?

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
    "genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "bruce_willis_involvement": {
      "type": "object",
      "properties": {
        "starred": {
          "type": "boolean",
          "description": "Indicates if Bruce Willis starred in the film."
        },
        "produced": {
          "type": "boolean",
          "description": "Indicates if Bruce Willis produced the film."
        }
      },
      "required": [
        "starred",
        "produced"
      ],
      "additionalProperties": false,
      "description": "Details of Bruce Willis's involvement in the film."
    },
    "jimmy_bennett_known_for_role": {
      "type": "boolean",
      "description": "Indicates if Jimmy Bennett is known for a role in this film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "bruce_willis_involvement",
    "jimmy_bennett_known_for_role"
  ],
  "additionalProperties": false
}
