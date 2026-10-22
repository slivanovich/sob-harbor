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
A Survivor from Warsaw: A Survivor from Warsaw, Op. 46, is a cantata by the Los Angeles-based Austrian composer Arnold Schoenberg, written in tribute to Holocaust victims.  The main narration is unsung; “never should there be a pitch” to its solo vocal line, wrote the composer.

Arnold Schoenberg: Arnold Franz Walter Schoenberg or Schönberg ( ; ] ; 13 September 187413 July 1951) was an Austrian composer, music theorist, and painter.  He was associated with the expressionist movement in German poetry and art, and leader of the Second Viennese School.  With the rise of the Nazi Party, Schoenberg's works were labelled degenerate music, because they were modernist, atonal and what even Paul Hindemith called "sonic orgies" and "decadent intellectual efforts".  He emigrated to the United States of America in 1934.

Samuel Friedman Foundation: The Samuel Friedman Foundation was established in 1956 by Samuel Friedman, in Buffalo, New York.  A later branch of the foundation was set up in Los Angeles at UCLA.  Friedman, who was born in Romania on January 1, 1919, was a survivor of concentration camps at both Dachau and Auschwitz, and was eventually liberated by United States forces.  After some time as a displaced person, he emigrated to the United States, eventually owned several restaurants in Niagara Falls, and became known as a successful New York businessman.  In 1956, he established the Samuel Friedman Foundation to support and strengthen Jewish educational initiatives and programs.  These projects have involved the local community in Buffalo, New York, and have continued after Samuel Friedman's death from a cardiac arrest.  The foundation maintains his original intention through the establishment of projects such as The Samuel Friedman Library in the Institute for Jewish Thought and Heritage at the University of Buffalo.  It also contributed significantly to the establishment of the Hineni Endowment Campaign at the Kadimah School in Buffalo.  The Samuel Friedman Foundation was termed a "medium"-sized grant giver in a report entitled "Profile of Foundation Giving in Western New York" prepared for the Western New York Grantmakers Association by the University at Buffalo Regional Institute.  It remains a non-profit organization, noted for its contributions to the general Buffalo community, and for its Rescue Award, given annually.

Blandine Ebinger: Blandine Ebinger (born Blandine Loeser) (4 November 1899, in Berlin – 25 December 1993, in Berlin) was a German actress and "chansonniere", the daughter of the pianist Gustav Loeser and the actress Margarete Wezel.  Ebinger became acquainted with Friedrich Hollaender in 1919, and with him she became heavily invested as a performer, writer, and composer in the Berlin cabaret scene in the 1920s, beginning in the cabaret and the .  She married Friedrich Hollaender, and she recorded many of his cabaret songs, including the set of songs entitled "Lieder eines armen Mädchens ".  Although Ebinger and Hollaender ended their marriage before Hollaender emigrated to the United States because of the increasingly hostile environment for Jewish citizens in the early 1930s, Ebinger nevertheless faced discrimination as a result of the marriage, much of which was directed at their half-Jewish daughter, Philine, who was briefly married to Georg Kreisler.  Ebinger emigrated to the United States in 1937, returning to Berlin in 1947.  She moved to Munich, where she met her second husband, the publisher Helwig Hassepflug, in 1961.  They eventually settled back in Berlin, where Blandine continued her career in the theater and as an actress on television productions.  Ebinger died on 25 December 1993 in Berlin and is buried on the Waldfriedhof Dahlem.  She was 94 years old.

Alexander Donat: Alexander Donat also Aleksander Donat in Polish (1905 – 16 June 1983); a chemist by training, and journalist by profession; was a Holocaust survivor imprisoned at the Warsaw Ghetto during the occupation of Poland by Nazi Germany in World War II.  He became an inmate of several Nazi forced labor and concentration camps and an eye witness to the Holocaust in Poland.  After the war, Donat emigrated with his family to the United States, settling in New York City, and went on to write about his wartime experiences.  He wrote "Jewish Resistance" (1964), "Holocaust Kingdom" (1965), and "The Death Camp Treblinka: a documentary" (1979), a series of memoirs devoted to these traumatic events.

Antoni Koper: Antoni Stefan Koper (September 6, 1906 – June 13, 1990) was active in the Polish resistance movement during World War II and served as a lieutenant in the Polish Home Army.  He helped rescue Jews from the Warsaw Ghetto and fought in the Warsaw Uprising.  After escaping from a Nazi prison camp, he first fled to London, and then emigrated to the United States.  There, he worked for the Defense Language Institute, United States Information Agency, and the Voice of America.  He died of cancer in 1990.

Jona Goldrich: Jona Goldrich (born Jona Goldreich; September 11, 1927 – June 26, 2016) was an American real estate developer and philanthropist.  Born in Lviv, in the late 1920s, he emigrated to Israel in the midst of World War II, where he served in the 1948 Arab–Israeli War and worked for a labor union.  By the 1950s, he emigrated to the United States, and he became a real estate developer and investor in Los Angeles County.  A Holocaust survivor, he supported Jewish causes in Israel and the United States.

Tibor Rubin: Tibor "Ted" Rubin (June 18, 1929 – December 5, 2015) was a Hungarian-born Holocaust survivor who emigrated to the United States in 1948 and received the Medal of Honor for his actions during the Korean War as a United States Army soldier and prisoner of war (POW) from President George W. Bush on September 23, 2005, 55 years later.  Rubin was repeatedly nominated for various military decorations, but was overlooked because of antisemitism by a superior.  Fellow soldiers who filed affidavits supporting Rubin's nomination for the Medal of Honor said that Rubin's sergeant "was an anti-Semite who gave Rubin dangerous assignments in hopes of getting him killed".  In November, 2016, President Obama signed legislation renaming the Long Beach California VA Medical Center after Rubin.

Lubomir Tomaszewski: Lubomir Tomaszewski is a Polish-American artist, born in 1923 in Warsaw, Poland In 1966 he emigrated to New York City in the United States.  He creates sculptures, fire, paintings and porcelain design.  He is an alumnus of the Warsaw Academy of Fine Arts.  Student of the Warsaw University of Technology.  He founded an international artistic movement of The Emotionalists, a group established in 1994.

Leibush Lehrer: Leibush L. Lehrer (1887 Warsaw - 1964 New York) was a leading Yiddish pedagogue, writer, philosopher and lyricist.  He authored several books on education, psychology, and literature.  Born in Warsaw, he emigrated to the United States in 1909.  From 1919 until his death, he lectured at the Jewish Teachers Seminary.  Lehrer was also involved with the research efforts of YIVO as the Secretary for the Section on Psychology and Education.  He was a proponent of the position that Judaism was an entire folk culture, not merely a religion.

Question: The composer of A Survivor from Warsaw emigrated to the United States in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_name": {
      "type": "string",
      "description": "The name of the composer."
    },
    "composition_title": {
      "type": "string",
      "description": "The title of the musical composition."
    },
    "emigration_details": {
      "type": "object",
      "properties": {
        "destination_country": {
          "type": "string",
          "description": "The country to which the composer emigrated."
        },
        "emigration_year": {
          "type": "integer",
          "description": "The year the composer emigrated."
        }
      },
      "required": [
        "destination_country",
        "emigration_year"
      ],
      "additionalProperties": false
    },
    "reason_for_emigration_mentioned": {
      "type": "boolean",
      "description": "Indicates if a reason for emigration is mentioned in the text."
    }
  },
  "required": [
    "composer_name",
    "composition_title",
    "emigration_details",
    "reason_for_emigration_mentioned"
  ],
  "additionalProperties": false
}
