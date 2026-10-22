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
Pearl Jam: Pearl Jam is an American rock band formed in Seattle, Washington, in 1990.  Since its inception, the band's line-up has consisted of Eddie Vedder (lead vocals), Mike McCready (lead guitar), Stone Gossard (rhythm guitar) and Jeff Ament (bass).  The band's fifth member is drummer Matt Cameron (also of Soundgarden), who has been with the band since 1998.  Boom Gaspar (piano) has also been a session/touring member with the band since 2002.  Drummers Dave Krusen, Matt Chamberlain, Dave Abbruzzese and Jack Irons are former members of the band.

Riot Act (album): Riot Act is the seventh studio album by American rock band Pearl Jam, released on November 12, 2002 through Epic Records.  Following a full-scale tour in support of its previous album, "Binaural" (2000), Pearl Jam took a year-long break.  The band then reconvened in the beginning of 2002 and commenced work on a new album.  The music on the record featured a diverse sound, including songs influenced by folk, art rock, and experimental rock.  The lyrics deal with mortality and existentialism, with much influence from both the political climate after the September 11, 2001 terrorist attacks and the accidental death of nine fans during Pearl Jam's performance at the 2000 Roskilde Festival.

Taylor Momsen: Taylor Michel Momsen (born July 26, 1993) is an American singer, songwriter, former actress, and model.  She is known for being the lead singer and frontwoman of the American rock band The Pretty Reckless.  She is also known for portraying the character of Jenny Humphrey on the CW teen drama series "Gossip Girl" (2007–2012) and Cindy Lou Who in the film "Dr. Seuss' How the Grinch Stole Christmas" (2000).

Pearl Jam (album): Pearl Jam (sometimes referred to as The Avocado Album or simply Avocado) is the eighth studio album by American alternative rock band Pearl Jam, released on May 2, 2006 on J Records.  It was the first and only release for J Records, their last album issued by Sony Music.  It was the band's first full-length studio release in almost four years, since "Riot Act" (2002).  Following their performances at the Vote For Change tour in 2004, the band commenced work on "Pearl Jam" in November 2004 at Studio X in Seattle, Washington and finished in February 2006.

Save You (Pearl Jam song): "Save You" is a song by the American rock band Pearl Jam, released on February 11, 2003 as the second single from the band's seventh studio album, "Riot Act" (2002).  Although credited to all members of Pearl Jam, it features lyrics written by vocalist Eddie Vedder and music primarily written by guitarist Mike McCready.  The song peaked at number 23 on the "Billboard" Mainstream Rock Tracks chart.  The song was included on Pearl Jam's 2004 greatest hits album, "rearviewmirror (Greatest Hits 1991–2003)".

Animal (Pearl Jam song): "Animal" is a song by the American rock band Pearl Jam, released in 1994 as the third single from the band's second studio album, "Vs." (1993).  Although credited to all members of Pearl Jam, it features lyrics written by vocalist Eddie Vedder and music primarily written by guitarist Stone Gossard.  The song peaked at number 21 on the "Billboard" Mainstream Rock Tracks chart.  The song was included on Pearl Jam's 2004 greatest hits album, "rearviewmirror (Greatest Hits 1991–2003)".

Daughter (song): "Daughter" is a song by the American rock band Pearl Jam, released in 1993 as the second single from the band's second studio album, "Vs." (1993).  Although credited to all members of Pearl Jam, it features lyrics written by vocalist Eddie Vedder and music primarily written by guitarist Stone Gossard.  The song topped both the Mainstream Rock and Modern Rock "Billboard" charts.  The song spent a total of eight weeks at number one on the Mainstream Rock chart.  "Daughter" eventually peaked at number 28 on the Top 40 Mainstream chart, becoming the band's first Top 40 single.  The song was included on Pearl Jam's 2004 greatest hits album, "rearviewmirror (Greatest Hits 1991–2003)".

Backspacer: Backspacer is the ninth studio album by the American alternative rock band Pearl Jam, released on September 20, 2009.  The bandmembers started writing instrumental and demo tracks in 2007, and got together in 2008 to work on an album.  It was recorded from February through April 2009 with producer Brendan O'Brien, who had worked on every Pearl Jam album except their 1991 debut "Ten" and 2006's self-titled record—although this was his first production credit since 1998's "Yield".  Material was recorded in Henson Recording Studios in Los Angeles, California and O'Brien's own Southern Tracks Recording in Atlanta, Georgia.  The music on the album—the shortest of the band's career—features a sound influenced by pop and new wave.  The lyrics have a more optimistic look than the ones in the politic-infused predecessors "Riot Act" and "Pearl Jam", something frontman Eddie Vedder attributed to the election of Barack Obama.

Vitalogy: Vitalogy is the third studio album by the American rock band Pearl Jam, released on November 22, 1994, through Epic Records.  Pearl Jam wrote and recorded "Vitalogy" while touring behind its previous album "Vs." (1993).  The music on the record was more diverse than previous releases, and consists of aggressive rock songs, ballads and other elements making this Pearl Jam's first experimental album.

Life Wasted: "Life Wasted" is a song by the American rock band Pearl Jam.  Featuring lyrics written by vocalist Eddie Vedder and music written by guitarist Stone Gossard, "Life Wasted" was released on August 28, 2006 as the second single from the band's eighth studio album, "Pearl Jam" (2006).  The song peaked at number 10 on the "Billboard" Modern Rock Tracks chart.  On "Pearl Jam", "Life Wasted" is reprised as a modified version on the album's tenth track, "Wasted Reprise".

Question: Are both Pearl Jam and Taylor Momsen involved in American music?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_involved_in_american_music": {
      "type": "boolean",
      "description": "True if both entities are involved in American music, false otherwise."
    },
    "entities": {
      "type": "array",
      "description": "Details about each entity mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "type": {
            "type": "string",
            "description": "The type of entity (e.g., 'band', 'artist')."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the entity."
          },
          "musical_involvement": {
            "type": "string",
            "description": "Description of the entity's involvement in music."
          }
        },
        "required": [
          "name",
          "type",
          "nationality",
          "musical_involvement"
        ],
        "additionalProperties": false
      }
    },
    "conclusion_reasoning": {
      "type": "string",
      "description": "A brief explanation for the conclusion."
    }
  },
  "required": [
    "is_involved_in_american_music",
    "entities",
    "conclusion_reasoning"
  ],
  "additionalProperties": false
}
