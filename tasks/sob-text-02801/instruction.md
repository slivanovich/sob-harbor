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
Oskar Aichinger: Oskar Aichinger is an Austrian avant-garde jazz pianist who has collaborated with musicians such as Stefan Németh, Franz Koglmann, Hannes Enzlberger, Steinaich Irrding, Burkhard Stangl, Oswald Eggers, Achim Tang, Franz Koglmann and Paul Skrepek Jun, among many others.

Heinrich Schnee: Heinrich Albert Schnee (Albert Hermann Heinrich Schnee; 4 February 1871 – 23 June 1949) was a German lawyer, colonial civil servant, politician, writer, and association official.  He served as the last Governor of German East Africa.

Ulrich Boner: Ulrich Boner, or Bonerius, (fl.  early 14th century), was a German-speaking Swiss writer of fable.

Neel Jani: Neel Jani (born 8 December 1983) is a Swiss professional racing driver of Indian Gujarati origin.  His father is from India and his mother is German-speaking Swiss.

Dieb13: Dieb13 is the performing name of Dieter Kovačič, a Viennese-based avant-garde musician.  He has also performed under the names Takeshi Fumimoto, Echelon, Dieter Bohlen, and dieb14.  After appearing on several compilations documenting the burgeoning Viennese avant-garde scene of the late 1990s, he released his first solo album in 2000.  He has gone on to perform in a number of collaborations with other notable performers, including Burkhard Stangl, erikm, Mats Gustafsson and the John Butcher Group.

Mikroton Recordings: Mikroton Recordings is an independent record label for free improvisation, mostly its electroacoustic direction, founded by the artist and producer Kurt Liedwart and based in Moscow, Russia.  Mikroton works with improvisers who used to be active in the field of electroacoustic improvisation like percussionist Günter Müller, laptop improviser , percussionist Jason Kahn, guitarist Keith Rowe, turntablists Dieb13 and eRikm, clarinettist Kai Fagaschinski, homemade electronics performer , guitarist Burkhard Stangl and others.  It usually published electroacoustic, electronic and mixed works, trying to research a land between electronic and acoustic fields, pairing unorthodox instruments and materials.  The label released two seminal compilation recordings for Austrian electroacoustic, experimental and improv group of artists known as klingt.org and Berlin Echtzeitmusik scene.  Mikroton Recordings also hosts concerts in Moscow and St. Petersburg and runs Teni Zvuka festival.

Burkhard Stangl: Burkhard Stangl (born 6 November 1960 in Eggenburg, Lower Austria) is a composer and musician, currently residing in Vienna, Austria.  Playing primarily guitar and electronics, he is a prolific performer in the world of electro-acoustic improvisation, having participated in over 50 recordings.  One of his most noted recordings is "schnee", a duet with Cristof Kurzmann, inspired by four films and a quote from writer Robert Walser.  It has been recorded live, as "schnee_live", and has spawned a similarly themed "meta-song suite," "neuschnee".  His 1997 opera "Der Venusmond" was recorded partially on the observation deck of the Empire State Building.

Gertrud Leutenegger: Gertrud Leutenegger (born 7 December 1948) is a German-speaking Swiss poet, novelist, playwright and theatre director.

Robert Walser (writer): Robert Walser (15 April 1878 – 25 December 1956) was a German-speaking Swiss writer.

Katharina Klement: Katharina Klement (born December 1, 1963 in Graz), is an Austrian composer and performer, currently residing in Vienna, Austria.  She studied piano, electroacoustic music and composition, with Dieter Kaufmann at Universität für Musik und darstellende Kunst in Vienna.  Her work is connecting the fields of notated and improvised, instrumental and electronic music.  Particular interest lays on the piano and its extended playing techniques.  She also does sound installations and is the founder and member of numerous ensembles for improvised music: "subshrubs" (Angélica Castelló, Maja Osojnik, Tamara Wilhelm, Katharina Klement), "Klement-Siewert" (duo with Martin Siewert), "deepseafish-K" (juun, Manon Liu Winter, Katharina Klement), "REDOX" (Annette Giesriegl, Kaja Farszky, Katharina Klement), "LEFT" (Isabelle Duthoit, Matija Schellander, Katharina Klement), "Ernst-Klement-Stangl" (Katharina Ernst, Burkhard Stangl, Katharina Klement), "t(w)o wanderers" (duo with Lynn Book).

Question: Which German-speaking Swiss writer inspired Burkhard Stangl to create the famed "schnee" duet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musical_work": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the musical work."
        },
        "type": {
          "type": "string",
          "description": "The type of the musical work, e.g., duet, opera."
        }
      },
      "required": [
        "title",
        "type"
      ],
      "additionalProperties": false
    },
    "main_artist": {
      "type": "string",
      "description": "The primary artist or composer of the work."
    },
    "collaborator": {
      "type": "string",
      "description": "The collaborating artist on the work."
    },
    "inspired_by_writer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the writer who inspired the work."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the writer."
        },
        "language": {
          "type": "string",
          "description": "The primary language of the writer's work."
        }
      },
      "required": [
        "name",
        "nationality",
        "language"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "musical_work",
    "main_artist",
    "collaborator",
    "inspired_by_writer"
  ],
  "additionalProperties": false
}
