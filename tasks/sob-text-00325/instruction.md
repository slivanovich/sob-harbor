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
Prairie Grove Confederate order of battle: The following Confederate Army units and commanders fought in the Battle of Prairie Grove of the American Civil War on December 7, 1862, in Washington County, Arkansas.  The Union order of battle is listed separately.

First Deep Bottom Confederate order of battle: The following Confederate Army units and commanders fought in the First Battle of Deep Bottom (July 27–29, 1864) of the American Civil War.  The Union order of battle is listed separately.

Second Corinth Confederate order of battle: The following Confederate Army units and commanders fought in the Second Battle of Corinth of the American Civil War on October 3 and 4, 1862, in Corinth, Mississippi.  Order of battle compiled from the army organization during the battle and reports.  The Union order of battle is listed separately.

Battle of Richmond: The Battle of Richmond, Kentucky, fought August 29–30, 1862, was a stunning Confederate victory by Major General Edmund Kirby Smith against Union major general, William "Bull" Nelson's forces, defending the town.  It was the first major battle in the Kentucky Campaign.  The battle took place on and around what is now the grounds of the Blue Grass Army Depot, outside Richmond, Kentucky.

Fort Donelson Confederate order of battle: The following Confederate Army units and commanders fought in the Battle of Fort Donelson of the American Civil War.  Order of battle compiled from the army organization, and the reports.  The Union order of battle is listed separately.

Mill Springs Confederate order of battle: The following Confederate Army units and commanders fought in the Battle of Mill Springs of the American Civil War on January 19, 1862 near present-day Nancy, Kentucky.  The Union order of battle is listed separately.

Richmond Confederate order of battle: The following Confederate Army units and commanders fought in the Battle of Richmond of the American Civil War.  The Union order of battle is listed separately.

Wilson's Creek Confederate order of battle: The following Confederate States Army units and commanders fought in the Battle of Wilson's Creek of the American Civil War, fought on August 10, 1861 near Springfield, Missouri.  Though identified with the Confederates, the Missouri State Guard were technically an independent army, as Missouri had not yet seceded, and were not folded into the Confederate Army of the West until March 17, 1862.  Though identified with the Confederates, the Arkansas State Trooops were technically not yet Confederate troops.  Arkansas had seceded on XX and be recognized as a Confederate States, but Brigadier General Nichols Pearce's troops had not been transferred from the State of Arkansas to the Confederate Government and had not been sworn into Confederate Service.  After the battle, Pearce's troops voted to disband rather than enter Confederate Service.

Champion Hill Confederate order of battle: The following Confederate Army units and commanders fought in the Battle of Champion Hill of the American Civil War.  The Union order of battle is listed separately.  Order of battle compiled from the army organization, returns of casualties and reports.

6th Florida Infantry Regiment: The 6th Florida Infantry Regiment' was raised by the Confederate State of Florida for service to the Provisional Army of the Confederate States of America.  Organized and released from state service in mid-April 1862, the regiment would leave the state in mid-June, 1862.  It was assigned from June through August 1862 to the Army of East Tennessee (Department of East Tennessee), General Edmund Kirby Smith commanding.  The Army of East Tennessee was redesignated as the Confederate Army of Kentucky on August 25, 1862, when General Smith led it into eastern Kentucky during the Confederate Heartland Offensive.  On November 20, 1862, the Army of Mississippi, General Braxton Bragg commanding, and the Army of Kentucky, General E. Kirby Smith commanding, became the Army of Tennessee.  General Bragg assumed command, and General Smith was reassigned to the Department of East Tennessee.  The 6th Florida would remain assigned to the Army of Tennessee until its surrender at Bentonville, North Carolina on April 26, 1865.

Question: The following Confederate Army units and commanders fought in which battle fought August 29–30, 1862, was a stunning Confederate victory by Major General Edmund Kirby Smith against Union major general, William "Bull" Nelson's forces, defending the town?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "battle_name": {
      "type": "string",
      "description": "The name of the battle."
    },
    "date_string": {
      "type": "string",
      "description": "The date or date range when the battle was fought."
    },
    "outcome": {
      "type": "string",
      "description": "The outcome of the battle, indicating the victorious side."
    },
    "confederate_commander": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Confederate commander."
        },
        "rank": {
          "type": "string",
          "description": "The rank of the Confederate commander."
        }
      },
      "required": [
        "name",
        "rank"
      ],
      "additionalProperties": false
    },
    "union_commander": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Union commander."
        },
        "rank": {
          "type": "string",
          "description": "The rank of the Union commander."
        }
      },
      "required": [
        "name",
        "rank"
      ],
      "additionalProperties": false
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the battle took place."
        },
        "state": {
          "type": "string",
          "description": "The state where the battle took place."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "campaign_significance": {
      "type": "string",
      "description": "The significance of the battle within its campaign."
    }
  },
  "required": [
    "battle_name",
    "date_string",
    "outcome",
    "confederate_commander",
    "union_commander",
    "location"
  ],
  "additionalProperties": false
}
