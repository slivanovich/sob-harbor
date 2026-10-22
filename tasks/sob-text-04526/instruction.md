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
Rina (given name): Rina is a feminine given name with multiple origins.  It is also a feminine name in the Sanskrit language meaning "melted" or "dissolved", and is also a Hebrew name meaning "song; joy".  The name Rina is also a Russian hypocoristic for "Ekaterina" and is a feminine given name of Japanese origins, where it was proportionately used the most in the twentieth century.

Lady Writer: "Lady Writer" is a 1979 song by Dire Straits, which appears on the band's second album "Communiqué".  When asked what the song was about, Knopfler said that he was watching TV one day, and there was a lady writer on the TV, and that's basically where the idea for the song came from.  Because the song says the writer is "talking about the Virgin Mary", some have speculated that the writer in question is Marina Warner, a view shared by Warner herself.

Money, Power &amp; Respect (song): "Money, Power & Respect" is the second single released from The LOX's debut album of the same name.  The song was produced by Hitmen members D-Dot and Amen-Ra and featured DMX, who contributed the song's fourth verse.  The song's chorus is performed by Lil' Kim; its motif is consistent with German sociologist Max Weber's Three-component theory of social stratification, which recognizes that one's wealth, power, and prestige, affects one's independent capability or ability to act on one's will.  The track samples Dexter Wansel's 1979 song "New Beginning".

Lindy (name): Lindy is a given name and a nickname.  It can be used by either gender.  As a female given name, it is a variant of names like Linda, Belinda, and Melinda, and the meaning of Lindy is "beautiful; pretty; sweet."  As a male name, it is a variant of names such as Lindsay and Lyndon, and the meaning is "linden tree mountain; Lincoln's marsh; island of linden trees; linden tree hill."  Lindy was most popular in the year 1979, when it ranked 586th.

Gary Numan: Gary Anthony James Webb (born 8 March 1958), known professionally as Gary Numan, is an English singer, songwriter, composer, musician and record producer.  Born in Hammersmith, West London, he first entered the music industry as lead singer of the new wave band Tubeway Army.  After releasing two studio albums with the band, Numan released his debut solo album "The Pleasure Principle" in 1979.

Down in the Park: "Down in the Park" is a 1979 song by the English band Tubeway Army.  It was released as the first single from the band's second album "Replicas", though was not a hit.  The song was written and produced by the band's frontman Gary Numan, and despite its lack of commercial success, has been performed by Numan regularly in his live shows throughout the years.

Zane: Zane is a surname which was popularized as a given name through the popular American writer Zane Grey.  Grey's given name was Pearl but he instead adopted his middle name, from his mother's family name, as a pen name.

Throw Some D's: "Throw Some D's" is the first single from the self-titled album of rap artist Rich Boy, and his most commercially successful song to date.  The single was produced by Butta and Polow da Don (who has a featured credit in the song).  The song contains samples from the 1979 song "I Call Your Name" by the R&B group Switch.  It has been certified platinum by the RIAA.

Park Sungho: Park Seong-ho or Park Sung-ho is a Korean name consisting of the family name "Park" and the given name "Seong-ho".  The name may refer to:

Girl of My Dreams: "Girl of My Dreams" is a song by Canadian pop rock band The Moffatts.  It was released in January 1999 as the third single from their third album, "".  The song was a hit in Canada, reaching number 19 on Canada's singles chart and peaked at number 4 on the Canadian "RPM" Adult Contemporary chart.  It is unrelated to the 1979 song of the same name by British band Bram Tchaikovsky.

Question: What was the given name of the writer of the 1979 song Down in the Park ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "song_year": {
      "type": "integer",
      "description": "The year the song was released."
    },
    "writer_details": {
      "type": "object",
      "properties": {
        "professional_name": {
          "type": "string",
          "description": "The professional name of the song's writer."
        },
        "given_name": {
          "type": "string",
          "description": "The full given name of the song's writer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the writer."
        }
      },
      "required": [
        "professional_name",
        "given_name",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "song_year",
    "writer_details"
  ],
  "additionalProperties": false
}
