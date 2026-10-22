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
The Tracks of My Tears: "The Tracks of My Tears" is a song written by Smokey Robinson, Pete Moore, and Marv Tarplin.  It is a multiple award-winning 1965 hit R&B song originally recorded by their group, The Miracles, on Motown's Tamla label.  In 1967, Johnny Rivers covered the song and his version was a number 10 hit on the "Billboard" Hot 100.  Linda Ronstadt recorded a hit cover of her own in 1975 that reached number 25 on the Hot 100 chart.  Numerous other artists have recorded the song over the years.

Any Way the Wind Blows (album): Any Way the Wind Blows is the second and final studio album by American country music duo Brother Phelps.  After its release, Doug re-joined country rock band The Kentucky Headhunters, of which he and Ricky Lee were both members previous to Brother Phelps' inception.  This album produced singles in its title track and "Not So Different After All", although neither charted in the Top 40 on the "Billboard" country charts.  The title track was originally recorded by J. J. Cale on his 1974 album "Okie".  The track "Ragtop" was previously recorded by The Kentucky Headhunters on their 1989 debut album "Pickin' on Nashville", while "Cinderella" is a cover of a song originally released by the rock band Firefall.  "Down into Muddy Water" would later be recorded by Shelly Fairchild on her 2004 debut album "Ride".

Long Time... Seldom Scene: "Long Time... Seldom Scene" is The Seldom Scene’s first-ever release with Smithsonian Folkways.  "Hickory Wind" is a homesick ballad that features the vocals of longtime friend of the Scene, Emmylou Harris, who originally recorded the song on her ‘Blue Kentucky Girl’ album in 1980.  “Wait a Minute” is a fresh take of a song originally recorded for 1974’s Old Train album and includes founding member John Starling (vocals) and guests Rickie Simpkins (fiddle) and Chris Eldridge (guitar), son of founding member Ben Eldridge (banjo).

Cry Wolf (Laura Branigan song): "Cry Wolf" is a song originally recorded by American pop singer Laura Branigan, released as the third single from her 1987 album "Touch".  It was written by singer-songwriter Jude Johnstone who later recorded the song herself for her 2002 debut album.  Stevie Nicks recorded a cover in 1989 for "The Other Side of the Mirror".

Live at Billy Bob's Texas (Stoney LaRue album): Live at Billy Bob's Texas is Stoney LaRue's first live album.  They are one of many bands to record a "Live at Billy Bob's Texas" album at the Fort Worth honky-tonk.  It was originally released in September 2005 as a limited edition CD/DVD combo.  It was re-released in 2006 with the full track listing.  The album included one new song, "Love You For Loving Me," as well as six cover songs.  The song, "Feet Don't Touch The Ground," was originally recorded by Brandon Jenkins on his 2003 album, "Unmended".  The song "Oklahoma Breakdown" was originally recorded by the Norman-based group, Hosty Duo.  "Goin' Down the Road (Feelin' Bad) is a folk song originally sung by Woody Guthrie.  The song The Weight was written by Robbie Robertson and recorded by The Band on their 1968 album, "Music from Big Pink".  "Long Black Veil" is a 1959 song, written by Danny Dill and Marijohn Wilkin and originally recorded by Lefty Frizzell as well as many other artists.  The album's cover photograph was by Texas photographer Todd Purifoy.

Try Me (Watashi o Shinjite): "Try Me" is a song originally recorded by English singer Lolita, written by Hinoky Team with production from Italian producer Dave Rodgers.  Toshiba-EMI released the song on December 21, 1994 as Lolita's first and only single from the album of the same name.  A year later, Japanese girl group Namie Amuro with Super Monkey's recorded their own rendition of the track, subtitled "Try Me (Watashi o Shinjite)" (Try Me (私を信じて) , Translate: "Believe Me") .

Somewhere in the Night (The Oak Ridge Boys song): "Somewhere in the Night" is a song originally recorded by The Oak Ridge Boys on their 1981 album "Fancy Free".  The song was later recorded by American country music group Sawyer Brown.  It was released in August 1987 as the first single and title track from the album "Somewhere in the Night".  The song reached #29 on the "Billboard" Hot Country Singles & Tracks chart.  The song was written by Rafe VanHoy and Don Cook.

A Lion's Trail: A Lion's Trail is a 2002 documentary film by François Verster about the rights for the popular song "The Lion Sleeps Tonight", also known as "Wimoweh", "Wimba Way" or "Awimbawe", a song written and recorded by the South African shepherd and singer of Zulu origin Solomon Linda with the Evening Birds as "Mbube".

The Lion Sleeps Tonight: "The Lion Sleeps Tonight", also known as "In The Jungle", or any of "Wimoweh", "Wimba Way" or "Awimbawe", is a song written and recorded originally by Solomon Linda with the Evening Birds for the South African Gallo Record Company in 1939, under the title "Mbube".  Composed in Zulu, it was adapted and covered internationally by many 1950's and 60's pop and folk revival artists, including the Weavers, Jimmy Dorsey, Yma Sumac, Miriam Makeba and the Kingston Trio.  In 1961, it became a number one hit in the United States as adapted in English with the best-known version by the doo-wop group the Tokens.  It went on to earn at least US$15 million in royalties from cover versions and film licensing.

Your Baby Doesn't Love You Anymore: "Your Baby Doesn't Love You Anymore" is a song originally recorded and made a minor hit by Ruby & the Romantics in 1965.  It appeared on their "Greatest Hits" album, and was released as a single on Kapp Records K-665 in April of that year.  On The Romantics' original version, the song's composer is listed as Lawrence (Larry) Weiss.  Although it was originally a B-side to the standard "We'll Meet Again", "Your Baby" received considerably more R&B radio airplay, but did not reach the "Billboard" Hot 100, only managing #8 on the Bubbling Under chart.

Question: A Lion's Trail is about the song originally recorded in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentary_title": {
      "type": "string",
      "description": "The title of the documentary film."
    },
    "song_title": {
      "type": "string",
      "description": "The primary title of the song that the documentary is about."
    },
    "original_artist": {
      "type": "string",
      "description": "The artist who originally recorded the song."
    },
    "original_recording_year": {
      "type": "integer",
      "description": "The year the song was originally recorded."
    }
  },
  "required": [
    "documentary_title",
    "song_title",
    "original_artist",
    "original_recording_year"
  ],
  "additionalProperties": false
}
