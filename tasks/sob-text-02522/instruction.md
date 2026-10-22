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
Dream Police: Dream Police is the fourth studio album by American rock band Cheap Trick.  It was released in 1979, and was their third release in a row produced by Tom Werman.  It is the band's most commercially successful studio album, going to No. 6 on the "Billboard" 200 chart and being certified platinum within a few months of its release.

Tom Werman: Tom Werman (born in Boston, MA) was an A&R man and record producer for Epic Records from 1970 into 1982.  He has produced 23 gold and platinum albums by acts including Mother's Finest, Ted Nugent, Cheap Trick, Molly Hatchet, Blue Öyster Cult, Mötley Crüe, Twisted Sister, Stryper, Hawks, Kix, L.A. Guns, and Poison.  While in A&R at Epic Records, he signed REO Speedwagon, Cheap Trick, Ted Nugent, Molly Hatchet and Boston to the label.  Werman became an independent producer in 1982 and continued to work until 2001, when he produced the music and soundtrack for the film "Rock Star", starring Mark Wahlberg and Jennifer Aniston.  Werman's producing credits also include key recordings by The Producers, Mother's Finest, Gary Myrick & The Figures, Jason & The Scorchers, Krokus, Lita Ford, Kix, LA Guns and Dokken.

Way of the World (Cheap Trick song): "Way of the World" is a single by American rock band Cheap Trick, released from their 1979 album "Dream Police".  The song was written by Rick Nielsen and Robin Zander and produced by Tom Werman.  In February 1980 it was released as a 7" vinyl single in the UK only, backed by "Oh, Candy," from the first Cheap Trick album, and peaked at #73.  It attempted to capitalize on the success of the mid-1979 single "I Want You to Want Me" and the live album "Cheap Trick at Budokan" which both entered the top 30.

Holy Man: Holy Man is a 1998 American comedy-drama film directed by Stephen Herek, written by Tom Schulman, and starring Eddie Murphy, Jeff Goldblum, Kelly Preston, Robert Loggia, Jon Cryer, and Eric McCormack.  The film was a critical and commercial failure.

All Shook Up (Cheap Trick album): All Shook Up is the fifth studio album by American rock band Cheap Trick.  Released in 1980, it was produced by former Beatles producer George Martin.  As such, this was the first album since their debut to be produced by someone other than Tom Werman.

The Mighty Ducks: The Mighty Ducks is a 1992 American sports comedy-drama film directed by Stephen Herek, starring Emilio Estevez.  It was produced by The Kerner Entertainment Company and Avnet–Kerner Productions and distributed by Walt Disney Pictures.  It is the first film in the "Mighty Ducks" trilogy.

The Great Gilly Hopkins (film): The Great Gilly Hopkins is a 2015 American comedy-drama film directed by Stephen Herek and written by David L. Paterson.  It is based on Katherine Paterson's 1978 children's book of the same name.  The film stars Sophie Nélisse, Julia Stiles, Glenn Close, Kathy Bates, Octavia Spencer, Bill Cobbs, and Billy Magnussen.  The film was released on October 7, 2016, by Lionsgate Premiere.

Hedwig and the Angry Inch (film): Hedwig and the Angry Inch is a 2001 American musical comedy-drama film written, adapted, and directed by John Cameron Mitchell, who also portrayed the title role, reprising his performance from the original production.  Based on Mitchell's and Stephen Trask's stage musical of the same name, the film follows a fictional rock band fronted by an East German transgender singer who survives a botched sex change operation.  Hedwig subsequently develops a relationship with a younger man, Tommy, becoming his mentor and musical collaborator, only to have Tommy steal her music and move on without her.  The film follows Hedwig and her backing band, the Angry Inch, as they shadow Tommy's tour, while exploring Hedwig's past and complex gender identity.

Funny Lady (soundtrack): Funny Lady is a soundtrack album by American vocalist Barbra Streisand.  It was released by Arista Records on March 15, 1975 to promote the 1975 American musical comedy-drama film "Funny Lady".  Executively produced by Peter Matz, the fifteen tracks on the album were performed by Streisand, James Caan, and Ben Vereen.  A soundtrack sequel to 1968's "Funny Girl", "Funny Lady" is a collection of songs from the point of view of American performer Fanny Brice. " How Lucky Can You Get", the album's only single released in April 1975, promoted the record and was written by Fred Ebb and John Kander, who also co-wrote the majority of the songs on "Funny Lady".

Rock Star (2001 film): Rock Star is a 2001 American musical comedy-drama film directed by Stephen Herek and starring Mark Wahlberg and Jennifer Aniston.  It tells the story of Chris "Izzy" Cole, a tribute band singer whose ascendance to the position of lead vocalist of his favorite band was inspired by the real-life story of Tim "Ripper" Owens, singer in a Judas Priest tribute band who was chosen to replace singer Rob Halford when he left the band.

Question: In which year was this American musical comedy-drama film directed by Stephen Herek, for which Tom Werman produced the music and soundtrack, released?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the American musical comedy-drama film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "music_soundtrack_producer": {
      "type": "string",
      "description": "The name of the person who produced the music and soundtrack for the film."
    },
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres for the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director_name",
    "music_soundtrack_producer",
    "film_genre"
  ],
  "additionalProperties": false
}
