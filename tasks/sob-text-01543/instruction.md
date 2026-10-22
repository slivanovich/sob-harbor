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
Listener (band): Listener is a spoken word rock band from Fayetteville, Arkansas.  Initially an underground hip hop project by Dan Smith, who used the moniker "Listener", the project evolved into a full-fledged rock band.  The current lineup consists of vocalist, trumpeter, and bassist Dan Smith, guitarist Jon Terrey, and drummer Kris Rochelle.

Circa Survive: Circa Survive is an American rock band from the Philadelphia suburb of Doylestown, formed in 2004.  The band, led by Anthony Green, consists of former members from Saosin, This Day Forward, and Taken.

Avalon (Anthony Green album): Avalon is the debut solo album by current Saosin and current Circa Survive, vocalist Anthony Green.  It was released August 5, 2008 on Photo Finish Records, with a US tour to coincide with its release.  Keith Goodwin, Tim Arnold, and Dan Schwartz (also known as the band Good Old War) have guest appearances on this record.  The album leaked in its entirety on August 1, 2008.  Anthony Green's Avalon is being made available on vinyl LP.  The package includes the limited Vinyl LP and Digital Remix CD of Avalon, remixes created by Colin Frangicetto of Circa Survive.

Bastille discography: The discography of Bastille, a British indie rock group, consists of two studio albums, three extended plays, ten singles and eight music videos. Originally a solo project by Dan Smith, Bastille was formed in 2010.  The band released its debut single "Flaws" / "Icarus" in July 2011 on the independent record label Young and Lost Club.  An extended play titled "Laura Palmer" followed later that year.  The critical success of the EP and extensive touring brought the group to the attention of Virgin Records, which signed them in December 2011.

Violent Waves: Violent Waves is the fourth studio album by the American rock band Circa Survive.  It was released on August 28, 2012.  As Circa Survive wanted a record that would capture the band's live sound, where they felt the magic of the band lay, they recorded the album in one week and produced it themselves.  Violent Waves is also Circa Survive's first and only album released without a record label.

Dan Smith (artist): Dan Smith is an American illustrator and graphic artist known for his distinctive "SMIF" signature, and his work for Wizards of the Coast, FASA, White Wolf, Steve Jackson Games, Iron Crown, Hasbro, Nintendo, Namco and others.  While known primarily as an illustrator, Dan Smith is also a designer of family card games, including "Battle of the Bands", Portable Adventures and the upcoming King of Crime.

The Amulet (album): The Amulet is the sixth studio album by American rock band Circa Survive, released on September 22, 2017.  The Amulet is Circa Survive's first album released through Hopeless Records, after departing their previous label, Sumerian Records.  As with previous Circa Survive albums, Esao Andrews created the album artwork.

Descensus (album): Descensus is the fifth studio album by the American rock band Circa Survive, released on November 24, 2014.  Descensus is Circa Survive's first album released through Sumerian Records, aside from the Deluxe CD/DVD version of the band's previous album, "Violent Waves" which was released on August 28, 2012.  As with Circa Survive's previous albums, Esao Andrews created the album artwork.

Appendage (EP): Appendage is Circa Survive's second EP.  It was released on November 30, 2010 through Atlantic Records.  It contains b-sides from the Blue Sky Noise sessions, as well as a demo of "Sleep Underground".  As with Circa Survive's previous three albums and EP, Esao Andrews created the artwork.

Bastille (band): Bastille (stylised as BΔSTILLE) are a British indie band formed in 2010.  The group began as a solo project by lead vocalist Dan Smith, but later expanded to include keyboardist Kyle Simmons, bassist and guitarist Will Farquarson, and drummer Chris Wood.  The name of the band derives from Bastille Day, which is celebrated on 14 July, the date of Smith's birthday.

Question: Which of the following groups is lead by vocalist Dan Smith: Circa Survive or Bastille?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "vocalist_in_question": {
      "type": "string",
      "description": "The name of the vocalist mentioned in the question."
    },
    "bands_evaluated": {
      "type": "array",
      "description": "A list of bands from the question, with details about their lead vocalist.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "is_led_by_vocalist_in_question": {
            "type": "boolean",
            "description": "True if this band is led by the vocalist in question, false otherwise."
          },
          "actual_lead_vocalist": {
            "type": "string",
            "description": "The name of the actual lead vocalist for this band."
          }
        },
        "required": [
          "band_name",
          "is_led_by_vocalist_in_question",
          "actual_lead_vocalist"
        ],
        "additionalProperties": false
      }
    },
    "answer_band_name": {
      "type": "string",
      "description": "The name of the band from the question that is led by the specified vocalist."
    }
  },
  "required": [
    "vocalist_in_question",
    "bands_evaluated",
    "answer_band_name"
  ],
  "additionalProperties": false
}
