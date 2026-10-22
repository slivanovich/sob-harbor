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
Cinq mélodies &quot;de Venise&quot;: Cinq mélodies "de Venise", Op. 58, is a song cycle by Gabriel Fauré, of five mélodies for voice and piano.  Composed in 1891, the cycle is based on five poems by Paul Verlaine, from the collections "Fêtes galantes" and "Romances sans paroles".  According to Fauré himself, the song cycle contains a number of musical themes which recur from song to song.  He used a similar technique for his later song cycle "La bonne chanson", which was also based on Verlaine's poetry.

Love Blows As the Wind Blows: Love Blows As the Wind Blows is a song cycle for voice and piano or string quartet composed in 191112 by George Butterworth (18851916).  It sets four poems by William Ernest Henley from his "Book of Verses" (1888).  The composer orchestrated three songs from the cycle in 1914, omitting "Fill a Glass with Golden Wine".

Cinq poèmes de Charles Baudelaire: The Cinq poèmes de Charles Baudelaire (CD 64) constitute a song cycle for voice and piano by Claude Debussy, on poems taken from "Les Fleurs du mal" by Charles Baudelaire.  Composed from December 1887 to March 1889, these five highly developed vocal pieces were not well received by Parisian musical circles because of the Wagnerian influence they revealed.

Les nuits d'été: Les nuits d'été ("Summer Nights"), Op. 7, is a song cycle by the French composer Hector Berlioz.  It is a setting of six poems by Théophile Gautier.  The cycle, completed in 1841, was originally for soloist and piano accompaniment.  Berlioz orchestrated one of the songs in 1843, and did the same for the other five in 1856.  The cycle was neglected for many years, but during the 20th century it became, and has remained, one of the composer's most popular works.  The full orchestral version is more frequently performed in concert and on record than the piano original.  The theme of the work is the progress of love, from youthful innocence to loss and finally renewal.

Erik Satie: Éric Alfred Leslie Satie (] ; 17 May 18661 July 1925), who signed his name Erik Satie after 1884, was a French composer and pianist.  Satie was a colourful figure in the early 20th-century Parisian avant-garde.  His work was a precursor to later artistic movements such as minimalism, Surrealism, repetitive music, and the Theatre of the Absurd.

The Book of the Hanging Gardens: The Book of the Hanging Gardens (German: Das Buch der hängenden Gärten ), Op. 15, is a fifteen-part song cycle composed by Arnold Schoenberg between 1908 and 1909, setting poems of Stefan George.  George's poems, also under the same title, track the failed love affair of two adolescent youths in a garden, ending with the woman's departure and the disintegration of the garden.  The song cycle is set for solo voice and piano.  The "Book of the Hanging Gardens" breaks away from conventional musical order through its usage of atonality.  The composition was premiered by Austrian singer Martha Winternitz-Dorda and pianist Etta Werndorf on January 14, 1910, in Vienna.

Shadows and Sun: Shadows and Sun / Ombres et Soleil: Selected Writings (1913-1952) is a comprehensive bilingual collection of the poems of Paul Eluard.  Translated by Cicely Buckley and published in 1995 by Oyster River Press, the book is illustrated with the cover art “The dreamer” by Pablo Picasso, and six pen and ink drawings by Picasso, René Magritte, Marc Chagall, and André Lhote.  Eluard’s simple language and sensitivity in the early and later love poems, and in the ‘poèmes engagés’ (poems committed to recovering justice for all), earned him the name of “the people’s poet.”  Eluard wrote before and after two world wars when he served as medic and infantryman.  His poem "Guernica" was written when Picasso created an anti-war painting inspired by the bombing of Guernica during the Spanish Civil War, when Nazis bombed the market place at midday.

Les nuits d'été discography: Les nuits d'été ("Summer Nights"), Op. 7, is a song cycle by the French composer Hector Berlioz, setting six poems by Théophile Gautier.  The cycle, completed in 1841, was originally for soloist and piano accompaniment.  Berlioz orchestrated one of the songs in 1843, and did the same for the other five in 1856.  The cycle was neglected for many years, but during the 20th century it became, and has remained, one of the composer's most popular works.  Of the many recordings made in the 20th and 21st centuries, most are of the orchestrated version and are sung by a soprano or mezzo-soprano.

Gaspard de la nuit: Gaspard de la nuit: Trois poèmes pour piano d'après Aloysius Bertrand is a suite of pieces for solo piano by Maurice Ravel, written in 1908.  It has three movements, each based on a poem or "fantaisie" from the collection "Gaspard de la Nuit — Fantaisies à la manière de Rembrandt et de Callot" completed in 1836 by Aloysius Bertrand.  The work was premiered in Paris, on January 9, 1909, by Ricardo Viñes.

Trois poèmes d'amour: The Trois poèmes d'amour ("Three Love Poems") is a 1914 song cycle for voice and piano by Erik Satie.  It is the only set of mélodies (French art songs) Satie composed to his own texts.  In performance it lasts 2–3 minutes.

Question: The Trois poèmes d'amour, ("Three Love Poems") is a 1914 song cycle for voice and piano by which French composer and pianist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_cycle_title": {
      "type": "string",
      "description": "The title of the song cycle."
    },
    "composition_year": {
      "type": "integer",
      "description": "The year the song cycle was composed."
    },
    "instrumentation": {
      "type": "string",
      "description": "The instrumentation for the song cycle."
    },
    "composer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the composer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the composer."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions of the composer."
        }
      },
      "required": [
        "name",
        "nationality",
        "professions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_cycle_title",
    "composition_year",
    "instrumentation",
    "composer"
  ],
  "additionalProperties": false
}
