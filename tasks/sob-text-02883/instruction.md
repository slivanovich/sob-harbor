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
Yushania alpina: Yushania alpina or African alpine bamboo is a perennial bamboo of the family Poaceae and the genus "Yushania" It can be found growing in dense but not large stands on the mountains and volcanoes surrounding the East African Rift between the altitudes of 2,500 meters (8,200 feet) and 3,300 meters (11,000 feet).

Eleutherococcus: Eleutherococcus is a genus of 38 species of thorny shrubs and trees in the family Araliaceae.  They are native to eastern Asia, from southeast Siberia and Japan to the Philippines and Vietnam.  18 species come from China, from central to western parts.

Eleutherococcus brachypus: Eleutherococcus brachypus (Chinese: 短柄五加 "duan bing wu jia") is a species of flowering plant in the family Araliaceae.  It is endemic to China, where it occurs in scrub fields and roadsides on mountain slopes in Gansu, Ningxia, and Shaanxi provinces.

Yushania: Yushania is a genus of bamboo in the grass family.

Eleutherococcus senticosus: Eleutherococcus senticosus is a species of small, woody shrub in the family Araliaceae native to Northeastern Asia.  It is often colloquially referred to as Siberian ginseng, eleuthero or ciwujia.  "E. senticosus" has a history of use in traditional Chinese medicine where it is known as "cì wǔ jiā" (刺五加).  In regard to the species's scientific name, "Eleutherococcus" (from Greek) means "free-berried," and "senticosus", from the Latin word "sentis" (thorn-bush, briar) is an adjective meaning "thorny" or "full of briers or thorns."

Eleutherococcus setulosus: Eleutherococcus setulosus is a plant species in the family Araliaceae.  It is native to the Chinese provinces of Anhui, Gansu, Sichuan and Zhejiang.

Eleutherococcus gracilistylus: Eleutherococcus gracilistylus, also known as Acanthopanax gracilistylus, is deciduous plant with dark blue berries.  It is considered a medicinal herb with significant effects.  A widely used Chinese plant, it is in the Araliaceae family, and mainly grows at an altitude of around 3000m.  It is also found in Gaoligongshan Nature Reserve in Yunnan Province, China.  It is widely distributed in China and has been used as a life-saving medicine against severe cases of paralysis, arthritis and liver disease; several experiments were carried out in 2003.  The leaves are 350g.

Chengiopanax sciadophylloides: Chengiopanax sciadophylloides is a flowering tree in the family Araliaceae native to Japan.  Previously included in the genus "Eleutherococcus", it is distinguished from other members of that genus by not having spines or prickles and ITS sequence data confirmed the separation.

Question: Are Yushania and Eleutherococcus in the same family?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genus_1_name": {
      "type": "string",
      "description": "The name of the first genus being compared."
    },
    "genus_1_family": {
      "type": "string",
      "description": "The family of the first genus."
    },
    "genus_2_name": {
      "type": "string",
      "description": "The name of the second genus being compared."
    },
    "genus_2_family": {
      "type": "string",
      "description": "The family of the second genus."
    },
    "are_in_same_family": {
      "type": "boolean",
      "description": "True if both genera belong to the same family, false otherwise."
    }
  },
  "required": [
    "genus_1_name",
    "genus_1_family",
    "genus_2_name",
    "genus_2_family",
    "are_in_same_family"
  ],
  "additionalProperties": false
}
