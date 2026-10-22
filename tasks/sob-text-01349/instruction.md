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
Chickamauga Confederate order of battle: The following Confederate States Army units and commanders fought in the Battle of Chickamauga of the American Civil War.  The Union order of battle is listed separately.  Order of battle compiled from the army organization during the campaign.

Battle of Davis's Cross Roads: The Battle of Davis's Cross Roads, also known as the Battle of Dug Gap, was fought September 10–11, 1863, in northwestern Georgia, as part of the Chickamauga Campaign of the American Civil War.  It was more of a series of maneuvers and skirmishes than an actual battle and casualties were negligible.

Battle of Chickamauga: The Battle of Chickamauga, fought on September 18–20, 1863 between Union and Confederate forces in the American Civil War, marked the end of a Union offensive in southeastern Tennessee and northwestern Georgia — the Chickamauga Campaign.  It was the first major battle of the war fought in Georgia, the most significant Union defeat in the Western Theater, and involved the second-highest number of casualties after the Battle of Gettysburg.

Georgia Sharpshooters: The 1st Battalion Georgia Sharpshooters were authorized by an act in April, 1862 by the Confederate Congress, and were formed in Savannah, Georgia.  The 1st Battalion Sharpshooters served at Fort McAllister defending the coast of Georgia in the Battle of Fort McAllister (1863).  They also saw action at the Battle of Jackson, Mississippi as well as the Battle of Chickamauga, and the Chattanooga Campaign.  As Confederate forces moved south, falling back through Atlanta.  The Sharpshooters fought to the end of the war, their last engagement being at the Battle of Bentonville in March, 1865.

23rd Tennessee Infantry Regiment: The 23rd Regiment, Tennessee Infantry was an infantry regiment from Tennessee that served with the Confederate States Army in the American Civil War.  Notable battles fought in include the Battle of Shiloh and the Battle of Chickamauga.

Battle of Aachen: The Battle of Aachen was a major combat action of World War II, fought by American and German forces in and around Aachen, Germany, between 2–21 October 1944.  The city had been incorporated into the Siegfried Line, the main defensive network on Germany's western border; the Allies had hoped to capture it quickly and advance into the industrialized Ruhr Basin.  Although most of Aachen's civilian population was evacuated before the battle began, much of the city was destroyed and both sides suffered heavy losses.  It was one of the largest urban battles fought by U.S. forces in World War II, and the first city on German soil to be captured by the Allies.  The battle ended with a German surrender, but their tenacious defense significantly disrupted Allied plans for the advance into Germany.

13th Tennessee Infantry Regiment: The 13th Regiment, Tennessee Infantry was an infantry regiment from Tennessee that served with the Confederate States Army in the American Civil War.  Notable battles fought in include the Battle of Shiloh and the Battle of Chickamauga.

Chickamauga Union order of battle: The following Union Army units and commanders fought in the Battle of Chickamauga of the American Civil War.  The Confederate order of battle is listed separately.  Order of battle compiled from the army organization during the campaign.

24th Tennessee Infantry Regiment: The 24th Regiment, Tennessee Infantry was an infantry regiment from Tennessee that served with the Confederate States Army in the American Civil War.  Notable battles fought in include the Battle of Shiloh and the Battle of Chickamauga.

Chickamauga Campaign: The Chickamauga Campaign of the American Civil War was a series of battles fought in northwestern Georgia from August 21 to September 20, 1863, between the Union Army of the Cumberland and Confederate Army of Tennessee.  The campaign started successfully for Union commander William S. Rosecrans, with the Union army occupying the vital city of Chattanooga and forcing the Confederates to retreat into northern Georgia.  But a Confederate attack at the Battle of Chickamauga forced Rosecrans to retreat back into Chattanooga and allowed the Confederates to lay siege to the Union forces.

Question: Were both Battle of Chickamauga and Battle of Aachen fought in the same continent?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_comparison": {
      "type": "string",
      "description": "The specific comparison being made in the question."
    },
    "battle_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the first battle."
        },
        "location": {
          "type": "string",
          "description": "Geographic location of the first battle."
        },
        "continent": {
          "type": "string",
          "description": "Continent where the first battle took place."
        }
      },
      "required": [
        "name",
        "location",
        "continent"
      ],
      "additionalProperties": false
    },
    "battle_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the second battle."
        },
        "location": {
          "type": "string",
          "description": "Geographic location of the second battle."
        },
        "continent": {
          "type": "string",
          "description": "Continent where the second battle took place."
        }
      },
      "required": [
        "name",
        "location",
        "continent"
      ],
      "additionalProperties": false
    },
    "same_continent": {
      "type": "boolean",
      "description": "True if both battles were fought on the same continent, false otherwise."
    }
  },
  "required": [
    "question_comparison",
    "battle_1",
    "battle_2",
    "same_continent"
  ],
  "additionalProperties": false
}
