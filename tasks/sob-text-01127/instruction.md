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
Team (Lorde song): "Team" is a song by New Zealand singer Lorde, taken from her debut studio album, "Pure Heroine" (2013).  The song was released on 13 September 2013 as the album's third single in Australia and New Zealand by Universal Music New Zealand, and the second in the United States and the United Kingdom by Lava and Republic Records.  The track was written by Lorde and Joel Little and produced by Little, with additional production from Lorde herself.  "Team" is a hybrid of alternative pop and electro-hop featuring synthesiser, bass and snare drum instrumentation over a handclap-based beat.  Lyrically, the track is a "tribute to her friends and country".

The Mix Tape, Vol. 1: The Mix Tape, Vol.  1 is the first installment of DJ Funkmaster Flex's "Mix Tape" series, released on November 21, 1995.  The album is a compilation of freestyles and previously released songs, all mixed with Funkmaster Flex's production.

Local H's Awesome Mix Tape 1: Local H's Awesome Mix Tape #1 is an EP by the alternative rock band Local H.  It was released on October 19, 2010 on the band's own G&P Records.  The EP features covers that the band has performed live.  The EP was released digitally, on CD as well as on a handful of cassette tapes.

The Team EP: The Team EP (stylized as The TEAM ep) is an extended play (EP) by American alternative rock band Local H.  "The Team EP" is the first Local H release to feature drummer Ryan Harding, who joined the band in November 2013, and was initially sold exclusively at Local H concerts.  Limited copies have since been made available online from G&P Records, the band's official merchandiser.

Bravado (song): "Bravado" is a song by New Zealand singer Lorde, originally included on her debut EP "The Love Club EP".  It was later featured on her "Tennis Court EP" and the extended version of her debut album "Pure Heroine" (2013).  The song was written by Lorde and Joel Little and was produced by the latter.  The track was released as a single on 6 September 2013, via iTunes Stores, in a number of European countries and India.  Characterised as a chamber pop and electropop song, "Bravado" addresses Lorde's introverted nature and the need to feign confidence in the music industry.  The single was well received by music critics and peaked at number five on the New Zealand Artist Singles chart.

Guardians of the Galaxy (soundtrack): Guardians of the Galaxy: Awesome Mix Vol.  1 (Original Motion Picture Soundtrack) is the soundtrack album for the Marvel Studios film of the same name.  Featuring the songs present on Peter Quill's mixtape in the film, the album was released by Hollywood Records on July 29, 2014.  A separate film score album, Guardians of the Galaxy (Original Score), composed by Tyler Bates, was also released by Hollywood Records on the same date, along with a deluxe version featuring both albums.  The soundtrack album reached number one on the US "Billboard" 200 chart, becoming the first soundtrack album in history consisting entirely of previously released songs to top the chart.

TRV$DJAM: TRV$DJAM was a collaboration project between Travis Barker of Blink-182 and Adam Goldstein, a.k.a. DJ AM.  They performed their first show on June 25, 2008 at the Roxy and released a mix tape online in August 2008 titled "Fix Your Face".  In June 2009, they released a 2nd mix tape titled "Fix Your Face Vol.  2 (Coachella' 09)".  Hours after performing for thousands of college students on September 19, 2008 in Columbia, South Carolina, Barker and DJ AM were critically injured in a fiery Learjet crash that killed four people.

Local H's Awesome Mix Tape 2: Local H's Awesome Mix Tape #2 is an extended play by American alternative rock duo Local H, which was released in December 2014 through their merchandiser, G&P Records.  Their version of Team was previously released as "The Team EP", which was sold exclusively through live shows and from the official G&P Records website.

Awesome Mix Tape vol. 6: Awesome Mix Tape vol.  6 is the fourth album by the ska/soul band The Pietasters.  It was released in 1999 (see 1999 in music).

The Mix Tape, Vol. II: The Mix Tape, Vol.  II is the second installment in Funkmaster Flex's "Mix Tape" series, released on February 11, 1997 through Loud Records.  Like his previous "Mix Tape" release, the albums is compilation of freestyles and previously released songs mixed together by Funkmaster Flex.

Question: Local H's Awesome Mix Tape 2 version of what song by new zeland singer lorde was previously released as "The Team EP"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song by Lorde."
    },
    "original_artist_details": {
      "type": "object",
      "properties": {
        "artist_name": {
          "type": "string",
          "description": "The name of the original artist."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country of origin of the original artist."
        },
        "original_album": {
          "type": "string",
          "description": "The debut studio album the song is taken from."
        },
        "album_release_year": {
          "type": "integer",
          "description": "The release year of the original album."
        }
      },
      "required": [
        "artist_name",
        "country_of_origin",
        "original_album",
        "album_release_year"
      ],
      "additionalProperties": false
    },
    "local_h_release_details": {
      "type": "object",
      "properties": {
        "ep_title": {
          "type": "string",
          "description": "The title of the EP by Local H that featured their version of the song."
        },
        "ep_initial_sales_channel": {
          "type": "string",
          "description": "The initial exclusive sales channel for the EP."
        },
        "later_compilation_album": {
          "type": "string",
          "description": "The title of the compilation album where Local H's version was later released."
        },
        "compilation_album_release_year": {
          "type": "integer",
          "description": "The release year of the compilation album."
        }
      },
      "required": [
        "ep_title",
        "ep_initial_sales_channel",
        "later_compilation_album",
        "compilation_album_release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "original_artist_details",
    "local_h_release_details"
  ],
  "additionalProperties": false
}
