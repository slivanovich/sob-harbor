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
The Teen Idles: The Teen Idles were an American hardcore punk band formed in Washington, D.C. in September 1979.  Consisting of teenagers Nathan Strejcek, Geordie Grindle, Ian MacKaye and Jeff Nelson, the Idles recorded two demo sessions and the 1980 "Minor Disturbance" EP before breaking up in November 1980.  The influential independent record label Dischord Records was originally created with the sole purpose of releasing the Teen Idles "Minor Disturbance" 7" record.  They were an early landmark in the D.C. hardcore movement, and MacKaye and Nelson would later form the seminal punk rock outfit Minor Threat.

Jeff Nelson (musician): Jeff Nelson (born 1962 in South Africa) is an American drummer and graphic designer.  He is best known as the drummer for the Washington, D.C. hardcore punk band Minor Threat.  Nelson and friend Ian MacKaye formed their first band, The Slinkees, in 1979.  Their next band was The Teen Idles.  He also co-founded the independent record label Dischord Records along with MacKaye in 1980, whose first record was the Teen Idles.  They continue to run Dischord together.  The duo also comprised the projects Skewbald/Grand Union and Egg Hunt; both bands recorded only one single.  Nelson has also played in the bands Feedbag, Three, Wonderama, Senator Flux, High Back Chairs, and Fast Piece of Furniture.  He founded Pedestrian Press in 1988 and Adult Swim Records in 1989.  An aficionado and collector of Jeep Wagoneers and Victorian architecture, Nelson currently lives in the historic "Old West End" of Toledo, Ohio.  In 2008 he formed a community organization called Save Our Scott, which led the fight to save Toledo's oldest high school, built in 1912.  (Jessup W. Scott High School was saved, and underwent a $42 million renovation).

Ian MacKaye: Ian Thomas Garner MacKaye ( ; born April 16, 1962) is an American singer, songwriter, guitarist, musician, record label owner and producer.  Active since 1979, MacKaye is best known as the co-founder and owner of Dischord Records, a Washington, D.C.-based independent record label and the frontman of the influential hardcore punk band Minor Threat and the post-hardcore band Fugazi.  MacKaye was also the frontman for the short-lived bands The Teen Idles, Embrace and Pailhead, a collaboration with the band Ministry.  MacKaye is a member of The Evens, a two-piece indie rock group he formed with his wife Amy Farina in 2001.

Hayley Williams: Hayley Nichole Williams (born December 27, 1988) is an American singer, songwriter and musician.  She serves as the lead vocalist, primary songwriter and occasional keyboardist of the rock band Paramore.  The band was formed in 2004 by Josh Farro, Zac Farro, Jeremy Davis and Williams.  The band consists of Hayley Williams, Zac Farro and Taylor York.  The band has five studio albums: "All We Know Is Falling" (2005), "Riot! " (2007), "Brand New Eyes" (2009), "Paramore" (2013) and "After Laughter" (2017).

Rozzlyn Rangers: Rozzlyn Rangers was the name taken by the 5 original members of the Dischord House in Arlington, Virginia (fairly near Rosslyn, Virginia) in October 1981: Ian MacKaye, Jeff Nelson, Rich Moore, Eddie Janney, and Sab Grey.  Dischord House housed Dischord Records (founded a year earlier by The Teen Idles, shortly thereafter to be run by Ian MacKaye and Jeff Nelson).  Despite its terribly low ceiling, many DC punk bands practiced in its basement over the years: Minor Threat, Skewbald, Iron Cross, The Faith, Second Wind, Rites of Spring, Embrace, Three, Fugazi, Beefeater, Fidelity Jones, Happy Go Licky, Kingface, One Last Wish, The Evens.

Egg Hunt: Egg Hunt was a one-off band/project of long time friends and musicians Ian MacKaye and Jeff Nelson, former singer and drummer of the hardcore punk band Minor Threat, respectively.  During a 1986 trip to England's Southern Studios to discuss possible European distribution of Dischord releases with owner John Loder, the three decided to make a record together, and the project was dubbed "Egg Hunt" for festive reasons (it was Easter time).  John took a seat in the producer's chair, while Ian and Jeff handled all the instruments.

The Evens: The Evens are a Washington, D.C. indie-rock duo, formed in the fall of 2001, comprising partners Ian MacKaye (guitars, vocals) (of Fugazi, formerly of Minor Threat) and Amy Farina (drums, vocals) (formerly of The Warmers).  After Ian MacKaye's band Fugazi entered a hiatus, The Evens began practicing extensively, and eventually played a few shows and recorded a self-titled album, released in March 2005 on MacKaye's label, Dischord Records.  The Evens are known for their unusual choices in venues for performances and the stylistic change from what many have dubbed the "D.C." or "Dischord" sound. " The Washington Post" has described the sound as "what happens when post-hardcore becomes post-post-hardcore."

Life Time (Rollins Band album): Life Time is the first full-length studio album by Rollins Band, fronted by ex-Black Flag singer, Henry Rollins.  The album was produced by Ian MacKaye, well known in the genre of hardcore punk for his work with Minor Threat and as co-owner of the Dischord record label.  MacKaye was also a childhood friend of Rollins, who acted as a roadie for MacKaye's band The Teen Idles.  It was originally released in 1987 and included four live tracks recorded in Kortrijk, Belgium in October 1987.  It was subsequently re-mastered and re-released in 1999 without the live tracks, but with the addition of three session tracks from the "Do It" album of 1987.  The 2014 reissue on Dischord includes the live tracks but not the bonus tracks included on the 1999 reissue .

Dischord Records discography: Dischord Records is a Washington, D.C.-based independent record label specializing in the independent punk music of the D.C.-area music scene.  The company is co-owned by Ian MacKaye and Jeff Nelson, who founded the label in December 1980.  Before founding Dischord, both MacKaye and Nelson were members of the Teen Idles, and the label was initially meant to only foster a single release from the defunct band, the "Minor Disturbance" EP.  By the time Dischord #1 was finished, many new bands had emerged from the same music scene, and like the Teen Idles, also began releasing their records through Dischord.

Amy Farina: Amy Farina is a musician living in Washington, D.C. As of 2001, Farina has played drums and sings in the Indie rock duo The Evens which includes her husband Ian MacKaye.  Previously she has played in The Warmers (which included Ian's younger brother Alec MacKaye), Mister Candy Eater, Ted Leo & the Pharmacists and with Lois Maffeo.  She and MacKaye welcomed their first child, Carmine Francis Farina MacKaye, on May 24, 2008.  She is the sister of Geoff Farina of the band Karate.

Question: Hayley Williams and Ian MacKaye, have which occupations in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "occupations": {
          "type": "array",
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
    },
    "person_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "occupations": {
          "type": "array",
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
    },
    "common_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Occupations shared by both individuals."
    }
  },
  "required": [
    "person_one",
    "person_two",
    "common_occupations"
  ],
  "additionalProperties": false
}
