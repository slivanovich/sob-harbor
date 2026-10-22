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
Modern Vampires: Modern Vampires (also billed as Revenant) is a 1998 black horror/comedy film that was released Oct 19, 1999 straight to video, written by Matthew Bright and directed by Richard Elfman.

Free Money (film): Free Money is a 1998 black comedy film directed by Yves Simoneau, produced by Nicolas Clermont and written by Anthony Peck and Joseph Brutsman, and starring Marlon Brando in his penultimate film (his final screen appearance was in 2001's "The Score").

Comedy horror: Comedy horror is a literary and film genre that combines elements of comedy and horror fiction.  Comedy horror has been described as able to be categorized under three types: "black comedy, parody and spoof."  The genre almost inevitably crosses over with the black comedy genre.  Comedy horror will often use satire on horror clichés as its main source of humour or take a story in a different perspective, such as "The Cabin in the Woods" and "Drag Me to Hell".

Dead Man on Campus: Dead Man on Campus is a 1998 black comedy film starring Mark-Paul Gosselaar and Tom Everett Scott.  It centers on the urban legend that a student gets straight As if their roommate commits suicide ("see" pass by catastrophe).  Two failing friends attempt to find a depressed roommate to push him over the edge and receive As.

A Murder of Crows (album): A Murder of Crows is the second full-length studio album by the progressive metal band Deadsoul Tribe, released on July 28, 2003 by InsideOut Music.  This time the entire band has come to play for the album with the addition of Roland Kerschbaumer for rhythm guitar and replaced Volker Wilschko to guitar.  The song, "Time" is the bonus track for the limited edition which comes in a slipcase.

Your Friends &amp; Neighbors: Your Friends & Neighbors is a 1998 black comedy film written and directed by Neil LaBute and starring Amy Brenneman, Aaron Eckhart, Catherine Keener, Nastassja Kinski, Jason Patric, and Ben Stiller in an ensemble cast.  This film was the first to be reviewed on the website Rotten Tomatoes.  The film's credit sequences feature music by Apocalyptica.

Deadsoul Tribe (album): Deadsoul Tribe is the debut full-length studio album by the progressive metal band Deadsoul Tribe, released on March 20, 2002.  The brief intro to "Powertrip" (before any instruments can be heard) is from the film, Fear and Loathing in Las Vegas.

Fear and Loathing in Las Vegas (film): Fear and Loathing in Las Vegas is a 1998 American black comedy road film adapted from Hunter S. Thompson's novel of the same name.  It was co-written and directed by Terry Gilliam, starring Johnny Depp as Raoul Duke and Benicio del Toro as Dr. Gonzo.  The two embark on an initially assigned journey with journalistic purpose which turns out to be an exploration of the Las Vegas setting under the effect of psychoactive substances.

Fragile Vastness: Fragile Vastness is a Greek band, formed in February 2000 by Babis Tsolakis (drums, former member of Piranha and Retrospect), Vangelis Yalamas (bass guitar, former member of Airged Lahm and Retrospect), Evi Katsamatsa (piano/keyboards, a piano teacher), Alex Flouros (guitars, former member of Sound Of Silence) and Zacharias Tsoumos (vocals, tenor at the National Greek Opera).  Their musical influence covers a wide spectrum of different kinds of music, like jazz, Latin and ethnic music, but they can be categorized as a progressive rock/progressive metal band.  After signing a contract with the record company Sleaszy Rider, they release their debut album called "Excerpts...", including the video clip for the song “Weep No More”, on the November 19, 2002.  In the beginning of 2004, Zacharias Tsoumos leaves the band due to obligations and is replaced by George Ikosipentakis.  With this synthesis, their second album "A Tribute To Life" was released in 2005.  Fragile Vastness has been a support band for bands like Sentenced, Pain of Salvation, Rage, Primordial, Deadsoul Tribe, Fates Warning and Helloween

Susan's Plan: Susan's Plan (also released as "Dying to Get Rich" on video) is a 1998 black comedy film directed by John Landis and starring Nastassja Kinski, Dan Aykroyd, Billy Zane, Rob Schneider, Lara Flynn Boyle and Michael Biehn.  The plot revolves around Susan's (played by Kinski) plan to kill her former husband (with the help of a group of misfits) and collect his life insurance.

Question: Deadsoul Tribe includes a song that was from which 1998 black comedy film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the black comedy film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film, specifically 'black comedy'."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that used content from the film."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album where the content from the film is featured."
    },
    "track_name": {
      "type": "string",
      "description": "The name of the track that includes content from the film."
    },
    "content_description": {
      "type": "string",
      "description": "A description of the content used from the film (e.g., 'brief intro')."
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "film_genre",
    "band_name",
    "album_name",
    "track_name",
    "content_description"
  ],
  "additionalProperties": false
}
