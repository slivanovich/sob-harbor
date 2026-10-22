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
The Killer (play): The Killer (French: Tueur sans gages , sometimes translated "The Killer without Reason" or "The Killer without Cause") is a play written by Eugène Ionesco in 1958.  It is the first of Ionesco's Berenger plays, the others being "Rhinocéros" (1959), "Exit the King" (1962), and "A Stroll in the Air" (1963).

Jacques Prévert: Jacques Prévert (] ; 4 February 190011 April 1977) was a French poet and screenwriter.  His poems became and remain popular in the French-speaking world, particularly in schools.  His best-regarded films formed part of the poetic realist movement, and include "Les Enfants du Paradis" (1945).

The Lesson: The Lesson (French: "La Leçon" ) is a one-act play by French-Romanian playwright Eugène Ionesco.  It was first performed in 1951 in a production directed by Marcel Cuvelier (who also played the Professor).  Since 1957 it has been in permanent showing at Paris' Théâtre de la Huchette, on an Ionesco double-bill with The Bald Soprano.  The play is regarded as an important work in the "Theatre of the Absurd".

Exit the King: Exit the King (French: Le Roi se meurt ) is an absurdist drama by Eugène Ionesco that premiered in 1962.  It is the third in Ionesco's "Berenger Cycle", preceded by "The Killer" (1958) and "Rhinocéros" (1959), and followed by "A Stroll in the Air" (1963).

The King and the Mockingbird: The King and the Mockingbird (French: Le Roi et l'oiseau , literally "The King and the Bird") is a 1980 traditionally animated feature film directed by Paul Grimault.  Begun in 1948 as "The Shepherdess and the Chimney Sweep" (loosely based on the fairy tale of the same name by Hans Christian Andersen), the film was a collaboration between Grimault and popular French poet and screenwriter, Jacques Prévert.  However the film suddenly stopped production and was released unfinished by its producer, without the approval of either Grimault or Prévert.  Through the course of the 1960s and 1970s, Grimault obtained the rights to the film and was able to complete a new version as they originally intended.  It was finished over 30 years after it was started.

The New Tenant: The New Tenant (French: "Le Nouveau Locataire" ) is a play written by Eugène Ionesco in 1955.  The central image is common to many Ionesco plays: something accumulates on stage and overwhelms the characters.  In this case its furniture.  The main characters are a gentleman, a caretaker, and two movers.  The caretaker talks as the gentleman, the "new tenant" of the title, directs the two movers who continuously bring in furniture.

Ylipe: Philippe Labarthe, pseudonym Ylipe (9 January 1936 – 8 March 2003) was a French humorist, artist, and writer.  He was born in Bordeaux and studied Fine Arts there before moving to Paris to work as a cartoonist, painter and aphorist.  He signed his cartoons "φlipe", using the Greek letter phi (φ) in place of the first three letters of his forename.  Maurice Nadeau misread the Greek φ as a Latin y and the name "Ylipe" stuck.  In the 1960s he contributed to "Arts", "L'Express", and "Lettres nouvelles", and signed the Manifesto of the 121 opposing the use of torture during the Algerian War.  He later exhibited paintings in New York and Paris under his own name, with backing from Eugène Ionesco and Jacques Prévert.  In 2000, a back injury prevented him painting and he returned to writing aphorisms.  His writing and painting often exhibit black humour; Dominique Noguez described him as a "sparkling misanthrope" (French: "misanthrope étincelant" ).  He died of lung cancer, having refused medical treatment.

Eugène Ionesco: Eugène Ionesco (born Eugen Ionescu, ] ; 26 November 1909 – 28 March 1994) was a Romanian-French playwright who wrote mostly in French, and one of the foremost figures of the French Avant-garde theatre.  Beyond ridiculing the most banal situations, Ionesco's plays depict the solitude and insignificance of human existence in a tangible way.

Donald Allen: Donald Merriam Allen (Iowa, 1912 – San Francisco, August 29, 2004) was an influential editor, publisher, and translator of contemporary American literature.  He is perhaps best known for his project "The New American Poetry 1945-1960" (1960), among the several important anthologies of contemporary American innovative writing he made available to the public.  Allen began his working life as a Japanese translator within the US military, serving in WWII.  After his military service, Allen became an editor at Grove Press, where he worked for sixteen years.  He was one of the first translators of the Romanian-French Absurdist playwright Eugène Ionesco, and Allen's 1958 volume "Four Plays of Eugène Ionesco" helped to introduce the playwright to American audiences in the 1960s.

Victims of Duty: Victims of Duty (French: Victimes du Devoir ) is a one-act play written in 1953 by French-Romanian playwright Eugène Ionesco.  An early work, it has not received the notoriety of his other works.  The play is in the Theatre of the Absurd style, of which Ionesco was a pioneer.

Question: Which writer was born first, Jacques Prévert or Eugène Ionesco?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "writer_comparison": {
      "type": "object",
      "properties": {
        "first_writer": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "birth_year": {
              "type": "integer"
            }
          },
          "required": [
            "name",
            "birth_year"
          ],
          "additionalProperties": false
        },
        "second_writer": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "birth_year": {
              "type": "integer"
            }
          },
          "required": [
            "name",
            "birth_year"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "first_writer",
        "second_writer"
      ],
      "additionalProperties": false
    },
    "earliest_birth_year": {
      "type": "integer"
    },
    "writer_born_first_name": {
      "type": "string"
    }
  },
  "required": [
    "writer_comparison",
    "earliest_birth_year",
    "writer_born_first_name"
  ],
  "additionalProperties": false
}
