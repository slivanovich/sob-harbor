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
Otello: Otello (] ) is an opera in four acts by Giuseppe Verdi to an Italian libretto by Arrigo Boito, based on Shakespeare's play "Othello".  It was Verdi's penultimate opera, and was first performed at the Teatro alla Scala, Milan, on 5 February 1887.

Die Walküre: Die Walküre (The Valkyrie), WWV 86B, is a music drama in three acts by Richard Wagner with a German libretto by the composer.  It is the second of the four works that form Wagner's cycle "Der Ring des Nibelungen" ("The Ring of the Nibelung").

Richard Wagner: Wilhelm Richard Wagner ( ; ] ; 22 May 181313 February 1883) was a German composer, theatre director, polemicist, and conductor who is primarily known for his operas (or, as some of his later works were later known, "music dramas").  Unlike most opera composers, Wagner wrote both the libretto and the music for each of his stage works.  Initially establishing his reputation as a composer of works in the romantic vein of Weber and Meyerbeer, Wagner revolutionised opera through his concept of the "Gesamtkunstwerk" ("total work of art"), by which he sought to synthesise the poetic, visual, musical and dramatic arts, with music subsidiary to drama.  He described this vision in a series of essays published between 1849 and 1852.  Wagner realised these ideas most fully in the first half of the four-opera cycle "Der Ring des Nibelungen" ("The Ring of the Nibelung").

Der Ring des Nibelungen: Der Ring des Nibelungen (The Ring of the Nibelung), WWV 86, is a cycle of four German-language epic music dramas composed by Richard Wagner.  The works are based loosely on characters from the Norse sagas and the "Nibelungenlied".  The composer termed the cycle a "Bühnenfestspiel" (stage festival play), structured in three days preceded by a " " ("preliminary evening").  It is often referred to as the Ring Cycle, "Wagner's Ring", or simply "The Ring".

Ring (video game): Ring: The Legend of the Nibelungen is a 1999 point-and-click adventure video game for Microsoft Windows developed by Arxel Tribe and published in North America by Red Orb Entertainment and in Europe by Cryo Interactive.  The game is based on Richard Wagner's four opera cycle "Der Ring des Nibelungen", and features music from various performances of the Vienna Philharmonic Orchestra conducted by Georg Solti from 1958 to 1964, chosen in collaboration with PolyGram and Decca.  French comic-book artist Philippe Druillet also worked on the game, providing much of the artwork.

What's Opera, Doc?: What's Opera, Doc?  is a 1957 American animated cartoon comedy-drama musical short in the "Merrie Melodies" series, directed by Chuck Jones for Warner Bros.  Cartoons.  The Michael Maltese story features Elmer Fudd chasing Bugs Bunny through a parody of 19th-century classical composer Richard Wagner's operas, particularly "Der Ring des Nibelungen" ("The Ring of the Nibelung"), "Der Fliegende Holländer", and "Tannhäuser".  It borrows heavily from the second opera in the "Ring Cycle" "Die Walküre", woven around the standard Bugs-Elmer conflict.

Lance Ryan: Lance Ryan (born 1 May 1971) is a Canadian operatic tenor, who has worked from Germany since 2005.  He is known for singing Siegfried in Wagner's "Der Ring des Nibelungen", which he performed at opera houses in Europe including the Bayreuth Festival.  He performed the tile roles of Verdi's "Otello" and Britten's "Peter Grimes".

Götterdämmerung: Götterdämmerung ( ; Twilight of the Gods), WWV 86D, is the last in Richard Wagner's cycle of four music dramas titled "Der Ring des Nibelungen " ("The Ring of the Nibelung", or "The Ring" for short).  It received its premiere at the Bayreuth Festspielhaus on 17 August 1876, as part of the first complete performance of the "Ring".

Rhinemaidens: The Rhinemaidens are the three water-nymphs ("Rheintöchter" or "Rhine daughters") who appear in Richard Wagner's opera cycle "Der Ring des Nibelungen".  Their individual names are Woglinde, Wellgunde and Flosshilde (Floßhilde), although they are generally treated as a single entity and they act together accordingly.  Of the 34 characters in the "Ring" cycle, they are the only ones who did not originate in the Old Norse "Eddas".  Wagner created his Rhinemaidens from other legends and myths, most notably the "Nibelungenlied" which contains stories involving water-sprites (nixies) or mermaids.  The key concepts associated with the Rhinemaidens in the "Ring" operas—their flawed guardianship of the Rhine gold, and the condition (the renunciation of love) through which the gold could be stolen from them and then transformed into a means of obtaining world power—are wholly Wagner's own invention, and are the elements that initiate and propel the entire drama.

Siegfried (opera): Siegfried, WWV 86C, is the third of the four music dramas that constitute "Der Ring des Nibelungen" ("The Ring of the Nibelung"), by Richard Wagner.  It premiered at the Bayreuth Festspielhaus on 16 August 1876, as part of the first complete performance of "The Ring" cycle.

Question: Are the libretto of Otello and Der Ring des Nibelungen in the same language?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "boolean",
      "description": "True if the librettos are in the same language, false otherwise."
    },
    "operas_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the opera."
          },
          "libretto_language": {
            "type": "string",
            "description": "The language of the opera's libretto."
          }
        },
        "required": [
          "title",
          "libretto_language"
        ],
        "additionalProperties": false
      },
      "description": "Details for each opera being compared."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the comparison result."
    }
  },
  "required": [
    "comparison_result",
    "operas_compared",
    "reasoning"
  ],
  "additionalProperties": false
}
