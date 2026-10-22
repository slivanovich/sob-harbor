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
Tamás Fellegi: Tamás László Fellegi (Budapest, January 7, 1956), Hungarian politician, jurist, political scientist, businessman, who served as Minister of National Development in Viktor Orbán's government from May 29, 2010 to December 14, 2011.  After that he was a minister without portfolio in Orbán II Cabinet.  Between 1996 and 2000 Sectoral Director, then CEE of Legal and Governmental Affairs of Hungarian Telecom (MATÁV Rt.).  Currently, he is Managing Partner of EuroAtlantic Solutions, an international consultancy firm.  In 2013, EuroAtlantic Solutions joined the Prime Policy Group consortium and registered as a foreign agent at the U.S. Department of Justice under the Foreign Agent Registration Act for its US-based activities political activities carried out on behalf of the Hungarian government.  Fellegi also serves as president of the Hungary Initiatives Foundation, a foundation created in November 2013 at the order Hungary's Prime Minister Viktor Orbán.

Viktor Orbán: Viktor Mihály Orbán (] ; born 31 May 1963) is a Hungarian politician and jurist.  He is the current Prime Minister of Hungary, a position he has held since 2010.  He also previously served as Prime Minister from 1998 to 2002.  He is the present leader of the national conservative Fidesz party, a post he has held since 2003 and, previously, from 1993 to 2000.  On 19 November 2016, Orbán surpassed István Bethlen as the 3rd longest-serving Prime Minister in Hungarian history.

György Matolcsy: György Matolcsy (born 18 July 1955 in Budapest) is a Hungarian politician and economist, current governor of the Hungarian National Bank (MNB).  He also served as Minister of Economy (2000–2002) during the first cabinet of Viktor Orbán and Minister of National Economy (2010–2013) in the Second Orbán Cabinet.

István Tisza: Count István Tisza de Borosjenő et Szeged (archaically English: Stephen Tisza; 22 April 1861 – 31 October 1918) was a Hungarian politician, prime minister, political scientist and member of Hungarian Academy of Sciences.  The prominent event in his life was Austria-Hungary's entry into the First World War when he was prime minister for the second time.  He was later assassinated during the Chrysanthemum Revolution on 31 October 1918 - the same day that Hungary terminated its political union with Austria.  Tisza supported the dual monarchy of Austria-Hungary and was representative of the then "liberal-conservative consent".

István Varga (politician): István Varga (born 23 June 1956) is a Hungarian politician and economist, who served as Minister of National Development and Economy between 2009 and 2010.  Gordon Bajnai appointed him on 29 April 2009, after Tamás Vahl withdrew from the designation of the ministerial position.  Before that the acting economy minister was Péter Hónig between 14 and 29 April.  Varga is married and has three children.

Zsolt Semjén: Zsolt Semjén (born 8 August 1962 in Budapest) is a Hungarian politician, currently minister without portfolio and Deputy Prime Minister in the second and third cabinet of Prime Minister Viktor Orbán.  Semjén is the leader of the Christian Democratic People's Party (KDNP) since 2003, which formed a coalition and alliance with Fidesz.

Sándor Fazekas: Sándor Fazekas (born 3 May 1963) is a Hungarian jurist and politician.  He has been Minister of Rural Development since 2010 in the cabinet of Prime Minister Viktor Orbán.  He served as mayor of his hometown, Karcag between 1990 and 2010.

István Stumpf: István Stumpf (born 5 August 1957) is a Hungarian politician.  A former member of the ruling Communist Hungarian Socialist Workers' Party, he was the last Vice President of National Council of the Patriotic People's Front from 1989 to 1990.  He also served as Minister of Prime Minister's Office between 1998 and 2002 in the first cabinet of Viktor Orbán.  He is a member of the Constitutional Court of Hungary since July 2010.

Zsuzsanna Németh: Lászlóné Németh or Zsuzsanna Németh (née "Zsuzsanna Serényi"; born July 16, 1953 in Budapest), Hungarian politician and economist, who served as Minister of National Development in Viktor Orbán's government between 23 December 2011 and 6 June 2014.

Prime Minister of Hungary: The Prime Minister of Hungary (Hungarian: "miniszterelnök" , lit.  "Minister-President") is the head of government of Hungary and the most powerful person in Hungarian politics.  He or she leads the majority party or coalition in the National Assembly, and is also the chairperson of the cabinet.  The current Prime Minister is Viktor Orbán, who has served since 29 May 2010.

Question: Tamás László Fellegi, Hungarian politician, jurist, political scientist, businessman, who served as Minister of National Development in the government of Viktor Mihály Orbán, a Hungarian politician and jurist, and is the current Prime Minister of which country, a position he has held since 2010?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "prime_minister": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the Prime Minister."
        },
        "current_title": {
          "type": "string",
          "description": "The current political title held by the individual."
        },
        "country_of_service": {
          "type": "string",
          "description": "The country for which the individual serves as Prime Minister."
        },
        "term_start_year": {
          "type": "integer",
          "description": "The year the current term as Prime Minister began."
        }
      },
      "required": [
        "name",
        "current_title",
        "country_of_service",
        "term_start_year"
      ],
      "additionalProperties": false
    },
    "related_official": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the official related to the Prime Minister."
        },
        "role_in_government": {
          "type": "string",
          "description": "The role held by the related official in the Prime Minister's government."
        },
        "prime_minister_served_under": {
          "type": "string",
          "description": "The name of the Prime Minister under whom the official served."
        }
      },
      "required": [
        "name",
        "role_in_government",
        "prime_minister_served_under"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The country Viktor Orb\u00e1n is the current Prime Minister of."
    }
  },
  "required": [
    "prime_minister",
    "related_official",
    "final_answer"
  ],
  "additionalProperties": false
}
