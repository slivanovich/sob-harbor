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
Elizium: Elizium is the third studio album by English gothic rock band Fields of the Nephilim.  It was released in September 1990 through record label Beggars Banquet.

Dawnrazor: Dawnrazor is the debut studio album by English gothic rock band Fields of the Nephilim.  It was released in May 1987, through record label Situation Two.

Nekromanteia: Nekromanteia is the second album from the band Fields of Aplomb, released in 2003.  The album is based on the writings of Eliphas Levi (1810–1875), a French occultist who helped revive interest in ritual magic in the 19th century.  Levi studied magic and practiced necromancy (an ancient art of conjuring the dead for the purpose of divination) on several occasions.

4 from the Village: 4 From the Village is an EP by the Anglo-Icelandic band Fields.  The EP was released via Black Lab Recordings on July 10 2006.

Everything Last Winter: Everything Last Winter is the debut album from the Anglo-Icelandic band Fields, first released April 2, 2007 by Atlantic Records.  The album was produced by Michael Beinhorn.  Tracks released as singles are "If You Fail We All Fail" and "Charming The Flames".  The album is dedicated to Alan Spenner and features many thanks including to the bands Snow Patrol, Editors, and Bloc Party.  The track "Song For The Fields" was featured as a "Single of the Week" on iTunes.

Fields (Fields album): Fields is the debut studio album by the English progressive rock band Fields, released in 1971.

Carl McCoy: Carl McCoy (born 18 January 1963, Lambeth, London, England) is the frontman for gothic rock band Fields of the Nephilim.

Baltimore: Baltimore ( , ] ) is the largest city in the U.S. state of Maryland, and the 29th-most populous city in the country.

Fields of Aplomb: Fields of Aplomb, abbreviated FoA, is a Gothic metal/alternative band formed in Baltimore in 1998 upon the demise of Pelican's Daughter.  known for surrealistic and gloomy lyrics.  Their first album, "Reverence for the Lost", addresses themes of extreme introversion.  Their second release "Nekromanteia" (2003), is based on the writings of Eliphas Levi (1810–1875), a French occultist who helped revive interest in magic in the 19th century.  Levi studied magic and practiced necromancy on several occasions.  In 2004 FoA released "Spiritum Oriundus" as a continuance of spiritual magic, however, focusing on seances and tormented appiritions.  In the winter of 2006, FoA released "Weoroscipe" which illuminated the power of seduction, black magic, fetishes, and faith. " Disillusionment" (2006) includes remaster of "Reverence for the Lost" and "Nekromaneia" plus two additional songs and a DVD.  The band took their name from the folklore tale of the inscribed surrounding land to the ancient Sumerian society (Fourth B.C), stating that those who died, either violently or tragically, their souls were to wonder the Fields of Adplumbum (Aplomb) until they acknowledged and accepted their fate.

Rubicon (English band): Rubicon was an early 1990s offshoot of the band Fields of the Nephilim who released two albums.

Question: What state was the band Fields of Aplomb formed in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "formation_location_city": {
      "type": "string",
      "description": "The city where the band was formed."
    },
    "formation_location_state": {
      "type": "string",
      "description": "The U.S. state where the band was formed."
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    }
  },
  "required": [
    "band_name",
    "formation_location_city",
    "formation_location_state"
  ],
  "additionalProperties": false
}
