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
Bangsamoro Assembly: The Bangsamoro Parliament (also known as the Bangsamoro Assembly) will be the legislature of Bangsamoro Autonomous Region, a proposed autonomous region of the Philippines.  The legislature will composed of at least 50 directly-elected members, who in turn are set to appoint a chief minister from among the members of the legislature.  The chief minister will then be tasked with appointing a deputy chief minister and to select the members of the Bangsamoro Cabinet.

List of political parties in Bougainville: Political parties in Bougainville lists political parties in the Autonomous Region of Bougainville, an autonomous region within Papua New Guinea.  The following political parties operate only within Bougainville.

Karakoram Province: Karakoram Province is a proposed autonomous region for the Shi'a Islam-majority areas of northern Pakistan.  According to the movement for autonomy in the 1980s, it was to span most of the Karakoram mountain range, covering Gilgit District, Kurram Agency and the Shia majority areas of Punjab and the North-West Frontier Province.  However, the Zia regime violently opposed any Shi'a movement for autonomy.

Autonomous Region in Muslim Mindanao: The Autonomous Region in Muslim Mindanao (Filipino: "Awtonomong Rehiyon sa Muslim Mindanao" , Arabic: ‎ ‎ "Al-ḥukm adh-dhātiyy al-'aqlīmiyy limuslimiyy mindanāu"; abbreviated ARMM) is an autonomous region of the Philippines, located in the Mindanao island group of the Philippines, that consists of five predominantly Muslim provinces: Basilan (except Isabela City), Lanao del Sur, Maguindanao, Sulu and Tawi-Tawi.  It is the only region that has its own government.  The region's "de facto" seat of government is Cotabato City, although this self-governing city is outside of its jurisdiction.

Tibetan independence movement: The Tibetan independence movement is a movement for the independence of Tibet and the political separation of Tibet from China.  It is principally led by the Tibetan diaspora in countries like India and the United States, and by celebrities and Tibetan Buddhists in the United States and Europe.  The movement is not supported by the 14th Dalai Lama, who although having advocated it from 1961 to the late 1970s, proposed a sort of high-level autonomy in a speech in Strasbourg in 1988, and has since then restricted his position to either autonomy for the Tibetan people in the Tibet Autonomous Region "within" China, or extending the area of the autonomy to include parts of neighboring Chinese provinces inhabited by Tibetans.

Ezekiel Massat: Ezekiel Massat is a Bougainvillean lawyer and politician.  Massat was appointed the Vice President of the Autonomous Region of Bougainville by President James Tanis on January 19, 2009.  Bougainville is an autonomous region within Papua New Guinea.

Gwangju Student Independence Movement: The Gwangju Student Independence Movement (Hangul: 광주 학생 독립 운동 Hanja:光州學生獨立運動), or Gwangju Student Movement was a Korean independence movement in Gwangju against the 22 August 1910 to 15 August 1945 Japanese rule of Korea.  The Gwangju Student Independence Movement took place in October and November 1929.  It is considered the second-most important Korean independence movement in the period of the Japanese occupation, with the March 1st Movement considered the most important.  The Gwangju Student Independence Movement spread out throughout the Korean Peninsula.

Bangsamoro Basic Law: The Bangsamoro Basic Law, often referred to by the acronym "BBL" (Filipino: "Batayang Batas para sa Rehiyong Awtonomo ng Bangsamoro" ), was a bill deliberated upon by the 16th Congress of the Philippines which sought to establishe a proposed new autonomous political entity known as the Bangsamoro Autonomous Region, replacing the current Autonomous Region in Muslim Mindanao (ARMM).

Bangsamoro peace process: In the late 1960s, an independence movement was founded in Mindanao, the Philippines to separate the Muslim majority-Moro areas from the rest of the Philippines.  The area is now called the Bangsamoro.

Bangsamoro (political entity): The Bangsamoro Autonomous Region (Filipino: "Rehiyong Awtonomo ng Bangsamoro" Arabic: ‎ ‎ "Munṭiqah banjisāmūrū dhātiyyah al-ḥukm") is a proposed autonomous region within the Philippines.  The proposal is part of the Framework Agreement on the Bangsamoro, a preliminary peace agreement signed between the Moro Islamic Liberation Front and the government.  When Rodrigo Duterte won as President of the Philippines in 2016, his administration announced that the Bangsamoro Basic Law bill would shelved instead of being taken up by the 17th Congress of the Philippines.

Question: The proposed autonomous region within the Philippines, originating from an independence movement to seperate the Muslim majority-Moro areas, is now called what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "region_name": {
      "type": "string",
      "description": "The name of the proposed autonomous region."
    },
    "region_status": {
      "type": "string",
      "description": "The current status of the region (e.g., proposed, existing)."
    },
    "parent_country": {
      "type": "string",
      "description": "The country within which the region is proposed or located."
    },
    "origin_of_proposal": {
      "type": "object",
      "properties": {
        "movement_type": {
          "type": "string",
          "description": "The type of movement that led to the proposal."
        },
        "movement_goal": {
          "type": "string",
          "description": "The objective of the originating movement."
        },
        "movement_founding_period": {
          "type": "string",
          "description": "The period when the movement was founded."
        }
      },
      "required": [
        "movement_type",
        "movement_goal",
        "movement_founding_period"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "region_name",
    "region_status",
    "parent_country",
    "origin_of_proposal"
  ],
  "additionalProperties": false
}
