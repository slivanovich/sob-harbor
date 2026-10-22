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
Die drei Pintos: Die drei Pintos ("The Three Pintos") is a comic opera of which Carl Maria von Weber began composing the music, working on a libretto by Theodor Hell.  The work was completed about 65 years after Weber's death by Gustav Mahler.

Hochschule für Musik Carl Maria von Weber: The "Carl Maria von Weber" College of Music (Hochschule für Musik "Carl Maria von Weber" in German, and also/formerly known as Dresden Conservatory or Dresden Royal Conservatory) is a college of music in Dresden, Germany.

Clarinet Quintet (Weber): The Clarinet Quintet in B♭ Major, Op. 34, is a clarinet quintet that was composed by Carl Maria von Weber from 1811 to 1815.  Like with most of Weber's other clarinet compositions, the quintet was written for the German clarinet virtuoso Heinrich Baermann.

Symphony No. 1 (Weber): Carl Maria von Weber's Symphony No. 1 in C was written in 1806–1807.  While not usually acknowledged as among Weber's greatest works (a fact readily admitted by Weber himself), it is a testament to the young composer's gift of melody.

Wiener Carneval: Wiener Carneval ("Viennese Carnival"), opus 3, is a waltz composed by Johann Strauss I in 1828.  The waltz was intended as a contribution to the carnival of 1828 Johann Strauss appeared as leader of a group of musicians at the balls at the Kettenbrücke in Leopoldstadt.  The fourth waltz theme incorporates melodies from Carl Maria von Weber's Ocean aria from Oberon, with Rezia’s words "Mein Hüon, mein Gatte, die Retter, sie nah’n" ("My Hüon, my husband, the rescuers approach"), partly as a tribute to Weber, who had died not long before Strauss' waltz was composed.

Bassoon Concerto (Weber): Carl Maria von Weber's Concerto for Bassoon in F Major, Op. 75 (J. 127) was composed in 1811 for Munich court musician Georg Friedrich Brandt, and then revised in 1822.  Primarily an opera conductor and composer, Weber had only arrived a few months earlier in Munich, where he was extremely well received.  The concerto is one of two pieces written for bassoon by Weber, the other being "Andante e Rondo Ungarese", Op. 35 (J. 158).  A typical performance lasts 18–20 minutes.

Silvana (opera): Silvana, J. 87, is an opera by Carl Maria von Weber, first performed in Frankfurt am Main on 16 September 1810.  The libretto, by , is a reworking of an earlier, unsuccessful opera by Weber, "Das Waldmädchen ".  Weber also reused music from the same piece in "Silvana".

Carl Maria von Weber: Carl Maria Friedrich Ernst von Weber (18 or 19 November 1786 5 June 1826) was a German composer, conductor, pianist, guitarist and critic, and was one of the first significant composers of the Romantic school.

Euryanthe: Euryanthe is a German "grand, heroic, romantic" opera by Carl Maria von Weber, first performed at the Theater am Kärntnertor, Vienna on 25 October 1823.  Though acknowledged as one of Weber's most important operas, the work is rarely staged because of the weak libretto by Helmina von Chézy (who, incidentally, was also the author of the failed play "Rosamunde", for which Franz Schubert wrote music).  "Euryanthe" is based on the 13th-century romance ""L'Histoire du très-noble et chevalereux prince Gérard, comte de Nevers et la très-virtueuse et très chaste princesse Euriant de Savoye, sa mye.""

Modest Mussorgsky: Modest Petrovich Mussorgsky (Russian: Моде́ст Петро́вич Му́соргский ; ] ; 21 March [O.S. 9 March] 1839 – 28 March [O.S. 16 March] 1881 ) was a Russian composer, one of the group known as "The Five".  He was an innovator of Russian music in the romantic period.  He strove to achieve a uniquely Russian musical identity, often in deliberate defiance of the established conventions of Western music.

Question: What occupation did Modest Mussorgsky and Carl Maria von Weber share?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_one_name": {
      "type": "string",
      "description": "The name of the first person mentioned in the question."
    },
    "person_one_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations for the first person."
    },
    "person_two_name": {
      "type": "string",
      "description": "The name of the second person mentioned in the question."
    },
    "person_two_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations for the second person."
    },
    "shared_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations shared by both individuals."
    },
    "count_shared_occupations": {
      "type": "integer",
      "description": "The number of occupations shared by both individuals."
    }
  },
  "required": [
    "person_one_name",
    "person_one_occupations",
    "person_two_name",
    "person_two_occupations",
    "shared_occupations",
    "count_shared_occupations"
  ],
  "additionalProperties": false
}
