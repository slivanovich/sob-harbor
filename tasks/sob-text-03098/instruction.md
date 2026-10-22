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
Confessions (Usher album): Confessions is the fourth studio album by American singer Usher.  It was released on March 23, 2004, by Arista Records.  Recording sessions for the album took place during 2003 to 2004, with its production handled by his longtime collaborator Jermaine Dupri, alongside with Jimmy Jam and Terry Lewis and Lil Jon, among others.  Primarily an R&B album, "Confessions" showcases Usher as a crooner through a mixture of ballads and up-tempos, incorporating musical genres of dance-pop, hip hop and crunk.  The album's themes generated controversy about Usher's personal relationships; however, the album's primary producer Jermaine Dupri claimed the album reflects his personal story.

Puppy Love (Bow Wow song): "Puppy Love" is the third single by rapper Lil' Bow Wow's debut album "Beware of Dog" (2000).  The song was written by Brian-Michael Cox Brian Casey, Brandon Casey and Jermaine Dupri and features R&B group Jagged Edge and samples the beat of LL Cool J's song "Kanday" from his album "Bigger and Deffer".  The music video premiered on June 19, 2001, and features Solange Knowles as the rapper's love interest.

So Many Ways (The Braxtons song): "So Many Ways" is the lead single by American vocal group The Braxtons taken from their debut album So Many Ways (1996) released on July 23, 1996.  The song was written by Carl-So-Lowe, Jermaine Dupri and produced by Jermaine Dupri.  The song was also featured on High School High soundtrack (1996).  The song charted at 83 on Billboard Hot 100 and 22 on US R&B/Hip-Hop Songs in the US. <ref name="HOT R&B/HIP-HOP SONGS"> </ref> The song reached the top 40 in the UK charting at 32 and in New Zealand the song charted at 17.

Trapped in Crime: Trapped in Crime is the third studio album by American rapper C-Murder, released on September 5, 2000 on No Limit Records and was produced by Jermaine Dupri, Donald XL Robertson and Carlos Stephens. The album features guest appearances by Fat Joe, Snoop Dogg, Da Brat, Jermaine Dupri, Silkk the Shocker and Young Gunz.  "Trapped in Crime" was another success for C-Murder, peaking at #8 on the "Billboard" 200 and becoming his third straight album to land in the top 10 on the Billboard 200 chart while simultaneously making it to #1 on the Top R&B/Hip-Hop Albums.  It Was Certified Platinum By The RIAA On April 7, 2001

Control Myself: "Control Myself" is a song by American rapper LL Cool J from his twelfth album, "Todd Smith" (2006).  It was produced by Jermaine Dupri and features fellow American singer Jennifer Lopez (the song also has spoken parts by Dupri, but he is not credited).  The track contains a sample of Afrika Bambaataa & Soulsonic Force's 1983 song "Looking for the Perfect Beat", while the vocals interpolate Grandmaster Flash & Melle Mel's 1983 song "White Lines (Don't Don't Do It)" and Afrika Bambaataa & Soulsonic Force's 1982 song "Planet Rock".

Jagged Edge (group): Jagged Edge is an American mainstream R&B group signed through Jermaine Dupri's So So Def Recordings.  The group has had a number of hit singles, many of which are produced by Dupri.  The group's members include identical twin lead singers Brandon and Brian Casey as well as Kyle Norman and Richard Wingo.  In addition to writing the bulk of the group's material, the Casey brothers have also written for Usher, Nivea and Toni Braxton.

Like Mike (soundtrack): Like Mike: Music From the Motion Picture is the soundtrack to the 2002 film, "Like Mike".  It was released on July 2, 2002 through So So Def Recordings and consisted of hip hop and contemporary R&B with production from the likes of Jermaine Dupri, The Neptunes and even Alicia Keys.  The soundtrack spawned two singles, the first being "Basketball", a cover of Kurtis Blow's 1984 song, performed by Lil' Bow Wow featuring Jermaine Dupri, Fabolous & Fundisha.  The other is "Take Ya Home" by Lil' Bow Wow, taken from his second album "Doggy Bag", which serves as the theme song for the film.

Stepped on My J'z: "Stepped on My J'z" is a song by American rapper Nelly.  The song features American singer Ciara and rapper Jermaine Dupri.  It was recorded for Nelly's fifth studio album, "Brass Knuckles".  The track was produced by Jermaine Dupri, and was released as the second single from the album, but the music video was released before.  This is the second time Ciara has worked with Jermaine Dupri, the first time working on the single "Like You" with Bow Wow.

Ocean's 7: Ocean's 7 was an American musical collective composed of members Jermaine Dupri, Usher, Trey Songz, Nelly, Bryan Michael-Cox, Johnta Austin and Dupri's assistant Tyrone.  The group had a short stint releasing the mixtape "3000 and 9 shit", on May 5, 2009.  The group was formed by record producer and rapper Dupri.  The group was modeled after the Rat Pack in the film "Ocean's 11".  Like the Rat Pack, Jermaine Dupri, Bryan Michael-Cox, Johnta Austin, are all friends and have teamed up to write and produce various hit singles for several artists in their careers.

Paradise (LL Cool J song): "Paradise" is a song by American rapper LL Cool J featuring American R&B singer Amerie.  Produced by Trackmasters, the track was released in early 2003 as the second single from LL Cool J's ninth studio album, "10" (2002).  It also appears on the soundtrack to the 2003 film "Deliver Us from Eva", in which LL Cool J stars alongside Gabrielle Union.  Singer Tweet was originally slated to provide vocals but Amerie was eventually chosen instead.  "Paradise" samples Keni Burke's 1982 smooth jazz hit "Risin' to the Top", penned by Burke, Allan Felder, and Norma Jean Wright.  The song samples Tamia's So into You.

Question: What American mainstream R&B group signed by Jermaine Dupri  has a song featuring samples the beat of LL Cool J's song "Kanday" from his album  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "rnb_group_name": {
      "type": "string",
      "description": "The name of the American mainstream R&B group."
    },
    "signing_producer": {
      "type": "string",
      "description": "The producer who signed the R&B group."
    },
    "song_featuring_group_and_sample": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song that features the R&B group and samples another track."
        },
        "lead_artist": {
          "type": "string",
          "description": "The primary artist of the song."
        },
        "features_rnb_group": {
          "type": "boolean",
          "description": "Indicates if the R&B group is featured on this song."
        }
      },
      "required": [
        "song_title",
        "lead_artist",
        "features_rnb_group"
      ],
      "additionalProperties": false
    },
    "sampled_track_details": {
      "type": "object",
      "properties": {
        "sampled_track_title": {
          "type": "string",
          "description": "The title of the sampled track."
        },
        "sampled_track_artist": {
          "type": "string",
          "description": "The artist of the sampled track."
        },
        "sampled_track_album": {
          "type": "string",
          "description": "The album from which the track was sampled."
        }
      },
      "required": [
        "sampled_track_title",
        "sampled_track_artist",
        "sampled_track_album"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "rnb_group_name",
    "signing_producer",
    "song_featuring_group_and_sample",
    "sampled_track_details"
  ],
  "additionalProperties": false
}
