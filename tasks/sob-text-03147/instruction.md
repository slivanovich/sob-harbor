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
Yangra: Yangra (Ganesh I) is the highest peak of the Ganesh Himal,

Kushan Pass: The Kushan Pass or Kaoshan Pass (el.  about 4,370 m or 14,340 ft) is a mountain pass just west of the famous Salang Pass (3,878 m. or 12,723 ft.) in the Hindu Kush mountain range of northern Afghanistan.  These two passes provided the most direct, if difficult, routes across the imposing east-west wall of the Hindu Kush mountains which divide northern Afghanistan or Tokharistan from Kabul province, which is closely connected to southern Afghanistan and Pakistan.  Nowadays, the Salang tunnel constructed by the Soviets in the 1960s, and the paved road through it make it by far the easiest route through the Hindu Kush Mountains.

Istor-o-Nal: Istor-o-Nal or इस्तोर-ओ-नल is the third highest mountain in the Hindu Kush, in the Chitral District of the North-West Frontier Province of Pakistan.  It is the 68th highest independent peak in the world.  It crowns a massif with eleven peaks of elevation more than 7000 m .  The peak is located a few kilometres northeast of Tirich Mir (the highest mountain in the Hindu Kush), across the Tirich Glacier.  Because Istor-o-Nal is behind the higher peak of Tirich Mir from many viewpoints, it is not easily visible and therefore not well known.

Mir Samir: Mir Samir, also called Mir Simir or Simirdar, is a mountain in the Hindu Kush in Afghanistan.  It was first climbed in 1959 despite a local tradition that it was unclimbable.  The English traveller Eric Newby and the diplomat Hugh Carless attempted to climb Mir Samir in 1956, as described in the humorous book "A Short Walk in the Hindu Kush".

2005 Hindu Kush earthquake: The 2005 Hindu Kush earthquake hit northeastern Afghanistan with a magnitude of 6.5 on December 12 at 21:47 (UTC).  According to the United States Geological Survey's ShakeMap and Did You Feel It?  products, the maximum Mercalli intensity was VI ("Strong") at Chitral.  Five people were killed in the Hindu Kush region and landslides blocked several roads near Bagh, Kashmir.  The earthquake occurred some 65 miles away from Faizabad, a city in the Hindu Kush mountains, but it could be felt in many neighboring areas.  It could even be felt about 200 miles away in Islamabad, Pakistan.  The quake was strong enough to trigger panic among survivors of October's devastating earthquake, who came out from their makeshift shelters in freezing temperatures.  Although magnitude-6 earthquakes typically cause severe damage, this quake caused relatively little due to the fact that it occurred deep underground (about 140 miles).

Buni Zom: The Buni Zom group is a prominent mountain area of Chitral, in the Hindu Raj range of Pakistan.  Buni Zom (main) is the highest peak of the group with an elevation of 6542 m .  It is located about 50 km (30 mi) northeast of the town of Chitral, and about 50 km (30 mi) east of Tirich Mir (7,708 m), the highest peak in the Hindu Kush.

Noshaq: Noshaq (also called Nowshak or Nōshākh; Urdu/Persian/Pashto: نوشاخ‎ ) is the highest peak in Afghanistan and the second highest peak in the Hindu Kush Range (after Tirich Mir) at 7492 m .  It lies on the border between Badakhshan Province in Afghanistan and Chitral District, Khyber Pakhtunkhwa, Pakistan, and is the world's westernmost 7,000 meter massif.

Tirich Mir: Tirich Mir (Khowar/Urdu: ‎ ) (alternatively Terich Mir, Terichmir and Turch Mir) is the highest mountain of the Hindu Kush range, and the highest mountain in the world outside of the Himalayas-Karakoram range, located in Chitral District of Pakistan.  The mountain was first climbed in 1950 by a Norwegian expedition consisting of Arne Næss, P. Kvernberg, H. Berg, and Tony Streather.  Tirich Mir overlooks Chitral town, and can be easily seen from the main bazaar.

Aconcagua: Aconcagua (] ) is the highest mountain outside Asia, at 6961 m , and by extension the highest point in both the Western Hemisphere and the Southern Hemisphere.  It is located in the Andes mountain range, in the Mendoza Province, Argentina, and lies 112 kilometres (70 mi) northwest of its capital, the city of Mendoza.  The summit is also located about five kilometres from San Juan Province and 15 kilometres from the international border with Chile.  The mountain itself lies entirely within Argentina and immediately east of Argentina's border with Chile.  Its nearest higher neighbor is Tirich Mir in the Hindu Kush, 16520 km away.  It is one of the Seven Summits.

Kuh-e Bandaka: Kuh-e Bandaka (Pashto: کوه بندکا) or Kohe Bandaka, Koh-i Bandaka, Bandako, or incorrectly "Koh-i-Bandakor") is one of the highest peaks of the Hindu Kush mountain range in northeastern Afghanistan.  It is northeast of Kabul and west of Chitral.  Separated by a relatively low pass from the core of the Hindu Kush, it is the highest mountain entirely within Afghanistan, and the most topographically prominent peak in all of Afghanistan.

Question: Both Yangra and Tirich Mir are very tall points but which is the highest peak of the Hindu Kush range?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "highest_peak_name": {
      "type": "string",
      "description": "The name of the highest peak in the specified range."
    },
    "highest_peak_range": {
      "type": "string",
      "description": "The mountain range to which the highest peak belongs."
    },
    "comparison_peaks": {
      "type": "array",
      "description": "Details of the peaks mentioned in the question for comparison.",
      "items": {
        "type": "object",
        "properties": {
          "peak_name": {
            "type": "string",
            "description": "The name of the peak."
          },
          "mountain_range": {
            "type": "string",
            "description": "The mountain range this peak belongs to."
          }
        },
        "required": [
          "peak_name",
          "mountain_range"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation derived from the context supporting the answer."
    }
  },
  "required": [
    "highest_peak_name",
    "highest_peak_range",
    "comparison_peaks",
    "reasoning"
  ],
  "additionalProperties": false
}
