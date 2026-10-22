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
Nights in Port Said: Nights in Port Said (French: Les nuits de Port Said) is a 1932 French film directed by Leo Mittler and starring Renée Héribel, Gustav Diessl and Oskar Homolka.

Hector Berlioz: Louis-Hector Berlioz (] (English: ); 11 December 1803 – 8 March 1869) was a French Romantic composer, best known for his compositions "Symphonie fantastique" and "Grande messe des morts" (Requiem).  Berlioz made significant contributions to the modern orchestra with his "Treatise on Instrumentation".  He specified huge orchestral forces for some of his works, and conducted several concerts with more than 1,000 musicians.  He also composed around 50 songs.  His influence was critical for the further development of Romanticism, especially in composers like Richard Wagner, Nikolai Rimsky-Korsakov, Franz Liszt, Richard Strauss, and Gustav Mahler.

Agoria (musician): Agoria (born Sébastien Devaud, January 16, 1976) is a French electronic record producer, composer and DJ.  He made four albums including the soundtrack to the movie "Go Fast".  He is one of the founders of the record label InFiné.  Since he is attached to the city of Lyon, he also took part in the creation of the French indie and electronic music festival Les Nuits Sonores.

Les Nuits Sans Kim Wilde: "Les Nuits Sans Kim Wilde" is a single by Laurent Voulzy about British singer Kim Wilde.  It was released in France as a single in 1985 after Wilde herself agreed to sing backing vocals on it.  In Germany the song was used as the B-side to "Belle-Ile-en-Mer Marie-Galante" (the French B-side to "Les Nuits Sans Kim Wilde").

Les nuits d'été: Les nuits d'été ("Summer Nights"), Op. 7, is a song cycle by the French composer Hector Berlioz.  It is a setting of six poems by Théophile Gautier.  The cycle, completed in 1841, was originally for soloist and piano accompaniment.  Berlioz orchestrated one of the songs in 1843, and did the same for the other five in 1856.  The cycle was neglected for many years, but during the 20th century it became, and has remained, one of the composer's most popular works.  The full orchestral version is more frequently performed in concert and on record than the piano original.  The theme of the work is the progress of love, from youthful innocence to loss and finally renewal.

Les nuits d'été discography: Les nuits d'été ("Summer Nights"), Op. 7, is a song cycle by the French composer Hector Berlioz, setting six poems by Théophile Gautier.  The cycle, completed in 1841, was originally for soloist and piano accompaniment.  Berlioz orchestrated one of the songs in 1843, and did the same for the other five in 1856.  The cycle was neglected for many years, but during the 20th century it became, and has remained, one of the composer's most popular works.  Of the many recordings made in the 20th and 21st centuries, most are of the orchestrated version and are sung by a soprano or mezzo-soprano.

Savage Nights: Savage Nights (French: Les Nuits Fauves ) is a 1992 French drama film directed and written by Cyril Collard.  It stars Collard, Romane Bohringer and Carlos López.  The film is an adaptation of Collard's semi-autobiographical novel "Les Nuits Fauves," published in 1989.  It won four César Awards including Best Film.

University of Michigan Athletic Hall of Honor: The University of Michigan Athletic Hall of Honor, founded in 1978, recognizes University of Michigan athletes, coaches, and administrators who have made significant contributions to the university's athletic programs.  To qualify for induction into the Hall of Honor, an individual must have been an All-American, set an NCAA, U.S., or world record, won an NCAA title, or made significant contributions to the university's athletic department as a coach or administrator.  The nomination and selection process is conducted by the Letterwinners M Club executive board.

Colonel Reyel: Rémy Ranguin better known by his stage name Colonel Reyel (born 5 October 1984) is a French dancehall, R&B and electro music artist.  His 2011 album "Au Rapport" reached the top of the French Albums Chart and two singles from the album, "Celui..." and "Toutes les nuits" topped the French Singles Chart in two consecutive weeks in February–March 2011.  In June 2011, "Au Rapport" went platinum.  He is of Guadeloupe origin.

Cyril Collard: Cyril Collard (] ; 19 December 1957, Paris − 5 March 1993, Paris) was a French author, filmmaker, composer, musician and actor.  He is known for his unapologetic portrayals of bisexuality and HIV in art, particularly his autobiographical novel and film "Les Nuits Fauves" ("Savage Nights").  Openly bisexual, Collard was also one of the first French artists to speak openly about his HIV-positive status.

Question:  Les nuits d'été is a song cycle by a romantic composer who made significant contributions to the modern orchestra with what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_cycle_title": {
      "type": "string",
      "description": "The title of the song cycle."
    },
    "composer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the composer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the composer."
        },
        "era": {
          "type": "string",
          "description": "The musical era the composer belongs to."
        }
      },
      "required": [
        "name",
        "nationality",
        "era"
      ],
      "additionalProperties": false
    },
    "orchestral_contribution": {
      "type": "string",
      "description": "The specific contribution made to the modern orchestra."
    }
  },
  "required": [
    "song_cycle_title",
    "composer",
    "orchestral_contribution"
  ],
  "additionalProperties": false
}
