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
Toccata and Fugue in D minor, BWV 565: The Toccata and Fugue in D minor, BWV 565, is a piece of organ music written, according to its oldest extant sources, by Johann Sebastian Bach.  The piece opens with a toccata section, followed by a fugue that ends in a coda.  It is one of the most famous works in the organ repertoire.

Prelude and Fugue in A minor, BWV 543: Prelude and Fugue in A minor, BWV 543 is a piece of organ music written by Johann Sebastian Bach sometime around his years as court organist to the Duke of Saxe-Weimar (1708–1717).

Toccata, Adagio and Fugue in C major, BWV 564: Toccata, Adagio, and Fugue in C major (BWV 564) is an organ composition by Johann Sebastian Bach.  As is the case with most other organ works by Bach, the autograph score does not survive.  The earliest manuscript copies were probably made in 1719–1727.  The title of the piece in these copies is given, as expected of organ literature of the time, simply as "Toccata in C major" (or more precisely, "Toccata ped: ex C" in one source and "Toccata ex C♮ pedaliter", referring to the obbligato pedal part).  The piece is an early work, probably composed in the mid-to-late Weimar years, i.e. 1710–1717.  It shares some similarities with other toccatas composed around the same time, such as BWV 538, BWV 540, and others: all show the influence of concerto style and form.

Great Fantasia and Fugue in G minor, BWV 542: The Great Fantasia and Fugue in G minor, BWV 542, is an organ prelude and fugue by Johann Sebastian Bach.  It acquired that name to distinguish it from the earlier Little Fugue in G minor, which is shorter.  This piece is not to be confused with the Prelude and Fugue in A minor, which is also for organ and also sometimes called "the Great".

Fugue in G minor, BWV 578: Fugue in G minor, BWV 578, (popularly known as the "Little Fugue"), is a piece of organ music written by Johann Sebastian Bach during his years at Arnstadt (1703–1707).  It is one of Bach's best known fugues and has been arranged for other voices, including an orchestral version by Leopold Stokowski.

Toccata and Fugue in F major, BWV 540: The Toccata and Fugue in F Major, BWV 540 is an organ work written by Johann Sebastian Bach.  The toccata is thought to be written after 1714, and the fugue before 1731.  It is thought by some that Bach joined together two previously separate pieces to create this work.

Toccata and Fugue in D minor, BWV 538: The Toccata and Fugue in D minor, BWV 538, is an organ piece by Johann Sebastian Bach.  Like the better-known BWV 565, BWV 538 also bears the title "Toccata and Fugue in D Minor", although it is often referred to by the nickname Dorian – a reference to the fact that the piece is written without a key signature – a notation that is uncommon today and leads one to assume the Dorian mode.

Prelude and Fugue in E minor, BWV 548: Prelude and Fugue in E minor, BWV 548 is a piece of organ music written by Johann Sebastian Bach sometime between 1727 and 1736, during his time in Leipzig.  The work is sometimes called "The Wedge" due to the tonal structure of the fugue theme.

Nun komm, der Heiden Heiland: "Nun komm, der Heiden Heiland " (original: "Nu kom der Heyden heyland ", English: "Now come, Saviour of the heathens") is a Lutheran chorale of 1524 with words written by Martin Luther, based on "Veni redemptor gentium " by Ambrose.  It was printed in the Erfurt "Enchiridion" of 1524.  The chorale was used as the prominent hymn for the first Sunday of Advent for centuries.  It was used widely in organ settings by Protestant baroque composers, most notably Johann Sebastian Bach: he set it as the opening chorale prelude BWV 599 of Orgelbüchlein; and three times—as BWV 659 (one of his best known organ compositions), BWV 660 and BWV 661—in his Great Eighteen Chorale Preludes.  Bach used the hymn in his chorale cantata "Nun komm, der Heiden Heiland", BWV 62 (1724) and in the opening chorale fantasia of his earlier cantata "Nun komm, der Heiden Heiland", BWV 61 , BWV 61 (1714).  Max Reger composed a chorale prelude as No. 29 of his 52 Chorale Preludes, Op. 67 in 1902.

Fantasia and Fugue in C minor, BWV 562: The Fantasia and Fugue in C minor, BWV 562 is a relatively short piece written for the organ by Johann Sebastian Bach.  Bach began the composition during his time in Weimar, and an unfinished fugue, probably by Bach, was added in his later life.  The piece features a heavily appoggiatura-laden harmony.

Question: The Toccata and Fugue in D minor, BWV 538, is an organ piece by Johann Sebastian Bach, like the better-known BWV 565, the Toccata and Fugue in D minor, BWV 565, is a piece of organ music written, according to its oldest extant sources, by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_name": {
      "type": "string",
      "description": "The name of the composer."
    },
    "piece_title": {
      "type": "string",
      "description": "The full title of the musical piece."
    },
    "bwv_number": {
      "type": "string",
      "description": "The Bach-Werke-Verzeichnis (BWV) number of the piece."
    },
    "instrumentation": {
      "type": "string",
      "description": "The primary instrument for which the piece was written."
    },
    "is_famous_work": {
      "type": "boolean",
      "description": "Indicates if the piece is considered one of the most famous works in its repertoire."
    }
  },
  "required": [
    "composer_name",
    "piece_title",
    "bwv_number",
    "instrumentation",
    "is_famous_work"
  ],
  "additionalProperties": false
}
