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
Killer (Kiss song): "Killer" is a song by the American hard rock band Kiss.  Featured on their 1982 album, "Creatures of the Night", the song was released as an A-side single in the United Kingdom.  Although "I Love It Loud" was an A-side single in the United States, it would be relegated to the B-side in the UK.  It was the first song Vinnie Vincent and Gene Simmons wrote together after the two had met.  In addition to not being able to chart at all, Kiss has never performed the song live and it has only been released as a single and on all issues of the "Creatures of the Night" album (the song was switched places with "Saint and Sinner" on the 1985 reissue).

Range Life (song): "Range Life" is a song by Pavement, the third single from their 1994 album "Crooked Rain, Crooked Rain".  The song attracted attention with controversial lyrics that seemed to mock alternative rock superstars the Smashing Pumpkins and the Stone Temple Pilots; Pumpkins frontman Billy Corgan expressed his displeasure in magazine interviews, while songwriter Stephen Malkmus maintained that his words had been misinterpreted and no insult was intended.  Regardless, Pavement, which was due to tour for Lollapalooza in 1994, got kicked out when the Smashing Pumpkins, the headlining act, threatened to cancel their Lollapalooza dates if Pavement played.  Pavement would eventually play Lollapalooza the next year.  An early 1993 demo of the song did not feature this verse; guitarist Spiral Stairs recalled in 2004 that when Malkmus first revealed these new lyrics to his bandmates at the New York City recording sessions for "CRCR", "we almost lost our lunch from laughing so much."  The single was not commercially released in the USA; it was issued by the band's UK label at the time, Big Cat.  Both B-sides are outtakes from the "Crooked Rain, Crooked Rain" sessions and are included on the 2004 of that album.  This song was one of many to be included in the group's greatest hits album "".

Paperback Writer: "Paperback Writer" is a 1966 song recorded and released by the English rock band the Beatles.  Written by Paul McCartney and John Lennon (credited to Lennon–McCartney), the song was released as the A-side of their eleventh single.  The single went to the number one spot in the United States, United Kingdom, Ireland, West Germany, Australia, New Zealand and Norway.

Kings and Queens (Killing Joke song): "Kings and Queens" is Killing Joke's third single from their fifth studio album, "Night Time".  It was originally released by E.G. Records on 21 March 1985 as a 12" and 7" single in the UK, and a 7" single by Polydor in the Netherlands.  It was produced by Chris Kimsey.  The 12" single featured "Kings and Queens (A Right Royal Mix)" as an A-side, and both "The Madding Crowd (Remixed by Killing Joke)" and "Kings and Queens" as B-sides. E.G.'s 7" single and Polydor's 7" single exempted "Kings and Queens (A Right Royal Mix)" and instead featured "Kings and Queens" as the A-side, and "The Madding Crowd (Remixed by Killing Joke)" as the B-side.  E.G. also released a remix of the song, "Kings and Queens (Knaves Mix)", as an A-side and featured the same B-sides as the 12" single of "Kings and Queens".

Consuela Biaz: "Malaika" / "Consuela Biaz" is a double A-side single by German band Boney M. and the first single taken from their fifth album "Boonoonoonoos" (1981).  It peaked at #13 in the German charts, their lowest placing so far after their commercial breakthrough.  Boney M. would use the double A-side format in this period, typically with the A1 being the song intended for radio and A2 being more squarely aimed at discos.  "Consuela Biaz" was first promoted as the A-side in Germany where the group performed it in pop show Musikladen.  After a promotional visit to Spain where the group found "Malaika" had become a Top 10 hit, the title was remixed and then promoted as the A-side.  It was the second consecutive Boney M. single not to be released in the UK and Japan.

Rain (Anthony Callea song): "Rain" is the second song released by "Australian Idol" series two runner-up Anthony Callea, and features on his self-titled debut album "Anthony Callea" (2005).  It was released as a double A-side set features the song plus his recording of Simon & Garfunkel's song "Bridge over Troubled Water", which he performed on "Australian Idol".

Rain (Beatles song): "Rain" is a song by the English rock band the Beatles first released in May 1966 as the B-side of the "Paperback Writer" single.  Both songs were recorded during the sessions for the album "Revolver" although neither appears on that album.

I See a Boat on the River / My Friend Jack: "I See a Boat on the River" / "My Friend Jack" is a double A-side single by German band Boney M., taken from their 1980 compilation album "The Magic of Boney M. - 20 Golden Hits".  "I See a Boat on the River" peaked at #5 in Germany but marked the group's waning popularity in the UK where "My Friend Jack" was promoted as the A-side, faring even worse than their the former single "I'm Born Again", stalling at #57.  Boney M. would use the double A-side format over the next years, typically with the A1 being the song intended for radio and A2 being more squarely aimed at discos.  The sides would usually be switched on the accompanying 12" single.

Crooked Rain, Crooked Rain: LA's Desert Origins: Crooked Rain, Crooked Rain: LA's Desert Origins is a double album by Pavement released on October 26, 2004.  It contains the band's second album, "Crooked Rain, Crooked Rain" (1994) in its entirety, as well as 37 of the band's other songs from that era, 25 of which (the entire second disc) were previously unreleased.  The album also contains a 62-page booklet of liner notes, which contain photographs, artwork, accounts from vocalist/guitarist Stephen Malkmus and guitarist Scott Kannberg (a.k.a. "Spiral Stairs"), and notes Malkmus wrote for "Melody Maker" about each of the songs on the original album.  The liner notes also feature a surreal and sensationalistic "interview" between Matador's Gerard Cosloy and the fictitious "Rob Jurkface".  According to Cosloy, he took questions by Pavement's biographer, Rob Jovanovic, changed them slightly, and wrote silly answers for them.

Let's Go Crazy: "Let's Go Crazy" is a 1984 song by Prince and The Revolution, from the album "Purple Rain".  It was the opening track on both the album and the film "Purple Rain".  "Let's Go Crazy" was one of Prince's most popular songs, and was a staple for concert performances, often segueing into other hits.  When released as a single, the song became Prince's second number-one hit on the "Billboard" Hot 100, and also topped the two component charts, the Hot R&B/Hip-Hop Songs and Hot Dance Club Play charts, as well as becoming a UK Top 10 hit.  The B-side was the lyrically controversial "Erotic City".  In the UK, the song was released as a double A-side with "Take Me with U".

Question: Who wrote the song on the A-side of the song "Rain"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "a_side_song_title": {
      "type": "string",
      "description": "The title of the song that was the A-side to 'Rain'."
    },
    "writers": {
      "type": "array",
      "description": "The individuals credited with writing the A-side song.",
      "items": {
        "type": "string"
      }
    },
    "performing_band": {
      "type": "string",
      "description": "The band that performed the A-side song."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the A-side song was released."
    }
  },
  "required": [
    "a_side_song_title",
    "writers",
    "performing_band",
    "release_year"
  ],
  "additionalProperties": false
}
