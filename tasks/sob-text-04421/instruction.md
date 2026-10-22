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
County Fair: "County Fair" is a song written by Brian Wilson and Gary Usher for the American rock band The Beach Boys.  It was originally released as the second track on their 1962 album "Surfin' Safari".  On November 26 of that year, it was released as the B-side to The Beach Boys' third single, "Ten Little Indians".  The same single was released in the UK in January 1963.

The Beach Boys: The Beach Boys are an American rock band formed in Hawthorne, California, in 1961.  The group's original lineup consisted of brothers Brian, Dennis, and Carl Wilson; their cousin Mike Love; and their friend Al Jardine.  Distinguished by their vocal harmonies and early surf songs, they are one of the most influential acts of the rock era.  The group, led by their principal songwriter and producer Brian, pioneered novel approaches to popular music form and production, combining their affinities for jazz-based vocal groups, 1950s rock and roll, and black R&B to create their unique sound.  He later arranged his compositions for studio orchestras and explored a variety of other styles, often incorporating classical or jazz elements and unconventional recording techniques in innovative ways.

Chug-A-Lug (The Beach Boys song): "Chug-A-Lug" is a song written by Brian Wilson, Gary Usher and Mike Love for the American rock band The Beach Boys.  It was released on their 1962 album "Surfin' Safari".

Surf Route 101: Surf Route 101 is a 1964 album by the Super Stocks, one of Gary Usher's ad-hoc surf and hot-rod studio groups.  The band's line up featured some of the best surf musicians of the period including Glen Campbell.  The title track "Surf Route 101" was a cover of a song from Jan and Dean's 1963 album "Drag City."  Brian Wilson had collaborated with Usher on "My First Love" "Muscle Beach Party" for the 1964 film "Muscle Beach Party", where they were originally performed by Dick Dale and his Del-Tones.  For the Super Stocks album Usher re-used the original backing tracks made for the film.

Heads You Win–Tails I Lose: "Heads You WinTails I Lose" is a song written by Brian Wilson and Gary Usher for the American rock band The Beach Boys.  It was released on their 1962 album "Surfin' Safari".

We'll Run Away: "We'll Run Away" is a song written by Brian Wilson and Gary Usher for the American rock band the Beach Boys, released on their 1964 album "All Summer Long".  The song is a doo-wop ballad in 12/8 time.  The lyrics are about a young couple wishing to elope, and their respective parents are warning them against such an impulse.

In My Room: "In My Room" is a song written by Brian Wilson and Gary Usher for the American rock band The Beach Boys.  It was released on their 1963 album "Surfer Girl".  It was also released as the B-side of the "Be True to Your School" single.  The single peaked at number 23 in the U.S. (the A-side peaked at number 6, for a two-sided top-40) and was eventually inducted into the Grammy Hall of Fame in 1999.  "In My Room" was ranked number 212 on "Rolling Stone's" list of The 500 Greatest Songs of All Time.

Cuckoo Clock (song): "Cuckoo Clock" is a song written by Brian Wilson and Gary Usher for the American rock band The Beach Boys.  It was released on their 1962 album "Surfin' Safari".  The song was written about the myna bird of Brian's father Murry Wilson.

Pet Projects: The Brian Wilson Productions: Pet Projects: The Brian Wilson Productions is a CD compilation album of the recorded work of record producer, songwriter, and musician Brian Wilson as he attempted to branch away from his band the Beach Boys during the early-to-mid-1960s and early 1970s.  The compilation features performing artists such as Glen Campbell, Gary Usher, the Honeys, American Spring, Jan and Dean, Sharon Marie, and the Survivors.  It was released with a full-color 20-page booklet with rare photos and a detailed essay.

409 (song): "409" is a song written by Brian Wilson, Mike Love, and Gary Usher for the American rock and roll band the Beach Boys.  The song features Love singing lead vocals.  It was originally released as the B-side of the single "Surfin' Safari" (1962).  It was later released on their 1962 album, "Surfin' Safari" and appeared again on their 1963 album, "Little Deuce Coupe".

Question: "Cuckoo Clock" is a song written by Brian Wilson and Gary Usher for a band formed in what California city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band for whom the song was written."
    },
    "formation_location": {
      "type": "string",
      "description": "The city in California where the band was formed."
    }
  },
  "required": [
    "song_title",
    "band_name",
    "formation_location"
  ],
  "additionalProperties": false
}
