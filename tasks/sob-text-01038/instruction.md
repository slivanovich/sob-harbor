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
Richard Strauss: Richard Georg Strauss (11 June 1864 – 8 September 1949) was a leading German composer of the late Romantic and early modern eras.  He is known for his operas, which include "Der Rosenkavalier", "Elektra", "Die Frau ohne Schatten" and "Salome"; his Lieder, especially his "Four Last Songs"; his tone poems, including "Don Juan", "Death and Transfiguration", "Till Eulenspiegel's Merry Pranks", "Also sprach Zarathustra", "Ein Heldenleben", "Symphonia Domestica", and "An Alpine Symphony"; and other instrumental works such as "Metamorphosen" and his Oboe Concerto.  Strauss was also a prominent conductor in Western Europe and the Americas, enjoying quasi-celebrity status as his compositions became standards of orchestral and operatic repertoire.

Macbeth (Strauss): Macbeth is a symphonic poem written by Richard Strauss between 1886 and 1888.  The work was his first tone poem, which Strauss described as "a completely new path" for him compositionally.  Written in some semblance of sonata form, the piece was revised more thoroughly than any of Strauss's other works; these revisions, focused primarily on the development and recapitulation sections, show how much the composer was struggling at this point in his career to balance narrative content with musical form.  Bryan Gilliam writes in "The New Grove Dictionary of Music and Musicians" that, "New path or not, "Macbeth" failed to find a firm place in the concert repertory, because it lacked the thematic cogency and convincing pacing of musical events so evident in the two antecedent works ["Don Juan" and "Tod und Verklärung" ("Death and Transfiguration")].  And despite revisions to the orchestration, in an attempt to restrain inner voices and highlight principal themes, "Macbeth" still falls short of "Don Juan" and "Tod und Verklärung" in sonic clarity."

Alessandra Marc: Alessandra Marc (born July 29, 1957) is an American dramatic soprano who has appeared at many of the world's opera houses and orchestras.  Marc is particularly known for her interpretations of the works of Richard Strauss, Richard Wagner, Giuseppe Verdi, music of the Second Viennese School, and the title role in Puccini's "Turandot".

Marilyn Cotlow: Marilyn Cotlow (born January 10, 1924) is an American lyric coloratura soprano best remembered for originating the role of Lucy in Gian Carlo Menotti's "The Telephone".  She sang professionally during the 1940s and 1950s in the United States and Europe, performing with such companies as the Metropolitan Opera.  After retiring from the stage, Cotlow taught voice at the Peabody Conservatory and currently teaches privately out of her home.  Several of her students have gone on to have successful careers, including Alessandra Marc and Jennifer Wilson.

Der Krämerspiegel: Der Krämerspiegel ("The Shopkeeper's Mirror"), Op. 66, is a 1918 song cycle of 12 songs written by Richard Strauss.  The songs were set to texts commissioned by Strauss in a piqued response to a contractual obligation to produce a set of songs for his publisher.  The texts were provided by Berlin literary critic Alfred Kerr, who wrote for Strauss a set of acidic verses ridiculing the music publishing business and containing in-jokes attacking some of Strauss' enemies such as Bote & Bock.  The list of titles is:

Renée Fleming: Renée Fleming (born February 14, 1959) is an American opera singer and soprano whose repertoire encompasses Richard Strauss, Mozart, Handel, bel canto, lieder, French opera and chansons, jazz and indie rock.  Fleming has a full lyric soprano voice.  She has performed coloratura, lyric, and lighter spinto soprano operatic roles in Italian, German, French, Czech, and Russian, aside from her native English.  She also speaks fluent German and French, along with limited Italian.  Her signature roles include Countess Almaviva in Mozart's "Le nozze di Figaro", Desdemona in Verdi's "Otello", Violetta in Verdi's "La traviata", the title role in Dvořák's "Rusalka", the title role in Massenet's "Manon", the title role in Massenet's "Thaïs", the title role in Richard Strauss's "Arabella", the Marschallin in "Der Rosenkavalier", and the Countess in "Capriccio".

Susanne Mentzer: Susanne Mentzer (born January 21, 1957) is an American operatic mezzo-soprano.  She is best known for singing trouser roles, such as Cherubino in Mozart's "Le nozze di Figaro", Idamante in Mozart's "Idomeneo", Octavian in Richard Strauss' "Der Rosenkavalier" and the composer in Strauss' "Ariadne auf Naxos", as well as other music of Mozart, Strauss, Rossini, Berlioz and Mahler.

Strauss: Strauss, Strauß or Straus is a common Germanic surname.  Outside Germany and Austria "Strauß" is always spelled "Strauss" (the letter "ß" is not used in the German-speaking part of Switzerland).  In classical music, "Strauss" usually refers to Richard Strauss or Johann Strauss II.

Emmanuel Chabrier: Alexis Emmanuel Chabrier (] ; January 18, 1841September 13, 1894) was a French Romantic composer and pianist.  Although known primarily for two of his orchestral works, "España" and "Joyeuse marche", he left an important corpus of operas (including "L'étoile"), songs, and piano music.  He was admired by composers as diverse as Debussy, Ravel, Richard Strauss, Satie, Schmitt, Stravinsky, and the group of composers known as Les six.  Stravinsky alluded to "España" in his ballet "Petrushka"; Gustav Mahler called "España" "the beginnings of modern music" and alluded to the "Dance Villageoise" in the "Rondo Burleske" movement of his Ninth Symphony.  Ravel wrote that the opening bars of "Le roi malgré lui" changed the course of harmony in France, Poulenc wrote a biography of the composer, and Richard Strauss conducted the first staged performance of Chabrier's incomplete opera "Briséïs".

Taillefer (Strauss): Taillefer is a cantata for choir and orchestra composed by Richard Strauss in 1903, Op. 52, TrV 207.  The text is a rendering of the medieval tale Taillefer by the German poet Ludwig Uhland (1787–1862).  The piece was written to celebrate the centenary of Heidelberg University and was premiered on the same day that Strauss received his honorary doctorate from the university, on 26 October 1903 in the newly built Heidelberg Town Hall with Strauss conducting.  It is written for a mixed chorus with three soloists, tenor (Taillefer), baritone (Duke William of Normandy), and soprano (the Duke's daughter and admirer of Taillefer), with a large orchestra.  The work was performed at the last night of The Proms in 2014.

Question: What does Alessandra Marc and Richard Strauss have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_musical_genre": {
      "type": "string",
      "description": "The musical genre both individuals are associated with."
    },
    "composer_name": {
      "type": "string",
      "description": "The name of the composer."
    },
    "performer_name": {
      "type": "string",
      "description": "The name of the performer."
    },
    "performer_connection_to_composer": {
      "type": "string",
      "description": "How the performer is connected to the composer's works."
    }
  },
  "required": [
    "common_musical_genre",
    "composer_name",
    "performer_name",
    "performer_connection_to_composer"
  ],
  "additionalProperties": false
}
