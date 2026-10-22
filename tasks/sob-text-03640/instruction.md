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
TVT Records: TVT Records was an American record label founded by Steve Gottlieb.  Over the course of its 25-year history, the label released some 25 Gold, Platinum and Multi-platinum releases.  Its roster included Nine Inch Nails, Ja Rule, Lil Jon, Underworld, KMFDM, Gravity Kills, The KLF, The Baldwin Brothers, Sevendust, Nothingface, the Wellwater Conspiracy, Brian Jonestown Massacre, The Holloways, The Cinematics, Buck-O-Nine, DJ Hurricane, Speech and Pitbull.  Its biggest commercial successes were the triple platinum Nine Inch Nails's "Pretty Hate Machine", two double platinum releases by Lil Jon, and platinum releases by Snoop Dogg and Tha Eastsidaz, Dashboard Confessional, Default and Ying Yang Twins as well as gold releases by Sevendust, Gravity Kills and The Black Crowes and Jimmy Page.  Additionally, TVT also had success overseas, achieving a gold release in Germany and Sweden with The Connells and scored platinum and gold records in Canada with Default.

Superstarved: Superstarved (stylized as superstarved★ or superstarved*) is the third studio album by Gravity Kills, released March 19, 2002.  The album is described as "more riff-oriented" and "grindier".

Guided by Voices: Guided by Voices (often abbreviated as GBV) is an American indie rock band from Dayton, Ohio.  It has made frequent personnel changes but always maintained the presence of principal songwriter Robert Pollard.

Gravity Kills (album): Gravity Kills is the debut studio album by industrial rock band Gravity Kills.  It was released in 1996 on TVT Records.  The album sold just under 500,000 copies.

Jim Marcus: James Marcus (born March 22, 1966) is a musician, artist, political activist, and respected typographer who is best known for his work as the lead singer and founder of the Industrial band Die Warzau.  He is credited as engineer, remixer, vocalist, songwriter, percussionist, drummer, bass player, pianist, keyboardist or artist on albums by Die Warzau, GoFight, Sister Machine Gun, Björk, Pigface, Pansy Division, The Swans, Haloblack, Chris Connelly, KMFDM, Skrew, Machines of Loving Grace, Stabbing Westward, Gravity Kills, Everplastic, Screaming Rachel, Dessau, Chemlab, The Final Cut, Testify, Mindfunk, Little Louis and various other artists across many different genres.  His work can be heard on some of the most popular tracks by many of these groups, such as the Pigface's "Asphole", "Aboriginal", "Steamroller", etc., KMFDM's "Light", Sister Machine gun's "Wired", "Lung", "Nothing", etc.

Rocky Morton: Rocky Morton (born 1955) is an English director.  He was the co-creator of Max Headroom and co-director on "Super Mario Bros".  Various music videos by Tom Tom Club, Talking Heads, Gravity Kills, Orgy, George Harrison and Miles Davis are credited to Morton.  Videos include "New Frontier".  Alongside his partner, Annabel Jankel, the duo made their television debut with the original "," and its Americanized version.  The duo made their big-screen debut with the remake of the film noir classic, "D.O.A.," starring Dennis Quaid and Meg Ryan.

Gravity Kills: Gravity Kills is an American industrial rock band from St. Louis, Missouri.  Their music was described by one critic as "a blending of eerie industrial rock with a pop-infused melodic chorus and a bit of hard-core head banging."

Hypersonic Hyperphonic: Hypersonic Hyperphonic is the second studio album by Tinfed, released on December 3, 1996 by Re-Constriction Records.  "Sonic Boom" noted that "Tinfed is one of those bands who would fit perfectly on tour with the likes of God Lives Underwater, Stabbing Westward, Filter & Gravity Kills which means they should do rather well with the current crossover audience."

Perversion (album): "Perversion" is a 1998 album by Industrial Rock act Gravity Kills.

Falling (Gravity Kills song): "Falling" is a song by industrial rock band Gravity Kills from the album "Perversion", released by TVT Records in 1998.

Question: Which band is from Ohio, Guided by Voices or Gravity Kills?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_topic": {
      "type": "string",
      "description": "The main topic of the question, comparing band origins."
    },
    "bands_information": {
      "type": "array",
      "description": "Details about the bands mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "origin_city": {
            "type": "string",
            "description": "The city where the band is from."
          },
          "origin_state": {
            "type": "string",
            "description": "The state where the band is from."
          }
        },
        "required": [
          "band_name",
          "origin_city",
          "origin_state"
        ],
        "additionalProperties": false
      }
    },
    "band_from_ohio": {
      "type": "string",
      "description": "The name of the band that is from Ohio."
    }
  },
  "required": [
    "question_topic",
    "bands_information",
    "band_from_ohio"
  ],
  "additionalProperties": false
}
