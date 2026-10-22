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
Beragee Bomb: Beragee Bomb is a 2013 comedy Meitei film directed by Oinam Gautam and written by Laishram Santosh.  It stars Gurumayum Bonny, Leishangthem Tonthoi, Loya, Suraj Sharma Laimayum and Edwin Soibam.  "Beragee Bomb" was released on 31 August 2013 at MFDC with a Red Carpet Event, hosted by WOL Media for the first time in Meitei cinema.  The official trailer of the film was released by WOL Media on 18 August 2013.  A sequel to the film titled "Moreh Maru" was produced by RT Motion Pictures and released in 2016.

This Is Sanlitun: This Is Sanlitun is a 2013 comedy film directed by Róbert Ingi Douglas.  It is a co-production between China, Iceland and Ireland.  It was screened in the Contemporary World Cinema section at the 2013 Toronto International Film Festival.

Playin' for Love: Playin' For Love is a 2013 comedy film starring Salli Richardson-Whitfield and Robert Townsend and directed by Townsend.  The film premiered in 2013 at the American Black Film Festival and released theatrically in the United States on January 16, 2015.

Chapel Perilous: Chapel Perilous is a 2013 comedy fantasy short film, directed by Matthew Lessner.  The film had its premiere at the 2013 Stockholm International Film Festival on November 7, 2013.

WNUF Halloween Special: The WNUF Halloween Special is a 2013 comedy horror film.  The main portion of the film was directed by Chris LaMartina, who also helped to co-write the film.  Parody commercials are shown throughout the film, some of which were written and directed by persons other than LaMartina.  The movie's plot follows a television personality that decides to investigate strange supernatural occurrences at a house purported to be haunted.  "WNUF Halloween Special" was given a limited VHS run of 300 copies on October 18, 2013, and was given a DVD release in November of the same year.

Problem (Natalia Kills song): "Problem" is a song by English singer Natalia Kills from her second studio album, "Trouble" (2013).  It was released on 12 March 2013 as the album's lead single.  The song has been used in films such as "Pitch Perfect 2" and "We're the Millers".

Gregory Go Boom: Gregory Go Boom is a 2013 comedy drama short film, written and directed by Janicza Bravo.  The film premiered at Jash during "YouTube Comedy Week" on May 23, 2013.

Coffee Town: Coffee Town is a 2013 comedy film.  The first feature film from CollegeHumor, it was released on July 9, 2013 on digital platforms and in select theatrical engagements, leading up to a festival premiere on July 27, 2013 at Just For Laughs in Montreal.

We're the Millers: We're the Millers is a 2013 American comedy film directed by Rawson Marshall Thurber.  The film's screenplay was written by Bob Fisher, Steve Faber, Sean Anders, and John Morris, based on a story by Fisher and Faber.  It stars Jennifer Aniston, Jason Sudeikis, Emma Roberts, Will Poulter, Nick Offerman, Kathryn Hahn, Molly Quinn and Ed Helms.  The plot follows a small-time pot dealer (Sudeikis) who convinces his neighbors to create a fake family, in order to smuggle in drugs from Mexico onto US soil.

Banjong Pisanthanakun: Bangjong Pisanthanakun (Thai: บรรจง ปิสัญธนะกูล ) is a Thai filmmaker and screenwriter.  He saw early success with his first two films, "Shutter" (2004) and "Alone" (2007), both horror films that he co-directed and co-wrote with Parkpoom Wongpoom.  Since then he has directed films in a variety of genres, including the 2010 romantic comedy "Hello Stranger", the 2013 comedy horror film "Pee Mak", and the 2016 drama "One Day".

Question: Who directed the 2013 comedy that the song "Problem" was in?

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
      "description": "The release year of the film."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "song_featured": {
      "type": "string",
      "description": "The title of the song featured in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "director",
    "song_featured"
  ],
  "additionalProperties": false
}
