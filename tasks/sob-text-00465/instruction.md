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
Robert Walser (writer): Robert Walser (15 April 1878 – 25 December 1956) was a German-speaking Swiss writer.

North Schleswig Germans: Approximately 15,000 persons in Denmark belong to an autochthonous ethnic German minority traditionally referred to as "hjemmetyskere" meaning "domestic Germans" in Danish, and as "Nordschleswiger" in German.  This minority of Germans hold Danish citizenship and self-identify as ethnic Germans.  They generally speak German or Low German alongside South Jutlandic dialect of Danish as their home languages. Furthermore, there are also several thousand German immigrants residing in Denmark with no historical connection to this group.

Damion Searls: Damion Searls is an American writer and translator.  He grew up in New York and studied at Harvard University and the University of California, Berkeley.  He specializes in translating literary works from Western European languages such as German, Norwegian, French, and Dutch.  Among the authors he has translated are Marcel Proust, Rainer Maria Rilke, Robert Walser, Ingeborg Bachmann, Thomas Bernhard, Kurt Schwitters, Peter Handke, Jon Fosse, and Nescio.  He has received numerous grants and fellowships for his translations.

Namibian Black German: Namibian Black German, also NBG, (German: "Küchendeutsch" , "kitchen German") is a pidgin language of Namibia that derives from standard German.  It is nearly extinct.  It was spoken mostly by Namibians who did not learn standard German during the period of German rule.  It was never a first language.  It is currently spoken as a second language by people over 50 years old, who these days usually also speak German, Afrikaans, or English.

Operation Corona: Operation "Corona" was a Royal Air Force (RAF) initiative to confuse German nightfighters during RAF bomber raids on German cities during World War II.  Both native speakers and people who could speak German to a standard where they could be taken for a native speaker impersonated German Air Defence officers.  They initiated communications via radio with German nightfighter pilots and countermanded previously given orders, thus reducing the efficiency of German air defence.

Nosferatu the Vampyre: Nosferatu the Vampyre is a 1979 West German art house vampire horror film written and directed by Werner Herzog.  Its original German title is Nosferatu: Phantom der Nacht ("Nosferatu: Phantom of the Night").  The film is set primarily in 19th-century Wismar, Germany and Transylvania, and was conceived as a stylistic remake of the 1922 German "Dracula" adaptation "Nosferatu".  It stars Klaus Kinski as Count Dracula, Isabelle Adjani as Lucy Harker, Bruno Ganz as Jonathan Harker, and French artist-writer Roland Topor as Renfield.  There are two different versions of the film, one in which the actors speak English, and one in which they speak German.

Elizabeth Bowen: Elizabeth Bowen, CBE ( ; 7 June 1899 – 22 February 1973) was an Irish novelist and short story writer.

Jakob von Gunten: Jakob von Gunten.  Ein Tagebuch is a novel by Swiss writer Robert Walser, first published in German in 1909.

Elizabeth Bibesco: Elizabeth Charlotte Lucy, Princess Bibesco ("née" Asquith; 26 February 1897 – 7 April 1945) was an English writer and socialite.  She was the daughter of a British Prime Minister and the wife of a Romanian aristocrat.  Active as a writer between 1921 and 1940, she drew on her experience in British high society in her work.  A final posthumous collection of her stories, poems and aphorisms was published under the title "Haven" in 1951, with a preface by Elizabeth Bowen.

Robert Walser (musicologist): Robert Walser is an American musicologist associated with the "new musicology".  He is author of the book "Running With the Devil: Power, Gender, and Madness in Heavy Metal Music", concerning heavy metal music.  Walser currently is a member of the faculty and director of the Center for Popular Music Studies at Case Western Reserve University.

Question: Did Elizabeth Bowen or Robert Walser speak German?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "query_subject_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person mentioned in the question."
        },
        "spoke_german": {
          "type": "boolean",
          "description": "True if the person spoke German, false otherwise."
        },
        "evidence": {
          "type": "string",
          "description": "The textual evidence from the context supporting whether the person spoke German."
        }
      },
      "required": [
        "name",
        "spoke_german",
        "evidence"
      ],
      "additionalProperties": false
    },
    "query_subject_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person mentioned in the question."
        },
        "spoke_german": {
          "type": "boolean",
          "description": "True if the person spoke German, false otherwise."
        },
        "evidence": {
          "type": "string",
          "description": "The textual evidence from the context supporting whether the person spoke German, or lack thereof."
        }
      },
      "required": [
        "name",
        "spoke_german",
        "evidence"
      ],
      "additionalProperties": false
    },
    "final_answer_person": {
      "type": "string",
      "description": "The name of the person who spoke German, if any."
    }
  },
  "required": [
    "query_subject_1",
    "query_subject_2",
    "final_answer_person"
  ],
  "additionalProperties": false
}
