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
List of awards and nominations received by U2: This is a comprehensive list of major music awards received by U2, an Irish rock band that formed in 1976, and whose members are Adam Clayton, Bono, The Edge, and Larry Mullen, Jr. U2 have been one of the most popular acts in the world since the mid-1980s.  The band has sold more than 145 million albums worldwide and has won 22 Grammy Awards, more than any other rock band.

One (U2 song): "One" is a song by Irish rock band U2.  It is the third track from their 1991 album "Achtung Baby", and it was released as the record's third single in February 1992.  During the album's recording sessions at Hansa Studios in Berlin, conflict arose between the band members over the direction of U2's sound and the quality of their material.  Tensions almost prompted the band to break up until they achieved a breakthrough with the improvisation of "One"; the song was written after the band members were inspired by a chord progression that guitarist the Edge was playing in the studio.  The lyrics, written by lead singer Bono, were inspired by the band members' fractured relationships and the German reunification.  Although the lyrics ostensibly describe "disunity", they have been interpreted in other ways.

Melon: Remixes for Propaganda: Melon: Remixes for Propaganda is a compilation of remixes released by Irish rock band U2 exclusively to members of the band's magazine/fan club, "Propaganda," in spring 1995.  Some of the remixes were previously available on singles and some have been re-released on later singles and compilations, while some remain exclusive to this set.  The title "Melon" is an anagram of "Lemon," which is a reference to U2's song of the same name that appears on two tracks of the album.

Zoo TV Live: Zoo TV Live is a live album by the Irish rock band U2.  It was released exclusively to subscribing members of U2's official site, replacing "U2.COMmunication" on 20 November 2006.  This double CD features the same material that is on the "" VHS and DVD releases, as well as one bonus track from the Zoo TV special, "Tryin' to Throw Your Arms Around the World."  Although U2's website refers to the album as ZOO2Live, the album is titled "Zoo TV Live" according to the actual CDs.  This album was discontinued from the website for the release of "" in 2007.  Recently for the U2.com 2012/13 subscriber offer, the album was included as part of a 'bundle' edition along with U22 and 11 instant downloads from U22.

Medium, Rare &amp; Remastered: Medium, Rare & Remastered is a compilation album of rarities and remastered tracks by the Irish rock band U2.  It was released exclusively to subscribing members of U2.com, replacing "" on 22 February 2009.  The double CD features tracks that were released as part of The Complete U2 digital box set, the bonus discs on the remastered albums to date, and some readily available single B-sides.

From the Sky Down: From the Sky Down is a 2011 American documentary film directed by Davis Guggenheim about rock band U2 and the production of their 1991 album "Achtung Baby".  The film documents the album's difficult recording period, the band members' relationships, and the group's creative process.  Guggenheim, who was commissioned by U2 to create the film to commemorate the record's 20th anniversary, spent several months in 2011 developing the documentary.  The band were filmed during a return visit to Hansa Studios in Berlin where parts of the album were recorded, and during rehearsals in Winnipeg for the Glastonbury Festival 2011.  The film contains unreleased scenes from the group's 1988 motion picture "Rattle and Hum", along with archival footage and stills from the "Achtung Baby" recording sessions.  Development of the album's emblematic song "One" is recounted through the replaying of old recording tapes.

U2 by U2: U2 by U2 is an autobiography written by the members of Irish rock band U2 and first published in London by HarperCollins in 2005.  Bono, The Edge, Adam Clayton, and Larry Mullen Jr. collaborated with their friend Neil McCormick, a staff music writer for "The Daily Telegraph" to write the only authorized biography of the band.  It portrays the story of U2 in their own words and pictures.

The LaFontaines: The LaFontaines are a Scottish band from Motherwell, North Lanarkshire, formed in 2010.  The band consists of Kerr Okan (lead vocals), Jamie Keenan (drums, vocals), John Gerard (bass, vocals), Iain Findlay (guitar), and Darren McCaughey (guitar, keyboard).  Their style is a unique blend of hip hop, rock and pop.  The band are named after American voice actor Don LaFontaine.

U2.Communication: U2.COMmunication is a live album recorded by U2 and released exclusively to members of its official website in 2005.  The album features performances from two different concerts from the Vertigo Tour—a concert in Chicago, filmed for the "" video, and a concert in Milan filmed for the "" video which was released with deluxe copies of the compilation album, "U218 Singles".  The album's title is a play on U2.COM, the band's website.

U2: U2 are an Irish rock band from Dublin formed in 1976.  The group consists of Bono (lead vocals and rhythm guitar), the Edge (lead guitar, keyboards, and backing vocals), Adam Clayton (bass guitar), and Larry Mullen Jr. (drums and percussion).  Initially rooted in post-punk, U2's musical style evolved throughout their career, yet has maintained an anthemic sound built on Bono's expressive vocals and the Edge's effects-based guitar textures.  Their lyrics, often embellished with spiritual imagery, focus on personal and sociopolitical themes.  Popular for their live performances, the group have staged several ambitious and elaborate tours over their career.

Question: Which band has more members, U2 or The LaFontaines?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_with_more_members": {
      "type": "string",
      "description": "The name of the band that has more members."
    },
    "bands_details": {
      "type": "array",
      "description": "Details for each band compared, including their name and member count.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "member_count": {
            "type": "integer",
            "description": "The number of members in the band."
          }
        },
        "required": [
          "band_name",
          "member_count"
        ],
        "additionalProperties": false
      }
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement summarizing which band has more members."
    }
  },
  "required": [
    "band_with_more_members",
    "bands_details",
    "comparison_result"
  ],
  "additionalProperties": false
}
