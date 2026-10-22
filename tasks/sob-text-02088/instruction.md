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
Multi-Facial: Multi-Facial is a 1995 American short drama film written, directed, produced, and scored by Vin Diesel.  The film stars Diesel as a multiracial actor and depicts the professional and emotional issues he faces.  "Multi-Facial" was noticed by Steven Spielberg, who would cast Diesel in "Saving Private Ryan" (1998).  It was released on DVD in 1999.

Saving Private Ryan: Saving Private Ryan is a 1998 American epic war drama film set during the Invasion of Normandy in World War II.  Directed by Steven Spielberg and written by Robert Rodat, the film is notable for its graphic portrayal of war, and for the intensity of its opening 27 minutes, which includes a depiction of the Omaha Beach assault during the Normandy landings.  It follows United States Army Rangers Captain John H. Miller (Tom Hanks) and a squad (Tom Sizemore, Edward Burns, Barry Pepper, Giovanni Ribisi, Vin Diesel, Adam Goldberg, and Jeremy Davies) as they search for a paratrooper, Private First Class James Francis Ryan (Matt Damon), who is the last-surviving brother of four servicemen.

Niland brothers: The Niland brothers were four American brothers of Irish descent from Tonawanda, New York, who served in the military during World War II.  Two survived the war, but for a time it was believed that only one, Frederick "Fritz" Niland, had survived.  After the reported deaths of his three brothers, Fritz was sent back to the United States to complete his service and only later learned that his brother Edward, missing and presumed dead, was actually captive in a Japanese POW camp in Burma.  Steven Spielberg's 1998 film "Saving Private Ryan" is loosely based on the brothers' story.

Janusz Kamiński: Janusz Zygmunt Kamiński, A.S.C. (] ; born June 27, 1959) is a Polish cinematographer and film director who started his career in the United States.  He rose to fame in the 1990s with his innovative work on "Schindler's List" (1993).  He has established a partnership with Steven Spielberg, working as a cinematographer on his movies since 1993.  He won the Academy Award for Best Cinematography for his work on "Schindler's List" and "Saving Private Ryan" (1998).  In recent years, Kamiński has also moved into the field of directing, first with the horror film "Lost Souls", and later television series like "The Event" and "The Divide".

Saving Private Ryan (soundtrack): Saving Private Ryan: Music from the Original Motion Picture Soundtrack is the soundtrack album for the 1998 film "Saving Private Ryan", directed by Steven Spielberg.  The album was produced by composer John Williams and distributed by DreamWorks Records.  Recorded in Symphony Hall, Boston, Massachusetts, the scores were performed by the Boston Symphony Orchestra, with two of the ten compositions featuring vocals from the Tanglewood Festival Chorus.  The soundtrack runs for almost an hour, while the film itself lasts over two hours.

Bonnie Curtis: Bonnie Kathleen Curtis (born March 26, 1966) is an American film producer whose credits include "Saving Private Ryan", "A.I.", "Minority Report", and "", directed by Steven Spielberg.  Her first solo project was the 2005 release "The Chumscrubber".  She then joined Mockingbird Pictures with partner Julie Lynn in 2011.  Curtis and Lynn produced Albert Nobbs, which was nominated for three Academy Awards.  Curtis is a co-recipient of the 1999 Producers Guild Award for Motion Picture Producer of the Year, for "Saving Private Ryan".  On March 12, 2015, Curtis was inducted into the Texas Film Hall of Fame.  Spielberg congratulated her via video message during the ceremony.

Band of Brothers (miniseries): Band of Brothers is a 2001 American war drama miniseries based on historian Stephen E. Ambrose's 1992 non-fiction book of the same name.  The executive producers were Steven Spielberg and Tom Hanks, who had collaborated on the 1998 World War II film "Saving Private Ryan".  The episodes first aired in 2001 on HBO.  The series won Emmy and Golden Globe awards in 2001 for best miniseries.

Matt Damon filmography: Matt Damon is an American actor, producer and screenwriter.  He made his screen debut at the age of 18 with a minor role in the 1988 film "Mystic Pizza".  After appearing in a series of supporting parts in much of the 1990s, Francis Ford Coppola cast Damon as the lead of the 1997 legal drama "The Rainmaker".  His breakthrough came later that year when he played the title role of an unrecognized genius in "Good Will Hunting", a drama which he also co-wrote with Ben Affleck.  Damon and Affleck won the Academy Award for Best Original Screenplay and Damon was nominated for Best Actor.  He followed it by playing the title roles of a soldier in Steven Spielberg's war drama "Saving Private Ryan" (1998) and of the criminal Tom Ripley in the thriller "The Talented Mr. Ripley" (1999), both of which gained critical and commercial success.  Damon's profile continued to expand in the 2000s, as he took on starring roles in two lucrative film franchises.  He featured as a con man in Steven Soderbergh's "Ocean's Trilogy" (2001–07) and played the titular spy Jason Bourne in four of the five films in the "Bourne" series (2002–16).

Gary Levinsohn: Gary Levinsohn is an American film producer.  He was nominated for the Academy Award for Best Picture, along with Steven Spielberg, Ian Bryce, Mark Gordon for the film "Saving Private Ryan".  He is the co-owner of Mutual Film Company.

List of Band of Brothers episodes: HBO's "Band of Brothers", a ten-part television World War II miniseries based on the book of the same title written by historian and biographer Stephen E. Ambrose, was executive produced by Steven Spielberg and Tom Hanks after their collaboration on the World War II film "Saving Private Ryan" (1998).  The episodes first aired in 2001 on HBO and are still run frequently on various TV networks around the world.

Question: Gary Levinsohn is an American film producer, and was nominated for the Academy Award for Best Picture, along with Steven Spielberg, for the film "Saving Private Ryan", an American epic war drama film, released in which year, and set during the Invasion of Normandy in World War II?

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
      "description": "The year the film was released."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "producers_nominated_for_best_picture": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of producers nominated for the Academy Award for Best Picture for this film."
    },
    "setting_event": {
      "type": "string",
      "description": "The specific historical event during which the film is set."
    },
    "setting_war": {
      "type": "string",
      "description": "The war during which the film is set."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "producers_nominated_for_best_picture",
    "setting_event",
    "setting_war"
  ],
  "additionalProperties": false
}
