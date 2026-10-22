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
The Silent Lie: The Silent Lie is a 1927 silent drama film, produced and released by Fox Film Corporation, directed by Raoul Walsh, and starring Walsh's then-wife Miriam Cooper.

John Carpenter: John Howard Carpenter (born January 16, 1948) is an American movie director, screenwriter, producer, musician, editor and composer.  Although Carpenter has worked with various movie genres, he is associated most commonly with horror, action and science fiction movies of the 1970s and 1980s.

Esther and the King: Ester e il re (English Translation: "Esther and the King") is a 1960 Italian / American international co-production religious epic film directed (with Mario Bava, the film's director of photography, who was credited as a co-director on Italian prints of the film), written, and produced by Raoul Walsh.  It was made in Cinemascope and DeLuxe Color, and produced at 20th Century Fox/ Raoul Walsh Productions, and was released by 20th Century Fox.  Joan Collins stars as Esther.  Based on the Old Testament, this epic recreates the Book of Esther, the tale that is the basis for the Jewish celebration of Purim.

Kindred of the Dust: Kindred of the Dust is a 1922 American silent film directed by Raoul Walsh, and starring his wife Miriam Cooper.  It was based upon the novel of the same name by Peter B. Kyne.  The film was the last independent picture for Walsh's production company, and the last film he and Cooper would make together.  Today it is one of Walsh's earliest surviving features, and is one of only two non-D. W. Griffith features of Cooper's that still is known to survive.

Dark Command: Dark Command is a 1940 Western film starring Claire Trevor, John Wayne and Walter Pidgeon loosely based on Quantrill's Raiders during the American Civil War.  Directed by Raoul Walsh from the novel by W.R. Burnett, "Dark Command" is the only film in which western icons John Wayne and Roy Rogers appear together, and was the only film Wayne and Raoul Walsh made together since Walsh discovered Wayne working as a prop mover, renamed him, and gave him his first leading role in the widescreen western "The Big Trail" a decade before.

Raoul Walsh: Raoul A. Walsh (March 11, 1887December 31, 1980) was an American film director, actor, founding member of the Academy of Motion Picture Arts and Sciences (AMPAS) and the brother of the silent screen actor George Walsh.  He was known for portraying John Wilkes Booth in the silent classic "The Birth of a Nation" (1915) and for directing such films as "The Big Trail" (1930), starring John Wayne, "High Sierra" (1941), starring Ida Lupino and Humphrey Bogart; and "White Heat" (1949), starring James Cagney and Edmond O'Brien.  He directed his last film in 1964.

The Pride of New York: The Pride of New York is a lost 1917 American silent war drama film directed by Raoul Walsh and starring his brother George Walsh.  It was produced by and distributed through the Fox Film Corporation.

The Serpent (1916 film): The Serpent was a 1916 American silent drama film directed by Raoul Walsh and starring Theda Bara.  The film based on the short story "The Wolf's Claw", by Philip Bartholomae, and its scenario was written by Raoul A. Walsh.  Produced and distributed by Fox Film Corporation, "The Serpent" was shot on location at Chimney Rock, North Carolina, and at the Fox Studio in Fort Lee, New Jersey.  It is now considered lost.

Marines, Let's Go: Marines, Let's Go is a 1961 CinemaScope colour Korean War film about three Marine buddies (Tom Tryon, David Hedison and Tom Reese) on shore leave in Japan and at war in Korea.  It was produced and directed by Raoul Walsh, who also wrote the story.  Walsh had previously had successes with films about the U.S. Marine Corps in World War I ("What Price Glory? "), the 1920s ("The Cock-Eyed World" and "Sadie Thompson"), and World War II ("Battle Cry").  This was the next-to-last film of Walsh's long directing career.

The Naked and the Dead (film): The Naked and the Dead is a 1958 Technicolor widescreen film based on Norman Mailer's World War II novel "The Naked and the Dead".  Directed by Raoul Walsh and filmed in Panama, the screenplay attributed to the Sanders brothers adds a strip tease and action scenes to Mailer's original narrative.  Made by RKO just before its demise, the film was released by Warner Brothers and was the last one Raoul Walsh directed for that studio.

Question: Raoul Walsh and John Carpenter, are of which nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nationality": {
      "type": "string",
      "description": "The nationality shared by the individuals."
    },
    "individuals": {
      "type": "array",
      "description": "A list of individuals whose nationality is being identified.",
      "items": {
        "type": "string"
      }
    },
    "number_of_individuals": {
      "type": "integer",
      "description": "The count of individuals listed."
    }
  },
  "required": [
    "nationality",
    "individuals",
    "number_of_individuals"
  ],
  "additionalProperties": false
}
