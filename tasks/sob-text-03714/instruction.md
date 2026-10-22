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
Teresio Olivelli: Teresio Olivelli (7 January 1916 – 12 January 1945) was an Italian Roman Catholic soldier during World War II and part of the Italian Resistance movement to Fascism and the Nazi regime.  Olivelli graduated in law in Pavia in 1938 and went on to comment in papers on the legal and social issues of the time before he became a volunteer fighter in the Spanish Civil War and in World War II with a notable campaign fought in Russia.  The war soured his views towards the Italian fascist regime of Benito Mussolini and his time in the resistance was marked with articles in a newspaper he founded dedicated to promoting the Christian message and attempting to improve upon aspects of fascism with a more Christian message.

Anna Hanika: Anna Hanika (27 June 1903 - 14 March 1988) was an Austrian accounts clerk who became a resistance activist during the Nazi years.

Uralmash-1: The Uralmash-1 (Уралмаш-1) was a Soviet prototype self-propelled gun developed during World War II.  It was a turretless, tracked armoured fighting vehicle designed by the Yekaterinburg-based Uralmash design bureau (UZTM) between autumn 1944 and spring 1945.  It used the chassis of the T-44 medium tank and was intended to replace the SU-100 which itself had only entered service with the Red Army in late 1944.  Two prototypes of the Uralmash-1 with different armament were built in early 1945, one with the 100 mm D-10 tank gun, the other with the 122 mm D-25S tank gun.  While mass production was initially recommended, the end of the war with Germany in May 1945 eventually caused the project to be cancelled due to lack of necessity.  If the Uralmash-1 had entered service, the 100 mm variant would have been designated SU-101 (СУ-101) while the 122 mm variant would have been designated SU-102 (СУ-102), in accordance with Soviet military nomenclature, where the "SU"-label stood for Samokhodnaya Ustanovka, or self-propelled gun.

LXXVI Panzer Corps: The LXXVI Panzer Corps ("LXXVI Panzerkorps", 76th Armoured Corps) was a panzer corps of Nazi Germany during World War II.  The headquarters were formed in France under Army Group D on 29 June 1943 as LXXVI Army Corps but renamed a month later.  In August it shipped to Italy to become part of 10th Army.  It spent the rest of the war in Italy fighting in the Italian Campaign mainly under 10th Army but with short periods from February 1944 (Battle of Anzio) and January 1945 (Spring 1945 offensive in Italy) under 14th Army.  The Corps was commanded for most of its active fighting by General Traugott Herr.

Tadeusz Zawadzki: Tadeusz Zawadzki codename: Zośka, Kajman, Kotwicki, Lech Pomarańczowy, Tadeusz (born January 24, 1921, Warsaw, Poland – died August 20, 1943, Sieczychy, near Wyszków, Poland) was a Polish Scoutmaster (harcmistrz), Polish scouting resistance activist and second lieutenant of the Armia Krajowa during the Second World War.  He is a main character in "Kamienie na szaniec", a book by Aleksander Kamiński, describing "Operation Arsenal" in Warsaw, as well as Barbara Wachowicz's "Rudy, Alek, Zośka".  Zawadzki himself commanded the Operation Arsenal, a daring action of the Polish resistance, which took place in Warsaw on March 26, 1943, and which resulted in freeing Zawadzki's former high school classmate, Jan Bytnar.

Rhodesian Armoured Corps: The Rhodesian Armoured Corps—the "Black Devils"—was the only standing armoured battalion of the Rhodesian Security Forces.  During World War II, it took part in the Allied Spring 1945 offensive and the Battle of Monte Cassino as part of South Africa's 6th Armoured Division.  The unit was among the first to enter a liberated Florence in July 1944.  Prior to 1963, its crews were trained in the United Kingdom or Aden Colony and were known as the "Selous Scouts" under the Federation of Rhodesia and Nyasaland.  After Rhodesia's Unilateral Declaration of Independence, maintaining the armoured vehicle fleet became a responsibility of the Rhodesian Light Infantry until Major Bruce Rooken-Smith reactivated the former "Rhodesian Armoured Car Regiment" in 1972.  During the Rhodesian Bush War, the regiment fought in several major campaigns and battles, particularly Operation Miracle in September 1979.  It was superseded by the new "Zimbabwe Armoured Corps" between 1980 and 1981.

Austria in the time of National Socialism: Austria in the time of National Socialism describes the period of Austrian history from March 12, 1938 when Austria was annexed by the German Third Reich (an event commonly known as "Anschluss") until the end of World War II in spring 1945.

Käthe Dahlem: Käthe Dahlem (born Käthe Weber: 20 March 1899 - 25 December 1974) was a German political activist (USPD, KPD) who, after being forced into exile, became an anti-fascist Resistance activist, participating in the Spanish Civil War and, subsequently, again based in France.  After 1945 she became a public official in the Soviet occupation zone (relaunched in October 1949 as the German Democratic Republic (East Germany)).  She was retired on health grounds in July 1949 and was subsequently caught up in her husband's difficulties with the ruling party, the party first secretary, Walter Ulbricht and other leading party comrades who had spent the war years in Moscow.  By the 1960s, however, the authorities were happy to honour her pre-war and wartime contribution.

Sandweiler German war cemetery: The Sandweiler German war cemetery is a World War II cemetery in Sandweiler, in southern Luxembourg.  It contains the graves of 10,913 German servicemen from the Battle of the Bulge in winter 1944 and spring 1945.  Of these, 5,599 were buried by the American war graves service during the war; American casualties were buried at the Luxembourg American Cemetery and Memorial about 1.5 km away in Hamm.

Adriano Tardelli: Adriano Tardelli (1896 - 1 February 1945) was an Italian resistance activist during World War II.

Question: Anna Hanika was an Austrian accounts clerk who became a resistance activist during what period of Austrian history from March 12, 1938 until the end of World War II in spring 1945?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who was a resistance activist."
    },
    "person_role": {
      "type": "string",
      "description": "The primary role of the person during the specified historical period."
    },
    "historical_period_details": {
      "type": "object",
      "properties": {
        "period_name": {
          "type": "string",
          "description": "The name of the historical period."
        },
        "period_start_date": {
          "type": "string",
          "description": "The start date of the historical period."
        },
        "period_end_description": {
          "type": "string",
          "description": "A description of the end of the historical period."
        },
        "country": {
          "type": "string",
          "description": "The country associated with this historical period."
        }
      },
      "required": [
        "period_name",
        "period_start_date",
        "period_end_description",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_role",
    "historical_period_details"
  ],
  "additionalProperties": false
}
