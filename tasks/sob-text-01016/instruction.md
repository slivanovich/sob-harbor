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
Santería: Santería, also known as Regla de Ochá, La Regla de Ifá, or Lucumi, is an Afro-American religion of Caribbean origin that developed in the Spanish Empire among West African descendants.  "Santeria" is a Spanish word that means the "worship of saints".  Santería is influenced by and syncretized with Roman Catholicism.  Its sacred language, a variety of Yoruba, is the Lucumí language.

Yoruba religion: The Yoruba religion, comprising the traditional religious concepts and practices of the Yoruba people, is found primarily in southwestern Nigeria and the adjoining parts of Benin, and Togo, commonly known as Yorubaland.  Yoruba religion is ancestral or partially ancestral to the Afro-American religions Santería, Trinidad Orisha, Umbanda, Brujería, Hoodoo, Candomblé, Quimbanda, Orisha, Xangô de Recife, Xangô do Nordeste, Comfa, Espiritismo, Santo Daime, Candomblé, Abakuá, Kumina, Winti, Sanse, Cuban Vodú, Dominican Vudú, Louisiana Voodoo, Haitian Vodou, and Vodun.  Yoruba religious beliefs are part of "itan", the complex cultural concepts which make up the Yoruba society.

The Religion: The Religion is a horror novel written in 1982 by Nicholas Conde.  It explores the ritual sacrifice of children to appease the pantheon of voodoo deities, through the currently used practice of Santería.  This is by no mean accurate, as the practice of Santería has never practiced nor condoned the sacrifice of humans, much less children, but the novel depicts the various deities and personas commonly seen in Santería, and it attempts to explain the connection and differences between Santería(white magic)and Brujeria (black magic).  In an essence, the novel shows that there is a difference between Santeria and Brujeria, in which Brujeria is the evil force in the novel, where as Santeria is a force for good .

Spiritual Baptist: The Spiritual Baptist (or Shouter Baptist) faith is a syncretic Afro-American religion that combines elements of traditional African religion with Christianity.  Despite the African influences, Spiritual Baptists consider themselves to be Christians.

Harold Courlander: Harold Courlander (September 18, 1908 – March 15, 1996) was an American novelist, folklorist, and anthropologist, an expert in the study of Haitian life.  The author of 35 books and plays and numerous scholarly articles, Courlander specialized in the study of African, Caribbean, Afro-American (U.S.), and Native American cultures.  He took a special interest in oral literature, cults, and Afro-American cultural connections with Africa.

Obeah: Obeah (sometimes spelled "Obi", "Obeah", or "Obia") is a term used by the Igbo tribe in Nigeria and in the West Indies to refer to sorcery and religious practices developed among enslaved West Africans of Igbo origin.  Obeah is similar to other Afro-American religions such as Palo, Haitian Vodou, Santería, and Hoodoo.  Obeah is practiced in The Bahamas, Barbados, Belize, Dominica, Guyana, Jamaica, Saint Vincent and the Grenadines, Suriname, Trinidad and Tobago, The Virgin Islands, and other Caribbean nations.

Cowrie-shell divination: Cowrie-shell divination refers to several distinct forms of divination using cowrie shells that are part of the rituals and religious beliefs of certain religions.  Though best-documented in West Africa as well as in Afro-American religions, such as Santería, Candomblé, and Umbanda, cowrie-shell divination has also been recorded in other regions, notably East Africa and India.

Osun: Osun (Ozun) is a major Orichá (manifestation of a god) in the Santería religion of the Caribbean(Cuba and Trinidad) brought over by West African slaves during the transatlantic slave trade.  Traditionally, Osun is a to the other Orichás, and he protects the orí (head) of Santería practitioners.  He is syncretized with Saint John the Baptist (Elijah, Ilesha, Ilungu) by the fact that out of vodun he came forth to know and accept Ethiopian Christianity and Jesus as one greater than he, hence the book of John.  The same book that spurred a memorable apocalyptic movie entitled, "The Book of Eli".  The Strong's Hebrew Concordance lists #7564 as " Rishah" meaning wickedness.

Babalú: "Babalú" is a Cuban popular afro song written by Margarita Lecuona, the cousin of composers Ernestina and Ernesto Lecuona.  The song title is a reference to the Santería deity Babalú Ayé.

Trinidad Orisha: Trinidad Orisha, also known as Shango, is a syncretic religion in Trinidad and Tobago and is of Caribbean origin, originally from West Africa (Yoruba religion) and influenced by Roman Catholicism.  Trinidad Orisha incorporates elements of Spiritual Baptism, and the closeness between Orisha and Spiritual Baptism has led to use of the term "Shango Baptist" to refer to members of either or both religions.  Anthropologist James Houk described Trinidad Orisha as an "Afro-American religious complex", incorporating elements mainly of traditional African religion and Yoruba and incorporates some elements of Christianity (Catholicism and Protestantism), Hinduism, Islam (especially Sufism), Buddhism, Judaism, Bahá'í, and Trinidad Kabbalah.

Question: The Afro-American religion of Caribbean, Santería, developed where? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "religion_name": {
      "type": "string",
      "description": "The name of the religion."
    },
    "religion_type": {
      "type": "string",
      "description": "The classification of the religion, e.g., Afro-American religion."
    },
    "origin_region": {
      "type": "string",
      "description": "The broader geographical region of origin for the religion."
    },
    "development_location": {
      "type": "string",
      "description": "The specific empire or territory where the religion developed."
    },
    "influenced_by": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Major religions or practices that influenced this religion."
    }
  },
  "required": [
    "religion_name",
    "religion_type",
    "origin_region",
    "development_location"
  ],
  "additionalProperties": false
}
