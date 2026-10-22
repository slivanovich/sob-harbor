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
Torrens Island Concentration Camp: The Torrens Island Internment Camp was a World War I concentration camp, located on Torrens Island in the Port River Estuary near Adelaide in South Australia.  The camp opened on 9 October 1914 and held up to 400 men of German or Austro-Hungarian background, or crew members of enemy ships who had been caught in Australian ports at the beginning of the war.  They were held without trial under the provisions of the "War Precautions Act 1914".

Bardufoss concentration camp: The Bardufoss concentration camp is located in Northern Norway in the municipality of Målselv.  During the occupation of Norway by Nazi Germany, the Nazi authorities established a "concentration camp in the town of Bardufoss," as an annex to the Grini concentration camp.  It opened in March 1944 to alleviate overflowing in other camps, particularly Grini and the Falstad concentration camp.  Situated in a cold climate, it was notorious for its hard work regime, sparse rations, and inadequate shelter.  It is estimated that some 800 prisoners passed through the camp, and when liberated about 550 were incarcerated.

Erich Zoddel: Erich Zoddel (August 9, 1913 – November 30, 1945) was a prisoner functionary at the Bergen-Belsen concentration camp.  In 1941, Zoddel was sentenced to a year in prison for theft before being transferred to Sachsenhausen concentration camp in 1942.  He worked as a forced laborer in the Heinkel factory in Oranienburg until October 1943.  In November 1943, after a brief stay at Buchenwald concentration camp, he was taken to Mittelbau-Dora concentration camp.  On 27 March 1944, Zoddel and 1,000 other prisoners from Mittelbau-Dora arrived at Bergen-Belsen.  By January 1945, Zoddel had risen in the ranks to a camp division.  Two days after the liberation of Bergen-Belsen by the British army on 15 April 1945, Zoddel killed a female detainee, a crime for which he was sentenced to death by a British military court in Celle on 31 August 1945.  On 17 November 1945, Zoddel was sentenced to life imprisonment in a second trial for his actions at Bergen-Belsen.  His execution was carried out later that month in Wolfenbüttel.

Dachau concentration camp: Dachau concentration camp (German: "Konzentrationslager (KZ) Dachau" , ] ) was the first of the Nazi concentration camps opened in Germany, intended to hold political prisoners.  It is located on the grounds of an abandoned munitions factory northeast of the medieval town of Dachau, about 16 km northwest of Munich in the state of Bavaria, in southern Germany.  Opened in 1933 by Heinrich Himmler, its purpose was enlarged to include forced labor, and eventually, the imprisonment of Jews, German and Austrian criminals, and eventually foreign nationals from countries that Germany occupied or invaded.  The Dachau camp system grew to include nearly 100 sub-camps, which were mostly work camps or "Arbeitskommandos ", and were located throughout southern Germany and Austria.  The camps were liberated by U.S. forces on 1 May 1945.

Ohrdruf concentration camp: Ohrdruf concentration camp was a Nazi forced labor and concentration camp located near Ohrdruf, south of Gotha, in Thuringia, Germany.  It was part of the Buchenwald concentration camp network and the first Nazi concentration camp liberated by U.S. troops.

Morgentaler v R: Morgentaler v R (also known as "Morgentaler v The Queen") is a decision of the Supreme Court of Canada where physician Henry Morgentaler unsuccessfully challenged the prohibition of abortion in Canada under the Criminal Code.  The Court found the abortion law was appropriately passed by Parliament under the laws of federalism.  This was the first of three Supreme Court decisions on abortion that were brought by Morgentaler.

Esterwegen concentration camp: The Esterwegen concentration camp near Esterwegen was an early Nazi concentration camp within a series of camps first established in the Emsland district of Germany.  It was established in the summer of 1933 as a concentration camp for 2000 so-called political "Schutzhäftlinge" (protective custody prisoners) and was for a time the second largest concentration camp after Dachau.  The camp was closed in summer of 1936.  Until 1945 the camp was used as a prison camp.  Political prisoners and so called "Nacht und Nebel"-prisoners were also held here.  Then Esterwegen served as a British internment camp, as a prison, and, until 2000, as a depot for the German Army.

Lobor concentration camp: The Lobor concentration camp or Loborgrad camp (Croatian: "Koncentracioni logor Lobor" ) was a concentration camp established in Lobor, Independent State of Croatia (modern-day Croatia) in the deserted palace of Keglevich family.  It was established on 9 August 1941, mostly for Serb and Jewish children and women.  The camp was established and operated by Ustaše, with 16 of its guards being members of the local Volksdeutsche community.  Its inmates were subjected to systematic torture, robbery and murder of "undisciplined" individuals.  All younger female inmates of the Lobor camp were subjected to rapes.  More than 2,000 people were inmates of this camp, at least 200 died in it.  All survived children and women were transported to Auschwitz concentration camp in August 1942 where they all were killed.

Henry Morgentaler: Henekh "Henry" Morgentaler, {'1': ", '2': ", '3': ", '4': "} (March 19, 1923 – May 29, 2013), was a Jewish Polish-born Canadian physician and pro-choice advocate who fought numerous legal battles aimed at expanding abortion rights in Canada.  As a youth during World War II, Morgentaler was imprisoned at the Łódź Ghetto and later at the Dachau concentration camp.

Herzogenbusch concentration camp: Herzogenbusch concentration camp (Dutch: "Kamp Vught" , ] , German: "Konzentrationslager Herzogenbusch" ] ) was a Nazi concentration camp located in Vught near the city of 's-Hertogenbosch, Netherlands.  Herzogenbusch was, with Natzweiler-Struthof in occupied France, the only concentration camp run directly by the SS in western Europe outside of Germany.  The camp was first used in 1943 and held 31,000 prisoners.  749 prisoners died in the camp, and the others were transferred to other camps shortly before the camp was liberated by the Allied Forces in 1944.  After the war the camp was used as a prison for Germans and Dutch collaborators.  Today there is a visitors' center with exhibitions and a national monument remembering the camp and its victims.  The camp is now a museum.

Question: Henry Morgentaler was imprisioned at a concentration camp opened in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person in question."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "imprisonment_camp": {
      "type": "object",
      "properties": {
        "camp_name": {
          "type": "string",
          "description": "The name of the concentration camp where the person was imprisoned."
        },
        "opening_year": {
          "type": "integer",
          "description": "The year the concentration camp was opened."
        }
      },
      "required": [
        "camp_name",
        "opening_year"
      ],
      "additionalProperties": false
    },
    "answer_year": {
      "type": "integer",
      "description": "The opening year of the concentration camp where the person was imprisoned."
    }
  },
  "required": [
    "person",
    "imprisonment_camp",
    "answer_year"
  ],
  "additionalProperties": false
}
