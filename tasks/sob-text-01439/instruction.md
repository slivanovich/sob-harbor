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
Project Funk da World: Project: Funk da World is the debut studio album by rapper Craig Mack, released September 20, 1994.  The album was the second release on Bad Boy Records, following The Notorious B.I.G.'s classic "Ready to Die" by one week.  Propelled by the success of the Platinum RIAA-selling smash hit single "Flava in Ya Ear", the album reached Gold-RIAA sales status on February 22, 1995.  "Flava In Ya Ear" also featured a successful remix (not included on the album), featuring guest verses from The Notorious B.I.G., Busta Rhymes, & LL Cool J.  The album's second single, "Get Down", was the rapper's second Top 40 hit in 1994, & achieved Gold sales status in the United States in April 1995.

Duets: The Final Chapter: Duets: The Final Chapter (sometimes referred as The Biggie Duets) is the fourth studio album and second and final posthumous album by late American rapper The Notorious B.I.G., and is a collection of songs featuring appearances of other prominent rappers.  The album was released by Bad Boy Records and Atlantic Records on December 20, 2005 and charted at #3 selling 438,000 copies, beaten by the extremely high sales of Jamie Foxx's "Unpredictable" and Mary J. Blige's "The Breakthrough".  In the UK it climbed as high as #13 after the release of the album's first single "Nasty Girl".  It is his third posthumous album that went Double-platinum and is said to be his last album of mainly new material.

Ready to Die: Ready to Die is the debut studio album by American rapper The Notorious B.I.G.; it was released on September 13, 1994, by Bad Boy Records and Arista Records.  The label's first release, the album features production by Bad Boy founder Sean "Puffy" Combs, Easy Mo Bee, Chucky Thompson, DJ Premier and Lord Finesse, among others.  Recording for the album took place during 1993-94 at The Hit Factory and D&D Studios in New York City.  The partly autobiographical album tells the story of B.I.G.'s experiences as a young criminal.  "Ready to Die" was the only studio album released during his life, as he was murdered sixteen days prior to the release of his second album, "Life After Death" in 1997.

Craig Mack: Craig Mack (born May 10, 1971) is an American rapper, who gained fame on Puff Daddy's Bad Boy Entertainment record label in the 1990s.  Although his first single was released under the name MC EZ in 1988, he is best known for his 1994 hit single "Flava In Ya Ear", which was released under his real name.  The remix of the single was the breakout appearance of The Notorious B.I.G., as well as one of the first solo appearances by Busta Rhymes.  The success of The Notorious B.I.G.'s debut album "Ready to Die" overshadowed Mack's early success on the Bad Boy label.

Victory (Puff Daddy song): "Victory" is a song recorded by American hip hop recording artist Puff Daddy.  The song was originally written by The Notorious B.I.G., Jason Phillips and Steven Jordan for his debut studio album "No Way Out" (1997).  It features heavy use of mafioso-style lyrics, as was popular at the time.  It features The Notorious B.I.G., who raps two verses, and Busta Rhymes, who raps the song's chorus.  The song also heavily sampled the Bill Conti song "Going the Distance", which featured on the soundtrack to the movie "Rocky" making it a darker start to a rap album that featured many (at the time) club-standard singles.  The song was released as a single in 1998, peaking at number 19 on the "Billboard" Hot 100.  This song featured the very last verses recorded by The Notorious B.I.G. before his 1997 death as these verses were recorded a day before his shooting.  The song was used for the video game by 2K Sports, "NBA 2K13" by Puff Daddy and the Family featuring The Notorious B.I.G. and Busta Rhymes.  This was re-used for the soundtrack of NBA 2K18.

Nasty Girl (The Notorious B.I.G. song): "Nasty Girl" is a song by rapper The Notorious B.I.G.  It was released in 2005 in the US and on January 16, 2006 in the UK.  The single reached #1 in the United Kingdom (this being his first #1 in the country, just under a year after "rival" rapper 2Pac had also achieved his first #1 there also with "Ghetto Gospel").  The song features guest appearances from Jagged Edge, P. Diddy, Avery Storm, and Nelly and the video also contains guest appearances from Pharrell, Usher, Fat Joe, 8 Ball & MJG, Teairra Mari, Jazze Pha, DJ Green Lantern, Naomi Campbell and Memphis Bleek.  It can be found on the album "", a remixed album of Biggie Smalls' work.  The lyrical section rapped by Notorious B.I.G is actually lifted from another of his songs called "Nasty Boy", featured on his second album "Life After Death".  Despite this, the production to the song "Nasty Boy" is completely different from that for "Nasty Girl", and apart from the lyrical sample, and the second verse (rapped by P. Diddy) rapped in the style of Biggie's second verse of Nasty Boy, the two songs bear no similarities.  The chorus, sung by Jagged Edge, which has the line "Grab your titties for B.I.G.", references "Player's Anthem", which he says "Bitches, rub your titties if you love Big Poppa".

The Untouchable: The Untouchable is the fourth studio album by American rapper Scarface.  The album was released on March 11, 1997, by Rap-a-Lot Records.  The album debuted at number one on the "Billboard" 200 chart for the first time in his career with the album; in addition it peaked at the top of the Top R&B/Hip-Hop Albums chart for two weeks, giving Scarface his second number one album there.  The effort included the smash hit single, "Smile", featuring Tupac Shakur, released shortly after the shooting deaths of Tupac and Notorious B.I.G..  It peaked at number 12 on the "Billboard" Hot 100 and is the only single released by Scarface to go Gold.

Who Shot Ya?: "Who Shot Ya?"  is a controversial hip-hop song by The Notorious B.I.G., a B-side to his 1995 hit single, "Big Poppa".  The track was later released on the posthumous album "Born Again", the remastered edition of "Ready to Die", and "The Greatest Hits".

What'cha Wanna Do (Pras Michel song): "What'cha Wanna Do" is a hip-hop song by Pras Michel, released as the fourth single from his debut solo studio album, "Ghetto Supastar".  The track features vocals from American group The Product G&B and rapper Free.  The single was due to be released on September 28, 1998, but was pulled, and a last minute replacement, "Blue Angels", was released instead.  The single was later released in the United States in January 1999, and a music video was filmed.  The single was scheduled for release in the United Kingdom in February 1999, but was once again pulled.  Some copies of the single found their way onto the shelves.  The music video features Michel performing the song in a club, surrounded by people.  It also shows him visiting a camp on Hawaii beach, and performing in between a group of girls, surrounded by palm trees.  The Product G&B make an appearance in the video.

Mo Money Mo Problems: "Mo Money Mo Problems" is a single by The Notorious B.I.G., the second single from his album "Life After Death".  Released posthumously, the single topped the "Billboard" Hot 100 for two weeks in 1997, replacing "I'll Be Missing You" from the chart, Puff Daddy's tribute to the rapper's death himself.  The song is Notorious B.I.G.'s second posthumous number one single, following "Hypnotize", making him the only artist in Hot 100 history to have two #1 singles posthumously.  It was the sixth song to hit #1 posthumously for a credited artist.  The song was nominated for the 1998 Grammy Award for Best Rap Performance by a Duo or Group.

Question: Who Shot Ya?, is a controversial hip-hop song by The Notorious B.I.G., the track was later released on the posthumous album "Born Again", the remastered edition of which debut studio album by American rapper The Notorious B.I.G.; it was released on September 13, 1994?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "artist": {
      "type": "string",
      "description": "The artist who released the album."
    },
    "release_date": {
      "type": "string",
      "description": "The original release date of the album."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album, e.g., 'debut studio album'."
    },
    "record_labels": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of record labels that released the album."
    },
    "remastered_edition_track_inclusion": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Tracks later included on the remastered edition of the album."
    }
  },
  "required": [
    "album_title",
    "artist",
    "release_date",
    "album_type",
    "record_labels",
    "remastered_edition_track_inclusion"
  ],
  "additionalProperties": false
}
