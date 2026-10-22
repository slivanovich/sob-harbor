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
Patrick Bruel: Patrick Bruel (] ; born Patrick Benguigui ] on 14 May 1959) is a French singer, actor, and professional poker player.

Theophanis Lamboukas: Theophanis Lamboukas (26 January 1936 – 28 August 1970), better known as Theo Sarapo was a French singer and actor, and the second husband of the French singer Édith Piaf.  Formerly a hairdresser, he was 26 years old when he married the 46-year-old Piaf.  He was introduced to her by Claude Figus, Piaf's secretary.

12 chansons d'avant le déluge: 12 chansons d'avant le déluge is the second album by experimental French singer Brigitte Fontaine, and the first by French rock singer Jacques Higelin, released in 1966 on the Productions Jacques Canetti label.  It was their only real release on the label, they would go on to release a few more singles that would be collected on the "15 chansons d'avant le déluge, suite et fin" album in 1976, before moving to the Saravah label.

Michel Fugain: Michel Fugain (born 12 May 1942 in Grenoble, Isère) is a French singer and composer.  Originally he released music along with his singers and dancers entitled "Le Big Bazar" but went for a more solo approach 1977.  In 1967, he released his first album: "Je n'aurai pas le temps" (French: "I won't have time").  The title track was later covered in English by John Rowles and was entitled ""If I only had time"".

Le Jaguar: Le Jaguar is a 1996 French film directed by Francis Veber starring Jean Reno, Patrick Bruel, Harrison Lowe, and Patricia Velásquez.  A shaman from the South American rain forest visits Paris for a public relations campaign along with a French ethnologist.  When the shaman's soul is apparently stolen, he enlists the help of a good-for-nothing named Perrin, with whom he spontaneously created a spiritual link.

Rue Saint Louis en l'Île: Rue Saint Louis en l'Île is the fifteenth album by experimental French singer Brigitte Fontaine, released in 2004 on the Virgin Records label.  It features a new version of "Le Nougat" from her "French corazon" album with Mustapha and Hakim Amokrane of French band Zebda, as well as a duet with Areski Belkacem, "Le Voile à l'école".  There's also a cover of Édith Piaf, "L'Homme à la moto", which was present before on an hommage album to the singer, in the words of Fontaine, "just to show off".

(Là) Où je pars: (Là) où je pars is the first solo album recorded by French singer Emmanuel Moire.  It was first released on 13 November 2006, then on 21 May 2007 in its second version.  Four tracks from the album were released as singles - "Le Sourire", "Ça me fait du bien", "Là où je pars" and "Si c'était ça la vie", but they were only available digitally and on airplay (except "Le Sourire", which was released as CD single and peak at number seven in France).  The album achieved some success : it debuted at a peak of number eight on the French albums chart and totaled 70 weeks in the top 200.  In Belgium (Wallonia), it started at number 71 on 25 November 2006 and reached number 34 seven weeks later, and fell off the top 100 after 18 weeks.  The album passed almost unnoticed in Switzerland where it was ranked low for a sole week.

Marcher dans le sable: Marcher dans le sable is a 2000 album recorded by French singer Gérald De Palmas.  It was his third studio album, and his most successful in terms of sales.  It reached number two in France and in Belgium (Wallonia) and remained for almost two years on the chart.  The album was awarded 'French album of the year' at the 2002 NRJ Music Awards and allowed De Palmas to win a Victoire de la Musique, the same year, in the category 'Male group or artist of the year'.  It provided three singles : "J'en rêve encore" was the most successful (#7 in France, #4 in Belgium Wallonia), followed by the two moderate hits "Une seule vie (marcher dans le sable)" and "Tomber" (respectively #30 and #35 in France).

Le Cœur d'un homme: Le Cœur d'un homme is an album by the French singer Johnny Hallyday.  It was released on November 12, 2007, and achieved huge success in France and Belgium (Wallonia).  It was led by the single "Always", a number 2 hit in France, and contains a cover version of Francis Cabrel's 1989 single "Sarbacane".  French actor Bruno Putzulu wrote one song of the album.  The final track of the album, "I Am the Blues", co-written by U2's lead singer Bono, is a rare example of a Hallyday song in English.

Sofia Mestari: Sofia Mestari (born 1980) is a French singer of Moroccan origin, at the age of ten she moved to Paris with her family.  Mestari represented France in the Eurovision Song Contest 2000 in Stockholm with the song On aura le ciel, which placed 23rd out of 24 with 5 points.  She released an album of the same name, with two singles, "On aura le ciel" and "Derrière les voiles", and 2003 saw the release of a new album "En plein coeur de la nuit" and featured the single "Ne pars pas".  "Ne pars pas" spent 23 weeks on the French Singles Chart and peaked at 27.  Sofia's third album, entitled "La vie en entier" was released on 16 June 2008.

Question: Le Jaguar is a 1996 film starring a French singer, actor, and professional what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor in question."
    },
    "actor_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions of the actor."
    },
    "missing_profession": {
      "type": "string",
      "description": "The specific profession requested in the question."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "actor_name",
    "actor_professions",
    "missing_profession"
  ],
  "additionalProperties": false
}
