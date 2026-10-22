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
Conrad Vogt-Svendsen: Conrad Vogt-Svendsen (6 March 1914 – 1 December 1973) was a Norwegian priest.  He was assistant seamen's priest in Hamburg during Second World War, helped with the White Buses operation in 1945, and was later main priest for the deaf in Norway.

List of subcamps of Neuengamme: Below is an incomplete list of SS subcamps of Neuengamme camp system operating from 1938 until 1945.  The Neuengamme concentration camp established by the SS in Hamburg, Germany, became a massive Nazi concentration camp complex using prisoner forced labour for production purposes in World War II.  Some 99 SS subcamps were part of the Neuengamme camp system, with up to 106,000 inmates.  The number of prisoners per location ranged from more than 5,000 to only a dozen at a work site.  Beginning in 1942, inmates of Neuengamme were also transported to the camp "Arbeitsdorf".  "Toward the ends of the war three times more prisoners were in satellite camps than in the main camp" wrote Dr. Garbe of the "Neuengamme Memorial Museum".  Several of the subcamps have memorials or plaques installed, but as of 2000, there was nothing at 28 locations.

Finn Moestue Husebye: Finn Moestue Huseby (11 May 1905 – 2001) was a Norwegian priest.  He graduated as cand.theol.  in 1930.  He worked as seamen's priest in New Orleans from 1931 to 1934, in Antwerp from 1935 to 1936, and in Hamburg from 1936 to 1942.  He had to leave Germany because of a conflict with Nazi-friendly Norwegians in Germany, and assistant priest Arne Berge took over after him as the seamen's priest in Hamburg.  He was parish priest in Brandbu from 1946.

Majdanek concentration camp: Majdanek, or KL Lublin, was a German concentration and extermination camp built and operated by the SS on the outskirts of the city of Lublin during the German occupation of Poland in World War II.  Although initially purposed for forced labor rather than extermination, the camp was used to kill people on an industrial scale during Operation Reinhard, the German plan to murder all Jews within their own General Government territory of Poland.  The camp, which operated from October 1, 1941, until July 22, 1944, was captured nearly intact, because the rapid advance of the Soviet Red Army during "Operation Bagration" prevented the "SS" from destroying most of its infrastructure, and the inept Deputy Camp Commandant Anton Thernes failed in his task of removing incriminating evidence of war crimes.  Therefore, Majdanek became the first concentration camp discovered by Allied forces.  Also known to the "SS" as "Konzentrationslager Lublin", Majdanek remains the best preserved Nazi concentration camp of the Holocaust.

Topovske Šupe concentration camp: The Topovske Šupe concentration camp (German: "Konzentrationslager Kanonen-Schuppen" ; Serbian: "Logor Topovske Šupe", Логор Топовске Шупе ) was a concentration camp located on the outskirts of Belgrade which was operated by Nazi Germany with the help of Milan Nedić's quisling government during World War II.  Located in the neighborhood of Autokomanda, on the site of an old military base, the camp held approximately 5,000 to 6,000 inmates from its establishment on 20 August 1941 until its closure in December of that year.  About 4,300 inmates were killed during its operation, of whom 3,000 were killed as hostages and 1,300 were killed as suspected anti-fascists.

Josef Kramer: Josef Kramer (10 November 1906 – 13 December 1945) was the Commandant of the Bergen-Belsen concentration camp.  Dubbed The Beast of Belsen by camp inmates, he was a notorious German Nazi war criminal, directly responsible for the deaths of thousands of people.  He was detained by the British army after the Second World War, convicted of war crimes and hanged on the gallows in Hamelin prison by British executioner Albert Pierrepoint.

White Buses: "White Buses" was an operation undertaken by the Swedish Red Cross and the Danish government in the spring of 1945 to rescue concentration camp inmates in areas under Nazi control and transport them to Sweden, a neutral country.  Although the operation was initially targeted at saving citizens of Scandinavian countries, it rapidly expanded to include citizens of other countries.

Celle massacre: The Celle massacre (euphemistically called ""Celler Hasenjagd"", "hare chase of Celle") was a massacre of concentration camp inmates that took place in Celle, Prussian Hanover, in the last weeks of the Second World War.  On 8 April, 1945 over 3,000 concentration camp internees were killed in an Allied air raid and subsequent attacks by SS guards, Gestapo, and Nazi party officials, as well as members of the public.  Some of the perpetrators of the massacre were later tried but all of those convicted for the crime were set free in the early 1950s.

Crveni Krst concentration camp: The Crveni Krst concentration camp (lit.  Red Cross concentration camp), located in Crveni Krst, Niš, was operated by the German Gestapo and used to hold captured Serbs, Jews and Romanis during the Second World War.  Established in mid-1941, it was used to detain as many as 35,000 people during the war and was liberated by the Yugoslav Partisans in 1944.  More than 10,000 people are thought to have been killed at the camp.  After the war, a memorial to the victims of the camp was erected on Mount Bubanj, where many inmates were shot.  A memorial museum was opened on the former campgrounds in 1967 and in 1979 the campgrounds were declared a Cultural Monument of Exceptional Importance and came under the protection of the Socialist Republic of Serbia.

Arne Berge: Arne Berge (29 June 1908 – 13 August 1988) was a Norwegian priest.  He was seamen's priest in Hamburg during World War II, when he also worked among Scandinavian prisoners in Germany, and helped planning and carrying out the White Buses operation.

Question: Conrad Vogt-Svendsen, was a Norwegian priest, he was assistant seamen's priest in Hamburg during Second World War, helped with the White Buses operation in 1945, an operation undertaken by the Swedish Red Cross and the Danish government in the spring of 1945 to rescue concentration camp inmates in areas under Nazi control, and transport them to which neutral country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person mentioned."
        },
        "role": {
          "type": "string",
          "description": "The role of the person during the specified period."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "operation": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the operation."
        },
        "year": {
          "type": "integer",
          "description": "The year the operation took place."
        },
        "purpose": {
          "type": "string",
          "description": "The main purpose of the operation."
        },
        "organizations_involved": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of organizations that undertook the operation."
        }
      },
      "required": [
        "name",
        "year",
        "purpose",
        "organizations_involved"
      ],
      "additionalProperties": false
    },
    "destination_country": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the neutral country to which inmates were transported."
        },
        "status": {
          "type": "string",
          "description": "The political status of the country during the operation (e.g., neutral)."
        }
      },
      "required": [
        "name",
        "status"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person",
    "operation",
    "destination_country"
  ],
  "additionalProperties": false
}
