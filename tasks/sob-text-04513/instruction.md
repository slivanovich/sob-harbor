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
Pet Sounds Studio: The Pet Sounds Recording Studio (usually referred to as simply Pet Sounds Studio or Pet Sounds, after the Beach Boys' album of the same name) was a recording studio located in Lexington, Kentucky (originally Denver, Colorado), founded by Robert Schneider of The Apples in Stereo and Jim McIntyre of Von Hemmling.  Many Elephant 6 albums have been recorded in the studio, including the critically acclaimed Neutral Milk Hotel album, "In the Aeroplane Over the Sea".  It was demolished in 1999; a high-rise condominium was subsequently erected on the site.

Exotica (Martin Denny album): Exotica is the first album by Martin Denny, released in 1957.  It contained Denny's most famous piece, "Quiet Village", and spawned an entire genre bearing its name.  It was recorded December 1956 in Webley Edwards' studio in Waikiki (not, as often reported, the Aluminum Dome at Henry J. Kaiser's Hawaiian Village Complex).  The album topped Billboard's charts in 1959.

With a Twist (Todd Rundgren album): With a Twist... is a 1997 album by Todd Rundgren.  Asked to produce an album of new versions of his older singles, Rundgren decided to record the songs in Bossa nova style with elements of Exotica, complete with tropical bird call effects at the beginning of "Hello, It's Me" similar to Martin Denny's recording "Quiet Village".  Continuing the theme, Rundgren toured theaters with a replica of a tiki bar, the performers on a very small stage with selected audience members being seated at tables also on the theater stage, and being served drinks by the monitor engineer/bartender.  The performers never acknowledged the larger theater audience, and the show ended when the last "bar patron" left the stage.

Exotica Volume II: Exotica Volume II was the second album by Martin Denny, released in 1958.

Pathway Studios: Pathway was a North London studio located at 2a Grosvenor Avenue, Newington Green, founded by producers Peter Ker and Mike Finesilver and later run by Mike until the mid 1990s.  Among the well-known artists who made their early recordings with producer Nick Lowe at Pathway Studios are The Damned, Madness, Elvis Costello, The Police, Squeeze, Haircut One Hundred, The Count Bishops with Mike Spenser, The Cannibals and John Foxx.  At the studio, Dire Straits recorded the demo and single versions of "Sultans of Swing", and the folk singer Ewan MacColl recorded his last album.  The 8-track studio, a former garage, was famous for its great atmosphere, cold temperatures, distinctive smell and excellent recordings.

Caravan (1936 song): "Caravan" is a jazz standard composed by Juan Tizol and Duke Ellington, and first performed by Ellington in 1936.  Irving Mills wrote seldom performed lyrics.  Its exotic sound interested exotica musicians; Martin Denny, Arthur Lyman, and Gordon Jenkins all covered it.  Woody Allen used the song in two of his films, "Alice" and "Sweet and Lowdown".  The song is also heavily featured in the 2014 film "Whiplash" as an important plot element.  The Mills Brothers recorded an a cappella version, making the instruments' sounds with their voices, and Johnny Mathis recorded the song in 1956.  There are more than 350 recordings of this song by Duke Ellington's orchestra, the great majority of them now in the public domain.

Exotica: Exotica is a musical genre, named after the 1957 Martin Denny album of the same title, popular during the 1950s to mid-1960s, typically with suburban Americans who came of age during World War II.  The musical colloquialism "exotica" means tropical ersatz good, the non-native, pseudo experience of insular Oceania, Southeast Asia, Hawaii, the Amazon basin, the Andes and tribal Africa.  Denny described the musical style as "a combination of the South Pacific and the Orient...what a lot of people imagined the islands to be like...it's pure fantasy though."  While the South Seas forms the core region, exotica reflects the "musical impressions" of every place from standard travel destinations to the mythical "shangri-las" dreamt of by armchair safari-ers.

Sessions at West 54th: Recorded Live in New York: Sessions at West 54th: Recorded Live in New York is the first live music DVD by Keb' Mo' recorded in June 1997 which was then released in 2000.  The performance was recorded for the television series Sessions at West 54th, a studio located in West 54th Street in New York City.  The songs recorded on the album are all from Keb' Mo's two prior studio albums.  Unlike the majority of Keb' Mo's albums, this contains no songs by Robert Johnson.

Waikiki: Waikīkī ( ; Hawaiian: ] ) (also known as Waikiki Beach) is a beachfront neighborhood of Honolulu, on the south shore of the island of Oʻ ahu, in Hawaii, United States.  Waikiki is most famous for Waikīkī Beach, but it is just one of six beaches in the district, the others being Queen's Beach, Kuhio Beach, Gray's Beach, Fort DeRussy Beach and Kahanamoku Beach.

Q Division Studios: Q Division Studios is a recording studio located in Somerville, Massachusetts, United States.  Founded in 1986, Q Division was originally located at 443 Albany Street in Boston, but moved to its current two-studio facility in 2000.  Bands that have recorded at Q Division include Pixies, who recorded their second album "Surfer Rosa" at the studio.

Question: Exotica, the first album by Martin Denny was recorded in a studio located in an area most famous for what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "artist_name": {
      "type": "string",
      "description": "The artist who recorded the album."
    },
    "recording_studio": {
      "type": "string",
      "description": "The name of the studio where the album was recorded."
    },
    "studio_location": {
      "type": "string",
      "description": "The general location where the studio was situated."
    },
    "location_famous_for": {
      "type": "string",
      "description": "The most famous feature or landmark of the recording location."
    }
  },
  "required": [
    "album_name",
    "artist_name",
    "recording_studio",
    "studio_location",
    "location_famous_for"
  ],
  "additionalProperties": false
}
