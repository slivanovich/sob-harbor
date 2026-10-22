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
Catatonia (band): Catatonia were an alternative rock band from Wales who gained popularity in the mid- to late 1990s.  The band formed in 1992 after Mark Roberts met Cerys Matthews.  The first major lineup featured Dafydd Ieuan on drums, Clancy Pegg on keyboard, Owen Powell on guitar and Paul Jones on bass.  They recorded two EPs, "For Tinkerbell" and "Hooked".

Road Rage (Catatonia song): "Road Rage" is a song recorded by the Welsh band Catatonia, taken from their second studio album, "International Velvet".  It was written by band member Mark Roberts, with the production credit given generally to the band.  "Road Rage" was released as the third single from the album, following their break-out success with the song "Mulder and Scully".  The title "Road Rage" was based on the murder of Lee Harvey by his girlfriend Tracie Andrews in December 1996, something for which singer Cerys Matthews later apologised to Harvey's mother.

Never Said Goodbye: Never Said Goodbye is the second solo studio album by Welsh singer-songwriter Cerys Matthews.  It was released on 21 August 2006 by Rough Trade Records.

Larry Adler: Lawrence "Larry" Cecil Adler (February 10, 1914 – August 6, 2001) was an American musician, one of the world's most skilled harmonica players.  Ralph Vaughan Williams, Malcolm Arnold, Darius Milhaud and Arthur Benjamin composed for him.  During his later career he collaborated with Sting, Elton John, Kate Bush and Cerys Matthews.

RPA &amp; The United Nations of Sound: RPA & The United Nations of Sound are a British alternative rock band formed by vocalist Richard Ashcroft, former lead singer of The Verve.  Ashcroft announced the formation of the band (which is a pseudonym more than a real band) and presented the video of the first single, "Are You Ready?" , on 18 January 2010 in an exclusive premiere on the "NME" website.  "Are You Ready?"  was released only in the UK on 1 April 2010 in a limited edition 12" vinyl.  On 9 April 2010 the band released a fanclub-only track, "Third Eye (Colombus Circle)".  In the first two weeks of June Ashcroft and his musicians completed a European tour (Ancona, Paris, Berlin, Cologne, Amsterdam, Manchester and London), then they played in Tokyo and Osaka on 7–8 August 2010 during the Summer Sonic Festival 2010 and also in Melbourne and Sydney respectively on 30 July and 31 July.  The band played in Australia also during the Splendour in the Grass Festival in late July.  The band's debut album as Richard's backing lineup, entitled "United Nations of Sound", was released on 19 July 2010.  "Born Again", the first proper single, was officially released the same day of the album as a digital download.

Cerys Matthews: Cerys Elizabeth Matthews, MBE ( ; born 11 April 1969) is a Welsh singer, songwriter, author, and broadcaster.  She was a founding member of Welsh rock band Catatonia and a leading figure in the "Cool Cymru" movement of the late 1990s.

United Nations of Sound (album): United Nations of Sound is the debut album by British alternative rock band RPA & The United Nations of Sound (pseudonym of Richard Ashcroft, arrived at his fourth solo album), released on 19 July 2010 through Parlophone (see 2010 in British music).  The album was released in the United States on 22 March 2011 under the name "Richard Ashcroft" through the record company Razor & Tie.

Catatonia Greatest Hits: Catatonia's Greatest Hits is a compilation of the band's best known songs, mainly the singles, but also included collaborations between Cerys Matthews with Space (on "The Ballad of Tom Jones") and with Tom Jones himself (on "Baby, It's Cold Outside").

Richard Ashcroft: Richard Paul Ashcroft (born 11 September 1971) is an English singer and songwriter.  He was the lead singer and occasional rhythm guitarist of the alternative rock band The Verve from their formation in 1990 until their original split in 1999.  He became a successful solo artist in his own right, releasing three UK top three solo albums.  The Verve reformed in 2007 but again broke up by summer 2009.  Ashcroft then founded a new band, RPA & The United Nations of Sound, and released a new album on 19 July 2010.  On 22 February 2016 Ashcroft announced his fourth solo album, "These People", set for release 20 May 2016.  Chris Martin of Coldplay has described Ashcroft as "the best singer in the world".

Jeff Irwin: Jeff Irwin (a.k.a. "the Yeti", born September 12, 1977) is an American, East Nashville, Tennessee based multi-instrumentalist.  He has performed with Griffin House, Cerys Matthews, Derek Webb and Sandra McCracken, Mat Kearney, Taylor Sorensen & the Trigger Code, and many others including Counting Crows.

Question: Are Richard Ashcroft and Cerys Matthews both authors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_authors": {
      "type": "boolean",
      "description": "True if both individuals are authors, false otherwise."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_author": {
            "type": "boolean",
            "description": "True if the individual is identified as an author in the context."
          },
          "known_professions": {
            "type": "array",
            "description": "Other professions or roles attributed to the individual in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "is_author",
          "known_professions"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the answer based on the context."
    }
  },
  "required": [
    "are_both_authors",
    "individuals",
    "reasoning"
  ],
  "additionalProperties": false
}
