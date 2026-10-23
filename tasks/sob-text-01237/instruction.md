{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPsychopathography of Adolf Hitler: The Psychopathography of Adolf Hitler is an umbrella term for psychiatric (pathographic, psychobiographic) literature that deals with the hypothesis that the German Führer and Reichskanzler Adolf Hitler (1889–1945) suffered from mental illness.  Both during his lifetime and after his death, Hitler has often been associated with mental disorders such as hysteria, megalomania or paranoid schizophrenia.  Psychiatrists and psychoanalysts who have diagnosed Hitler as having mental disturbance include well-known figures such as Walter C. Langer and Erich Fromm.  Other researchers, such as Fritz Redlich, have concluded that Hitler probably did not have these disorders.\n\nFlensburg Government: The Flensburg Government (German: \"Flensburger Regierung\" ), also known as the Flensburg Cabinet (\"Flensburger Kabinett\"), the Dönitz Government (\"Regierung Dönitz\"), or the Schwerin von Krosigk Cabinet (\"Kabinett Schwerin von Krosigk\"), was the short-lived government of Nazi Germany during a period of three weeks around the end of World War II in Europe.  The government was formed following the suicide of Adolf Hitler on 30 April 1945 during the Battle of Berlin.  It was headed by Grand Admiral Karl Dönitz as the Reichspräsident and Lutz Graf Schwerin von Krosigk as the Leading Minister.\n\nConspiracy theories about Adolf Hitler's death: Conspiracy theories about Adolf Hitler's death contradict the fact that Adolf Hitler committed suicide in his \"Führerbunker\" on 30 April 1945.  Most of these theories hold that Hitler and his wife, Eva Braun, survived and escaped the city of Berlin.  While subject to some exposure in popular culture, examples being books such as \"Grey Wolf: The Escape of Adolf Hitler\", these viewpoints are regarded by mainstream historians as disproven fringe theories.\n\nKarl Dönitz: Karl Dönitz (sometimes spelt Doenitz) (] ; 16 September 1891 – 24 December 1980) was a German admiral who played a major role in the naval history of World War II.  Dönitz briefly succeeded Adolf Hitler as the head of state of Germany.\n\nPersonal standard of Adolf Hitler: The personal standard of Adolf Hitler was designed after Reichspräsident Paul von Hindenburg died on 2 August 1934.  Adolf Hitler abolished the title \"Reichspräsident\" and in its place instituted the title of \"Führer\" which henceforth could only be used when referring to him personally.  Hindenburg used a personal standard consisting of a black eagle on a square gold background edged by a border of black, white and red bands.  Hitler decided on 19 August 1934 to adopt a personal standard for himself, which was called \"Personal standard for Adolf Hitler as Leader and Chancellor of the German Nation\".  As he was also Supreme Commander of the Armed Forces it was somewhat later known as \"The personal standard for Adolf Hitler as Leader and Supreme Commander of the Armed Forces\" (German: \"Standarte des Führers und Obersten Befehlshabers der Wehrmacht\").\n\nThe Mind of Adolf Hitler: The Mind of Adolf Hitler: The Secret Wartime Report, published in 1972 by Basic Books, is based on a World War II report by psychoanalyst Walter C. Langer which probed the psychology of Adolf Hitler from the available information.  The original report was prepared for the Office of Strategic Services (OSS) and submitted in late 1943 or early 1944; it is officially entitled \"A Psychological Analysis of Adolph Hitler: His Life and Legend\".  The report is one of two psychoanalytic reports prepared for the OSS during the war in an attempt to assess Hitler's personality; the other is \"Analysis of the Personality of Adolph Hitler\" by the psychologist Henry A. Murray who also contributed to Langer's report.  The report eventually became 1000 pages long.\n\nHans-Georg von Friedeburg: Hans-Georg von Friedeburg (15 July 1895 – 23 May 1945) was a German admiral, the deputy commander of the U-boat Forces of Nazi Germany and the last Commander-in-Chief of the Kriegsmarine.  He was the only representative of the armed forces to be present at the signing of the German instruments of surrender both in Reims on 7 May and in Berlin on 8 May 1945. \" Generaladmiral\" von Friedeburg committed suicide shortly afterwards, upon the dissolution of the Flensburg Government.\n\nLeibstandarte SS Adolf Hitler order of battle: The Leibstandarte SS \"Adolf Hitler\" (LSSAH) was founded in September 1933 as Adolf Hitler's personal Bodyguard formation.  It was given the title \"Leibstandarte Adolf Hitler\" (LAH) in November, 1933.  On 13 April 1934, by order of Himmler, the regiment became known as the \"Leibstandarte SS Adolf Hitler\" (LSSAH).  In 1939 the LSSAH became a separate unit of the Waffen-SS aside the SS-TV and the SS-VT.\n\nHistoriography of Adolf Hitler: The Historiography of Adolf Hitler deals with the academic studies of Adolf Hitler from the 1930s to the present.  In 1998, a German editor said there were 120,000 studies of Hitler and Nazi Germany.  Since then a large number more have appeared, with many of them decisively shaping the historiography regarding Hitler.\n\nMürwik: Mürwik (Danish: \"Mørvig\" ) is a community of Flensburg on the east side of the Flensburg Firth.  It is on the Angeln peninsula.  Mürwik is the location of the Naval Academy at Mürwik, which is the main academy that trains German Navy officers.  Nazi Germany's final government, the Flensburg government, was located in Mürwik.\n\nQuestion: Who was apart of the Flensburg Government and succeeded Adolf Hitler?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"government_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the short-lived government.\"\n    },\n    \"head_of_state_successor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the individual who succeeded Adolf Hitler as head of state.\"\n        },\n        \"role_in_government\": {\n          \"type\": \"string\",\n          \"description\": \"The role held by this individual in the government.\"\n        },\n        \"succeeded_adolf_hitler\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if this individual succeeded Adolf Hitler as head of state.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_government\",\n        \"succeeded_adolf_hitler\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"other_key_members\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of another key member of the government.\"\n          },\n          \"role_in_government\": {\n            \"type\": \"string\",\n            \"description\": \"The role held by this individual in the government.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"role_in_government\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of other key individuals who were part of the government.\"\n    }\n  },\n  \"required\": [\n    \"government_name\",\n    \"head_of_state_successor\",\n    \"other_key_members\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "government_name": {
        "type": "string",
        "description": "The name of the short-lived government."
      },
      "head_of_state_successor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual who succeeded Adolf Hitler as head of state."
          },
          "role_in_government": {
            "type": "string",
            "description": "The role held by this individual in the government."
          },
          "succeeded_adolf_hitler": {
            "type": "boolean",
            "description": "Indicates if this individual succeeded Adolf Hitler as head of state."
          }
        },
        "required": [
          "name",
          "role_in_government",
          "succeeded_adolf_hitler"
        ],
        "additionalProperties": false
      },
      "other_key_members": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of another key member of the government."
            },
            "role_in_government": {
              "type": "string",
              "description": "The role held by this individual in the government."
            }
          },
          "required": [
            "name",
            "role_in_government"
          ],
          "additionalProperties": false
        },
        "description": "A list of other key individuals who were part of the government."
      }
    },
    "required": [
      "government_name",
      "head_of_state_successor",
      "other_key_members"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
