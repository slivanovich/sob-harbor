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
Christoph Martin Wieland: Christoph Martin Wieland (] ; 5 September 1733 – 20 January 1813) was a German poet and writer.  He is best-remembered for having written the first Bildungsroman ("Geschichte des Agathon"), as well as the epic "Oberon", which formed the basis for Carl Maria von Weber's opera of the same name.

Bassoon Concerto (Weber): Carl Maria von Weber's Concerto for Bassoon in F Major, Op. 75 (J. 127) was composed in 1811 for Munich court musician Georg Friedrich Brandt, and then revised in 1822.  Primarily an opera conductor and composer, Weber had only arrived a few months earlier in Munich, where he was extremely well received.  The concerto is one of two pieces written for bassoon by Weber, the other being "Andante e Rondo Ungarese", Op. 35 (J. 158).  A typical performance lasts 18–20 minutes.

Silvana (opera): Silvana, J. 87, is an opera by Carl Maria von Weber, first performed in Frankfurt am Main on 16 September 1810.  The libretto, by , is a reworking of an earlier, unsuccessful opera by Weber, "Das Waldmädchen ".  Weber also reused music from the same piece in "Silvana".

Oberon: Oberon is a king of the fairies in medieval and Renaissance literature.  He is best known as a character in William Shakespeare's play "A Midsummer Night's Dream", in which he is Consort to Titania, Queen of the Fairies.

Peter und Ännchen: "Peter und Ännchen" premiered on 29 September 1809 in the theatre of the Ludwigsburg Palace near Stuttgart.  The opera was popular in Germany in its day and a version of the score for voice and piano was published by Breitkopf & Härtel.  It was also performed in Paris in 1810 as "Pierre et Annette".  Franz Carl Hiemer had written the libretto for Abeille's first opera, "Amor und Psyche" (1800) as well as the libretti for Carl Maria von Weber's operas "Silvana" and "Abu Hassan".

Amor und Psyche: Amor und Psyche is an opera ("singspiel") in four acts composed by Ludwig Abeille to a German "libretto" by Franz Carl Hiemer (1768–1822).  Based on the story of Cupid and Psyche, the opera premiered on January 18, 1800 at the Hoftheater (Herzöglichestheater) in Stuttgart.  "Amor und Psyche" was popular in Germany in its day and a version of the score for voice and piano was published by Breitkopf & Härtel.  Franz Carl Hiemer went on to write the libretto for Abeille's third opera, "Peter und Ännchen" (1809) as well as the libretti for Carl Maria von Weber's operas "Silvana" and "Abu Hassan".

Euryanthe: Euryanthe is a German "grand, heroic, romantic" opera by Carl Maria von Weber, first performed at the Theater am Kärntnertor, Vienna on 25 October 1823.  Though acknowledged as one of Weber's most important operas, the work is rarely staged because of the weak libretto by Helmina von Chézy (who, incidentally, was also the author of the failed play "Rosamunde", for which Franz Schubert wrote music).  "Euryanthe" is based on the 13th-century romance ""L'Histoire du très-noble et chevalereux prince Gérard, comte de Nevers et la très-virtueuse et très chaste princesse Euriant de Savoye, sa mye.""

Die drei Pintos: Die drei Pintos ("The Three Pintos") is a comic opera of which Carl Maria von Weber began composing the music, working on a libretto by Theodor Hell.  The work was completed about 65 years after Weber's death by Gustav Mahler.

Hochschule für Musik Carl Maria von Weber: The "Carl Maria von Weber" College of Music (Hochschule für Musik "Carl Maria von Weber" in German, and also/formerly known as Dresden Conservatory or Dresden Royal Conservatory) is a college of music in Dresden, Germany.

Symphony No. 1 (Weber): Carl Maria von Weber's Symphony No. 1 in C was written in 1806–1807.  While not usually acknowledged as among Weber's greatest works (a fact readily admitted by Weber himself), it is a testament to the young composer's gift of melody.

Question: who was a character in A midsummer's night dream as well as the name of Carl Maria von Weber's opera?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The name of the character and opera."
    },
    "role_in_play": {
      "type": "string",
      "description": "Description of the entity's role in William Shakespeare's play 'A Midsummer Night's Dream'."
    },
    "opera_details": {
      "type": "object",
      "properties": {
        "composer": {
          "type": "string",
          "description": "The composer of the opera with this name."
        },
        "source_material": {
          "type": "string",
          "description": "The epic that formed the basis for the opera."
        },
        "source_material_author": {
          "type": "string",
          "description": "The author of the epic that formed the basis for the opera."
        }
      },
      "required": [
        "composer",
        "source_material",
        "source_material_author"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "entity_name",
    "role_in_play",
    "opera_details"
  ],
  "additionalProperties": false
}
