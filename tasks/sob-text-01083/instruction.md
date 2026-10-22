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
Gerardo Ortiz: Gerardo Ortiz Medína (born October 5, 1989), simply known as Gerardo Ortiz, is an American regional Mexican singer-songwriter, and record producer.  Gerardo Ortiz grew up in Pasadena, California where he attended Blair High School.  In 2010, he garnered a Grammy nomination for Best Norteño Album for his debut album "Ni Hoy Ni Mañana".  At the 2013 Mexican "Billboard" Music Awards, he was awarded four awards: Male Artist of the Year, Norteño Album of the Year, Norteño Artist of the Year, and Artist of the Year, Songs.  He was also nominated for a Grammy Award for Best Regional Mexican Music Album in 2013, for his album "El Primer Ministro".

Saint Dog: Saint Dog is an American singer.  Originally from Chisholm, Minnesota, he was an original member of the Kottonmouth Kings along with D-Loc and Brad Daddy X.  He started his career as part of the hip hop group P.T.B. (P-Town Ballers) along with D-Loc and Johnny Richter.  Daddy X had joined the group, and Johnny Richter had left for personal reasons.  The three remaining members formed the Kottonmouth Kings.  He contributed to their first three releases ("Stoners Reeking Havoc", "Royal Highness", and "Hidden Stash") before leaving to pursue a career with his brother, Big Hoss.  A small feud between Saint Dog and the Kottonmouth Kings had started after the departure of Saint from the group, but quickly simmered down and soon after disappeared altogether.  Saint Dog is currently signed to Suburban Noize Records.  On November, 18th, 2016 Saint Dog announced he signed a deal with Force 5 Records, a label run by ex Primer 55 vocalist, The DRP, with a new album coming out in early 2017.

Primer 55: Primer 55 is an American nu metal that is based in Louisville, Kentucky.  The name originates from the combination of Primer, meaning "something that's unfinished," and 55, which refers to Interstate 55, "the road that drugs run on to get to Chicago through Memphis".

Law of the Jungle (album): Law of the Jungle is a compilation album of various early jungle music tracks by various artists, released in 1994 in the United States on Moonshine Music.  Jungle had started to emerge in the United Kingdom a couple of years earlier but despite its growth, albeit slow, in the United States, no jungle albums were available on the American market.  Moonshine conceived the album as a primer for jungle music for American shores, using music from British jungle label SOUR Records, and as a spin-off to their fast tempo techno compilation series "Speed Limit 140 BPM+".  "Law of the Jungle" was the first jungle album released in the United States.

Family for Life: Family for Life is an EP by Primer 55, released independently through Crash Music.

Preston Nash: Preston Nash is an American musician, drummer, music educator, composer/songwriter, music producer, and former radio personality and producer.  He is best known as the drummer for Dope, Primer 55, Society 1, and The Color Red.  He is also known as the former producer for "The Ralph Bailey Show" on 1560 KNZR out of Bakersfield, California.  As a songwriter and composer, he's written music used in independent films, jingles heard on radio stations around the United States, and has collaborated and recorded with artists including Virus, Billie Stevens, and cellist Tina Guo.

Introduction to Mayhem: Introduction To Mayhem is the major label debut album by the American nu metal band Primer 55.  Released on January 25, 2000, it is a reissue of the band's 1999 EP "As Seen On TV".

The Hieroglyphs of Ancient Egypt: The Hieroglyphs of Ancient Egypt is part of a new genre of books focussed on Egyptian hieroglyphs.  The book is a primer on hieroglyphs from the viewpoint of topical use within history, with example photographs or illustrations.  The later chapters discuss the hieroglyphs and the history of their translation.

Frank Fontsere: Frank Fontsere (born September 2, 1967), is a professional drummer from Marietta, Georgia.  He is known mostly for his work in rap/metal group, Stuck Mojo (1996–2000) and heavy metal group, Fozzy (1999–2005, 2009–present).  He has also been a member of Agent Cooper (2004, 2005), The Duke (2005) and Primer 55 (2007).

(The) New Release: (the) New Release is the second and final studio album by American nu metal band Primer 55.  Released on August 14, 2001, the album peaked at #1 on the "Billboard" Heatseekers chart and #102 on the "Billboard" 200.  It had one single, "This Life," which peaked at #37 on Mainstream Rock Tracks.  This would be the band's final record with Island Records, who allegedly cut support shortly after the album's release due to the September 11 attacks.

Question: What genre of music is Primer 55?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "music_genre": {
      "type": "string",
      "description": "The genre of music the band plays."
    },
    "origin_city": {
      "type": "string",
      "description": "The city where the band is based."
    },
    "origin_country": {
      "type": "string",
      "description": "The country where the band is based."
    }
  },
  "required": [
    "band_name",
    "music_genre",
    "origin_city",
    "origin_country"
  ],
  "additionalProperties": false
}
