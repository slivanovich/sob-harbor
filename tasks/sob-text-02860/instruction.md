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
Into the Widening World: Into the Widening World is a collection of 26 short fictional coming-of-age stories.  It was written by many authors including: Nadine Gordimer, Ben Okri, Bharati Mukherjee, Alice Munro and Gabriel Garcia Marquez.

Starbook: Starbook, subtitled ""A Magical Tale of Love and Regeneration"," is a 2007 novel by Nigerian poet and novelist Ben Okri.

Paint the Change: Paint the Change is a global street art project that uses public art and community dialogue to discuss social justice issues.  The project's latest mural is a monumental piece in Shoreditch, East London, featuring words by Ben Okri and art by Ben Eine to commemorate the victims and survivors of the Grenfell Tower fire in London.  Paint the Change is also the umbrella project for the global street art and human rights project Education Is Not A Crime.

Young Maverick: Young Maverick is a 1979 television series.  The series was a sequel of the 1957 series "Maverick", which had starred James Garner as roving gambler Bret Maverick.  Charles Frank played Ben Maverick, the son of Bret's first cousin Beau Maverick, making him Bret's first cousin once removed.  Frank's real-life wife Susan Blanchard played his girlfriend Nell, while John Dehner (who appeared in "Maverick"'s "Shady Deal At Sunny Acres") appeared as a frontier marshal who had arrested Ben's father Beau decades before.  The series was cancelled by CBS after six hour-long episodes had been shown, leaving two which were never aired on the network.  All eight episodes were screened later that year on BBC1 in the UK.

The Famished Road: The Famished Road is the Booker Prize-winning novel written by Nigerian author Ben Okri.  The novel, published in 1991, follows Azaro, an "abiku" or spirit child, living in an unnamed, most likely Nigerian, city.  The novel employs a unique narrative style incorporating the spirit world with the "real" world in what some have classified as magical realism.  Others have labeled it African Traditional Religion realism.  Still others choose to simply call the novel fantasy literature.  The book exploits the belief in the coexistence of the spiritual and material worlds that is a defining aspect of traditional African life.

Henry Charles Frank Morant: Henry Charles Frank Morant (188528 October 1952) was an Australian writer.  He was born at Dulverton, England and died at St Kilda, Victoria, Australia.

Legge-Bourke: The family name originated with the adoption by Lt-Col Nigel Walter Henry Legge, of the Coldstream Guards (whose father, Hon. Sir Henry Charles Legge, K.C.V.O., descended from the Earls of Dartmouth), of the additional surname of 'Bourke', by Royal Licence, 26 April 1911, on succeeding to the estate of the Hon. Henry Lorton Bourke, of Hayes, Co.  Meath, a descendant of the Earls of Mayo.  Henry Lorton Bourke and Henry Charles Legge's wives were both daughters of Gustavus William Lambart (his eldest son was created a baronet); when Bourke and his wife died without issue, his estate was inherited by his nephew.

Frederick Charles Frank: Sir Frederick Charles Frank, OBE, FRS (6 March 1911 – 5 April 1998), known as Sir Charles Frank, was a British theoretical physicist.  He is best known for his work on crystal dislocations, including (with Thornton Read) the idea of the Frank–Read source of dislocations.  He also proposed the cyclol reaction in the mid-1930s, and made many other contributions to solid state physics, geophysics, and the theory of liquid crystals.

Dangerous Love (novel): Dangerous Love is a 1996 novel by Ben Okri set in Lagos of the 1970s.  The novel is a reworking of an earlier book, "The Landscapes Within".  The book is more conventional and realist than Okri's previous works.  The subject concerns love, corruption and memories of the Biafran War in Nigeria.

Ben Okri: Ben Okri OBE FRSL (born 15 March 1959) is a Nigerian poet and novelist.  Okri is considered one of the foremost African authors in the post-modern and post-colonial traditions, and has been compared favourably to authors such as Salman Rushdie and Gabriel García Márquez.

Question: Are Ben Okri and Henry Charles Frank Morant both writers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_writers": {
      "type": "boolean",
      "description": "True if both individuals are identified as writers, false otherwise."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_writer": {
            "type": "boolean",
            "description": "True if the individual is identified as a writer in the context."
          },
          "profession_details": {
            "type": "string",
            "description": "Specific details about their profession as a writer, if available."
          }
        },
        "required": [
          "name",
          "is_writer",
          "profession_details"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why the answer is true or false based on the context."
    }
  },
  "required": [
    "are_both_writers",
    "individuals",
    "reasoning"
  ],
  "additionalProperties": false
}
