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
Scott Shiflett: Scott David Shiflett (born August 22, 1966) is an American musician who has been the bassist in the punk rock band Face to Face since 1995.  Born in Santa Barbara, California, he is the brother of Foo Fighters lead guitarist Chris Shiflett.  Scott has also performed in the bands Viva Death, Me First and the Gimme Gimmes, Jackson United, and 22 Jacks.

Foo Fighters discography: The discography of Foo Fighters, an American rock band formed in 1994 by Dave Grohl, consists of nine studio albums, four extended plays (EPs), six video albums, and 36 singles.  The current Foo Fighters line-up consists of Grohl (vocals and guitar), Taylor Hawkins (drums), Rami Jaffee (keyboard), Nate Mendel (bass), Chris Shiflett (guitar), and Pat Smear (guitar).

Glitter in the Gutter: Glitter in the Gutter is singer-songwriter Jesse Malin's third studio album, released on Adeline Records on March 20, 2007.  "Glitter in the Gutter" includes Malin's cover of The Replacements' "Bastards of Young," and the album features guest appearances from Bruce Springsteen (backing vocals on "Broken Radio"), Jakob Dylan (backing vocals on "Black Haired Girl"), Josh Homme, and Chris Shiflett of Foo Fighters and Me First and the Gimme Gimmes.  Jesse Malin's good friend Ryan Adams guests on several tracks as well.

Chris Shiflett &amp; the Dead Peasants: Chris Shiflett & the Dead Peasants is the debut self-titled album from Chris Shiflett, lead guitarist of Foo Fighters.  The Dead Peasants are his second side project, following Jackson United, and the backing band is composed of different musicians than that of Jackson United.

Exhausted (song): "Exhausted" is the first Foo Fighters release and the lead single from the debut album.  It was only issued as a promotional single, pressed on black 12" vinyl.  The song is notable for being the first original Foo Fighters track released to the public, when it premiered January 8, 1995 on Eddie Vedder's Self-Pollution Radio broadcast.

List of Foo Fighters band members: Foo Fighters is an American alternative rock band formed by multi-instrumentalist and vocalist Dave Grohl in 1994.  After recording the album "Foo Fighters" alone, Grohl enlisted guitarist Pat Smear, bassist Nate Mendel and drummer William Goldsmith to join the band.  This lineup recorded the second Foo Fighters album, 1997's "The Colour and the Shape", although most of Goldsmith's drum recordings were removed and re-recorded by Grohl for the release, after he left the band due to creative tensions.  Goldsmith was replaced by Taylor Hawkins, and Franz Stahl replaced Smear after he also departed, although he only remained in the band for a short period and did not record an album with the group.  The group's third album, "There Is Nothing Left to Lose", featured Hawkins on drums and was released in 1999.

All My Life (Foo Fighters song): "All My Life" is a song by the American band Foo Fighters, released as the first single from their fourth album, "One by One".  The song won a Grammy Award for Best Hard Rock Performance, and spent ten straight weeks at number 1 on the Hot Modern Rock Tracks chart and it peaked at number 3 on the Hot Mainstream Rock Tracks chart.  It was also a top 5 hit on the UK Singles Chart.

Miracle (Foo Fighters song): "Miracle" is the fifth single released from the fifth Foo Fighters album, "In Your Honor".  It was released as a promotional single only and no retail single was released.  John Paul Jones from Led Zeppelin plays piano on this song.

One by One (Foo Fighters album): One by One is the fourth studio album by American rock band Foo Fighters, released on October 22, 2002 by RCA.  The album is the first to feature guitarist Chris Shiflett.  Production on the album was troubled, with initial recording sessions considered unsatisfying and raising tensions between the band members.  They eventually decided to redo the album from scratch during a two-week period at frontman Dave Grohl's home studio in Alexandria, Virginia.  The songs on the album, which include the successful singles "All My Life" and "Times Like These", have been noted for their introspective lyrics and a heavier and more aggressive sound compared to the band's earlier work, which Grohl said was intended to translate the energy of the Foo Fighters' live performances into a recording.

Songs from the Laundry Room: Songs from the Laundry Room is an EP by American rock band Foo Fighters, released exclusively for Record Store Day 2015.  This EP and the Foo Fighters album are the two Foo Fighters releases upon which Dave Grohl plays all the instruments.

Question: What award did a single from the first Foo Fighters album to feature Chris Shiflett win?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the Foo Fighters album that first featured Chris Shiflett."
    },
    "album_release_year": {
      "type": "integer",
      "description": "The release year of the album."
    },
    "featured_musician": {
      "type": "string",
      "description": "The name of the musician whose first album with the band is being identified."
    },
    "single_details": {
      "type": "object",
      "properties": {
        "single_name": {
          "type": "string",
          "description": "The name of the single from the identified album."
        },
        "award_won": {
          "type": "string",
          "description": "The name of the award won by the single."
        },
        "award_category": {
          "type": "string",
          "description": "The specific category of the award won."
        }
      },
      "required": [
        "single_name",
        "award_won",
        "award_category"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_name",
    "album_release_year",
    "featured_musician",
    "single_details"
  ],
  "additionalProperties": false
}
