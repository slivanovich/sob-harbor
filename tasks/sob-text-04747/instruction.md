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
Kimble County, Texas: Kimble County is a county located on the Edwards Plateau in the U.S. state of Texas.  As of the 2010 census, its population was 4,607.  Its county seat is Junction.  The county was created in 1858 and organized in 1876.  It is named for George C. Kimble, who died at the Battle of the Alamo.

A Slight Demonstration: A Slight Demonstration is a 2007 book about the 1864 Civil War Battle of Decatur, a pivotal event in Confederate General John B. Hood's disastrous Tennessee Campaign late in the war, in which a Union force of only 2-5,000 soldiers prevented Hood's 23,000 strong army from crossing the Tennessee River.  It was written by Noel Carpenter, a former Decatur native and Air Force officer.  The book is published by Legacy Books & Letters of Austin, Texas.  It is the first book solely devoted to the Battle of Decatur.

Tennis Court Oath: On June 20th, 1789, the members of the French Estates-General for the Third Estate, who had begun to call themselves the National Assembly, took the Tennis Court Oath (French: "Serment du Jeu de Paume" ), vowing "not to separate, and to reassemble wherever circumstances require, until the constitution of the kingdom is established."  It was a pivotal event in the early days of the French Revolution.

2014 Texas Revolution season: The 2014 Texas Revolution season was the team's fifteenth season as a professional indoor football franchise, fifth in the Indoor Football League (IFL), and second as the "Texas Revolution".  One of nine teams in the IFL for the 2014 season, the Texas Revolution competed in the United Conference for the second consecutive year.  The team played their home games at the Allen Event Center in Allen, Texas.  Chris Williams returned to the IFL as the Texas Revolution's director of football operations and head coach for 2014.  The team started strong but faltered, compiling a 3–11 record and missing the playoffs.  In the post-season, Williams resigned and the team announced their departure from the IFL.

2015 Texas Revolution season: The 2015 Texas Revolution season was the team's sixteenth season as a professional indoor football franchise, third as the "Texas Revolution", and first as a member of Champions Indoor Football (CIF).  One of nine teams in the CIF for the 2015 season, the Revolution played their home games at the Allen Event Center in Allen, Texas.

2013 Texas Revolution season: The 2013 Texas Revolution season was the team's fourteenth season as a football franchise, fourth in the Indoor Football League (IFL), and first as the "Texas Revolution".  One of just nine teams competing in the IFL for the 2013 season, the Texas Revolution were realigned to the United Conference.  The team played their home games at the Allen Event Center in Allen, Texas.  Head coach Billy Back led the team to a 5–9 record and they failed to qualify for post-season play.

Black Friday (1978): Black Friday (Persian: جمعه سیاه "Jom'e-ye Siyāh") is the name given to 8 September 1978 (17 Shahrivar 1357 Iranian calendar) because of the shootings in Jaleh Square (Persian: میدان ژاله "Meydān-e Jāleh") in Tehran, Iran.  The deaths and the reaction to them has been described as a pivotal event in the Iranian Revolution when any "hope for compromise" between the protest movement and the Mohammad Reza Shah's regime was extinguished.

George C. Kimble: George C. Kimble (alternately spelled Kimbell or Kimball, March 6, 1803 – March 6, 1836) was a defender and officer of the Alamo Mission in San Antonio, who died at the Battle of the Alamo.  Kimble County in the hill country of Texas is named in his honor.

Battle of the Alamo: The Battle of the Alamo (February 23 – March 6, 1836) was a pivotal event in the Texas Revolution.  Following a 13-day siege, Mexican troops under President General Antonio López de Santa Anna launched an assault on the Alamo Mission near San Antonio de Béxar (modern-day San Antonio, Texas, United States), killing all of the Texian defenders.  Santa Anna's cruelty during the battle inspired many Texians—both Texas settlers and adventurers from the United States—to join the Texian Army.  Buoyed by a desire for revenge, the Texians defeated the Mexican Army at the Battle of San Jacinto, on April 21, 1836, ending the revolution.

Army of the Republic of Texas: The Army of the Republic of Texas was the land-based component of the armed forces for the Republic of Texas.  It directly descended from the Texian Army, which was established on October 2, 1835, to fight for independence from Mexico in the Texas Revolution.  The army was provisionally formed from the Consultation in November 1835, and officially established on September 5, 1836, from Article II, Section 5 of the Constitution of the Republic of Texas.  After Texas' annexation by the United States, the Army of the Republic of Texas was merged into the United States Army.  Today, the 141st Infantry Regiment trace their lineage back to the Texas Revolution.

Question: Which pivotal event in the Texas Revolution did  George C. Kimble did at 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pivotal_event": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the pivotal event."
        },
        "revolution": {
          "type": "string",
          "description": "The revolution the event was a part of."
        },
        "date_range": {
          "type": "string",
          "description": "The date range of the event."
        }
      },
      "required": [
        "name",
        "revolution"
      ],
      "additionalProperties": false
    },
    "person_involved": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person involved."
        },
        "fate_in_event": {
          "type": "string",
          "description": "What happened to the person during the event."
        }
      },
      "required": [
        "name",
        "fate_in_event"
      ],
      "additionalProperties": false
    },
    "event_significance": {
      "type": "string",
      "description": "A description of why the event was pivotal."
    }
  },
  "required": [
    "pivotal_event",
    "person_involved",
    "event_significance"
  ],
  "additionalProperties": false
}
