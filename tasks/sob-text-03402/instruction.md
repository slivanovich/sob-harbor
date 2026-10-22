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
Karl-Otto Koch: Karl-Otto Koch (] ; 2 August 1897 – 5 April 1945) was a mid-ranking commander in the SS of Nazi Germany who was the first commandant of the Nazi concentration camps at Buchenwald and Sachsenhausen.  From September 1941 until August 1942, he served as the first commandant of the Majdanek concentration camp in occupied Poland, stealing vast amounts of valuables and money from murdered Jews.  His wife, Ilse Koch, also took part in the notorious crimes at Buchenwald and Majdanek.

Werner Grothmann: Werner Grothmann (23 August 1915 – 26 February 2002) was a mid-ranking commander in the Waffen-SS of Nazi Germany and "aide-de-camp" to "Reichsführer-SS" Heinrich Himmler from 1940 until Himmler's death in 1945.

Karl Nicolussi-Leck: Karl Nicolussi-Leck (14 March 1917 – 30 August 2008) was a mid-ranking commander in the Waffen-SS of Nazi Germany during World War II.  He was a recipient of the Knight's Cross of the Iron Cross.

Georg Preuß: Georg Preuß (24 April 1920 – 3 February 1991) was a mid-ranking commander in the Waffen-SS of Nazi Germany during World War II.  He was a convicted war criminal.

Rudolf Lehmann (SS officer): Rudolf Lehmann (30 January 1914 – 13 September 1983) was a mid-ranking commander the Waffen-SS of Nazi Germany during World War II.  He was a recipient of the Knight's Cross of the Iron Cross.  Following the war, Lehmann authored a unit history of SS Division Leibstandarte published in German by HIAG, the post-war Waffen-SS lobby group, and in English by J.J. Fedorowicz Publishing.

Josef Diefenthal: Josef Diefenthal (5 October 1915 – 13 April 2001) was a mid-ranking commander in the Waffen-SS of Nazi Germany and a war criminal during World War II.  He was a recipient of the Knight's Cross of the Iron Cross on 5 February 1945 for his actions during the Ardennes Offensive, while in command of the 3rd Battalion, 2nd SS Panzer Grenadier Regiment, SS Division Leibstandarte.

Erich Priebke: Erich Priebke (29 July 1913 – 11 October 2013) was a German mid-level SS commander in the SS police force (SiPo) of Nazi Germany.  In 1996 he was convicted of war crimes in Italy, for participating in the Ardeatine massacre in Rome on 24 March 1944.  335 Italian civilians (among them 75 Italians of Jewish ancestry) were killed in retaliation for a partisan attack that killed 33 men of the German SS Police Regiment Bozen.  Priebke was one of the men held responsible for this mass execution.  After the defeat of Nazi Germany, he received help from a bishop stationed in Rome and fled to Argentina on a Vatican passport, where he lived for over 50 years.

Gustav Laabs: Gustav Laabs (born 20 December 1902-died 12 March 1980) was a German SS commander during the Nazi era.  During the Second World War, he worked as a gas van operator at the Chełmno extermination camp in Wartheland.  As an operator of a gas van, Laabs was directly involved in and responsible for the genocidal extermination of over 100,000 men, women and children, most of whom were killed on account of being Jewish.  After the war, he was tried and convicted for his crimes against humanity.  Despite being convicted, Laabs was given the lenient sentence of 15 years (subsequently reduced to 13 years) by a regional court in Landgericht Bonn, Germany.  Far from being outliers, such instances of leniency, extended to perpetrators of genocide and crimes against humanity during trials in post-Nazi Germany, constituted the norm, as evidenced by the fact that most of the perpetrators of Nazi war crimes and the Final Solution were not brought to justice.  Many former SS officers and Nazis, who were directly responsible for perpetrating genocide and murdering countless innocent people, were contracted to work for US and British intelligence agencies as part of the war against the USSR and Communism (also see Operation Paperclip for more on post-WWII Allied collaboration with Nazis).

Ilse Koch: Ilse Koch (] ; née "Margarete Ilse Köhler"; 22 September 1906 – 1 September 1967) was the wife of Karl-Otto Koch, commandant of the Nazi concentration camps Buchenwald (1937–1941) and Majdanek (1941–1943).  In 1947, she became one of the first prominent Nazis to be tried by the U.S. military.

Otto Günsche: Otto Günsche (24 September 1917 – 2 October 2003) was a mid-ranking commander in the Waffen-SS of Nazi Germany during World War II.  He was a member of the SS Division Leibstandarte before he became Adolf Hitler's personal adjutant.  Günsche was taken prisoner by soldiers of the Red Army in Berlin on 2 May 1945.  After being held in various prisons and labour camps in the USSR, he was released from Bautzen Penitentiary on 2 May 1956.

Question: The mid-ranking commander in the SS of Nazi Germany Karl-Otto Koch took part in Holocaust crimes with which accomplice who was tried by the U.S. military in 1947?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "karl_otto_koch_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "rank": {
          "type": "string"
        },
        "role": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "rank",
        "role"
      ],
      "additionalProperties": false
    },
    "accomplice_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "relationship_to_karl_otto_koch": {
          "type": "string"
        },
        "involvement_in_crimes": {
          "type": "string"
        },
        "trial_information": {
          "type": "object",
          "properties": {
            "trial_year": {
              "type": "integer"
            },
            "prosecuting_body": {
              "type": "string"
            },
            "trial_significance": {
              "type": "string"
            }
          },
          "required": [
            "trial_year",
            "prosecuting_body",
            "trial_significance"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "relationship_to_karl_otto_koch",
        "involvement_in_crimes",
        "trial_information"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the accomplice who was tried by the U.S. military in 1947."
    }
  },
  "required": [
    "karl_otto_koch_details",
    "accomplice_details",
    "final_answer"
  ],
  "additionalProperties": false
}
