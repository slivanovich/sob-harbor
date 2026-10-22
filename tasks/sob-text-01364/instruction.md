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
The Paper Cranes: The Paper Cranes are a Canadian indie pop band from Victoria, British Columbia.  The band is composed of the husband and wife duo of Ryan McCullagh (Guitar, Bass, Vocals) and Miranda Roach (Keyboard, Drum Sequencing).  Despite several line-up changes during their career the group remains centered on the husband-wife team.  The band take their name from the book, "Sadako and the Thousand Paper Cranes" by Eleanor Coerr.

Jason Hammel (musician): Jason Edward Hammel is an American musician, producer, and actor.  He is a vocalist and drummer for Mates of State, of which he is half complemented by his wife, Kori Hammel, a vocalist and keyboardist for the band.  Hammel went to high school in Stewartville, Minnesota, where he played in rock bands.  He then attended Kansas University where he graduated Phi Beta Kappa.  There in 1997 he met Kori, then Kori Gardner.  They moved to San Francisco together and got married.  He trains martial arts and is a black belt in kyokushin karate.  In 2015, alongside his wife he starred in his first feature film, The Rumperbutts.  Jason and Kori live in Connecticut

Antietam (band): Antietam is an indie rock band from Louisville, Kentucky formed in 1984 by members of the Babylon Dance Band, husband and wife duo Tara Key and Tim Harris.  They released six albums between 1985 and 1995, and since the late 1980s have been based in New York.  They ceased working as a band in 1996 but reformed in 2004 and have gone on to release several more albums.

Mates of State: Mates of State are an American indie pop duo, active since 1997.  The group consists of the husband-and-wife team of Kori Gardner (vocals, organ, synthesizer, piano, electric piano, and occasional guitar) and Jason Hammel (vocals, drums, percussion, and occasional synthesizer).

The Lapse: The Lapse was an American indie band formed in late 1997.  The band was first signed to Gern Blandsten, then Southern Records.  A larger deal with Matador Records fell through in 2001.  The Lapse was the duo of then boyfriend/girlfriend Chris Leo (ex-Native nod and brother of Ted Leo) and Toko Yasuda (Enon, ex-Blonde Redhead).  They formed The Lapse after the breakup of their previous band, The Van Pelt.  The Lapse had Leo on guitar and Yasuda on bass with both handling vocals.  The band welcomed a long list of guest musicians over the years, including Don Devore (bass), Justin DuClos (drums), and Garry Keating (bass).

Sodagreen: Sodagreen (; stylized as sodagreen) is a Taiwanese indie band formed in 2001.  Its members have been unchanged since 2003.  Sodagreen emerged in the Taiwanese indie music scene after receiving the Grand Jury Award in the Hohaiyan Gongliau Rock Festival in 2004, after which it signed a contract with Willlin Music.  The band is the first indie band to hold a concert in the Taipei Arena.  The band is well known for its main vocalist and songwriter Wu Tsing-Fong, who is prominent for his poetic lyrics, unique performing style, and wide vocal range.

Crushes (The Covers Mixtape): Crushes (The Covers Mixtape) is the sixth full-length release by husband/wife duo Mates of State.  It was released digitally via iTunes as well as from the band's website on June 15, 2010.  As stated in the title, the album is the duo's first mixtape.  On the band's website, they explained the reason for the mixtape's creation.  "We've been talking about doing a covers record for a long time.  We'd hear a great song at 2 AM while driving the straight line from one part of Texas to the next, and all we'd want to do is play that song as if we had written it."  The album was recorded and produced by Kori Gardner and Jason Hammel, making it their first self-produced record to date.  The album was mixed by Peter Katis (The National, Interpol, Frightened Rabbit, Jónsi), a longtime collaborator.  The third track "Sleep the Clock Around" was featured in the film The Art of Getting By.

The Rumperbutts: The Rumperbutts is a 2015 American musical comedy written and directed by Marc Brener, starring Kori Gardner and Jason Hammel of the indie pop duo Mates of State, as well as Vanessa Ray, Josh Brener and Arian Moayed.  Marc Brener and Dena Hysell, of Rumpus Room Productions, are the producers of the film.  The film is distributed by Mance Media and was released theatrically on May 22, 2015.  The film was also released in HD and 4K Ultra HD formats.

Princeton Rays: The Princeton Rays are a minor league baseball team in Princeton, West Virginia, USA.  They are an Advanced Rookie-level team in the Appalachian League and have been an affiliate of the Tampa Bay Rays since September 27, 1996.  The Princeton franchise began play in the Appalachian League in 1988 and was previously affiliated with the Pittsburgh Pirates (1988–89), was a co-op team known as the Princeton Patriots (1990), and then was affiliated with the Cincinnati Reds (1991–96) before joining forces with Tampa Bay.  The Princeton Rays play their home games at H.P. Hunnicutt Field, which originally opened in 1988 (and was completely rebuilt in 2000 on the same site) and seats 1,950 fans.  The team plays an annual 68-game schedule that traditionally extends from mid-June through the end of August.  Through the completion of the 2012 season, the franchise has seen 57 former players move on to play regular season major league baseball that at one time wore the Princeton uniform.  This list of players includes big names such as Brandon Backe, Rocco Baldelli, Carl Crawford, Jonny Gomes, Josh Hamilton, Seth McClung, Pokey Reese, Matt Moore, Wade Davis, Desmond Jennings, Jeremy Hellickson, Jason Hammel, and Jared Sandberg.  NFL quarterback Doug Johnson (1997 P-Rays) and current NBA referee David Guthrie (1995 Princeton Reds) also played professional baseball for Princeton teams.  The team is operated on a not-for-profit basis.

Polvo: Polvo is an American indie noise rock band from Chapel Hill, North Carolina.  The band, formed in 1990, is fronted by guitarists/vocalists Ash Bowie and Dave Brylawski.  Brian Quast plays drums, and Steve Popson plays bass guitar.  Eddie Watkins was the band's original drummer, but did not rejoin the band upon its reunion in 2008.

Question: Jason Hammel plays drums with husband and wife duo in which American indie band formed in 1997?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the American indie band."
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    },
    "genre": {
      "type": "string",
      "description": "The musical genre of the band."
    },
    "members": {
      "type": "array",
      "description": "Key members of the band, especially the husband-wife duo.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the band member."
          },
          "role": {
            "type": "string",
            "description": "The primary role of the member in the band (e.g., drums, vocals)."
          },
          "is_part_of_duo": {
            "type": "boolean",
            "description": "Indicates if the member is part of the core husband-wife duo."
          }
        },
        "required": [
          "name",
          "role",
          "is_part_of_duo"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "band_name",
    "formation_year",
    "genre",
    "members"
  ],
  "additionalProperties": false
}
