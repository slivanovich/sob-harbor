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
Bhangra (dance): The term Bhaṅgṛā (Punjabi: ਭੰਗੜਾ , ; pronounced ] Listen) refers to the traditional dance from the Indian subcontinent originating in the Majha area of the Punjab region, free form traditional Bhangra originating in Punjab, India and modern Bhangra developed by the Punjabi diaspora.

Cycleonium: "The cycleonium is a computer based music instrument.  Every day objects like a bicycle and a bottle, and also a propeller are put in a new context and form the base of the sound design.  They lose their conventional function consequently and have to be considered as indispensable parameters of this instrument."  It was developed by Daniel Dominguez Teruel from 2007–2009 and built with the support of Chiron-Werke GmbH & Co.  KG.

Vielle à roue et à manche: The vielle à roue et à manche (called dulcigurdy by some luthiers) is a modern term for an early music instrument, of unknown original name, of the hurdy-gurdy family, but distinct in that the notes were changed by fingering the neck rather than pressing tangent keys.  The instrument has several strings which are constantly bowed by a spinning wheel turned by a crank, producing unbroken musical notes.

Pena (musical instrument): The Pena, also known as "Bana", "Bena" or "Tingtelia", is a mono string instrument falling in the lute category, similar to some of the traditional Indian stringed musical instruments such as Ravanahatha, "Ubo" or the "Kenda", found in various parts of the country.  It is the traditional music instrument of the Meitei community of Manipur, India and some parts of Bangladesh and is played either solo or in group, in folk music or as the accompanying musical instrument for Lai Haraoba festivals.  Pena playing is becoming a dying art as only 145 active Pena players are reported in Manipur.  The Center for Research on Traditional and Indigenous Art (Laihui), an organization headed by renowned Pena player, Khangembam Mangi Singh, has mandated vision to revive Pena music.

Československé hudební nástroje: Československé hudební nástroje, oborový podník (Czechoslovak Musical Instruments, specialized business) was — during the era of communist Czechoslovakia from 1948 to 1992 — a state owned music instrument manufacturing company headquartered in Hradec Králové.  The company name was later amended — "Československé hudební nástroje, státní podník" — to reflect ownership by the government.  In the 1970s, 50% of its musical instrument export products were supplied to the Soviet Union.

Musical Instrument Factory of Riga: Musical Instrument Factory of Riga (Latvian: "Rīgas mūzikas instrumentu fabrika" — "LMIF") was the largest Soviet electronic music instrument manufacturer.  It was based in Riga (former USSR, now Latvia).  RMIF synthesizers became very popular among rock and pop bands in Eastern Bloc.  The plant also produced drum kits.  After the dissolution of the USSR in 1991 RMIF went bankrupt.

Ghader Abdollahzadeh: Qadir Abdullahzada (23 October 1925 – 21 May 2009) also known as Qale Mere (Sorani Kurdish: قالەمەڕە) or Mame Qale (Sorani Kurdish: مامه قاله) born in village of Kulice (pron: Kulija; in Sorani Kurdish: كولیجه) in northwestern Iran, is one of the best known Kurdish traditional musicians.  He played shimshal/ney (long flute), a Kurdish traditional music instrument.  He started to play shimshal (Ney) as a young and homeless man aiming to earn his daily bread.  He played on the streets for an unknown number of years until he was an old man and was filmed by a journalist which was published as a documentary.  He was known for the long tones he could create and to play for hours without holding breaks.

Bugchu: Bugchu (Punjabi: ਬੁਘਚੂ ), also spelled as Bughchu, Bugdu or Bughdu, is a traditional musical instrument native to the Punjab region.  It is used in various cultural activities like folk music and folk dances such as bhangra, Malwai Giddha etc.  It is a simple but unique instrument made of wood.  Its shape is much similar to damru, an Indian musical instrument.  It makes a sound similar to its name, ""bugchoo"".

Gagar: Gagar (Punjabi: ਗਾਗਰ , pronounced: gāger), a metal pitcher used to store water in earlier days, is also used as a musical instrument in number of Punjabi folk songs and dances.  It is played with both hands with rings worn in fingers.  It is closely associated with the other music instrument, Gharha, which is an earthen pitcher.

Carolina Eyck: Carolina Eyck born on December 26, 1987, is a German musician specialising in playing the Theremin, an electronic instrument.  Her performances around the world have helped to promote the unusual music instrument.

Question: What is a traditional music instrument from India that makes the sound "bugchoo"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "instrument_name": {
      "type": "string",
      "description": "The name of the musical instrument."
    },
    "origin_region": {
      "type": "string",
      "description": "The geographical region where the instrument is native."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country associated with the instrument's origin."
    },
    "is_traditional": {
      "type": "boolean",
      "description": "Indicates if the instrument is traditional."
    },
    "sound_description": {
      "type": "string",
      "description": "A description of the sound the instrument makes."
    },
    "associated_activities": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Cultural activities or music genres where the instrument is used."
    },
    "material": {
      "type": "string",
      "description": "The primary material the instrument is made of."
    },
    "shape_description": {
      "type": "string",
      "description": "A description of the instrument's shape, often compared to other objects."
    }
  },
  "required": [
    "instrument_name",
    "origin_region",
    "is_traditional",
    "sound_description",
    "material"
  ],
  "additionalProperties": false
}
