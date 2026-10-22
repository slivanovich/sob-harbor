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
Grandmaster Melle Mel and the Furious Five: Grandmaster Melle Mel and the Furious Five was released in 1984 by Sugarhill Records after the split between Grandmaster Flash and Melle Mel.  For this album, Melle Mel kept the group name 'the Furious Five' (although the line-up changed) and used the title 'Grandmaster'.  Rappers Cowboy and Scorpio left with Melle Mel although Mel's brother The Kidd Creole (N. Glover) and Rahiem remained with Flash.  New rappers King Lou, Kami Kaze, and Tommy Gunn joined, as did Flash's best friend E. Z. Mike as DJ.

Old School Flava: Old School Flava is the second album by the old school rap group, Treacherous Three.  It was released in 1994 for Wrap Records and was produced by DJ Easy Lee, DJ Clark Kent, T La Rock, Ced Gee, Rahiem, Special K, Kool Moe Dee and LA Sunshine.  Guests include Big Daddy Kane, Chuck D and Heavy D.

Essential Cuts: Essential Cuts is a budget compilation album by Grandmaster Flash and the Furious Five released on CD in 2005.  Although titled to Grandmaster Flash alone, it does not contain any tracks from Flash's later Elektra Records albums and mainly features tracks from "The Message" era.

The Greatest Mixes: The Greatest Mixes is a remix compilation album by Grandmaster Flash and the Furious Five originally released by Sanctuary Records in 1997 in the United Kingdom.  It contains rare non-album tracks and new and original remixes from both Grandmaster Flash and the Furious Five and Grandmaster Melle Mel.

They Said It Couldn't Be Done: They Said It Couldn't Be Done is the third album released by Grandmaster Flash, which followed the breakup of the Furious Five because of the departure of rappers Melle Mel, Scorpio, and Keith Cowboy.  For "They Said It Couldn't Be Done", Flash signed with Elektra Records and retained the services of Rahiem and The Kidd Creole.  New rappers Lavon (Kevin LaVon Dukes), Mr Broadway (Russell Wheeler), and dancer Larry Love (Larry Parker) were added.  It was originally released in April 1985.  It was re-issued on CD in the US for the first time in 2005 (DBK Works dbk514). It was the first album the group released on a major label.  It was produced by Gavin Christopher and Grandmaster Flash (the group).  The album also included "Girls Love the Way He Spins," "Sign of the Times" "Paradise," and "Rock the House (Alternate Groove)."  It was the first hip hop album released by Elektra Records.

Hip Hop Galsen: Quickly, podiums enlarged their performances from dancers only to rappers as well.  It was a time when soon-to-be hip hop artists were still mimicking American artists they actively used to listen to such Africa Bambaataa, Grandmaster Flash, Furious Five, Delight, Doug E. Fresh or Public Enemy for the most well-known.  Indeed, rap, the MC performance, was still then a phonetic repetition, a copycatting of either American rappers or, with Hip Hop booming in France in the 1980s, of French hip hop artists such as Assassin, NTM, IAM or Mc Solaar.  Without the real capacity for translating the movement and its expressions in Senegalese terms yet, the mid-1980s in Dakar were however definitively hip hop.  And whenever the classical hip hop film Beat Street was circulating in local cinemas, young people were following the movie from showroom to showroom in order to view it again and again and to know by heart the famous lyrics of Grandmaster Flash.

Grandmaster Flash &amp; the Furious Five (album): Grandmaster Flash & The Furious Five is a compilation album release by Grandmaster Flash & the Furious Five ("On The Strength" is their official second album).  It was released in July 1983, and it is a compilation of their Sugar Hill Records hit singles including "The Message", "New York New York and "White Lines".  Over half of the tracks were single-only releases prior to this compilation.

Grandmaster Flash and the Furious Five: Grandmaster Flash and the Furious Five were an American hip hop group formed in the South Bronx of New York City in 1976.  Composed of one DJ (Grandmaster Flash) and five rappers (Melle Mel, The Kidd Creole, Keith Cowboy, Mr. Ness/Scorpio, and Rahiem), the group's use of turntablism, break-beat deejaying, and conscious lyricism were significant in the early development of hip hop music.

The Official Adventures of Grandmaster Flash: The Official Adventures of Grandmaster Flash is a DJ mix album by Grandmaster Flash and was released in January 2002.  It is a mix album consisting of interview snippets, newly recorded old school hip hop mixes, live Grandmaster Flash and the Furious Five segments and four other tracks by various artists that were popular in Flash's early DJ repertoire.

New York New York (Grandmaster Flash song): New York New York is a 1983 song by Grandmaster Flash and the Furious Five off their compilation albums Grandmaster Flash & The Furious Five (1983) and Greatest Messages (1984).  It made #17 on the R&B Singles chart, #49 on the New Zealand Singles Chart and #82 on the UK Singles Chart.

Question: What kind of music did Old School Flava and Grandmaster Flash and the Furious five create?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "music_genre": {
      "type": "string",
      "description": "The primary music genre that applies to both groups."
    },
    "groups_involved": {
      "type": "array",
      "description": "Details about each group and how their genre is described in the context.",
      "items": {
        "type": "object",
        "properties": {
          "group_name": {
            "type": "string",
            "description": "The name of the music group."
          },
          "genre_description_in_context": {
            "type": "string",
            "description": "The specific term or phrase used in the context to describe the group's genre."
          }
        },
        "required": [
          "group_name",
          "genre_description_in_context"
        ],
        "additionalProperties": false
      }
    },
    "genre_commonality_note": {
      "type": "string",
      "description": "A note explaining the relationship between the genre terms used for the groups."
    }
  },
  "required": [
    "music_genre",
    "groups_involved",
    "genre_commonality_note"
  ],
  "additionalProperties": false
}
