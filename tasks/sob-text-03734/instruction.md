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
Fifth Beatle: The fifth Beatle is an informal title that various commentators in the press and entertainment industry have applied to people who were at one point a member of the Beatles, or who had a strong association with the "Fab Four" (John Lennon, Paul McCartney, George Harrison, and Ringo Starr) during the group's existence.  The "fifth Beatle" claims first appeared in the press immediately upon the band's rise to global fame in 1963–64.  The members have offered their own beliefs of the "fifth Beatle":

Pete Best: Randolph Peter "Pete" Best (born Randolph Peter Scanland, 24 November 1941) is an English musician, principally known as an original member and first drummer of the Beatles, from 1960 to 1962.  He has been referred to as the Fifth Beatle.

Stuart Sutcliffe: Stuart Fergusson Victor Sutcliffe (23 June 1940 – 10 April 1962) was a British painter and musician best known as the original bass guitarist for the Beatles.  Sutcliffe left the band to pursue his career as a painter, having previously attended the Liverpool College of Art.  Sutcliffe and John Lennon are credited with inventing the name, "Beetles", as they both liked Buddy Holly's band, the Crickets.  The band used this name for a while until Lennon decided to change the name to "the Beatles", from the word "beat".  As a member of the group when it was a five-piece band, Sutcliffe is one of several people sometimes referred to as the "Fifth Beatle."

Murray the K: Murray Kaufman (February 14, 1922 – February 21, 1982), professionally known as Murray the K, was an influential rock and roll impresario and disc jockey of the 1950s, 1960s and 1970s.  During the early days of Beatlemania, he frequently referred to himself as the fifth Beatle.

Giles Martin Foody: Giles Martin Foody from the University of Nottingham, Nottinghamshire, UK was named Fellow of the Institute of Electrical and Electronics Engineers (IEEE) in 2013 "for contributions to the remote sensing of land cover".

Gregory Paul Martin: Gregory Paul Martin (born 21 January 1957) is a British writer/producer and actor of stage, film and television.  He is the eldest son of Beatles producer Sir George Martin and the half-brother of the music producer Giles Martin.

Love (Beatles album): Love is a soundtrack remix album of music recorded by the Beatles, released in November 2006.  It features music compiled and remixed as a mashup for the Cirque du Soleil show of the same name.  The album was produced by George Martin and his son Giles Martin, who said, "What people will be hearing on the album is a new experience, a way of re-living the whole Beatles musical lifespan in a very condensed period."

Nigel Godrich: Nigel Timothy Godrich (born 28 February 1971) is an English record producer, recording engineer and musician.  He is best known for his work with the English rock band Radiohead, having produced all of their studio albums since "OK Computer" (1997); he has been dubbed the "sixth member" of the band, in an allusion to George Martin being called the "Fifth Beatle".  Godrich has also worked extensively with Radiohead singer Thom Yorke on his solo material, and is a member of the bands Atoms for Peace (with Yorke) and Ultraísta.  Other acts Godrich has worked with include Beck, Paul McCartney, U2, R.E.M. and Roger Waters.  He is the creator of the music webseries "From the Basement".

George Martin: Sir George Henry Martin {'1': ", '2': ", '3': ", '4': "} (3 January 19268 March 2016) was an English record producer, arranger, composer, conductor, audio engineer, and musician.  He was referred to as the "Fifth Beatle", including by Paul McCartney, in reference to his extensive involvement on each of the Beatles' original albums.  Martin produced 30 number-one hit singles in the United Kingdom and 23 number-one hits in the United States.

Giles Martin: Giles Martin (born 9 October 1969) is an English record producer, songwriter, composer and multi-instrumentalist.  His studio recordings, stage shows, TV and film works have been critically acclaimed and commercially successful around the globe.  He is the son of Beatles producer George Martin and half-brother of actor Gregory Paul Martin.

Question: What relative of Giles Martin was referred to as the "Fifth Beatle"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "relative_name": {
      "type": "string",
      "description": "The name of the relative of Giles Martin."
    },
    "relationship_to_giles_martin": {
      "type": "string",
      "description": "The familial relationship of the person to Giles Martin."
    },
    "was_referred_as_fifth_beatle": {
      "type": "boolean",
      "description": "Indicates if the relative was referred to as the 'Fifth Beatle'."
    },
    "reason_for_title": {
      "type": "string",
      "description": "The reason why the person was referred to as the 'Fifth Beatle'."
    }
  },
  "required": [
    "relative_name",
    "relationship_to_giles_martin",
    "was_referred_as_fifth_beatle",
    "reason_for_title"
  ],
  "additionalProperties": false
}
