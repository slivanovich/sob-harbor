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
Impacto: "Impacto" (English: Impact ) is the first single by Puerto Rican reggaeton performer Daddy Yankee from his fifth studio album "".  It was released on April 12, 2007 by El Cartel Records.  "Impacto" was nominated for Song of the Year at the Premios Lo Nuestro 2008.  The official remix features American singer Fergie.

Cypher Zero: Cypher Zero (whose given name is Michael Aaron Woldow) is an entertainer and entrepreneur.  Zero began his career as a performer in 1995.  Zero has also used the aliases Sebastian Perluna and Sebastian Dupree.

Emanuel (name): Emanuel, Emmanuel, Emmanuil or Immanuel is a masculine given name or surname derived from the Hebrew name ("Immanuel", meaning ′God is with us′).  The name is common to both Jewish and Christian naming traditions.  The middle Hebrew letter "mem" is a gemination giving rise to the co-existence of single "m" and double "mm" (romanized) transliterations in many languages.  The name has many variant spellings, including Emanuele in Italy, Imanol in Basque and Manuel in Portuguese and Spanish.

Kyung-jae: Kyung-jae, Gyeong-jae, and Kyoung-jae are various Latin-alphabet spellings of a single Korean male given name.  The meaning differs based on the hanja with which the name is written.  There are 54 hanja with the reading "kyung" and 20 hanja with the reading "jae" on the South Korean government's official list of hanja which may be used in given names.

José María: José María (abbreviated José Mª) is a Spanish language male given name, usually considered a single given name rather than two names, and is a combination of the Spanish names of Joseph and Mary, the parents of Jesus Christ.  The separate names "José" for males and "María" for females also exist in the Spanish language.  They can also combine in the inverse order forming the "female" name "María José" (M.ª José); that is, the gender of the compound names "José María" and "María José" is determined by their first component.  The name "José María" is colloquially shortened to "José Mari", "Josema" or replaced by the hypocoristic forms "Chema" or "Chemari".

Areum (name): Areum, also spelled Ah-reum, is a Korean feminine given name.  Unlike most Korean given names, which are composed of two single-syllable Sino-Korean morphemes each written with one hanja, Areum is an indigenous Korean name (고유어이름 ), a single two-syllable word meaning "beauty".  It is one of a number of such native names, along with others such as Ha-neul ("sky"), Seul-ki ("wisdom"), and Sora ("conch shell") that have become more popular in South Korea in recent decades.

Hitomi (given name): Hitomi (ヒトミ, ひとみ ) is a feminine Japanese given name.  It is often written with the single kanji 瞳 (Japanese for "eye") or the two kanji 仁美.  It can also come from 智 (hito) meaning "wisdom, intellect" and 美 (mi) meaning "beautiful".  Individuals may alternatively write the name using the hiragana as ひとみ.  The singer hitomi writes her stage name using the Latin alphabet.

Daddy Yankee: Ramón Luis Ayala Rodríguez (born February 3, 1977), known by his stage name Daddy Yankee, is a Puerto Rican singer, songwriter, rapper, actor and record producer.  Ayala was born in Río Piedras, Puerto Rico, and was raised in the neighborhood of Villa Kennedy Housing Projects.  According to the "New York Times", he is known as the "King of Reggaetón" by music critics and fans alike.

Sora (Korean given name): So-ra is a Korean feminine given name.  Unlike most Korean given names, which are composed of two single-syllable Sino-Korean morphemes each written with one hanja, So-ra is an indigenous Korean name, a single two-syllable word meaning "conch shell".  It is one of a number of such native names (called 고유어 이름) that have become more popular in South Korea in recent decades.  In some cases, however, parents also choose to register hanja to represent the name, picking them solely for their pronunciation (for example, 曙羅 , with hanja meaning "sunlight" and "net", respectively).  There are 45 hanja with the reading "so" and 14 hanja with the reading "ra" on the South Korean government's official list of hanja which may used in given names.

Bora (Korean name): Bora is a Korean feminine given name.  Unlike most Korean given names, which are composed of two single-syllable Sino-Korean morphemes each written with one hanja, Bora is an indigenous Korean name (고유어이름 ): a single two-syllable word meaning "purple".  It is one of a number of such native names, along with others such as Ha-neul, ("sky"), Seul-ki ("wisdom"), and Sora ("conch shell"), that have become more popular in South Korea in recent decades.  In some cases, however, parents also choose to register hanja to represent the name, picking them solely for their pronunciation (for example, 珤羅 , with hanja meaning "jewel" and "net", respectively).  There are 18 hanja with the reading "bo" and 14 hanja with the reading "ra" on the South Korean government's official list of hanja which may used in given names.

Question: What is the given name of the performer who released the single Impacto ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "performer_stage_name": {
      "type": "string",
      "description": "The stage name of the performer."
    },
    "performer_given_name": {
      "type": "string",
      "description": "The given name of the performer."
    },
    "single_name": {
      "type": "string",
      "description": "The name of the single released by the performer."
    }
  },
  "required": [
    "performer_stage_name",
    "performer_given_name",
    "single_name"
  ],
  "additionalProperties": false
}
