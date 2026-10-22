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
Hedwig and the Angry Inch (film): Hedwig and the Angry Inch is a 2001 American musical comedy-drama film written, adapted, and directed by John Cameron Mitchell, who also portrayed the title role, reprising his performance from the original production.  Based on Mitchell's and Stephen Trask's stage musical of the same name, the film follows a fictional rock band fronted by an East German transgender singer who survives a botched sex change operation.  Hedwig subsequently develops a relationship with a younger man, Tommy, becoming his mentor and musical collaborator, only to have Tommy steal her music and move on without her.  The film follows Hedwig and her backing band, the Angry Inch, as they shadow Tommy's tour, while exploring Hedwig's past and complex gender identity.

Tent of Miracles (novel): Tent of Miracles (Portuguese: "Tenda dos Milagres" ) is a Brazilian Modernist novel.  It was written by Jorge Amado in 1967 and published the following year.  It was later adapted to a 1977 Cinema Novo (Nouvelle Vague) film by director/screenplay writer Nelson Pereira dos Santos.

Pedro Yanowitz: Peter Yanowitz (born September 13, 1967, Chicago, Illinois, United States), also known as Pedro Yanowitz, is an American musician, songwriter, and visual artist.  Yanowitz was the original drummer of The Wallflowers, and for Natalie Merchant on her first three solo records "Tigerlily", "Ophelia", and "Live in Concert".  He also played drums for Money Mark, the Black Sabbath tribute band Hand of Doom with Melissa Auf der Maur, and with Nina Nastasia, on her album "Dogs".  Other artists Yanowitz has played drums with include: Yoko Ono, Allen Ginsberg, and Wilco .  Yanowitz was also the bass player, songwriter, and producer for the band Morningwood.  Currently, Yanowitz is the drummer of Exclamation Pony with Ryan Jarman, and he is also performed as 'Schlatko', the drummer of The Angry Inch in the Tony award winning Broadway musical Hedwig and the Angry Inch, starring Neil Patrick Harris, Andrew Rannells, Michael C. Hall, John Cameron Mitchell, Darren Criss, and Taye Diggs.

Tenda dos Milagres (film): Tenda dos Milagres is a 1977 Brazilian drama film directed by Nelson Pereira dos Santos, based on the novel of the same name by Jorge Amado.  It stars Hugo Carvana, Sonia Dias and Severino Dada.  The director satirizes and exposes racism in Brazilian society.  The most notable example where this is done is in a flashback scene where Brazilians are shown listening with approving interest to Nazi race theories in the late 1930s.  "Tenda dos Milagres" was shot in Salvador, Bahia.

John Cameron Mitchell: John Cameron Mitchell (born April 21, 1963) is an American actor, writer and director, best known for originating the title role in the musical "Hedwig and the Angry Inch", and reprising it in the 2001 film adaptation directed by him, as well as for directing the films "Shortbus" (2006) and "Rabbit Hole" (2010).

Nelson Pereira dos Santos: Nelson Pereira dos Santos (born 22 October 1928) is a Brazilian film director.  He directed films such as "Vidas Secas" (Barren Lives), based on the book with the same name by Brazilian writer Graciliano Ramos.

Rio, 100 Degrees F.: Rio, 100 Degrees F "(Portuguese: Rio, 40 Graus") is a 1955 Brazilian film written and directed by Nelson Pereira dos Santos.  It is dos Santos' first feature work, inspired by the Italian Neo-Realism, and is considered a precursor of the Cinema Novo movement.

Hedwig and the Angry Inch (musical): Hedwig and the Angry Inch is a rock musical about a fictional rock and roll band fronted by a genderqueer East German singer, Hedwig Robinson.  The book is by John Cameron Mitchell, and the music and lyrics are by Stephen Trask.  The story draws on Mitchell's life as the son of a U.S. Army Major General who once commanded the U.S. sector of occupied West Berlin.  The character of Hedwig was inspired by a German divorced U.S. Army wife who was a Mitchell family babysitter and moonlighted as a prostitute at her Junction City, Kansas, trailer park home.  The music is steeped in the androgynous 1970s glam rock style of David Bowie (who co-produced the Los Angeles production of the show), as well as the work of John Lennon and early punk performers Lou Reed and Iggy Pop.

Ian Mullan: Ian Divine Mullan (born February 8, 1984) is a Canadian actor, writer, singer, producer and dandy.  Mullan is best known for acting, writing and producing the 2012 Queer Acts Theatre Festival show Sissydude, A Dandy Rock Musical, 2013's Best of the Coast bronze medal winner.  Previously, Mullan wowed audiences with his breakthrough starring role in Trrrash productions' 2009 staging of John Cameron Mitchell's musical Hedwig and the Angry Inch.

Hedwig and the Angry Inch (soundtrack): "Hedwig and the Angry Inch" is a 1998 musical about a fictional rock and roll band fronted by an East German genderqueer singer.  The text is by John Cameron Mitchell, and the music and lyrics are by Stephen Trask.  The musical has gathered a devoted cult following, and the musical has been adapted into the 2001 American musical film of the same name.

Question: Which director, Nelson Pereira dos Santos or John Cameron Mitchell is best known for originating the title role in the musical "Hedwig and the Angry Inch", and reprising it in the 2001 film adaptation directed by him?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director_name": {
      "type": "string",
      "description": "The name of the director who fits the description."
    },
    "film_adaptation_title": {
      "type": "string",
      "description": "The title of the film adaptation directed by the person."
    },
    "film_adaptation_year": {
      "type": "integer",
      "description": "The release year of the film adaptation."
    },
    "musical_title": {
      "type": "string",
      "description": "The title of the musical where the role was originated."
    },
    "role_originated": {
      "type": "string",
      "description": "The name of the title role originated by the director."
    },
    "is_also_actor": {
      "type": "boolean",
      "description": "Indicates if the director also portrayed the title role."
    }
  },
  "required": [
    "director_name",
    "film_adaptation_title",
    "film_adaptation_year",
    "musical_title",
    "role_originated",
    "is_also_actor"
  ],
  "additionalProperties": false
}
