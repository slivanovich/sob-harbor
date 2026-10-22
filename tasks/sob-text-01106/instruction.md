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
Pearl Jam Official Bootlegs: The Pearl Jam "Official" Bootlegs are a large, continually growing series of live albums by the American alternative rock band Pearl Jam.  Pearl Jam noted the desire of fans to own a copy of the shows they attended and the popularity of bootleg recordings.  The band had been open in the past about allowing fans to make amateur recordings, and these "official bootlegs" were an attempt to provide a more affordable and better quality product for fans.  The band has sold more than 3.5 million copies of shows since launching the bootleg series in 2000.  The official bootlegs are a complete record of almost every show the band plays, excluding club "warm-up" dates.

Elderly Woman Behind the Counter in a Small Town: "Elderly Woman Behind the Counter in a Small Town" is a song by the American rock band Pearl Jam.  The song is the tenth track on the band's second studio album, "Vs." (1993).  Although credited to all members of Pearl Jam, it was primarily written by vocalist Eddie Vedder.  The length of the song's title was a reaction by the band to the fact that most of its songs featured one-word titles.  The song is often referred to simply as "Small Town" by the band and its fans.  Despite the lack of a commercial single release, the song managed to reach number 17 on the "Billboard" Modern Rock Tracks chart.  An acoustic version of the song can be found on the "Go" single.  The song was included on Pearl Jam's 2004 greatest hits album, "rearviewmirror (Greatest Hits 1991–2003)".  The song was used in promos for the final season of "Rescue Me".

Pearl Jam (album): Pearl Jam (sometimes referred to as The Avocado Album or simply Avocado) is the eighth studio album by American alternative rock band Pearl Jam, released on May 2, 2006 on J Records.  It was the first and only release for J Records, their last album issued by Sony Music.  It was the band's first full-length studio release in almost four years, since "Riot Act" (2002).  Following their performances at the Vote For Change tour in 2004, the band commenced work on "Pearl Jam" in November 2004 at Studio X in Seattle, Washington and finished in February 2006.

Rearviewmirror: "Rearviewmirror" is a song by the American rock band Pearl Jam.  The song is the eighth track on the band's second studio album, "Vs." (1993).  Although credited to all members of Pearl Jam, it was primarily written by vocalist Eddie Vedder.  The song was included on Pearl Jam's 2004 greatest hits album, "rearviewmirror (Greatest Hits 1991–2003)".

No Devotion: No Devotion are a Welsh/American alternative rock band formed in 2014.  They are composed of American vocalist Geoff Rickly (of the band Thursday) from New Jersey, and former band members of the Welsh band Lostprophets.  The band formed in the wake of Lostprophets' dissolution in 2013.

Pearl Jam: Pearl Jam is an American rock band formed in Seattle, Washington, in 1990.  Since its inception, the band's line-up has consisted of Eddie Vedder (lead vocals), Mike McCready (lead guitar), Stone Gossard (rhythm guitar) and Jeff Ament (bass).  The band's fifth member is drummer Matt Cameron (also of Soundgarden), who has been with the band since 1998.  Boom Gaspar (piano) has also been a session/touring member with the band since 2002.  Drummers Dave Krusen, Matt Chamberlain, Dave Abbruzzese and Jack Irons are former members of the band.

Riot Act (album): Riot Act is the seventh studio album by American rock band Pearl Jam, released on November 12, 2002 through Epic Records.  Following a full-scale tour in support of its previous album, "Binaural" (2000), Pearl Jam took a year-long break.  The band then reconvened in the beginning of 2002 and commenced work on a new album.  The music on the record featured a diverse sound, including songs influenced by folk, art rock, and experimental rock.  The lyrics deal with mortality and existentialism, with much influence from both the political climate after the September 11, 2001 terrorist attacks and the accidental death of nine fans during Pearl Jam's performance at the 2000 Roskilde Festival.

Pearl Jam 2012 Tour: The Pearl Jam 2012 Tour was a concert tour by the American rock band Pearl Jam.  The first leg of the tour consisted of thirteen shows in Europe, including a headling appearance at the Isle of Wight Festival.  American punk band X were the opening band for the arena shows.  Due to high ticket demand for pre-sale tickets, the third-party website handling the sale had to be taken offline.  The Pearl Jam fanclub cited "an act of sabotage" to the site.  For the second show at the Ziggo Dome in Amsterdam, a fan of the band created the setlist.

Backspacer: Backspacer is the ninth studio album by the American alternative rock band Pearl Jam, released on September 20, 2009.  The bandmembers started writing instrumental and demo tracks in 2007, and got together in 2008 to work on an album.  It was recorded from February through April 2009 with producer Brendan O'Brien, who had worked on every Pearl Jam album except their 1991 debut "Ten" and 2006's self-titled record—although this was his first production credit since 1998's "Yield".  Material was recorded in Henson Recording Studios in Los Angeles, California and O'Brien's own Southern Tracks Recording in Atlanta, Georgia.  The music on the album—the shortest of the band's career—features a sound influenced by pop and new wave.  The lyrics have a more optimistic look than the ones in the politic-infused predecessors "Riot Act" and "Pearl Jam", something frontman Eddie Vedder attributed to the election of Barack Obama.

Daughter (song): "Daughter" is a song by the American rock band Pearl Jam, released in 1993 as the second single from the band's second studio album, "Vs." (1993).  Although credited to all members of Pearl Jam, it features lyrics written by vocalist Eddie Vedder and music primarily written by guitarist Stone Gossard.  The song topped both the Mainstream Rock and Modern Rock "Billboard" charts.  The song spent a total of eight weeks at number one on the Mainstream Rock chart.  "Daughter" eventually peaked at number 28 on the Top 40 Mainstream chart, becoming the band's first Top 40 single.  The song was included on Pearl Jam's 2004 greatest hits album, "rearviewmirror (Greatest Hits 1991–2003)".

Question: Was the band Pearl Jam or No Devotion formed before the year 2000?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_formed_before_2000": {
      "type": "boolean",
      "description": "True if any of the specified bands were formed before the year 2000."
    },
    "bands_info": {
      "type": "array",
      "description": "Information about the bands mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the band was formed."
          }
        },
        "required": [
          "band_name",
          "formation_year"
        ],
        "additionalProperties": false
      }
    },
    "bands_meeting_criteria": {
      "type": "array",
      "description": "Names of bands that were formed before the year 2000.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "band_formed_before_2000",
    "bands_info",
    "bands_meeting_criteria"
  ],
  "additionalProperties": false
}
