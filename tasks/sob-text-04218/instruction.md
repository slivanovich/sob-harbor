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
Yunus-bek Yevkurov: Yunus-bek Bamatgireyevich Yevkurov (Russian: Юну́с-бек Баматгире́евич Евку́ров ; born 23 July 1963) is the head of the southern Russian republic of Ingushetia, appointed by President Dmitry Medvedev on 30 October 2008.  The following day, the People's Assembly of the Republic of Ingushetia, the republic's regional parliament, voted in favor of Yevkurov's appointment, making him the third Head of Ingushetia.

Akhmed Malsagov: Akhmed Malsagov is a former interim president of the southern Russian republic of Ingushetia.  The duration of his term was between December 2001 and May 2002.

Dmitry Medvedev: Dmitry Anatolyevich Medvedev ( ) (Russian: Дми́трий Анато́льевич Медве́дев , "Dmitriy Anatolyevich Medvedev"; ] , born 14 September 1965) is a Russian politician, currently the Prime Minister of Russia.  From 2008 to 2012, Medvedev served as the third President of Russia.

Head of the Republic of Ingushetia: The Head of the Republic of Ingushetia (Russian: Глава Республики Ингушетия ), formerly "President of the Republic of Ingushetia", is the highest office within the Government of Ingushetia, Russia.  The Head is elected by Russian citizens living in Ingushetia.  Term of service is five years.

Ingush Head election, 2013: Indirect elections for the Head of the Republic of Ingushetia were held on 9 September 2013.  Incumbent Head Yunus-Bek Yevkurov was re-elected for another 5 year term.

Rustaman Makhauri: Rustaman Makhauri (born 1978) is a Chechen military commander and a close associate of Doku Umarov, the anti-Russian underground Chechen leader.  Makhauri was appointed by Umarov as Minister of Defense; he is suspected of being responsible for a series of attacks against the forces loyal to the governments in Chechnya and neighboring Ingushetia.  He was captured by police in July 2009 in Ingushetia's district of Sunzhen and charged with involvement in the June 22, 2009 attack on the Ingush president Yunus-Bek Yevkurov.

Murat Zyazikov: Murat Magometovich Zyazikov (Russian: Мура́т Магоме́тович Зя́зиков ) (born September 10, 1957) is an Ingush politician who was the second president of the southern Russian republic of Ingushetia.  He was born in what is now Kyrgyzstan.  Zyazikov was a controversial politician in Ingushetia.

Rashid Gaysanov: Rashid Yakhyayevich Gaysanov (Russian: Рашид Яхьяевич Гайсанов ; born 17 September 1972), last name also spelled Gaisanov, is a Russian politician in the southern Republic of Ingushetia.  He has served as the Prime Minister of Ingushetia under Ingush President Yunus-bek Yevkurov.  He was further appointed the acting President of Ingushetia following an assassination attempt against Yevkurov in June 2009.

Abdul Madzhid (Dagestan rebel): Ilgar Mollachiev, better known as Emir Abdul Madzhid (Majid), was the militant leader of the Shariat Jamaat of the Caucasian Front in the Second Chechen War, in the volatile southern Russian republic of Dagestan.  He was the deputy of Rappani Khalilov until Khalilov's death in September 2007.  He was then appointed the new leader of the Shariat Jamaat by the orders of Dokka Umarov.  His nationality was Tsakhur.

Roddy Scott: On 26 September 2002 Scott was killed in the Russian republic of Ingushetia.  Russian soldiers found his body in Ingushetia's Galashki region, near the border with the war-torn republic of Chechnya, following a fierce battle between Russian forces and a group of Chechen rebel fighters in which at least 17 were killed and a Russian helicopter was shot down.  Scott had accompanied the Chechens from Ruslan Gelayev's unit as they crossed from Georgia into Russia and was apparently killed by a bullet in the viewfinder of his camera while filming the firefight, United Press International reported.  According to the Kavkaz Center, however, he was killed alone while trying to surrender.  At first, the Kremlin officials said Scott might still be alive.

Question: Yunus-bek Yevkurov was appointed the head of the southern Russian republic of Ingushetia by a president that served during what years?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "appointed_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who was appointed."
        },
        "position": {
          "type": "string",
          "description": "The position to which the person was appointed."
        }
      },
      "required": [
        "name",
        "position"
      ],
      "additionalProperties": false
    },
    "appointing_president": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the president who made the appointment."
        },
        "term_start_year": {
          "type": "integer",
          "description": "The start year of the president's term."
        },
        "term_end_year": {
          "type": "integer",
          "description": "The end year of the president's term."
        }
      },
      "required": [
        "name",
        "term_start_year",
        "term_end_year"
      ],
      "additionalProperties": false
    },
    "republic_of_appointment": {
      "type": "string",
      "description": "The name of the republic where the appointment took place."
    }
  },
  "required": [
    "appointed_person",
    "appointing_president",
    "republic_of_appointment"
  ],
  "additionalProperties": false
}
