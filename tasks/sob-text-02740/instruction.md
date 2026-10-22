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
Ty Dolla Sign: Tyrone William Griffin Jr. (born April 13, 1985), known professionally as Ty Dolla Sign (stylized as Ty Dolla $ign or Ty$), is an American singer, rapper, songwriter, and record producer.  He first gained major recognition in 2010 for his feature on YG's "Toot It and Boot It", which he had written and produced for Def Jam Recordings.  In the summer of 2013, he signed a record deal with Wiz Khalifa's Taylor Gang Records.  In November 2015, he released his debut studio album, "Free TC", which peaked at number 14 on the US "Billboard" 200.

Boys (Charli XCX song): "Boys" is a single by English singer Charli XCX, released on 26 July 2017 by Asylum Records and Atlantic Records UK.  The song serves as the lead single from her untitled upcoming third studio album.  In August 2016, Charli XCX revealed that her upcoming album would largely be produced by Sophie and Stargate.

Free TC: Free TC is the debut studio album by American singer and rapper Ty Dolla Sign.  It was released on November 13, 2015, by Atlantic Records.  As executive producers by Ty Dolla Sign and Wiz Khalifa enlisted a variety of collaborators; including DJ Mustard, DJ Spinz, Cardo, Johnny Juliano, R. Kelly, Kendrick Lamar, Brandy and Kanye West, among others.

Campaign (mixtape): Campaign is the ninth mixtape by American singer and rapper Ty Dolla Sign.  It was first released commercially on September 23, 2016, by Atlantic Records.  The mixtape was supported by three singles: "Campaign" featuring Future, "No Justice" featuring Big TC, and "Zaddy".  The mixtape is a recurring theme expressing the views of Ty Dolla Sign and his friends and family on the presidential campaigns of Donald Trump and Hillary Clinton.

DJ Dahi: Dacoury Natche (born March 10, 1983), professionally known as DJ Dahi, is an American DJ, songwriter and record producer from Inglewood, California.  Dahi is perhaps best known for producing "Worst Behavior" by Canadian rapper Drake, as well as American rapper Kendrick Lamar's critically acclaimed album cut "Money Trees", which features Lamar's label-mate Jay Rock.  Dahi has also produced several tracks for various artists such as Dr. Dre, Lily Allen, Freddie Gibbs, Dom Kennedy, Lupe Fiasco, Vince Staples, Mac Miller, Ty Dolla Sign, Pac Div, Travi$ Scott, Vic Mensa, Casey Veggies, Smoke DZA, Big Sean, Tinashe, Logic, and Big K.R.I.T., among others.  Aside from his solo production career, Dahi is also a member of production team D.R.U.G.S., alongside Chordz 3D, Buddah Shampoo, Nate 3D, James Koo, Fuego and Ty Dolla Sign.  He is currently working on an album with LOTB.  The album is set to release early August.

After the Afterparty: "After the Afterparty" is a single by British singer Charli XCX, released on 28 October 2016 by Asylum Records and Atlantic Records UK.  The song serves as the lead single from her untitled third studio album to be released 2018, and features American rapper Lil Yachty.  In August 2016, Charli XCX revealed that her upcoming album would largely be produced by Sophie and Stargate.

Dark Sky Paradise: Dark Sky Paradise is the third studio album by American rapper Big Sean.  It was released on February 24, 2015, by GOOD Music and Def Jam Recordings.  The album features guest appearances from Kanye West, Drake, Ariana Grande, Chris Brown, Ty Dolla Sign, Jhené Aiko, PartyNextDoor, Lil Wayne, John Legend and E-40, while the production was handled by a variety of collaborators, including Key Wane, DJ Mustard, DJ Dahi and Kanye West, who also serves as the album's executive producer alongside Big Sean himself.  The album was supported by five singles: "I Don't Fuck with You" featuring E-40, "Paradise", "Blessings" featuring Drake, "One Man Can Change the World" featuring Kanye West and John Legend, and "Play No Games" featuring Chris Brown and Ty Dolla Sign.

Cashmere Cat: Magnus August Høiberg (born 29 November 1987), known professionally as Cashmere Cat, is a Norwegian DJ, record producer, musician and turntablist.  He is best known for producing songs for various artists, as well as remixing and editing songs from those respective artists as well.  He also represented Norway in the DMC World DJ Championships as DJ Final from 2006 to 2009.  His debut EP, "Mirror Maru", released in October 2012, gained recognition from several other producers.

Drop That Kitty: "Drop That Kitty" is a song by American rapper Ty Dolla Sign, featuring English singer Charli XCX and American singer Tinashe.  The track was produced by Stargate and Cashmere Cat.  The song was written by Ty Dolla Sign, Tinashe, and Charlotte Atichison.  It was released as digital download in the United States on February 17, 2015, originally intended as the first single from "Free TC" but was later scrapped.  Sign raps the track's main verses, while XCX sings its chorus hook and Tinashe its bridge and pre-chorus hook.  The lyrical content in the song serve as a four-step dance instructional and contain several sexual euphemisms and innuendos.  It discusses a scenario of meeting someone attractive in a club and communicating basest desires to them, while extolling the virtues of physical flexibility.

My Krazy Life: My Krazy Life is the debut studio album by American rapper YG.  It was released on March 18, 2014, by Pu$haz Ink, CTE World and Def Jam Recordings.  Recording sessions took place from 2012 to 2014 in various recording studios, mostly from Atlanta, Georgia to Los Angeles, California.  The album features guest appearances from Kendrick Lamar, Drake, Lil Wayne, Nicki Minaj, Rich Homie Quan, Ty Dolla Sign, Schoolboy Q, Meek Mill, Jay Rock, Jeezy, TeeFlii and RJ, while the production was primarily handled by frequent collaborator DJ Mustard, along with production from Ty Dolla Sign and Terrace Martin.

Question: "Drop That Kitty" is a song by American rapper Ty Dolla Sign, featuring English singer Charli XCX and American singer Tinashe, the  track was produced by Stargate and which Norwegian DJ, record producer, musician and turntablist, known professionally as who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "producer_details": {
      "type": "object",
      "properties": {
        "professional_name": {
          "type": "string",
          "description": "The professional name of the producer."
        },
        "real_name": {
          "type": "string",
          "description": "The real name of the producer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the producer."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles held by the producer."
        }
      },
      "required": [
        "professional_name",
        "real_name",
        "nationality",
        "roles"
      ],
      "additionalProperties": false
    },
    "other_producers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other producers of the song mentioned in the context."
    }
  },
  "required": [
    "song_title",
    "producer_details",
    "other_producers"
  ],
  "additionalProperties": false
}
