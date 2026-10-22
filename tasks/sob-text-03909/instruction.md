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
Showtime, Storytime: Showtime, Storytime is a video release, released as a double Blu-ray, DVD and CD from Finnish symphonic metal band Nightwish.  Nuclear Blast recorded their live performance at Wacken Open Air in Wacken, Germany on August 3, 2013.  "Showtime, Storytime" is the first Nightwish production to feature Floor Jansen on vocals.  She initially replaced previous vocalist Anette Olzon during their North America tour leg, and on October 9, 2013, it was revealed that she would become an official band member, along with Troy Donockley.  The running time of the concert is 1 hour and 38 minutes.  The album also contains a 120-minute documentary about the first days of Jansen in the band, still as an only live member, and her process of adaptation in the band, called "Please Learn the Setlist in 48 Hours".

Imaginaerum (film): Imaginaerum (also promoted as Imaginaerum by Nightwish) is a 2012 Finnish-Canadian musical fantasy film co-written and directed by Stobe Harju.  It was developed with and features music from Finnish symphonic metal band Nightwish's seventh studio album of the same name; Nightwish's keyboardist and songwriter Tuomas Holopainen co-wrote the film.  "Imaginaerum", which is produced by Markus Selin from Solar Films Inc. along with Nightwish, is the feature film debut of Stobe Harju.

Planet Hell: Planet Hell is a song played by the Finnish symphonic metal band Nightwish.  The song was recorded for their 2004 album "Once".  Though it is known as a symphonic metal song, many argue it as falling under the gothic metal category.  The song begins with a male choir chanting "Ah" (in an introduction reminiscent of Dark Chest of Wonders), with orchestral background music for a full minute before the band starts playing.  Planet Hell also features the vocals of the bands bassplayer Marco Hietala.  It is the Nightwish song in which Hietala gets to use his vocals the most.

Endless Forms Most Beautiful (album): Endless Forms Most Beautiful is the eighth album by Finnish symphonic power metal band Nightwish.  It was released on March 27, 2015 in Argentina and most of Europe, March 30 in the UK, and March 31 in the US.  The album is the band's first featuring singer Floor Jansen and the first with Troy Donockley as a full-time member.  It was recorded without drummer Jukka Nevalainen, who took a break from the band due to severe insomnia.  Drumming was by Kai Hahto of Wintersun and Swallow the Sun.  The album includes only five Nightwish members, despite its being their first album release as a sextet.

Floor Jansen: Floor Jansen (] ; born 21 February 1981 in Goirle) is a Dutch singer, songwriter, and vocal coach.  She is the lead vocalist of Finnish symphonic metal band Nightwish.

Élan (song): "Élan" is a single by Finnish symphonic metal band Nightwish, the first from their eighth album "Endless Forms Most Beautiful".  The song marks the first Nightwish song to feature its newest frontwoman, Dutch singer Floor Jansen, on vocals, and also the first to feature Troy Donockley as a full-time member and Kai Hahto as a temporary replacement for Jukka Nevalainen.

Oceanborn Europe Tour: Oceanborn Europe Tour was a concert tour by Finnish symphonic metal band Nightwish from November 12 to December 12, 1999.  The tour is notable for featuring the band's first European concerts.  Oceanborn Europe Tour followed a Finnish leg with 33 shows, the Summer of Wilderness.  In this tour, Nightwish played beside German heavy metal band Rage, and Nightwish was occasionally supported by Finnish singer Tapio Wilska, singing in the songs "The Pharaoh Sails to Orion" and "Devil and the Deep Dark Ocean"; Tuomas Holopainen performed "Beauty and the Beast" and "Astral Romance" beside Nightwish's frontwoman, Tarja Turunen.

Wish I Had an Angel: "Wish I Had An Angel" is the eleventh single for Finnish symphonic metal band Nightwish, the second from their fifth album "Once".  The song features vocals by then-vocalist Tarja Turunen and bassist Marco Hietala.  The song was still performed live after Turunen's departure with Anette Olzon, before her departure, and current vocalist Floor Jansen afterwards.

Nightwish discography: The discography of the Finnish symphonic metal band Nightwish consists of eight studio albums, one extended play, four live albums, seven compilations, thirteen music videos and twenty one singles.  The band was formed in 1996 by songwriter and keyboardist Tuomas Holopainen, guitarist Emppu Vuorinen, and former vocalist Tarja Turunen; Nightwish's current line-up has six members although Turunen has been replaced by Anette Olzon, and the original bassist, Sami Vänskä, has been replaced by Marco Hietala, who also took over the male vocalist part.  Olzon left the band in 2012 and was replaced by Floor Jansen.

Marty Raybon: Marty Raybon (born December 8, 1959) is an American country music artist.  He is known primarily for his role as the lead singer of the band Shenandoah, a role which he held from 1985 to 1997, until he rejoined the band in 2014.  He recorded his first solo album, "Marty Raybon", in 1995 on Sparrow Records.  Before leaving Shenandoah in 1997, he and his brother Tim formed a duo known as the Raybon Brothers, which had crossover success that year with the hit single "Butterfly Kisses".

Question: Who is the lead vocalist of Finnish symphonic metal band Nightwish, Marty Raybon or  Floor Jansen?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band in question."
    },
    "band_genre": {
      "type": "string",
      "description": "The musical genre of the band."
    },
    "lead_vocalist_name": {
      "type": "string",
      "description": "The name of the current lead vocalist of the band."
    },
    "other_candidate_name": {
      "type": "string",
      "description": "The name of the other person mentioned in the question."
    },
    "is_other_candidate_vocalist_of_band": {
      "type": "boolean",
      "description": "Indicates whether the other candidate is a vocalist of the band."
    }
  },
  "required": [
    "band_name",
    "band_genre",
    "lead_vocalist_name",
    "other_candidate_name",
    "is_other_candidate_vocalist_of_band"
  ],
  "additionalProperties": false
}
