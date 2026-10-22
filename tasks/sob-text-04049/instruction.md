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
I'm a Ruin: "I’m a Ruin" is a song by Welsh singer-songwriter Marina Diamandis, professionally known as Marina and the Diamonds.  It was released on 2 February 2015 as the third official single from her third studio album, "Froot", two months before the release of the album.  A music video for the song was released the following day, and premiered on Noisey.  During its initial premiere on BBC Radio 1 in the United Kingdom, host Huw Stephens announced that the song would be officially released as a single in the United Kingdom on 22 March 2015 .  "I'm a Ruin" was praised by critics, who commended its production, lyrical content, and Diamandis' vocal delivery; it was further hailed as a highlight of "Froot".

Power &amp; Control: "Power & Control" is a song by Welsh singer Marina Diamandis, professionally known as Marina and the Diamonds, from her second studio album, "Electra Heart" (2012).  It was released on 20 July 2012 by 679 Artists and Atlantic Records as the second single from the record.  Diamandis collaborated with former Swedish House Mafia member Steve Angello while writing the track, and enlisted Greg Kurstin to oversee its production.  An electropop and power pop track, "Power & Control" describes the struggle between romantic partners in achieving superiority in their relationship.

Radioactive (Marina and the Diamonds song): "Radioactive" is a song by Welsh recording artist Marina and the Diamonds from the deluxe version of her second studio album "Electra Heart" (2012).  It was released on 23 September 2011 as the first promotional single from the record; it preceded the premiere of the official lead single "Primadonna" on 20 March 2012.

Disconnect (song): "Disconnect" is a song by British electronic music group Clean Bandit and Welsh singer-songwriter Marina and the Diamonds.  It was composed by Marina and the Diamonds and Jack Patterson, with the song's production handled by Luke Patterson, Jack Patterson and Mark Ralph.  It was released to digital retailers on 23 June 2017, as the fourth single from the band's upcoming second studio album.  The song is Marina and the Diamonds' first single since her 2015 album "Froot".

1998 WPF Draft: The 1998 WPF Draft was the second annual collegiate draft for the WPSL/WPF's 1998 season, and was held on December 7, in Palm Springs, CA in conjunction with the 1998 NFCA National Convention.  Draft order was based on teams' finish in 1997.  Georgia Pride and Carolina Diamonds tied with the same record during the 1997 regular season.  Georgia lost more games to Carolina in the 1997 head-to-head series and chose ahead of Carolina in the odd-numbered rounds.  Carolina chose ahead of Georgia in the even numbered rounds.

How to Be a Heartbreaker: "How to Be a Heartbreaker" is a song by Welsh recording artist Marina and the Diamonds from the American version of her second studio album "Electra Heart" (2012).  It was released on 7 December 2012 by 679 Artists and Atlantic Records as the third and final single from the record.  Diamandis worked with Ammar Malik, Benny Blanco, Cirkut, Daniel Omelio, and Dr. Luke during the songwriting process, and enlisted Blanco, Cirkut, and Dr. Luke to oversee its production.

Mowgli's Road: "Mowgli's Road" is a song by Welsh recording artist Marina and the Diamonds from her debut studio album, "The Family Jewels" (2010).  The song was released on 13 November 2009 as the album's second single, containing a cover of the Late of the Pier song "Space and the Woods" as its B-side.  "Mowgli's Road" originally appeared as a B-side to the single "Obsessions", which was released on 16 February 2009 by Neon Gold Records.

Marina and the Diamonds: Marina Lambrini Diamandis (Greek: Μαρίνα-Λαμπρινή Διαμαντή ; born 10 October 1985), known professionally as Marina and the Diamonds, is a Welsh singer-songwriter.  Diamandis has described herself as an "indie artist with pop goals" and often analyses components of human behavior in her music.  She is additionally known for her unconventional fashion styles.

Happy (Marina and the Diamonds song): "Happy" is a song by Welsh singer-songwriter Marina Diamandis, professionally known as Marina and the Diamonds.  It is the opening track on her third album, "Froot", and was released on 12 December 2014 as the second song from her "Froot of the Month" campaign, which was the monthly release of a new song up until the album's release.  An acoustic video for the song was released on 18 December 2014.  The song also serves as the second official single from the album.

Froot (song): "Froot" is a song by Welsh singer Marina Diamandis, known professionally as Marina and the Diamonds.  It was released for streaming on 10 October 2014, to coincide with the singer's birthday, and later received a full digital release as the lead single from her third studio album "Froot".  Diamandis premiered the single on YouTube.

Question: Which Marina and the Diamonds song was released on December 7?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "artist_name": {
      "type": "string",
      "description": "The professional name of the artist."
    },
    "release_details": {
      "type": "object",
      "properties": {
        "release_date": {
          "type": "string",
          "description": "The specific date the song was released."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the song was released."
        },
        "album_name": {
          "type": "string",
          "description": "The name of the album the song is from."
        },
        "is_single": {
          "type": "boolean",
          "description": "Indicates if the song was released as a single."
        },
        "single_order": {
          "type": "integer",
          "description": "The sequential number of the single from the album."
        }
      },
      "required": [
        "release_date",
        "release_year",
        "album_name",
        "is_single",
        "single_order"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "artist_name",
    "release_details"
  ],
  "additionalProperties": false
}
