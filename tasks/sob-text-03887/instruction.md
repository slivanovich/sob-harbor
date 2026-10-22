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
Mallik Rehan Tomb, Sira: Mallik Rehan Tomb, Sira also known as Mallik Rehan Dargah in Sira in Karnataka, India is a mausoleum built over the grave of Mallik Rehan who was governor of Sira province.

Adam Tandy: Adam Tandy is a British television producer and director, perhaps best known for his collaborations with Armando Iannucci.  As such, he has worked on "The Saturday Night Armistice", "The Armando Iannucci Shows", "Time Trumpet" and most recently "The Thick of It".  In 2009 he moved into film producing with the hit "Thick of It" adaptation "In the Loop".  After the 2012 series of "The Thick of It", he has produced "Catastrophe" for Channel 4, as well as "Inside No. 9" and "Detectorists" for the BBC.

Time Trumpet: Time Trumpet is a six-episode satirical television comedy series which aired on BBC Two in 2006.  The series was written by Armando Iannucci, Roger Drew and Will Smith in a similar manner to Iannucci's earlier one-off programmes "" and "".  One sketch was later spun off by Irish network RTÉ into the cult TV series "Soupy Norman" in 2007.

The Armando Iannucci Shows: The Armando Iannucci Shows is a series of eight programmes directed by Armando Iannucci and written by Iannucci with Andy Riley and Kevin Cecil.  It was shown on UK's Channel 4 from September to October 2001.  Each episode focused on specific themes relating to human nature and existentialism, around which Iannucci would weave a series of surreal sketches and monologues.

Puneet Sira: Puneet Sira (born 3 December 1967) is a British and Bollywood film director, producer, screenwriter and actor.

I Proud to Be an Indian: I Proud to Be an Indian (Hindi: एक भारतीय होने पर गर्व , Urdu: ‎ ) is a 2004 Indian Hindi action film written and directed by Puneet Sira and produced by Sohail Khan.

Kisaan: Kisaan (Hindi: किसान "Kisān") is a 2009 Bollywood film directed by Puneet Sira, which focuses on Farmers' suicides in India Its title is Hindi for "farmer".

Armando Iannucci's Charm Offensive: Armando Iannucci's Charm Offensive is a British radio comedy programme broadcast on BBC Radio 4 first broadcast in 2005 with a second series in 2006, a third in 2007 and a fourth in 2008.  Series 2, 3 and 4 of the show were broadcast in the popular Friday evening slot, which it has shared with "The News Quiz" and "The Now Show".  It is hosted by comedian Armando Iannucci and each week a panel of fellow comedians make satirical and surreal observations on current events.  Vaughan Savidge provides voice overs.

Jai Veeru: Jai Veeru is a Hindi action film directed by Puneet Sira, and starring Fardeen Khan, Kunal Khemu, Dia Mirza, Arbaaz Khan and Anjana Sukhani.  The film was released on 13 March 2009.  It is a remake of the 1996 action, "Bulletproof".  The title of the film is named after the famous characters, Jai and Veeru from the film "Sholay".

Armando Iannucci: Armando Giovanni Iannucci, OBE ( ; born 28 November 1963) is a Scottish satirist, writer, television director, and radio producer.

Question: The director Armando Iannucci has an OBE. Does the director Puneet Sira also have one?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person whose OBE status is being queried."
    },
    "has_obe": {
      "type": "boolean",
      "description": "True if the person has an OBE, false otherwise."
    },
    "comparison_person_name": {
      "type": "string",
      "description": "The name of the person used for comparison regarding the OBE status."
    },
    "comparison_person_has_obe": {
      "type": "boolean",
      "description": "True if the comparison person has an OBE, false otherwise."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the 'has_obe' status based on the provided context."
    }
  },
  "required": [
    "person_name",
    "has_obe",
    "comparison_person_name",
    "comparison_person_has_obe",
    "reasoning"
  ],
  "additionalProperties": false
}
