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
Beats of Rage: Beats of Rage is an open source 2D customisable video game engine designed by Senile Team and inspired by Sega's classic "Streets of Rage" series of beat'em up games.  It was initially released as a video game tribute for "Streets of Rage 2" with characters from "The King of Fighters".

XO Tour Llif3: "XO Tour Llif3" (pronounced "XO Tour Life") is a single by American rapper Lil Uzi Vert from his EP "Luv Is Rage 1.5" (2017) and debut album "Luv Is Rage 2" (2017).  It was released on March 24, 2017, by Generation Now and Atlantic Records.  The track was produced by TM88, with co-production by JW Lucas.  It peaked at number seven on the US "Billboard" Hot 100, becoming Lil Uzi Vert's highest-charting single as a solo artist and second top 10 entry overall after his feature on "Bad and Boujee" with Migos.

Lil Uzi Vert: Symere Woods (born July 31, 1994), better known by his stage name Lil Uzi Vert, is an American hip hop recording artist.  Based in Philadelphia, he gained recognition after releasing his debut single, "Money Longer", and several mixtapes, including "Luv Is Rage", "Lil Uzi Vert vs. the World", and "The Perfect Luv Tape".  Lil Uzi Vert has also collaborated with Migos on "Bad and Boujee", which became Lil Uzi Vert's first US "Billboard" Hot 100 number-one single.  In August 2017, Lil Uzi Vert released his debut studio album, Luv Is Rage 2, where it reached number one on the Billboard 200 Albums Chart.

Luv Is Rage 2: Luv Is Rage 2 is the debut studio album by American rapper Lil Uzi Vert.  It was released on August 25, 2017, by Generation Now and Atlantic Records.  The album serves as a sequel to Uzi Vert's commercial breakthrough mixtape "Luv Is Rage" (2015).  It features guest appearances from The Weeknd and Pharrell Williams.

The Weeknd: Abel Makkonen Tesfaye (born February 16 1990), known professionally as The Weeknd (pronounced "the weekend"), is a Canadian singer, songwriter and record producer.

2003 in Cage Rage Championships: The year 2003 is the 2nd year in the history of the Cage Rage Championships, a mixed martial arts promotion based in the United Kingdom.  In 2003 Cage Rage Championships held 3 events, "Cage Rage 2".

Emo hip hop: Emo hip hop (also known as emo rap) is a subgenre of hip hop fusing beats common in hip hop music with lyrical themes,vocals, and musicianship common in 2000's emo music.  Artists such as Lil Uzi Vert (In his album Luv Is Rage 2)

Streets of Rage (video game): Streets of Rage (ベアナックル 怒りの鉄拳 , Bea Nakkuru: Ikari no Tekken , "Bare Knuckle: Furious Iron Fist") is a side-scrolling beat 'em up video game developed and published by Sega in 1991 for Mega Drive/Genesis.  It is the first installment of the "Bare Knuckle/Streets of Rage" series which was followed by "Streets of Rage 2" and "Streets of Rage 3".  The game was converted to Game Gear, Sega CD and Master System.  In 2007, the game was released for the Wii's Virtual Console in North America and Europe, and in 2009 it was released for the iOS via the App Store.  It was again made available as part of Sonic's Ultimate Genesis Collection in 2009 on both the PlayStation 3 and Xbox 360 consoles.

Streets of Rage 2: Streets of Rage 2, released in Japan as Bare Knuckle II: The Requiem of the Deadly Battle (ベア・ナックルII 死闘への鎮魂歌 , Bea Nakkuru Tsū: Shitō he no Chinkonka ) , is a side-scrolling beat 'em up video game published by Sega in 1992 for the Mega Drive/Genesis console and developed by an ad hoc team of several companies: Sega, Ancient, Shout!  Designworks, MNM Software and H.I.C.  It is the second game in the "Streets of Rage" series, a sequel to "Streets of Rage" and followed by "Streets of Rage 3".

Luv Is Rage 1.5: Luv Is Rage 1.5 is the third extended play by American rapper Lil Uzi Vert.  It was independently released on February 26, 2017 via Uzi's SoundCloud and on mixtape websites, such as DatPiff as a prequel to his debut album "Luv Is Rage 2" (2017).  The project includes four tracks and features production from Derelle Rideout, DJ Plugg, DP Beats, JW Lucas and TM88

Question: Who guest appeared on Luv is Rage 2?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "guest_artists": {
      "type": "array",
      "description": "A list of artists who made guest appearances on the album.",
      "items": {
        "type": "object",
        "properties": {
          "artist_name": {
            "type": "string",
            "description": "The stage name of the guest artist."
          },
          "real_name": {
            "type": "string",
            "description": "The real name of the guest artist, if known."
          },
          "role": {
            "type": "string",
            "description": "The role of the artist on the album."
          }
        },
        "required": [
          "artist_name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    }
  },
  "required": [
    "album_name",
    "guest_artists",
    "release_year"
  ],
  "additionalProperties": false
}
