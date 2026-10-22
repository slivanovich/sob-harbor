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
Come Taste the Band: Come Taste The Band is the tenth studio album by the English rock band Deep Purple, originally released in October 1975.  It was co-produced and engineered by the band and longtime associate Martin Birch.  It is the only Deep Purple studio record featuring Tommy Bolin, who replaced Ritchie Blackmore on guitar and is also the final of three albums to feature Glenn Hughes on bass and David Coverdale on lead vocals, before Coverdale later left to form Whitesnake.

Coverdale•Page: Coverdale•Page was a musical collaboration featuring Whitesnake and former Deep Purple lead vocalist David Coverdale, and former Led Zeppelin guitarist Jimmy Page.

List of Whitesnake band members: Whitesnake are a British hard rock band originally from Middlesbrough.  Formed in 1978, initially as vocalist David Coverdale's backing band, the group originally featured guitarists Micky Moody and Bernie Marsden, bassist Neil Murray, drummer Dave Dowle and keyboardist Peter Solley, who released their first EP "Snakebite" in 1978.  Solley was replaced later in the year by Coverdale's former Deep Purple bandmate Jon Lord, while the group's drummer Ian Paice replaced Dowle in 1979 after the release of "Lovehunter".  Whitesnake was briefly put on hiatus in 1982, before returning later in the year with Mel Galley, Colin Hodgkinson and Cozy Powell in place of Marsden, Murray and Paice.  Shortly after the recording of "Slide It In", Hodgkinson was replaced by the returning Murray, while John Sykes also joined the band; both new members featured on the US reissue of the album, which featured re-recorded tracks.  Both Galley and Lord left the band shortly after the album's release.

Burton C. Bell: Burton Christopher Bell (born February 19, 1969) is an American musician and vocalist.  Bell is best known as co-founder and frontman of the metal band Fear Factory.  His singing style mixes clean and shouted vocals with death growls.

Restless Heart (Whitesnake album): Restless Heart is the ninth studio album recorded by Whitesnake.  This was their first new studio album since 1989's "Slip of the Tongue".  The CD remains unreleased in the US.  This album was to be a David Coverdale solo album, but record company pressure forced it to be released under the "David Coverdale & Whitesnake" moniker.

Coverdale•Page (album): Coverdale•Page is an album by Whitesnake lead vocalist David Coverdale and former Led Zeppelin and London session guitarist Jimmy Page (as Coverdale•Page), released by Geffen Records on 15 March 1993.  The album was recorded at Little Mountain Sound Studios in Vancouver, Criteria Studios in Miami, Highbrow Productions in Nevada and Abbey Road Studios, London.  Recording commenced in the fall of 1991 and concluded in early 1992.  It was produced by Jimmy Page, David Coverdale and Canadian record producer, Mike Fraser.

David Coverdale: David Coverdale (born 22 September 1951) is an English rock singer best known for his work with Whitesnake, a hard rock band he founded in 1978.  Before Whitesnake, Coverdale was the lead singer of Deep Purple from 1973 to 1976, after which he established his solo career.  A collaboration with Jimmy Page resulted in a 1993 album that was a commercial and critical success.  In 2016, Coverdale was inducted into the Rock and Roll Hall of Fame as a member of Deep Purple, giving one of the band's induction speeches.

White Snake (album): White Snake is the first solo album by David Coverdale, released in 1977.  Coverdale would use the album title as the name of his future band, first known as "David Coverdale's Whitesnake" and soon afterwards shortened to Whitesnake.

Snakebite (album): Snakebite is the first official release by the British hard rock band Whitesnake.  The original EP initially featured only four tracks and was released in the UK in June 1978 and never published in the US.  "Snakebite" was re-released in September 1978 as a Double Extended Play containing four extra studio tracks taken from David Coverdale's second solo album "Northwinds".  The EP sleeve is entitled "David Coverdale's Whitesnake" and features photographs of the live band in concert.  All tracks from the original EP also were used as bonus tracks on the 2006 remaster of Whitesnake's debut studio album "Trouble".

List of band members in David Coverdale's bands: David Coverdale is best known for his band Whitesnake.  Whitesnake emerged when Coverdale wanted to name his backing band on tour, before becoming a device for him to promote himself with though it remained his backing band and not a band in its own right.  Later Coverdale would return to solo work and would also work with Jimmy Page on a project.  Aside from Coverdale himself, there was a number of other overlaps in membership of these various groups.  To construct an accurate chronology of his backing band therefore, the line-ups for David Coverdale Band, Whitesnake and Coverdale-Page have been included.

Question: Are David Coverdale and Burton C. Bell both founders or co-founders of a band?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_founders": {
      "type": "boolean",
      "description": "Indicates if both individuals are founders or co-founders of a band."
    },
    "david_coverdale_founding_details": {
      "type": "object",
      "properties": {
        "is_founder": {
          "type": "boolean",
          "description": "True if David Coverdale founded a band."
        },
        "band_name": {
          "type": "string",
          "description": "The name of the band David Coverdale founded."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year David Coverdale founded the band."
        }
      },
      "required": [
        "is_founder",
        "band_name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "burton_c_bell_founding_details": {
      "type": "object",
      "properties": {
        "is_founder": {
          "type": "boolean",
          "description": "True if Burton C. Bell founded or co-founded a band."
        },
        "is_co_founder": {
          "type": "boolean",
          "description": "True if Burton C. Bell was a co-founder of a band."
        },
        "band_name": {
          "type": "string",
          "description": "The name of the band Burton C. Bell co-founded."
        }
      },
      "required": [
        "is_founder",
        "is_co_founder",
        "band_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "are_both_founders",
    "david_coverdale_founding_details",
    "burton_c_bell_founding_details"
  ],
  "additionalProperties": false
}
