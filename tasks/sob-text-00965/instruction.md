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
String Quintet, Op. 4 (Beethoven): The String Quintet in E-flat major, Op.  4, was composed by Ludwig van Beethoven in 1795.  It was adapted from his Octet in E-flat major, Op. 103, which, despite its high opus number, was in fact composed by Beethoven in 1792/1793 but was published only in 1837, ten years after the composer's death.  The Quintet was published in Vienna in 1796.

Ludwig van Beethoven: Ludwig van Beethoven ( , ; ] ; baptised 17 December 177026 March 1827) was a German composer and pianist.  A crucial figure in the transition between the Classical and Romantic eras in Western art music, he remains one of the most famous and influential of all composers.  His best-known compositions include 9 symphonies, 5 piano concertos, 1 violin concerto, 32 piano sonatas, 16 string quartets, his great Mass the "Missa solemnis", and one opera, "Fidelio".

Ludwig van Beethoven (1712–1773): Ludwig van Beethoven the Elder, also Ludovicus van Beethoven and Lodewijk van Beethoven (January 5, 1712 – December 24, 1773) was a professional singer and music director, best known as the grandfather of the composer Ludwig van Beethoven.

Bagatelles, Op. 126 (Beethoven): Ludwig van Beethoven's Bagatelles, Op. 126, dedicated to his brother Johann van Beethoven, were published late in his career, in the year 1825.  A bagatelle, in Beethoven's usage, is a kind of brief character piece.

Ludwig van Beethoven (Baerer): Ludwig van Beethoven is a series of sculptures of Ludwig van Beethoven by German-American sculptor Henry Baerer.  Versions are displayed in Central Park in New York City, Golden Gate Park in San Francisco, and Prospect Park in Brooklyn.  The sculpture in Central Park was dedicated on July 22, 1884.  It includes two bronze statues, including a bust of Beethoven and an allegorical female figure on a polished Barre Granite pedestal.

Beethoven Gesamtausgabe: The Beethoven "Gesamtausgabe" is the first collected edition of the works of Ludwig van Beethoven.  Its full title is "Ludwig van Beethovens Werke: vollständige kritisch durchgesehene überall berechtige Ausgabe" (which roughly translated means "Ludwig van Beethoven's Works: complete, critical, thoroughly revised, authorized edition").  It was published between 1862 and 1865, with a supplementary volume appearing in 1888.

Beethoven concert of 22 December 1808: The Beethoven concert of 22 December 1808 was a benefit concert held for Ludwig van Beethoven at the Theater an der Wien in Vienna that featured the public premieres of Beethoven's Fifth and Sixth Symphonies, the Fourth Piano Concerto and the Choral Fantasy.  This concert, then called an "Akademie", occurred in a very cold hall and was approximately four hours duration.  Its featured performers were an orchestra, chorus, vocal soloists, and the composer as piano soloist.  Beethoven biographer Barry Cooper refers to the concert, in terms of its content, as the "most remarkable" of Beethoven's career.

Ludwig van (film): Ludwig van (full title: "Ludwig van: A report"; German: "Ludwig van: ein Bericht") is a black-and-white German film by Mauricio Kagel.  Filmed in 1969, it was first screened the following year.  The work was commissioned by Westdeutscher Rundfunk for the bicentennial celebrations of the birth of Ludwig van Beethoven in 1970.  The film examines the reception of the composer and his works and how he has become a consumer product of the culture industry.  The soundtrack is an arrangement of fragments of Beethoven's works, modified as if heard by the deaf composer himself; it is distinct from Kagel's 1970 composition "Ludwig van".  Prominent contemporary artists including Dieter Roth, Stefan Wewerka (), Robert Filliou, and Joseph Beuys were involved in the design.  According to "Gramophone", "at first it’s a laugh a minute ... then Kagel's film turns dark".

Beethoven Project Trio: The Beethoven Project Trio is an American piano trio that was formed in Chicago in 2008.  Its founding members are pianist George Lepauw, violinist Sang Mee Lee and cellist Wendy Warner.  The first public concert given by the trio was on March 1, 2009 at Chicago’s Murphy Auditorium for the world premiere of a recently rediscovered piano trio by (Hess 47) Ludwig van Beethoven, as well as the American premiere of another Beethoven trio (Anhang 3) and the Chicago premiere of yet another Trio (Opus 63); the performance also included the well-known “Archduke” Trio by Beethoven.  John von Rhein, music critic of the Chicago Tribune, wrote about the trio's first concert that "for musicians who had never worked together as a trio before, pianist George Lepauw, violinist Sang Mee Lee and cellist Wendy Warner made a splendid ensemble, playing with finely judged balance, evenness of sound and unanimity of style [...] Lepauw, Lee and Warner ended their program with Beethoven’s familiar “Archduke” Trio, a masterpiece that drew fully on their individual and collective abilities.  The slow movement emerged with particular eloquence here."

List of Camper Van Beethoven band members: The following is a complete chronology of the various line-ups of alternative rock music group Camper Van Beethoven.  Camper Van Beethoven (originally called "Camper Van Beethoven and the Border Patrol,") formed in 1983 in Redlands, California, before relocating to Santa Cruz, California in 1984 and San Francisco, California in 1988.  Prior to Camper Van Beethoven, band members David Lowery, Chris Molla, Victor Krummenacher and Bill McDonald played in several similarly conceived groups, with names like the Estonian Gauchos and Sitting Duck, that performed songs later found in the Camper Van Beethoven repertoire.  Other members of these groups included Johnny Hickman and Eric Laing.

Question: what nationality was ludwig van beethoven?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_name": {
      "type": "string",
      "description": "The full name of the composer."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the composer."
    },
    "occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations held by the composer."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the composer."
    },
    "death_year": {
      "type": "integer",
      "description": "The death year of the composer."
    }
  },
  "required": [
    "composer_name",
    "nationality",
    "occupations",
    "birth_year",
    "death_year"
  ],
  "additionalProperties": false
}
