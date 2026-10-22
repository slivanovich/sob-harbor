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
Battle of Pusan Perimeter: The Battle of Pusan Perimeter was a large-scale battle between United Nations and North Korean forces lasting from August 4 to September 18, 1950.  It was one of the first major engagements of the Korean War.  An army of 140,000 UN troops, having been pushed to the brink of defeat, were rallied to make a final stand against the invading North Korean army, 98,000 men strong.

Battle of Peleliu: The Battle of Peleliu, codenamed Operation Stalemate II by the United States military, was fought between the U.S. and the Empire of Japan during the Mariana & Palau Campaign of World War II, from September to November 1944, on the island of Peleliu.

Battle of the Bowling Alley: In the Battle of the Bowling Alley (August 12–25, 1950), United Nations (UN) forces defeated North Korean forces early in the Korean War near the city of Taegu, South Korea.  The battle took place in a narrow valley, dubbed the "Bowling Alley", which was north of Taegu.  It followed a week of fighting between the Korean People's Army (KPA) 13th Division and the Republic of Korea Army's (ROK) 1st Division along the latter's last defensible line in the hills north of the city.  Reinforcements, including the US Army's 27th and 23rd Infantry Regiments were committed to bolster the South Koreans' defenses.  This battle and several others were smaller engagements of the Battle of Pusan Perimeter.

Battle of P'ohang-dong: The Battle of P'ohang-dong was an engagement between the United Nations and North Korean forces early in the Korean War, with fighting continuing from 5–20 August 1950 around the town of P'ohang-dong, South Korea.  It was a part of the Battle of Pusan Perimeter, and was one of several large engagements fought simultaneously.  The battle ended in a victory for the United Nations after their forces were able to drive off an attempted offensive by three North Korean divisions in the mountainous eastern coast of the country.

15th Division (North Korea): The 15th Infantry Division was a military formation of the Korean People's Army during the 20th Century.  The division fought in the 1950 Korean War; it took part in the North Korean advance from Seoul to Taejon, and fought in the Battle of Pusan Perimeter.  The 15th Division fought along the eastern coast, above Pusan, eventually being annihilated.

First Battle of Naktong Bulge: The First Battle of Naktong Bulge was an engagement between United States and North Korean forces early in the Korean War from August 5–19, 1950 in the vicinity of Yongsan (Yeongsan, Changnyeong county) and the Naktong River in South Korea.  It was a part of the Battle of Pusan Perimeter, and was one of several large engagements fought simultaneously.  The battle ended in a victory for the United States after large numbers of US reinforcements destroyed an attacking North Korean division.

Battle of Pusan Perimeter logistics: Logistics in the Battle of Pusan Perimeter (August 4 – September 15, 1950) during the Korean War played a decisive role in the battle.  Efficient logistics, the management of personnel and materiel, supported United Nations (UN) supply lines while the North Koreans' routes of supply were steadily reduced and cut off.  UN logistics improved throughout the Battle of Inchon and the defeat of the North Korean army at Pusan.

Battle of Taegu: The Battle of Taegu was an engagement between UN and North Korean forces early in the Korean War, with fighting continuing from August 5–20, 1950 around the city of Taegu, South Korea.  It was a part of the Battle of Pusan Perimeter, and was one of several large engagements fought simultaneously.  The battle ended in a victory for the United Nations after their forces were able to drive off an offensive by North Korean divisions attempting to cross the Naktong River and assault the city.

Battle of Battle Mountain: The Battle of Battle Mountain was an engagement between United Nations (UN) and North Korean (NK) forces early in the Korean War from August 15 to September 19, 1950, on and around the Sobuk-san mountain area in South Korea.  It was one of several large engagements fought simultaneously during the Battle of Pusan Perimeter.  The battle ended in a victory for the UN after large numbers of United States (US) and Republic of Korea (ROK) troops were able to prevent a North Korean division from capturing the mountain area.

Battle of Ka-san: The Battle of Ka-san was an engagement between United Nations (UN) and North Korean forces early in the Korean War from September 1 to September 15, 1950, in the vicinity of Ka-san in South Korea.  It was a part of the Battle of Pusan Perimeter, and was one of several large engagements fought simultaneously.  The battle ended in a victory for the United Nations after large numbers of United States (US) and Republic of Korea (ROK) troops repelled a strong North Korean attack.

Question: Did the Battle of Pusan Perimeter or the Battle of Peleliu happen first?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "compared_battles": {
      "type": "array",
      "description": "Details of the battles being compared.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the battle."
          },
          "start_date": {
            "type": "string",
            "description": "The start date of the battle."
          }
        },
        "required": [
          "name",
          "start_date"
        ],
        "additionalProperties": false
      }
    },
    "earlier_battle": {
      "type": "object",
      "description": "Details of the battle that occurred first.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the earlier battle."
        },
        "start_date": {
          "type": "string",
          "description": "The start date of the earlier battle."
        }
      },
      "required": [
        "name",
        "start_date"
      ],
      "additionalProperties": false
    },
    "later_battle": {
      "type": "object",
      "description": "Details of the battle that occurred second.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the later battle."
        },
        "start_date": {
          "type": "string",
          "description": "The start date of the later battle."
        }
      },
      "required": [
        "name",
        "start_date"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "A direct answer to the question stating which battle happened first."
    }
  },
  "required": [
    "compared_battles",
    "earlier_battle",
    "later_battle",
    "answer"
  ],
  "additionalProperties": false
}
