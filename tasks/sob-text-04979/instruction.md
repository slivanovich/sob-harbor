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
Christian Peschken: Christian "Chris" Peschken (born June 9, 1955) is a German-American cameraman, director, producer and screenwriter.  He has been involved in film and radio & television production since 1974.

Thilakam (1960 film): Thilakam is a Tamil language film released in 1960 with Prem Nazir and M. N. Rajam in the lead roles.  It was directed by Krishnan–Panju, and produced by AVM Productions.

Kuzhandaiyum Deivamum: Kuzhandaiyum Deivamum (English: "Child and God" ) is a 1965 Tamil-language Indian film directed by the duo Krishnan–Panju, starring Jaishankar, Jamuna and Kutty Padmini.  An adaptation of Disney's "The Parent Trap" (1961), itself based on the German novel "Lottie and Lisa", the film tells the story of two twin girls bringing together their separated parents.  The film, produced by AVM Productions and featuring music by M. S. Viswanathan, released on 19 November 1965.  It was a big financial success, leading to remakes into Telugu as "Leta Manasulu" (1966), Hindi as "Do Kaliyaan" (1967), Malayalam as "Sethubandhanam" (1974) and Kannada as "Makkala Bhagya" (1976).

Petralthan Pillaiya: Petralthan Pillaiya ("Should one be a biological parent to provide love and care?")  is a 1966 Indian Tamil-language drama film directed by Krishnan–Panju.  The film features M. G. Ramachandran and B. Saroja Devi in lead roles.  It is a remake of Charlie Chaplin's 1921 American comedy-drama film, "The Kid".  It was produced by Vasu, under "Sri Muthukumaran Pictures".  The film was the last time that T. S. Balaiah and M. R. Radha played beside Ramachandran.  This is the 25th and final collaboration between Ramachandran and M. R. Radha, as a few days after the film was completed, Radha shot Ramachandran, wounding him.  The film was remade in Hindi as "Kunwara Baap" and "Asthamirohini".

Do Kaliyaan: Do Kaliyan is a 1968 film directed by R. Krishnan and S. Panju.  It stars Mala Sinha, Biswajeet, Mehmood and Neetu Singh.  It is a remake of Tamil movie "Kuzhandaiyum Deivamum" which itself was a copy of the 1953 film "Twice Upon a Time" and 1961 movie "The Parent Trap" which were ultimately based on the Erich Kästner's German novel "Lottie and Lisa" ("Das doppelte Lottchen").  It was declared a hit at the box office and revitalized the career of its lead actor Bishwajeet.

Krishnan–Panju: R. Krishnan (1909–1997) and S. Panju (1915–1984), collectively referred to as Krishnan–Panju, were Indian filmmakers.  The duo directed more than 50 films in South Indian languages and in Hindi.

Idhaya Veenai: Idhaya Veenai (English: "The Heart's Veena" ) is a 1972 Indian Tamil-language film directed by R. Krishnan and S. Panju, starring M. G. Ramachandran in the lead role Lakshmi, Manjula, Sivakumar, M. N. Nambiar, M. G. Chakrapani and among others.

Ratha Kanneer: Ratha Kanneer (English: "Blood Tears" ) is a 1954 Indian Tamil-language drama film directed by R. Krishnan and S. Panju.  The screenplay was written by Tiruvarur K. Thangaraj, and the film features M. R. Radha in the lead role.  The film was produced by Perumal Mudaliar of National Pictures.  The story revolves around Mohanasundaram, a returned-from-abroad, westernised, rich man who shows arrogance and contempt towards anything part of Indian culture and anyone below his social standards.

Engal Thangam: Engal Thangam (English: "Our Gold") is a Tamil thriller film directed by the famous team Krishnan–Panju released in 1970.  M. G. Ramachandran and Jayalalithaa featured in this film.  It was a super hit movie and ran more than 100 days in Chennai, Madurai and Trichy.

Poompaavai: Poompaavai is a 1944 Indian Tamil-language film directed by the duo Krishnan–Panju in their directorial debut.  Produced under the banner of Leo Films, it features K. R. Ramaswamy, U. R. Jeevarathinam, K. Sarangkapani, K. R. Chellam, T. R. Ramachandran, A. R. Sakunthala, S. V. Sahasranamam, D. Balasubramaniam, N. S. Krishnan, T. A. Madhuram, M. R. Durairaj and ‘Kottapuli’ K. P. Jayaraman.

Question: Christian Peschken and Krishnan–Panju, both have been involved in what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1_name": {
      "type": "string",
      "description": "The name of the first entity mentioned in the question."
    },
    "entity_2_name": {
      "type": "string",
      "description": "The name of the second entity mentioned in the question."
    },
    "common_involvement_area": {
      "type": "string",
      "description": "The common area of involvement for both entities."
    },
    "entity_1_specific_involvements": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of specific involvements for the first entity."
    },
    "entity_2_specific_involvements": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of specific involvements for the second entity."
    }
  },
  "required": [
    "entity_1_name",
    "entity_2_name",
    "common_involvement_area",
    "entity_1_specific_involvements",
    "entity_2_specific_involvements"
  ],
  "additionalProperties": false
}
