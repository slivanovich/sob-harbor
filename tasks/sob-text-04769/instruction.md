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
10th Motorized Cavalry Brigade (Poland): The 10th Cavalry Brigade (Polish: "10.  Brygada Kawalerii" ) was a Polish military unit in World War II.  It was the only fully operational Polish motorized infantry unit during the Invasion of Poland, as Warsaw Armoured Motorized Brigade was not completed by September 1, 1939.  Commanded by Colonel, later General Stanisław Maczek, it is considered one of few Polish World War II military units (brigade size or larger) not to have been decisively defeated in 1939 .  Another was General Franciszek Kleeberg's Independent Operational Group Polesie ( a corps or field army).

George S. Patton: General George Smith Patton Jr. (November 11, 1885 – December 21, 1945) was a senior officer of the United States Army who commanded the U.S. Seventh Army in the Mediterranean and European theaters of World War II, but is best known for his leadership of the U.S. Third Army in France and Germany following the Allied invasion of Normandy in June 1944.

First Motion Picture Unit: The First Motion Picture Unit (FMPU), later 18th Army Air Forces Base Unit, was the primary film production unit of the US Army Air Forces (USAAF) during World War II and was the first military unit made up entirely of professionals from the film industry.  It produced more than 400 propaganda and training films, which were notable for being informative as well as entertaining.  Films for which the unit is known include "Resisting Enemy Interrogation", "" and "The Last Bomb"—all of which were released in theatres.  Veteran actors such as Clark Gable, William Holden, Clayton Moore, and future President Ronald Reagan and directors such as John Sturges served with the FMPU.  The unit also produced training films and trained combat cameramen.  FMPU personnel served with distinction during World War II.

18th (Croatian) Eastern Bosnian Brigade: The 18th (Croatian) Eastern Bosnian Brigade was a World War II military unit of the Yugoslav Partisans.  It was formed in October 1943 in the Husino village (in today's Bosnia and Herzegovina) after the capitulation of Italy forced the Germans to move a large part of their forces to the Adriatic coast (in order to disarm the Italian army before the Partisans did).  The formation of the unit allowed the Partisans to liberate the lightly guarded city of Tuzla and hold it for 40 days, before the Germans retook it in Operation Ferkel.

658th Eastern Battalion: The 658th Eastern Battalion (German: "Ost Bataillon 658" ) was an Eastern Front World War II military unit of the Wehrmacht composed of Estonians.  It was formed on 23 October 1942 from "Estnische Sicherungs-Abteilung 181" by the German 18th Army and fought in Northern Russia.  In June 1944 it was dissolved and its personnel used to form the "47th Waffen-Grenadier Regiment 2nd Battalion" of the 20th Waffen Grenadier Division of the SS (1st Estonian).

Lim-Sandžak Chetnik Detachment: The Lim-Sandžak Chetnik Detachment (Serbian: Лимско—Санџачки Четнички Одред ) was a military unit of Chetniks that was established in northern Montenegro and Sandžak at the end of June 1942, during World War II.  In August 1942, it was commanded by Pavle Đurišić, and was the largest and the most elite military unit of Draža Mihailović at that time.

Pattern 1908 and 1912 cavalry swords: The 1908 Pattern Cavalry Trooper's Sword (and the 1912 Pattern, the equivalent for officers) was the last service sword issued to the cavalry of the British Army.  It has been called the most effective cavalry sword ever designed, although ironically its introduction occurred as swords finally became obsolete as military weapons.  In use, it, like other thrust-based cavalry swords, is best described as a one-handed lance, due to its complete lack of utility for anything but the charge.  In fact, the closely related US Model 1913 Cavalry Saber was issued with only a saddle scabbard, as it was not considered to be of much use to a dismounted cavalryman.  Colonial troops, who could expect to engage in melee combat with opposing cavalry frequently carried cut and thrust swords either instead of, or in addition to the P1908/1912.

Model 1913 Cavalry Saber: The Model 1913 Cavalry Saber, commonly referred to as the Patton Saber, was a cavalry saber designed for the U.S. Army by Second Lieutenant (later General) George S. Patton in 1913.  Patton suggested the revision from a curved sword and edge and cutting technique to a thrusting style of attack, following his extensive training in France.

5th Krajina (Kozara) Assault Brigade: The 5th Krajina (Kozara) Assault Brigade was a World War II military unit of the Yugoslav Partisans.  It was formed on September 22, 1942, at Palež on the Kozara mountain out of the 2nd 'Mladen Stojanović' Partisan Detachment.  On the day of the brigade was formed it had around 1,100 soldiers armed with 940 rifles and 45 light machine-guns.

Hawley Products Company: Hawley Products Company is a manufacturer of loudspeaker components.  The company is the oldest manufacturer of loudspeaker diaphragms in the world.  Historically, the company produced a variety of products composed of fibrous or plastic materials, including helmets, globes, microwave trays, automotive components, suitcases, and furniture.  Most notably, the company is remembered for its World War II military helmets and helmet liners used by soldiers in the United States Army, Marines, and Navy.  Hawley Products is the original designer of the M1 steel helmet liner.  The company is also one of the two original manufacturers of the M1 steel helmet liner, alongside General Fibre Company.  Additionally, Hawley Products designed and manufactured several versions of the pressed fiber military sun helmet used by the US military during World War II.  The military continued to use this sun helmet throughout most of the 20th century, including Naval personnel during the Persian Gulf War.

Question: Which World War II military unit was commanded by the designer of the Model 1913 Cavalry Saber?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "saber_designer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who designed the saber."
        },
        "rank_at_design": {
          "type": "string",
          "description": "The rank of the designer at the time the saber was designed."
        },
        "later_rank": {
          "type": "string",
          "description": "The later rank achieved by the designer."
        }
      },
      "required": [
        "name",
        "rank_at_design",
        "later_rank"
      ],
      "additionalProperties": false
    },
    "saber_designed": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the cavalry saber designed."
        },
        "design_year": {
          "type": "integer",
          "description": "The year the saber was designed."
        }
      },
      "required": [
        "name",
        "design_year"
      ],
      "additionalProperties": false
    },
    "commanded_military_unit": {
      "type": "object",
      "properties": {
        "unit_name": {
          "type": "string",
          "description": "The name of the military unit commanded by the saber designer."
        },
        "conflict": {
          "type": "string",
          "description": "The conflict during which the unit was commanded."
        }
      },
      "required": [
        "unit_name",
        "conflict"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "saber_designer",
    "saber_designed",
    "commanded_military_unit"
  ],
  "additionalProperties": false
}
