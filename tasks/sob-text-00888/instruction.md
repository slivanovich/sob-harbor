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
Just Like Us!: Just Like Us!  is the fourth studio album by American pop rock group Paul Revere & the Raiders.  Produced by Terry Melcher and released on January 3, 1966, by Columbia Records, it featured the U.S. hit single "Just Like Me".  Unlike their later albums, on which Mark Lindsay was the primary lead singer, the lead vocal duties on "Just Like Us!"  were split among him and the other band members, guitarist Drake Levin, bassist Phil Volk, and drummer Mike Smith.

Swagga Like Us: "Swagga Like Us" is a song by American hip hop recording artists Jay-Z, T.I., Kanye West, and Lil Wayne.  It was released on September 6, 2008 in the United States as the fifth single from T.I.'s album "Paper Trail", and was also slated for inclusion on Jay-Z's eleventh album "The Blueprint 3" (2009), although it ultimately did not make the final track listing.  The song was produced by West and is constructed primarily around a vocal sample of "Paper Planes" by British musician M.I.A.

Paper Planes: "Paper Planes" is a song by British rapper M.I.A. from her second studio album, "Kala" (2007).  The song was written by M.I.A. and Diplo.  The song's backing track is a replayed sample of the 1982 song "Straight to Hell" by The Clash, and the members of The Clash are credited as co-writers of the song.  The chorus of "Paper Planes" was widely speculated to be based on the chorus to the 1992 song "Rump Shaker" by Wreckx-N-Effect, although that song's writers are not credited.  It was produced by Diplo with additional production by Switch.  "Paper Planes" was released for download in August 2007 and as the album's third single by XL Recordings and Interscope Records on 11 February 2008.

Rhythm &amp; Blues (Robert Palmer album): Rhythm & Blues is the thirteenth studio album by the British musician Robert Palmer.  His thirteenth solo studio album, it was released in 1999 and was his first new release in 5 years.  The album reached No. 118 in the UK but did not chart in the US.  Palmer's long-term girlfriend Mary Ambrose sang background vocals on some tracks, as did Sharon O'Neill who co-wrote "True Love".

Building a Better Me: Building a Better Me is the fifth full-length album from San Diegan punk band Dogwood, released in 2000.  Instrumentation for the album was produced and recorded by Sam Boukas and Dogwood at Goldentrack studio in San Diego, but vocals were produced and recorded at the Blasting Room studios in Fort Collins, Colorado by Descendents and ALL guitarist Stephen Egerton, whose vocals appear on the final track "Nothing New".  In 2001 the band was awarded the San Diego Music Award for best Punk band for the album.

Lost Souls Like Us: Lost Souls Like Us is Benjy Davis Project's fourth studio album, released on March 2, 2010.  It was recorded at Rivergate Studios in Hendersonville, TN.  The album featured the current band line-up of Benjy Davis and Mic Capdevielle.  In addition to Davis and Capdevielle, the album featured a cast of seasoned studio musicians: Mark "Sparky" Matejka of Lynyrd Skynyrd, Danny Chauncey of .38 Special and Jason "Slim" Gambill of Lady Antebellum all contributed guitar parts; Ethan Pilzer (Jewel, Big & Rich) played bass; Jason Spiewak and Bobby Capps played piano and organ; and Sara Jean Kelley sang background vocals.

It's Only Christmas: "It's Only Christmas" is a song by Irish pop singer and Boyzone frontman Ronan Keating, released as the second single from his sixth studio album, "Winter Songs", exclusively in Australia and New Zealand.  The version of the song featured on the British version of "Winter Songs" features vocals from Hayley Westenra, however, the version of the song featured on the Australian version of the album replaces her vocals with those of Kate Ceberano, and thus, whose vocals appear on the single.  Although not an international hit like his previous singles, Keating's version of the song failed to make the Top 100 of the Australian Singles Chart, peaking at #134 after one week on the chart.

Wish You Would: "Wish You Would" is a song by American hip hop recording artist Ludacris, released September 2, 2008 as the first promo single from his sixth studio album "Theater of the Mind" (2008).  The song, produced by DJ Toomp, features Ludacris' former rival, fellow Southern rapper T.I..  At the 2009 Grammy Awards, the song was nominated for an award in the category of Best Rap Performance by a Duo or Group.  The song ultimately lost to T.I.'s respective single, "Swagga Like Us".

Shape (song): "Shape" is a song by English girl group Sugababes, released as the fourth and final single from their second studio album, "Angels with Dirty Faces" (2002).  It was composed by Sting, Dominic Miller, and Craig Dodds, who produced the song.  The midtempo pop and R&B ballad incorporates a sample of Sting's 1993 recording "Shape of My Heart", whose vocals are featured in the chorus.  It received mixed reviews from critics, who were ambivalent towards the sample of "Shape of My Heart".

¡Viva la Cobra!: ¡Viva la Cobra!  is the second studio album by Cobra Starship.  The album was released on October 23, 2007.  It was produced by Fall Out Boy's Patrick Stump, whose vocals also feature throughout the album.  The album peaked at No. 80 on "Billboard" 200.  It has sold more than 40,000 copies to date.

Question: What is the name of the studio album by the British musician around whose vocals "Swagga Like Us" was constructed?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the studio album."
    },
    "artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the musician or group."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the musician."
        },
        "is_group": {
          "type": "boolean",
          "description": "Indicates if the artist is a group (true) or a solo musician (false)."
        }
      },
      "required": [
        "name",
        "nationality",
        "is_group"
      ],
      "additionalProperties": false
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "sampled_song_details": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song from the album that was sampled."
        },
        "sampled_by_song": {
          "type": "string",
          "description": "The title of the song that used the vocal sample."
        }
      },
      "required": [
        "song_title",
        "sampled_by_song"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_name",
    "artist",
    "release_year",
    "sampled_song_details"
  ],
  "additionalProperties": false
}
