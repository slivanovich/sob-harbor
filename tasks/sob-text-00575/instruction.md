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
Dario Seixas: Dario Seixas Filho (born March 11, 1971) is a rock bass player, who most recently played with the multi-platinum band Jack Russell's Great White.  He has also toured with the hard rock band Firehouse and recorded their 2003 release Prime Time.  He has been credited by the Brazilian media as the first Brazilian musician to play in a top hard rock band.  Seixas has also toured with metal legend Stephen Pearcy of RATT, and is a current member of the bands Goodbye Thrill and Crown of Thorns.  His stage presence and bass tricks have earned him the reputation of a "not to miss" performer.

Espen Sommer Eide: Espen Sommer Eide was born in Oslo, Norway.  Espen played music originally on percussion instruments, flutes and trumpet, before emphasising computer-generated sounds.  He currently lives in Bergen, Norway where he is involved in the city's experimental music scene.  Eide has released several solo albums as Phonophani, under the Rune Grammofon record label.  Phonophani is multi-instrumentalist and digital electronics music, characterized by various manipulated live instruments integrated with pure electronic sounds.

Dimmer (band): Dimmer was the name under which New Zealand musician Shayne Carter (formerly of Straitjacket Fits, The DoubleHappys, and Bored Games) recorded and played music from 1994-2012.  It began as an umbrella name for jam sessions and home recordings, with various members and guests, but became a more settled four-piece rock band (especially from 2006–10, when only the bassist changed).  37 musicians played a part in Dimmer's 18 years, with Carter the only permanent fixture.

Dial MTV: Dial MTV is a television series on MTV that played music videos.  It premiered February 17, 1986.  Much like "Total Request Live", "Dial MTV" played the top five or top ten most requested videos of the day, as requested by viewers who dialed in (hence, the name) to vote for their favorite video.  The countdown started with the fifth or tenth most requested video and ended with the most requested.  The show generally aired Monday through Friday for 30 minutes to one hour.  The scheduling and length fluctuated over the years.

C4 (New Zealand): C4 was a New Zealand television channel owned and operated by MediaWorks New Zealand.  C4 was available on both digital terrestrial and satellite platforms and played music around the clock and had some speciality music shows such as "HomeGrown" (New Zealand music show), "Video Hits" and "Biggest Records Right Now".  The channel was originally launched in 2003 as a re-branding of TV4 which had been broadcasting since 1997.  On 1 May 2010, as C4 had been moving away from music programming since 2008, the jukebox side was split off and was re-launched as C4 2.  C4 2 was only available on digital Freeview terrestrial and satellite platforms.  At the end of 2010 an announcement was made that MediaWorks would again re-brand the current C4 channel as FOUR, which meant C4 2 would become just C4.  C4 shut down on 26 June 2014 at 1 am.  It was replaced by The Edge TV on 27 June 2014 at 4 pm.

Rene Paulo: Rene Paulo (born in 1930) is an American pianist.  Born in the rural district of Schofield, Paulo grew up in Wahiawa, Hawaii.  His grandparents on his mother's side were from the Philippines, becoming naturalized US citizens after his grandfather joined the US military.  Rene's musical background is in classical music, and he studied briefly at the Juilliard School of Music in New York with Lonnie Epstein and Gerald Tracy.  He soon branched out into improvisation, listening to jazz pianists such as Art Tatum, Alec Templeton, Fats Waller, Earl "Fatha" Hines, and boogie woogie styles.  He is known as "Hawaii's Favorite and Most Famous Pianist" and has been invited repeatedly to perform in Las Vegas, Los Angeles, and Tokyo.  Paulo played with famous artists like Alfred Apaka, Hilo Hattie, Don Ho and Sandii.  He has played music at a church in Kapolei, Hawaii that was founded by Pastor Danny Yamashiro and is the father of cosmopolitan and versatile saxophonist Michael Paulo.

The Bucks: The Bucks were a band who played music based largely on Irish folk, touring briefly and recording and releasing one album for WEA Records in 1994.  While remaining obscure, the band was formed by well-known Irish musicians Ron Kavana and Terry Woods (of The Pogues, Sweeney's Men and Steeleye Span).  Paddy Keenan played pipes.  James McNally (Storm, Pogues, Afro-Celt Sound System) was also a member, as were several members of Kavana's primary group, The Alias Band (Miriam Kavana, Fran Byrne).

Rachel's: Rachel's were an American chamber music group that formed in Louisville, Kentucky, in 1991.  Former Rodan guitarist Jason Noble played music individually and referred to himself as Rachel's but then began collaborating with core members violist Christian Frederickson and pianist Rachel Grimes.  The group's work was strongly influenced by classical music, particularly inspired by the minimalist music of the late 20th century, and its compositions reflect this.  While the trio formed the core part of the band, the group's recordings and performances featured a varying ensemble of musicians, who played a range of string instruments (including viola and cello) in combination with piano, guitars, electric bass guitar, and a drum set that included a large orchestral bass drum.  A key influence on the music of Rachel's was the music of the English composer Michael Nyman, whose music the group's work resembles in both instrumentation and compositional style.

Stephen Pearcy: Stephen Eric Pearcy (born July 3, 1956), known as Stephen Pearcy, is an American musician.  He is best known as the founder, singer, and songwriter of the heavy metal band Ratt.  He has also been in the bands Firedome, Crystal Pystal, Arcade, Vicious Delite, Vertex.  He has also recorded four records as a solo artist.

Panoram: Panoram was the trademark name of a visual jukebox that played music accompanied by a synched, filmed image (the effect being the equivalent of 1980s music videos) popular within the United States during the 1940s.  The device consisted of a jukebox playing a closed-loop 16mm film reel projected onto a glass screen.

Question: Name the member of Ratt that has played music with Dario Seixas Filho and Firedome?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the musician."
    },
    "bands_associated": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of bands the musician has been a member of."
    },
    "collaborations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "collaborator_name": {
            "type": "string",
            "description": "The name of the artist or band collaborated with."
          },
          "collaboration_type": {
            "type": "string",
            "description": "The nature of the collaboration (e.g., 'toured with', 'recorded with')."
          }
        },
        "required": [
          "collaborator_name",
          "collaboration_type"
        ],
        "additionalProperties": false
      },
      "description": "A list of collaborations the musician has had with other artists or bands."
    },
    "role_in_ratt": {
      "type": "string",
      "description": "The musician's role within the band Ratt."
    }
  },
  "required": [
    "musician_name",
    "bands_associated",
    "collaborations",
    "role_in_ratt"
  ],
  "additionalProperties": false
}
