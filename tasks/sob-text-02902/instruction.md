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
Jamie Raeburn: "Jamie Raeburn" is a traditional Scottish song about transportation.  Jamie Raeburn is reputed to have been a baker in Glasgow before being sentenced for petty theft, although he was allegedly innocent, and then sent out to the colonies as punishment.

The Bonnie Banks o' Loch Lomond: "The Bonnie Banks o' Loch Lomond", or simply "Loch Lomond" for short, is a well-known traditional Scottish song (Roud No. 9598) first published in 1841 in "Vocal Melodies of Scotland".  The song prominently features Loch Lomond, the largest Scottish loch, located between the counties of Dunbartonshire and Stirlingshire.  In Scotland, the song is often the final piece of music played during an evening of revelry (a dance party or dinner, etc.).

Annie Laurie (1936 film): Annie Laurie is a 1936 British comedy film directed by Walter Tennyson and starring Will Fyffe, Polly Ward and Bruce Seton.  The film takes its name from, but is not based on, the traditional Scottish song "Annie Laurie".  It was made at Cricklewood Studios in London.

Dumbarton's Drums: Dumbarton's Drums is a traditional Scottish song.

Avalanche (Thea Gilmore album): Avalanche is the fifth album by English singer-songwriter Thea Gilmore.  It was released on 9 September 2003 on the Hungry Dog record label.  The album peaked at number 62 on the UK Albums Chart. " Uncut" magazine ranked "Avalanche" at number 59 of its "Albums of the Year" for 2003 and said of Gilmore: "You can here her growing in stature with every record she makes."

I Dreamed I Saw St. Augustine: "I Dreamed I Saw St. Augustine" is a song by Bob Dylan that was originally released on his 1967 album "John Wesley Harding".  It was recorded at the first "John Wesley Harding" session on October 17, 1967.  It has been covered by many artists, including Joan Baez on her all-Dylan album "Any Day Now", as well as by Vic Chesnutt, Eric Clapton, John Doe, Thea Gilmore, Adam Selzer and Dirty Projectors.  In addition, Jimi Hendrix at one point intended to cover this song, but felt it was too personal to Dylan and instead covered a different song from the album, "All Along the Watchtower".

The Gallant Forty Twa: "The Gallant Forty Twa" is a traditional Scottish song associated with the 42nd Foot regiment known as the Black Watch.  It is generally dated to the mid-19th century, although it may have been based on an older tune from Ulster.  It was reportedly sung by soldiers from the regiment during the Dunkirk evacuation.

The Parting Glass: "The Parting Glass" is a Scottish traditional song, often sung at the end of a gathering of friends.  It was purportedly the most popular parting song sung in Scotland before Robert Burns wrote "Auld Lang Syne".  The song is particularly popular in Ireland and amongst Irish communities.

Ailein duinn: Ailein duinn ("Dark-haired Alan") is a traditional Scottish song for solo female voice, a lament that was written in Gàidhlig for Ailean Moireasdan ("Alan Morrison") by his fiancée, Annag Chaimbeul ("Annie Campbell").  Ailean Moireasdan was a sea captain from the isle of Lewis.  In the spring of 1788 he left Stornoway to go to Scalpay, Harris, where he was to marry Annag Chaimbeul ("Annie Campbell").  Unfortunately, they sailed into a storm and all the crew sank with the vessel, except Annag.  The broken-hearted Annag wasted away through grief and composed this lament for her lost love.  Annag lost her will to live and died a few months afterwards.  Her body was washed ashore near where her fiancé's was found.

The Threads EP: The Threads EP is an EP by Thea Gilmore, her first release after she parted with former label Sanctuary.  The disc was sold only on her 2007 spring tour with remaining copies sold through the official web site afterwards.  All songs were written by Gilmore except "The Parting Glass", a traditional song she arranged.

Question: When was the tour of Thea Gilmore's EP that included a traditional Scottish song?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "ep_name": {
      "type": "string",
      "description": "The name of the EP."
    },
    "tour_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year of the tour."
        },
        "season": {
          "type": "string",
          "description": "The season of the tour."
        }
      },
      "required": [
        "year",
        "season"
      ],
      "additionalProperties": false
    },
    "included_traditional_song": {
      "type": "boolean",
      "description": "Indicates if the EP included a traditional song."
    },
    "traditional_song_info": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the traditional song."
        },
        "origin": {
          "type": "string",
          "description": "The origin of the traditional song."
        }
      },
      "required": [
        "song_title",
        "origin"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "ep_name",
    "tour_details",
    "included_traditional_song",
    "traditional_song_info"
  ],
  "additionalProperties": false
}
