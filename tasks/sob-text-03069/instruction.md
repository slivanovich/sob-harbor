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
Singing in the Rain (Simple Plan song): "Singing in the Rain" is a song by Canadian rock band Simple Plan from their fifth studio album, "Taking One for the Team" (2016).  On the album, American musical duo Rock City are featured on the track, with an additional verse written by the duo's Timothy and Theron Thomas, however the single version does not include this feature.  The solo Simple Plan version of "Singing in the Rain" was released to digital retailers on March 25, 2016 as the album's third official single.

Vessel (Twenty One Pilots album): Vessel is the third studio album by American musical duo Twenty One Pilots, which was released on January 8, 2013.  It is the band's first album released via Fueled by Ramen, and is their major-label debut album.  As of July 2016, the album has sold over 569,000 copies.

Fake You Out: "Fake You Out" is a song by American musical duo Twenty One Pilots, from their third studio album, "Vessel" (2013).  Lead vocalist Tyler Joseph wrote the track and produced it alongside Greg Wells.  It is a synth-pop and indie rock song whose lyrics talk about "putting a facade for people" and lying about one's true self.

Car Radio (song): "Car Radio" is a song written and recorded by American musical duo Twenty One Pilots, originally released in 2011 on their second studio album, "Regional at Best".  It was re-released in March 2014 as the fifth and final single from their third studio album, "Vessel".  The song is seen as the duo's most experimental, as it has no sung words or hooks in it.

Guns for Hands: "Guns for Hands" is a song written and recorded by American musical duo Twenty One Pilots, released as a single only in Japan.  The song appears on their second self-released album, "Regional at Best", their third album "Vessel", their 2012 "Three Songs" EP, and their 2013 EP, "Migraine".  The video was directed by Mark C. Eshleman.  The song reached number 21 on the Japan Hot 100.

Twenty One Pilots discography: American musical duo Twenty One Pilots have released four studio albums, one live album, seven extended plays, fifteen singles and eighteen music videos.  The band was formed in 2009 and currently consists of Tyler Joseph and Josh Dun.  They put out two self-released albums, "Twenty One Pilots" in 2009 and "Regional at Best" in 2011, before being signed by Fueled by Ramen in 2012.  They released their third studio album, "Vessel", with Fueled by Ramen in 2013.  Their fourth studio album, "Blurryface", was released on May 15, 2015 through the same label.  On November 25, 2016, they released "Blurryface Live", a three-LP, Tri-Gatefold Picture Disc Vinyl featuring the live audio recorded during a concert at The Fox Theater in Oakland, CA.

Holding On to You (Twenty One Pilots song): "Holding On to You" is a song written and recorded by American musical duo Twenty One Pilots, for their second studio album "Regional at Best".  A partially re-recorded version of the song appeared on their third studio album, "Vessel".  "Holding On to You" was released as the first single from "Vessel" in the iTunes Store worldwide on September 11, 2012.  A video for the song was released on November 15.  The video was directed by Jordan Bahat.  The song impacted alternative radio on December 4, 2012, and released to mainstream radio on June 11, 2013.  It is the band's debut single.

Twenty One Pilots: Twenty One Pilots (stylized as TWENTY ØNE PILØTS, and formerly as twenty | one | pilots) is an American musical duo originating from Columbus, Ohio.  The band was formed in 2009 by lead vocalist Tyler Joseph along with former members Nick Thomas and Chris Salih, who left in 2011, and currently consists of Joseph and drummer Josh Dun.  The duo rose to fame in the mid-2010s after several years of touring and independent releases.

House of Gold (Twenty One Pilots song): "House of Gold" is a song written and recorded by American musical duo Twenty One Pilots, from their third studio album "Vessel".  The song initially appeared as a bonus track on their second self-released album "Regional at Best", albeit with a different vocal track.  "House of Gold" was released as the third single from "Vessel", impacting radio on August 6, 2013.  The music video for the song was released on October 2.

Lovely (Twenty One Pilots song): "Lovely" is a song by American musical duo Twenty One Pilots, for their third studio album "Vessel".  It was originally featured on their self-released second studio album "Regional at Best", but was re-recorded for "Vessel" and included as a Japanese bonus track for the album.  "Lovely" was released as a promotional single for the band's trip to Japan, being released on Warner Japan on April 17.  The song reached number 67 on the Japan Hot 100, respectively.

Question: What American musical duo from Columbus, Ohio have a third studio album called Vessel?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "duo_name": {
      "type": "string",
      "description": "The name of the musical duo."
    },
    "duo_nationality": {
      "type": "string",
      "description": "The nationality of the musical duo."
    },
    "duo_origin_city": {
      "type": "string",
      "description": "The city where the musical duo originated."
    },
    "duo_origin_state": {
      "type": "string",
      "description": "The state where the musical duo originated."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the studio album."
    },
    "album_studio_number": {
      "type": "integer",
      "description": "The sequential number of the studio album."
    }
  },
  "required": [
    "duo_name",
    "duo_nationality",
    "duo_origin_city",
    "duo_origin_state",
    "album_name",
    "album_studio_number"
  ],
  "additionalProperties": false
}
