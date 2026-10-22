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
Andrea Chénier: Andrea Chénier is a verismo opera in four acts by the composer Umberto Giordano, set to an Italian libretto by Luigi Illica.  It was first performed on 28 March 1896 at La Scala, Milan.  The opera's story is based loosely on the life of the French poet André Chénier (1762–1794), who was executed during the French Revolution.  The character Carlo Gérard is partly based on Jean-Lambert Tallien, a leading figure in the Revolution.

Andrea Chénier discography: This is a list of recordings of Andrea Chénier, an opera by the composer Umberto Giordano, which was first performed at the Teatro alla Scala, Milan, on 28 March 1896.

Mario Lanza: Opera Arias and Duets: Mario Lanza: Opera Arias and Duets is a compact disc from RCA Victor released October 8, 2001 of recordings re-mastered in 1999. (ASIN B00000JMH3).  At the time of its release was the only all-operatic Mario Lanza CD collection that RCA has issued.  It includes several previously unreleased versions of a number of operatic arias associated with Lanza, together with the duet "Dio ti giocondi" from "Otello" with soprano Licia Albanese, the Improvviso ("Un di all'azzurro spazio") from "Andrea Chénier", and "M'appari" from "Martha".  The CD also includes four recordings from "The Mario Lanza Radio Show."  Writing in "Records and Recordings" in October 1967, the critic Delcie C. Howard described Lanza's recording of the Improvviso featured here as "a well-nigh model account of this impassioned outpouring."

Prince Igor (song): "Prince Igor" is a song inspired by the Polovtsian Dances of Borodin's opera "Prince Igor".  The main vocals are performed by Warren G, the Russian refrain by Sissel Kyrkjebø and the instrumental background is provided by The Rapsody.  Warren G uses the same rap lyrics as in his song "Reality", available on the album "Take a Look Over Your Shoulder".

André Chénier: André Marie Chénier (30 October 176225 July 1794) was a French poet of Greek and Franco-Levantine origin, associated with the events of the French Revolution of which he was a victim.  His sensual, emotive poetry marks him as one of the precursors of the Romantic movement.  His career was brought to an abrupt end when he was guillotined for supposed "crimes against the state", near the end of the Reign of Terror.  Chénier's life has been the subject of Umberto Giordano's opera "Andrea Chénier" and other works of art.

Valentina Bartolomasi: Valentina Bartolomasi (1889-1932) was an Italian soprano who had a major opera career from 1910 through 1927.  Particularly successful in the dramatic soprano repertoire, she was Italy's leading Wagnerian soprano of her day.  She notably appears on the first complete recordings made of Umberto Giordano's "Andrea Chénier" (as Maddalena de Coigny), Giacomo Puccini's "Tosca" (in the title role), and Giuseppe Verdi's "Aida" (in the title role).

Andrea Chénier (film): Andrea Chénier, also spelled "Andrea Chenier", is a 1955 Italian musical melodrama film directed by Clemente Fracassi.

Prince Igor: Prince Igor (Russian: Князь Игорь , "Knyaz' Igor'") is an opera in four acts with a prologue, written and composed by Alexander Borodin.  The composer adapted the libretto from the Ancient Russian epic "The Lay of Igor's Host", which recounts the campaign of Rus' prince Igor Svyatoslavich against the invading Cuman ("Polovtsian") tribes in 1185.  He also incorporated material drawn from two medieval Kievan chronicles.  The opera was left unfinished upon the composer's death in 1887 and was edited and completed by Nikolai Rimsky-Korsakov and Alexander Glazunov.  It was first performed in St. Petersburg, Russia, in 1890.

Giuseppe Borgatti: Giuseppe Borgatti (Cento, March 17, 1871 – Reno di Leggiuno, October 18, 1950) was an Italian dramatic tenor with an outstanding voice.  (See Michael Scott, cited below, for a laudatory appraisal of his singing.)  The creator of the title role in Umberto Giordano's verismo opera "Andrea Chénier", he subsequently earned renown for his performances of the music of Richard Wagner, becoming in 1904 the first Italian tenor to appear at the Bayreuth Festival.  He sang a variety of leading roles at La Scala, Milan, from 1896 until 1914, but deteriorating eyesight caused by glaucoma put a premature end to his stage career, after which he turned successfully to teaching.

Mark Delavan: Mark Delavan is an American operatic bass-baritone.  He made his professional debut in 1986 at the San Francisco Opera in a small role in Giuseppe Verdi's "Don Carlos".  He spent the next three years performing in numerous comprimario roles with the company.  He has since returned to that opera house to sing Scarpia in Giacomo Puccini's "Tosca" (2004, with Carol Vaness in the title role) and Wotan in Richard Wagner's "The Ring Cycle" (2008, 2010, and 2011).  In 2001 he made his debut at the Metropolitan Opera as Amonasro in Verdi's "Aida" with Deborah Voigt in the title role, Luciano Pavarotti as Radamès, Olga Borodina as Amneris, and James Levine conducting.  He has since been heard at the Met as Alfio in Pietro Mascagni's "Cavalleria rusticana", Carlo Gérard in "Andrea Chénier", Count Tomsky in "The Queen of Spades", Don Carlo in Verdi's "La Forza del Destino", the Messenger in Richard Strauss' "Die Frau ohne Schatten", Scarpia, and the title roles in Verdi's "Nabucco", Verdi's "Rigoletto", and Verdi's "Simon Boccanegra".

Question: Which opera was performed first, Andrea Chénier or Prince Igor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "opera_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "first_performance_date": {
            "type": "string"
          },
          "first_performance_year": {
            "type": "integer"
          },
          "first_performance_location": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "first_performance_date",
          "first_performance_year",
          "first_performance_location"
        ],
        "additionalProperties": false
      }
    },
    "earlier_performed_opera_title": {
      "type": "string"
    },
    "earlier_performance_year": {
      "type": "integer"
    },
    "later_performed_opera_title": {
      "type": "string"
    },
    "later_performance_year": {
      "type": "integer"
    },
    "comparison_summary": {
      "type": "string"
    }
  },
  "required": [
    "opera_details",
    "earlier_performed_opera_title",
    "earlier_performance_year",
    "later_performed_opera_title",
    "later_performance_year",
    "comparison_summary"
  ],
  "additionalProperties": false
}
