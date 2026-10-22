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
Dresden Philharmonic: The Dresdner Philharmonie (unofficial English translation: Dresden Philharmonic) is a German symphony orchestra based in Dresden.  Its principal concert venue is the "Kulturpalast".  The orchestra also performs at the "Kreuzkirche", the Hochschule für Musik Dresden, and the Schloss Albrechtsberg.  It receives financial support from the city of Dresden.  The choral ensembles affiliated with the orchestra are the Dresden Philharmonic Choir and Dresden Philharmonic Chamber Choir.

Girl Anachronism: "Girl Anachronism" is a song by American dark cabaret duo The Dresden Dolls, released as a promo single from their self-titled debut album.  The lyrics, alternately angry, apologetic, and full of complaint, deal with Amanda Palmer, the band's lead singer, as a "problem child", a trait which she blames on the fact that she was born a few days premature, by Caesarean section.  As the song grows, the lyrics split into various subplots, all of which are related to feeling out of place or out of time.

Amanda Palmer: Amanda MacKinnon Gaiman Palmer ( ; born April 30, 1976), sometimes known as Amanda Fucking Palmer (AFP), is an American singer-songwriter who is the lead singer, pianist, and lyricist of the duo The Dresden Dolls.  She performs as a solo artist, and was also one-half of the duo Evelyn Evelyn, and the lead singer and songwriter of Amanda Palmer and the Grand Theft Orchestra.

The Dresden Dolls (EP): The Dresden Dolls is the self-titled debut EP by American dark cabaret band The Dresden Dolls, released in 2001.  It is a completely separate release from the band's 2003 debut studio album, also titled "The Dresden Dolls".

Coin-Operated Boy: "Coin-Operated Boy" is a single by The Dresden Dolls duo, taken from the self-titled debut album "The Dresden Dolls".  It was produced by Martin Bisi and released on December 13, 2004 by Roadrunner Records.  "Coin-Operated Boy" was written by Amanda Palmer.  The song makes heavy use of staccato, and includes instruments such as a toy piano.

The Dresden Dolls (album): The Dresden Dolls is the eponymous debut studio album by American Brechtian Punk Cabaret duo The Dresden Dolls.  It was recorded by Brooklyn producer Martin Bisi and released on 26 September 2003 on 8ft.  Records, the band's personal label.  Upon signing with Roadrunner Records, the album was re-released on April 27, 2004.  The enhanced CD included a video for "Girl Anachronism".  The album artwork was also modified to mask which record sleeves had been used in the album artwork.

The Dresden Dolls: The Dresden Dolls is an American musical duo from Boston, Massachusetts.  Formed in 2000, the group consists of Amanda Palmer (lead vocals and piano; additional: keyboards, harmonica, ukulele) and Brian Viglione (drums and percussion; additional: guitar, bass guitar, backing vocals).  The two describe their style as "Brechtian punk cabaret", a phrase invented by Palmer because she was "terrified" that the press would invent a name that "would involve the word "gothic"".  The Dresden Dolls are part of an underground dark cabaret movement that started gaining momentum in the early 2000s.

Sing (The Dresden Dolls song): "Sing" is the first single by The Dresden Dolls duo, taken from the second studio album "Yes, Virginia...".  It was never released in shops, only as a promo for radio stations.  The music video, directed by Michael Pope, prominently featured living statues and centered on the plotline of a video of the Dresden Dolls playing the song being sent to various people in different locations and occupations.  It also featured the band performing on a stage.

8in8: 8in8 is a supergroup comprising Ben Folds, Amanda Palmer, Neil Gaiman, and Damian Kulash of OK Go.  In 2011 they gathered together with the intention of writing and recording eight songs in eight hours, hence the name "8in8".  Aside from being friends, members of the group have various connections with each other: Neil Gaiman and Amanda Palmer are married, and Ben Folds appeared on and produced Palmer's solo debut "Who Killed Amanda Palmer".  The band have been referred to as a supergroup, acknowledging that moniker by describing themselves as "tomorrow's supergroup today".  The musical members of 8in8 each have different styles and the EP "Nighty Night" was created to reflect each one, with main lyricist Gaiman adapting to suit.

Good Day (The Dresden Dolls song): "Good Day" is the debut single by The Dresden Dolls duo, taken from the self-titled debut album "The Dresden Dolls".  It was originally released by Important Records Records in December 2003 in an edition of 500 on white vinyl.  The set also included a photograph signed by Amanda Palmer and Brian Viglione.  The 7" was later reissued in October 2005 on Palmer's own 8 Ft. Records during the band's Fall 2005 North American tour.  The cover of the reissue depicted a painting by Barnaby Whitfield that recreated the photo from the original release.

Question: The lead singer of the duo The Dresden Dolls also performs in what supergroup?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "supergroup_name": {
      "type": "string",
      "description": "The name of the supergroup."
    },
    "lead_singer_name": {
      "type": "string",
      "description": "The name of the lead singer of The Dresden Dolls."
    },
    "is_supergroup_explicitly_stated": {
      "type": "boolean",
      "description": "Indicates if the group is explicitly referred to as a 'supergroup' in the text."
    },
    "other_members": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other members of the supergroup."
    }
  },
  "required": [
    "supergroup_name",
    "lead_singer_name",
    "is_supergroup_explicitly_stated",
    "other_members"
  ],
  "additionalProperties": false
}
