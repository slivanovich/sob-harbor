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
The X Factor (UK series 9): The X Factor is a British television music competition to find new singing talent.  The ninth series began airing on ITV on 18 August 2012 and ended on 9 December 2012.  Dermot O'Leary returned as presenter of the main show on ITV, whilst Caroline Flack and Olly Murs returned to co-present "The Xtra Factor" on ITV2.  Louis Walsh, Gary Barlow and Tulisa returned as judges.  Nicole Scherzinger was confirmed as the fourth permanent judge after Geri Halliwell, Leona Lewis, Rita Ora, Mel B, Anastacia and Scherzinger herself stood in as guest judges for the vacant position left by Kelly Rowland.  After the 8 December show, two of Scherzinger's acts, James Arthur and Jahméne Douglas, became the top two, meaning that Scherzinger was guaranteed to win.  Arthur was announced as the winner on 9 December, and released a cover of Shontelle's "Impossible" as his winner's song.  As of 2016, it is the most successful winner's single in the show's history.

Doll Domination: Doll Domination is the second and final studio album by American girl group the Pussycat Dolls, released on September 19, 2008 by Interscope Records.  Following the success of their debut studio album, "PCD" (2005), Nicole Scherzinger attempted to launch her solo career with "Her Name is Nicole"; however after four unsuccessful singles and a number of push-backs, Scherzinger decided to focus on the group's second album.  The album's release was preceded by the departure of the group's longest-standing member Carmit Bachar.  Development began in February 2008 where the group worked with previous collaborators Sean Garrett, Polow da Don and Timbaland and new ones such as Darkchild, J-Roc and Ne-Yo.  Additionally four songs recorded for "Her Name is Nicole" were given by Scherzinger as she felt that the songs were better suited for the group.

When I Grow Up (The Pussycat Dolls song): "When I Grow Up" is a song by American girl group The Pussycat Dolls from their second and final studio album "Doll Domination" (2008).  It was released by Interscope Records on June 3, 2008, as the lead single from the album.  "When I Grow Up" was their first single following the departure of the group's longest-standing member Carmit Bachar.  It was first recorded for Nicole Scherzinger's planned solo project, "Her Name Is Nicole", but after its cancellation and Scherzinger's return to the group, she felt that the song was better suited for the group.  It was written by Theron Thomas, Timothy Thomas and Rodney "Darkchild" Jerkins, who also produced the song.  It is an uptempo electropop song.  It samples the 1966 song, "He's Always There" by British rock band The Yardbirds.  "When I Grow Up" speaks about the desire to be famous, and was described as being "autobiographical" by Scherzinger.

Whatever U Like: "Whatever U Like" is a song by American recording artist Nicole Scherzinger, featuring rapper T.I..  The duo, along with Sean Garrett and Polow da Don, composed the song for Scherzinger's planned debut studio album "Her Name Is Nicole".  Interscope Records released "Whatever U Like" as Scherzinger's solo debut single on July 30, 2007.

I Hate This Part: "I Hate This Part" is a song by American girl group The Pussycat Dolls from their second album, "Doll Domination" (2008).  The song was written by Wayne Hector, Lucas Secon, Jonas Jeberg and Mich Hansen and produced by the latter two along with Ron Fair and Nicole Scherzinger.  It was first recorded for Nicole Scherzinger's planned solo project, "Her Name Is Nicole", but after its cancellation the song was given to the group.  "I Hate This Part" was released on October 14, 2008 as the second international single and impacted contemporary hit radio stations on October 20, 2008 as the fourth single in the United States by Interscope Records.  "I Hate this Part" is a dance/R&B-influenced pop song which ditches the Doll's usual sexual image in favor of introspection.  Lyrically the song is about the conversation before a breakup.

Justin Hawkins: Justin David Hawkins (born 17 March 1975) is an English musician and singer-songwriter, best known for being the lead singer and lead guitarist of The Darkness, alongside his brother, guitarist Dan Hawkins.  Heavily influenced by classic hard rock and heavy metal bands of the 1970s and 1980s (particularly Queen, Aerosmith, Def Leppard and AC/DC), Hawkins is noted for his falsetto singing voice and on-stage persona.  He was also the lead singer and guitarist for the band Hot Leg, formed in 2008, and now on hiatus.  Since 2005 he is also active in his synthpop alter ego British Whale.

Hush Hush; Hush Hush: "Hush Hush; Hush Hush" is a song by American female group The Pussycat Dolls from their second and final studio album, "Doll Domination" (2008).  Written by Nicole Scherzinger, Andreas Romdhane, Josef Larossi, Ina Wroldsen, Dino Fekaris, Frederik Perren and produced by Quiz & LaRossi and Dave Audé for the remixed version, it was released as the album's sixth and final single on May 12, 2009.  Lead and background vocals for both versions of the song are performed solely by lead singer Nicole Scherzinger.  The release caused controversy as the single was credited as "Pussycat Dolls featuring Nicole Scherzinger" which caused tension within the group and rumored that Scherzinger would be going solo.

Killer Love: Killer Love is the debut solo studio album by American singer Nicole Scherzinger, former lead singer of The Pussycat Dolls.  It was released from March 18, 2011, by Interscope Records, in association with its affiliated record labels.  Scherzinger had been working on a solo album since 2005, under the title "Her Name Is Nicole" and was originally due for release in 2007.  However, unsuccessful singles and poor timing led the project being pushed back numerous times into 2008 and 2009.  After releasing The Pussycat Dolls' second album "Doll Domination" (2008), Scherzinger shelved the project entirely citing bad timing and creative issues as the reasons for its cancellation.  Many of its songs were reassigned to the Dolls or other artists.  In 2010, Moroccan producer RedOne was brought on board for a second attempt at launching her solo album.

Right There (Nicole Scherzinger song): "Right There" is a song recorded by American singer Nicole Scherzinger for her debut studio album, "Killer Love" (2011).  Written by Ester Dean, Frank Romano, Daniel Morris and co-written and produced by Jim Jonsin, the Island-flavored midtempo pop song sees Scherzinger singing about her lover and telling other women to stay away.  "Right There" first impacted radio as Scherzinger's third international single on April 1, 2011, after previous singles met success in the United Kingdom.  "Right There" was Scherzinger's third consecutive top three single from her debut album.  The song was then re-released on May 17, 2011 in the United States, as "Killer Love"' s lead single, and was remixed to feature two new verses from American rapper 50 Cent.  It has reached over 130 million views on YouTube making it VEVO certified.

Nicole Scherzinger: Nicole Scherzinger ( ; born Nicole Prescovia Elikolani Valiente; June 29, 1978) is an American recording artist, actress and television personality born in Honolulu, Hawaii and raised in Louisville, Kentucky.  She performed initially in high school plays, and studied at Wright State University before dropping out to pursue a musical career alongside the American rock band Days of the New and later auditioned for "Popstars", becoming a member of the short-lived girl group Eden's Crush.  She rose to fame as the lead singer of the burlesque troupe-turned-recording act the Pussycat Dolls, who became one of the world's best-selling girl groups.  During their hiatus, Scherzinger planned to embark on her solo career with "Her Name is Nicole", but it was later shelved after four singles failed to impact the charts significantly.

Question: Justin Hawkins and Nicole Scherzinger, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_details": {
      "type": "array",
      "description": "Details about the individuals mentioned, including their names and listed occupations.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the person."
          },
          "occupations": {
            "type": "array",
            "description": "A list of occupations for the person as stated in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      }
    },
    "common_occupation": {
      "type": "string",
      "description": "The occupation that both individuals share."
    },
    "occupation_category": {
      "type": "string",
      "description": "A broader category for the identified common occupation."
    }
  },
  "required": [
    "person_details",
    "common_occupation",
    "occupation_category"
  ],
  "additionalProperties": false
}
