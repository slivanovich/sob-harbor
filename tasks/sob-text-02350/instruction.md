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
Marchetto da Padova: Marchetto da Padova (Marchettus of Padua; fl.  1305 – 1319) was an Italian music theorist and composer of the late medieval era.  His innovations in notation of time-values were fundamental to the music of the Italian ars nova, as was his work on defining the modes and refining tuning.  In addition, he was the first music theorist to discuss chromaticism.

Helen Mirra: Helen Mirra is an American conceptual artist.  Mirra has been artist-in-residence at University of California at Berkeley, and a guest of the DAAD Artists-in-Berlin Program.

Roland C. Jordan: Roland Carroll Jordan, Jr (born 1938) is an American composer and music theorist.  He studied in Texas and Pennsylvania before receiving his Ph.D. from Washington University in St. Louis, where he taught theory and composition for three decades.  As a composer, Jordan has written for both large ensembles and chamber groups, and as a music theorist, he has explored the uses of phenomenological methodology and structuralist/post-structuralist theory.

Emeka Ogboh: Emeka Ogboh (born 1977) is a Nigerian sound and installation artist best known for his soundscapes of life in Lagos.  Trained as an artist, he began working with sounds that characterize cities following an Egyptian multimedia art program.  He presents unmodified field recordings from Lagos city lifefor instance, its danfo share taxi systemin gallery installations with headphones and speakers.  His non-audio work uses iconography from Lagos city life.  He participated in the DAAD Artists-in-Berlin Program and 2015 Venice Biennale, and received the 2016 Bremen Böttcherstraße Art Award.  His work has exhibited at the Brooklyn Museum, American National Museum of African Art, Menil Collection, Casino Luxembourg, and Kiasma.  Critics noted his soundscapes' chaos and complexity, and his focus on recontextualizing rather than transforming the city's sounds.

Preston Trombly: Preston Andrew Trombly (born December 30, 1945, in Hartford, Connecticut) is an American composer, visual artist, and broadcast personality.  He is a program host on Sirius XM's Symphony Hall classical music channel.

Philip Corner: Philip Lionel Corner (born April 10, 1933; name sometimes given as Phil Corner) is an American composer, trombonist, alphornist, vocalist, pianist, music theorist, music educator, and visual artist.

DAAD Artists-in-Berlin Program: The DAAD Artists-in-Berlin Program (German: "Berliner Künstlerprogramm des DAAD") is a residential program for artists of all countries and ages run by the German Academic Exchange Service (German: ‘Deutscher Akademischer Austauschdienst', DAAD) in Berlin.  Originally initiated by the Ford Foundation in 1963, the program has been run by the DAAD – with the assistance of the German Federal Foreign Office and the Senate of Berlin – since 1965.  The program annually invites around 20 artists working within visual arts, literature, music and film to spend a year (in the case of film, six months) living and working in Berlin.  It is aimed at artists who have already demonstrated considerable talent, but are yet to become fully established.  It is one of the foremost artistic programs in Europe, and has hosted artists, filmmakers and writers such as Steve McQueen, Susan Sontag, John Cage, Margaret Atwood, Asghar Farhadi, Damien Hirst, Nan Goldin, Shahzia Sikander, Chirikure Chirikure and AA Bronson.  Katharina Narbutovič is currently head of the program.

John Cage: John Milton Cage Jr. (September 5, 1912 – August 12, 1992) was an American composer, music theorist, writer, philosopher, and artist.  A pioneer of indeterminacy in music, electroacoustic music, and non-standard use of musical instruments, Cage was one of the leading figures of the post-war avant-garde.  Critics have lauded him as one of the most influential composers of the 20th century.  He was also instrumental in the development of modern dance, mostly through his association with choreographer Merce Cunningham, who was also Cage's romantic partner for most of their lives.

Albert Patron: Alberto Patron (born December 26, 1969), known in America also as Albert Patron, is an Italian composer, music theorist, writer, philosopher and artist.  A pioneer of indeterminacy in music, aporetic music, and non-standard use of musical instruments, Patron the leading figures of the contemporary trent aporetic music as well as aporetic philosophy.  Critics have lauded him as one of the most innovative Italian composers of the last 20 years.  He was also instrumental in the development of philosophy.

Gioseffo Zarlino: Gioseffo Zarlino (31 January or 22 March 1517 – 4 February 1590) was an Italian music theorist and composer of the Renaissance.  He was possibly the most famous European music theorist between Aristoxenus and Rameau, and made a large contribution to the theory of counterpoint as well as to musical tuning.

Question: What American composer, music theorist, writer, philosopher, and artist did DAAD Artists-in-Berlin Program host?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The full name of the artist."
    },
    "nationalities": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of nationalities of the artist."
    },
    "professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions held by the artist."
    },
    "hosted_by_daad_program": {
      "type": "boolean",
      "description": "Indicates whether the artist was hosted by the DAAD Artists-in-Berlin Program."
    }
  },
  "required": [
    "artist_name",
    "nationalities",
    "professions",
    "hosted_by_daad_program"
  ],
  "additionalProperties": false
}
