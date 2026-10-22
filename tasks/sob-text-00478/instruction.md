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
Mundari language: Mundari (Muɳɖa) is a Munda language of the Austroasiatic language family spoken by the Munda people, and is closely related to Santali and Ho.  Mundari is primarily spoken by Munda tribal people in eastern India, Bangladesh, and Nepal.  Mundari Bani, a script specifically to write Mundari, was invented by Rohidas Singh Nag.  Ho and Mundari are ethnically and linguistically close but the regional identities of the speakers are distinct.  Ho and Mundari have been called two sister languages by some researchers and scholars and the Ho is a sister tribe of the "'Munda tribe"'.  It is believed that Ho speakers were originally "Mundas".  In the course of time, from the fourteenth to seventeenth century A.D., they separated for unknown reasons and migrated from the Bandhgaon-Khunti region to the Singhbhum or Kolhan region.  Therefore, Ho and Mundari are linguistically similar.

Chuukic languages: Chuukic ( ), also rendered Trukic ( ) historically, is a subgroup of the Chuukic–Pohnpeic family of the Austronesian language family.  The languages are primarily spoken in Chuuk State and Yap State of the Federated States of Micronesia.

New Orleans English: New Orleans English is American English native to the city of New Orleans and its metropolitan area.  Native English speakers of the region actually speak a number of varieties, including: the variety most recently brought in and spreading since the 20th century among white communities of the South in general (Southern U.S. English); the variety primarily spoken by black residents (African American Vernacular English); the variety spoken by Cajuns in southern Louisiana (Cajun English); the variety traditionally spoken by affluent white residents of the city's Uptown and Garden District; and the variety traditionally spoken by lower middle- and working-class white residents of Eastern New Orleans, particularly the Ninth Ward (sometimes known, since at least the 1980s, as Yat).  However, only the last two varieties are unique to New Orleans and are typically those referred to in the academic research as "New Orleans English."  These two varieties specific to New Orleans likely developed around the turn of the nineteenth century and most noticeably combine speech features commonly associated with both New York City English and, to a lesser extent, Southern U.S. English.  The noticeably New York-like characteristics include the NYC short-"a" split system (so that "mad" and "map", for example, do not have the same vowel), the diphthongizing of to [ɔə] or [ɔʷ] , non-rhoticity, "th"-stopping (so that, for example, "those" may merge with "doze"), and the recently disappearing coil–curl merger.  Noticeably Southern characteristics include the fronting of and possible monophthongization of (just these features, plus non-rhoticity, often characterize the Uptown accent).

Indo-Aryan languages: The Indo-Aryan or Indic languages are the dominant language family of the Indian subcontinent.  They constitute a branch of the Indo-Iranian languages, itself a branch of the Indo-European language family.  Indo-Aryan speakers form about one-half of all Indo-European speakers (about 1.5 of 3 billion), and more than half of all Indo-European languages recognized by "Ethnologue".  While the languages are primarily spoken in South Asia, pockets of Indo-Aryan languages are found to be spoken in Europe and the Middle East.

Suki language: Suki is a Gogodala-Suki language spoken by about 3500 people several miles inland along the Fly River in southwestern Papua New Guinea.  Suki is primarily spoken in six villages of the Western Province: Gwaku, Iwewi, Ewe, Gwibaku, Duru, and Isala.  Suki is genetically related to the three other languages of the Gogodala–Suki stock, Gogodala, Ali, and Walua, but is considered a family-level isolate within this group.  As with many Papuan languages, there are very few published materials on Suki.  The literacy rate in Suki is 5-15%, English is the language of instruction in schools and Hiri Motu is also spoken.

Tshangla language: Tshangla (/tsʰaŋla/ ), also called Sharchop, is a Sino-Tibetan language of the Bodish branch closely related to the Tibetic languages and much of its vocabulary derives from Classical Tibetan.  Tshangla is primarily spoken in Eastern Bhutan and acts as a lingua franca in the country particularly among Sharchop/Tshangla communities, it is also spoken in Arunachal Pradesh, India and Tibet.  Tshangla is the principal pre-Tibetan (pre-Dzongkha) language of Bhutan.

Pohnpeic languages: Pohnpeic, also rendered Ponapeic, is a subgroup of the Chuukic–Pohnpeic branch of Micronesian in the Austronesian language family.  The languages are primarily spoken in Pohnpei State of the Federated States of Micronesia.

Gulf of Morbihan: The Gulf of Morbihan is a natural harbour on the coast of the Département of Morbihan in the south of Brittany, France.  This English name is taken from the French version: "le golfe du Morbihan".  It is more accurately called 'the Morbihan' directly from its Breton name which is "Ar Mor Bihan", meaning 'the little sea' (Compare the Welsh "y môr bychan"), as opposed to the Atlantic Ocean outside, ("Ar Mor Bras").  Legend says that there are as many islands in the Gulf as there are days of the year.  However, this is untrue and the gulf has about 40, depending on the tide.  Many islands are private property, except the largest two, l'Île-aux-Moines and l'Île-d'Arz.

Federated States of Micronesia: The Federated States of Micronesia ( ; abbreviated FSM and also known simply as Micronesia) is an independent sovereign island nation and a United States associated state consisting of four states from west to east, Yap, Chuuk, Pohnpei and Kosraethat are spread across the Western Pacific Ocean.  Together, the states comprise around 607 islands (a combined land area of approximately 702 km2 ) that cover a longitudinal distance of almost 2700 km just north of the equator.  They lie northeast of New Guinea, south of Guam and the Marianas, west of Nauru and the Marshall Islands, east of Palau and the Philippines, about 2900 km north of eastern Australia and some 4000 km southwest of the main islands of Hawaii.

Austric languages: Austric is a large hypothetical grouping of languages primarily spoken in Southeast Asia, the Pacific, and the eastern Indian subcontinent.  It includes the Austronesian language family of Taiwan, the Malay Archipelago, Pacific Islands, and Madagascar, as well as the Austroasiatic language family of mainland Southeast Asia, Eastern India, Nepal and Bangladesh.  The hypothesis of a genetic relationship between these two language families is not widely accepted among linguists.

Question:  Pohnpeic languages are primarily spoken in a nation that contains how many islands?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "language_family": {
      "type": "string",
      "description": "The broader language family to which Pohnpeic belongs."
    },
    "primary_speaking_location": {
      "type": "object",
      "properties": {
        "state": {
          "type": "string",
          "description": "The specific state where the language is primarily spoken."
        },
        "nation": {
          "type": "string",
          "description": "The nation where the language is primarily spoken."
        }
      },
      "required": [
        "state",
        "nation"
      ],
      "additionalProperties": false
    },
    "nation_details": {
      "type": "object",
      "properties": {
        "total_islands": {
          "type": "integer",
          "description": "The total number of islands in the specified nation."
        },
        "land_area_km2": {
          "type": "number",
          "description": "The combined land area of the nation's islands in square kilometers."
        }
      },
      "required": [
        "total_islands"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "language_family",
    "primary_speaking_location",
    "nation_details"
  ],
  "additionalProperties": false
}
