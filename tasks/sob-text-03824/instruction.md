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
American Bellydancer: American Bellydancer is a 2005 documentary film directed by Jonathan Brandeis.  It features Bellydancers including Ansuya, Rachel Galoob-Ortega, Suhaila Salimpour, Rachel Brice and Sonia.

Li Yang (Crazy English): Li Yang (; born 1969 in Changzhou, Jiangsu) is a Chinese educator and language instructor.  He is the creator of "Crazy English", an unorthodox method of teaching English.  He claimed to have taught English to more than 20 million people in a decade.

Richard Short (actor): Richard Ian Porterfield Short (born 8 October 1975) is an English actor based in Los Angeles.  He is starring in the 2017 TV drama series "Mary Kills People".  In 2017 he appeared in the independent film "The Dare" and in 2016 "Crazy Famous".  On television he has had recurring roles on "Vinyl" and "Covert Affairs" and has appeared on "American Horror Story", "White Collar", and "Blue Bloods".  Short has appeared in more than 30 films and television shows in the USA and UK.  On Broadway, he was a member of the 2011 company of Jez Butterworth's Jerusalem at the Music Box Theatre.

Kenneth Thomson (actor): Kenneth Thomson (January 7, 1899 – January 26, 1967) was an American character actor active during the silent and early sound film eras.  He, along with his wife Alden Gay, was a founding member of the Screen Actors Guild.  The group was founded after meetings held at the Thomsons' home during 1933.  During his brief twelve-year career in front of the camera, he appeared in over 60 films.  After appearing in several Broadway plays during the early and mid-1920s, Thomson would make his film debut with a starring role in 1926's "Risky Business".  Over the next four years, he would appear in over a dozen films, in either starring or featured roles.  In 1930 alone he would appear in ten films, half of which were in starring roles, such as "Lawful Larceny", which also starred Bebe Daniels and Lowell Sherman (who also directed), and "Reno", whose other stars were Ruth Roland and Montagu Love; the other half would see him in featured roles as in "A Notorious Affair", starring Billie Dove, Basil Rathbone, and Kay Francis.  During the rest of the 1930s, he would appear in numerous films, mostly in either supporting or featured roles, such as "The Little Giant" (1933), starring Edward G. Robinson and Mary Astor, and "Hop-Along Cassidy" (1935), starring William Boyd; although he occasionally would have a starring role, as in opposite Harold Lloyd in 1932's "Movie Crazy".

Crazy English: Crazy English () is a brand name related to a non-traditional method

Kirsten Dunst: Kirsten Caroline Dunst ( ; born April 30, 1982) is an American actress.  She made her film debut in Woody Allen's short film "Oedipus Wrecks" for the anthology film "New York Stories" (1989).  At the age of twelve, Dunst gained widespread recognition as Claudia in "Interview with the Vampire" (1994), a role for which she was nominated for a Golden Globe Award for Best Supporting Actress.  She appeared in "Little Women" the same year and in "Jumanji" the following year.  After a recurring role in the third season of the NBC medical drama "ER" (1996–97) as Charlie Chemingo and starring in films such as "Wag the Dog" (1997), "Small Soldiers" (1998), the 1998 English dub of "Kiki's Delivery Service" (1989), and "The Virgin Suicides" (1999), Dunst began making romantic comedies and comedy-dramas, starring in "Drop Dead Gorgeous" (1999), "Bring It On" (2000), "Get Over It" and "Crazy/Beautiful" (both released in 2001).

The Crazy World of Arthur Brown (album): The Crazy World of Arthur Brown is the eponymous debut studio album by the English psychedelic rock band the Crazy World of Arthur Brown, released in June 1968.  The album was produced by the Who's manager Kit Lambert with associate production by Pete Townshend.  The album was released in June 1968 on Lambert's Track Records label in the UK, with North American distribution handled by Atlantic Records.  The album was released in the US in September.  (Early North American copies of the album, while distributed by Atlantic, bore the Track Records imprint; later pressings were released on the Atlantic label proper.)

Awara Paagal Deewana: Awara Paagal Deewana (Hindi: आवारा पागल दीवाना , English: "Wayward, Crazy, Insane") is a 2002 Indian Hindi action comedy film directed by Vikram Bhatt.  The film's music was composed by Anu Malik, and the lyrics by Sameer.  It has a plot loosely inspired by "The Whole Nine Yards", and features action scenes choreographed by stunt director Dion Lam, who worked on "The Matrix" and Hong Kong action films.  "Awara Paagal Deewana" was one of the highest grossing Hindi films of the year 2002.  It was notable for lavish and exotic song picturisations, stunts/action scenes by Akshay Kumar, and Paresh Rawal's popular comical chemistry with Johnny Lever, who played a funny character called Chhota Chhatri.

Crazy Legs (dancer): Richard Colón (born January 1, 1966), better known by his stage name Crazy Legs, is an American b-boy from the Bronx New York City, USA.  He was featured in the earliest stories on hip hop dancing to appear in mainstream press, and as president of the Rock Steady Crew brought the form to London and Paris in 1983.  Today he is also involved in community outreach, dance instruction and dance theater productions.  His pioneering status is reflected in his appearances in fiction films and documentaries.  Crazy Legs is the most well known and commercially successful of the few original members remaining of the Rock Steady Crew, and is its current president.

Crazy English (film): Crazy English is a 1999 Chinese documentary directed by Zhang Yuan.  The film premiered along with Zhang's "Seventeen Years" at the 1999 Locarno International Film Festival.  It established Zhang's position as a "legitimate" director after years of working independently from, and often at odds with, the Chinese authorities.

Question: What type of films are both Crazy English and American Bellydancer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_titles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The titles of the films being queried."
    },
    "film_type": {
      "type": "string",
      "description": "The common type of film for all listed titles."
    },
    "count_of_films": {
      "type": "integer",
      "description": "The number of films identified."
    }
  },
  "required": [
    "film_titles",
    "film_type",
    "count_of_films"
  ],
  "additionalProperties": false
}
