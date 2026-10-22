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
The World of Ice &amp; Fire: The World of Ice & Fire is a companion book for George R. R. Martin's "A Song of Ice and Fire" fantasy series.  Written by Martin, Elio M. García Jr. and Linda Antonsson, it was published by Bantam on October 28, 2014.  The 326-page volume is a fully illustrated "history compendium" of Martin's fictional Westeros, written from the perspective of an in-world "Maester" and featuring newly written material, family trees, and extensive maps and artwork.

A Song of Ice and Fire: A Song of Ice and Fire is a series of epic fantasy novels by the American novelist and screenwriter George R. R. Martin.  He began the first volume of the series, "A Game of Thrones", in 1991 and had it published in 1996.  Martin, who initially envisioned the series as a trilogy, has published five out of a planned seven volumes.  The fifth and most recent volume of the series published in 2011, "A Dance with Dragons", took Martin five years to write.  He is still writing the sixth novel, "The Winds of Winter".

George R. R. Martin: George Raymond Richard Martin (born George Raymond Martin; September 20, 1948), often referred to as George R. R. Martin, is an American novelist and short-story writer in the fantasy, horror, and science fiction genres, screenwriter, and television producer.  He is best known for his series of epic fantasy novels, "A Song of Ice and Fire", which was later adapted into the HBO series "Game of Thrones" (2011–present).  Martin serves as the series's co-executive producer, and also scripted four episodes of the series.

A Song of Ice and Fire fandom: The "A Song of Ice and Fire" fandom is an international and informal community of people drawn together by George R. R. Martin's "A Song of Ice and Fire" book series, the HBO television series "Game of Thrones", and the related merchandise.

Elio M. García Jr. and Linda Antonsson: Elio Garcia and Linda Antonsson are authors known for their contributions and expertise in the "A Song of Ice and Fire" series by George R. R. Martin, co-writing in 2014 with Martin "The World of Ice & Fire", a companion book for the series.  They are also the founders of the fansite Westeros.org, one of the earliest fan websites for "A Song of Ice and Fire".

The Blood of Olympus: The Blood of Olympus is a young adult novel written by American author Rick Riordan and is the fifth and final book in "The Heroes of Olympus" series.  It was released on October 7, 2014.  The seven demigods of the Prophecy of Seven—Percy Jackson, Annabeth Chase, Jason Grace, Leo Valdez, Piper McLean, Hazel Levesque, and Frank Zhang—go on their final adventure to defeat Gaea while Nico di Angelo, Reyna Avila Ramírez-Arellano, and Coach Gleeson Hedge attempt to bring the Athena Parthenos to Camp Half-Blood in order to prevent a war between the Roman and Greek demigods.  The chapters are written from the perspectives of Jason, Piper, Leo, Reyna, and Nico, making it the first time in the series that someone other than one of the seven demigods of the prophecy is the viewpoint character.  It is the second time that Percy appears without being a viewpoint character (first being in "The Lost Hero").

Ned Stark: Eddard "Ned" Stark is a fictional character in the 1996 fantasy novel "A Game of Thrones" by George R. R. Martin, and the first season of "Game of Thrones", HBO's adaptation of Martin's "A Song of Ice and Fire" series.  In the storyline, Ned is the lord of Winterfell, an ancient fortress in the North of the fictional continent of Westeros.  Though the character is established as a primary character in the novel and the TV adaptation, Martin's plot twist at the end involving Ned shocked both readers of the book and viewers of the TV series.

Maisie Williams: Margaret Constance "Maisie" Williams (born 15 April 1997) is an English actress.  She made her professional acting debut as Arya Stark in the HBO fantasy television series "Game of Thrones" in 2011, for which she won the EWwy Award for Best Supporting Actress in a Drama, the Portal Award for Best Supporting Actress – Television and Best Young Actor, and the Saturn Award for Best Performance by a Younger Actor.  In 2016, she was nominated for a Primetime Emmy Award for Outstanding Supporting Actress in a Drama Series.

Rebels, Rogues &amp; Sworn Brothers: Rebels, Rogues & Sworn Brothers is an album by punk/alt-country band Lucero.  It was released in 2006.  The album features less country influence than any previous release.  It was the band's last album for an independent label before signing with Universal Music Group in 2008.  The name of the album comes from the appendix of Storm of Swords, the third book in George R.R. Martin's Song of Ice and Fire series.

Arya Stark: Arya Stark is a fictional character in American author George R. R. Martin's award-winning "A Song of Ice and Fire" epic fantasy novel series.  She is a prominent point of view character in the novels, with the third most viewpoint chapters overall out of all the characters in the series so far, and is the only viewpoint character to appear in every published book of the series.

Question:  In George R. R. Martin's A song of Ice and Fire series who plays the only viewpoint character to appear in every published book of the series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "series_name": {
      "type": "string",
      "description": "The name of the book series the character is from."
    },
    "character_role_description": {
      "type": "string",
      "description": "A description of the character's specific role or significance in the series."
    }
  },
  "required": [
    "actor_name",
    "character_played",
    "series_name",
    "character_role_description"
  ],
  "additionalProperties": false
}
