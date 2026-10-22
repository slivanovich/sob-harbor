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
Anna Kaufmann: Anna Kaufmann was a German operatic soprano who was a principal artist at the Bavarian State Opera in Munich from 1869 to 1872.  Just prior to her appointment, the great soprano Mathilde Mallinger had left the Bavarian State Opera and Kaufmann succeeded her in the roles of Elsa in Richard Wagner's "Lohengrin", Elisabeth in Wagner's "Tannhäuser", and Eva in Wagner's "Die Meistersinger von Nürnberg" among other parts.  She notably created the roles of Woglinde in Wagner's "Das Rheingold" on September 22, 1869 and Fricka in Wagner's "Die Walküre" on June 26, 1869.  Currently, no further biographical details about Kaufmann's life both before and after her time at the Bavarian State Opera have surfaced.

Otto Edelmann: Otto Edelmann (February 5, 1917 in Vienna – May 14, 2003 in Vienna) was an Austrian bass.  He was born in Vienna and studied singing in Vienna with Gunnar Graarud.  His debut was at Gera as Figaro in Mozart's "The Marriage of Figaro".  He later sang the Vienna State Opera, the Edinburgh Festival and the Metropolitan Opera.  He sang at the Bayreuth Festival immediately after its reopening in 1951 after World War II, performing the role of Hans Sachs in Wagner's "Die Meistersinger von Nürnberg".  (He also recorded as Veit Pogner the goldsmith in the same work in one of Hans Knappertsbusch's early recorded performances.)  He also sang Ochs in Richard Strauss's "Der Rosenkavalier" at the first performances in the new Salzburg Festspielhaus in 1960.  In 1957, he recorded the role of Wotan opposite Kirsten Flagstad in Georg Solti's recording of Act III of Wagner's "Die Walküre" (an album made prior to the later famous complete set of "Der Ring des Nibelungen").  He died in Vienna.

Die Walküre: Die Walküre (The Valkyrie), WWV 86B, is a music drama in three acts by Richard Wagner with a German libretto by the composer.  It is the second of the four works that form Wagner's cycle "Der Ring des Nibelungen" ("The Ring of the Nibelung").

Hannelore Bode: Hannelore Bode (born 2 August 1941) is a German operatic soprano.  She performed at the Bayreuth Festival from 1968 to 1978, including Elsa in "Lohengrin", Eva in "Die Meistersinger von Nürnberg", and several parts in the 1976 Jahrhundertring, including Sieglinde in "Die Walküre".  She performed internationally and recorded operas with conductors such as Eugen Jochum, Silvio Varviso and Pierre Boulez.

Kaspar Bausewein: Kaspar Bausewein (15 November 1838, Aub – 18 November 1903, Munich) was a German operatic bass who was active at the Bavarian State Opera from 1858 through 1900.  While there, he notably portrayed several characters in the world premieres of operas composed by Richard Wagner.  He created Pogner in "Die Meistersinger von Nürnberg" (June 21, 1868), Fafner in "Das Rheingold" (September 22, 1869), Hunding in "Die Walküre" (June 26, 1870), and Harald in "Die Feen" (June 29, 1888).

Loretta Di Franco: Loretta Di Franco is an American operatic soprano who is chiefly known for her more than 900 performances at the Metropolitan Opera from 1961-1995.  Originally a member of the Met's opera chorus, she eventually was promoted to singing small comprimario roles beginning with one of the pages in Wagner's "Tannhäuser" and the peasant girl in "The Marriage of Figaro" in 1961.  She went on to win the Metropolitan Opera National Council Auditions in 1965 which led to her first substantial role, Chloe in "The Queen of Spades".  She continued to appear annually at the Met for the next 30 years, performing both leading and supporting roles.  Some of the parts she performed at the Met included Annina in "La traviata", both the Aunt and Barena in Janáček's "Jenůfa", Barbarina and Marcellina in "The Marriage of Figaro", Berta in "The Barber of Seville", Countess Ceprano in "Rigoletto", the Dew Fairy and the Sandman in "Hansel and Gretel", Feklusa in "Káťa Kabanová", the First Lady in "The Magic Flute", the Flower Seller in Britten's "Death in Venice", Frasquita in "Carmen", Gerhilde in "Die Walküre", Giannetta in "L'elisir d'amore", Helen in "Mourning Becomes Electra", Ines in "Il trovatore", Jouvenot in "Adriana Lecouvreur", Kate Pinkerton in "Madama Butterfly", Laura in "Luisa Miller", Lauretta in "Gianni Schichi", Lisa in "La sonnambula", Marianne in "Der Rosenkavalier", Marthe in "Faust", Musetta in "La bohème", Oscar in "Un ballo in maschera", Samaritana in "Francesca da Rimini", Woglinde in both "Das Rheingold" and "Götterdämmerung", Xenia in "Boris Godunov", Zerlina in "Don Giovanni", and title role in "Lucia di Lammermoor".  In 1991 she created the role of the Woman with Child in the world premiere of John Corigliano's "The Ghosts of Versailles".

Intermezzo (opera): Intermezzo, Op.  72, is an opera in two acts by Richard Strauss to his own German libretto, described as a "Bürgerliche Komödie mit sinfonischen Zwischenspielen " (bourgeois comedy with symphonic interludes).  It premiered at the Dresden Semperoper on 4 November 1924, with sets that reproduced Strauss' home in Garmisch.  The first Vienna performance was in January 1927.

Karin Branzell: Karin Branzell (24 September 189115 December 1974) was a Swedish operatic contralto (sometimes described as a mezzo-soprano), who had a prominent career at the Metropolitan Opera, New York, and in Europe.  Her very wide range enabled her to sing both contralto roles and the occasional soprano role.  She was particularly noted for her singing of the music of Richard Wagner, in roles such as Ortrud ("Lohengrin"), Venus ("Tannhäuser"), Erda ("Das Rheingold" and "Siegfried"), Brangäne ("Tristan und Isolde"), and Brunnhilde ("Die Walküre").  She was considered on a par with Margarete Klose and Kerstin Thorborg as a Wagnerian contralto.  Amneris ("Aida"), Dalila ("Samson et Dalila"), Herodias ("Salome"), and Clytemnestra ("Elektra") were among her other renowned roles.

Thomas Thomaschke: Thomas Thomaschke (born 2 August 1943) is a German bass singer in opera and concert.  He has appeared in parts such as Hunding in Wagner's "Die Walküre" and Sarastro in Mozart's "Die Zauberflöte" in major opera houses in Europe and international festivals.  He has also performed and recorded oratorios and cantatas.

Herta Glaz: Herta Glaz (also spelled Hertha; September 16, 1910 in Vienna – January 28, 2006 in Hamden, Connecticut) was an American operatic mezzo-soprano, voice teacher, and opera director of Austrian birth.  She became a United States citizen in 1943.  She was a fixture at the Metropolitan Opera between 1942-1956 where she sang in more than 300 performances.  She was also highly active with the San Francisco Opera between 1944-1951.  Some of the roles she portrayed on stage were Marcellina in "Le Nozze di Figaro", Annina, Siegrune in "Die Walküre", Flosshilde in "Götterdämmerung" and Magdalene in "Die Meistersinger von Nürnberg".

Question: Which of these has the most acts, Die Walküre or Intermezzo?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "opera_with_most_acts": {
      "type": "string",
      "description": "The name of the opera that has the most acts."
    },
    "number_of_acts_most": {
      "type": "integer",
      "description": "The number of acts for the opera with the most acts."
    },
    "compared_operas": {
      "type": "array",
      "description": "Details for each opera included in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "opera_name": {
            "type": "string",
            "description": "The name of the opera."
          },
          "number_of_acts": {
            "type": "integer",
            "description": "The number of acts in this opera."
          }
        },
        "required": [
          "opera_name",
          "number_of_acts"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "opera_with_most_acts",
    "number_of_acts_most",
    "compared_operas"
  ],
  "additionalProperties": false
}
