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
Long, Long Ago: "Long, Long Ago" is a song dealing with nostalgia, written in 1833 by English composer Thomas Haynes Bayly.  Originally called "The Long Ago", its name was apparently changed by the editor Rufus Wilmot Griswold when it was first published, posthumously, in a Philadelphia magazine, along with a collection of other songs and poems by Bayly.  The song was well received, and became one of the most popular songs in the United States in 1844.

KNM ER 3883: KNM ER 3883 is the catalogue number of a fossilized skull (nearly complete cranium) of the species "Homo erectus".  The fossil was discovered by Richard Leakey in 1976 in Koobi Fora, east of Lake Turkana (formerly lake Rudolf), Kenya.

KNM ER 992: KNM ER 992 is a old fossilized lower jaw discovered by Richard Leakey in 1971 at Lake Turkana, Kenya.  The mandible was considered by C. Groves and V. Mazak to be the holotype specimen for "Homo ergaster".

Candles Long Ago: Candles Long Ago is the 14th album by popular children's entertainers Sharon, Lois & Bram, originally released in 1993.  It is the first, and only, Chanukah album produced by the trio.  Unlike other Sharon, Lois & Bram albums, "Candles Long Ago" is a miniature album featuring only eleven songs, of which many appear on their previous album "Candles, Snow & Mistletoe" and one from their second album, "Smorgasbord".  O It was sold as part of the Sharon, Lois & Bram mini collection at a cheaper price than the trio's regular full-length albums.

KNM ER 406: KNM ER 406 is an almost complete fossilized skull of the species "Paranthropus boisei".  It was discovered in Koobi Fora, Kenya by Richard Leakey and H. Mutua in 1969.

KNM ER 3733: KNM ER 3733 is a fossilized hominid cranium of the extinct hominid "Homo ergaster", which is interchangeably referred to as "Homo erectus".  It was discovered in 1975 in Koobi Fora, Kenya, right next to Lake Turkana, by Bernard Ngeneo, a field worker for Richard Leakey.  Its geographic location is not to be confused with that of KNM WT 15000, Turkana Boy, also known as Nariokotome Boy, who was also found near Lake Turkana nine years later in 1984.

Kamoya Kimeu: Kamoya Kimeu, (born 1940) is one of the world's most successful fossil collectors who, together with paleontologists Meave Leakey and Richard Leakey, is responsible for some of the most significant paleoanthropological discoveries.  Kimeu found a "Homo habilis" skull known as KNM ER 1813, an almost complete "Homo erectus" skeleton named KNM-WT 15000 or Turkana Boy (also known as Nariokotome boy), and in 1964 the jaw of a "Paranthropus boisei" skull known as the Peninj Mandible.  He has two fossil primates named after him: "Kamoyapithecus hamiltoni" and "Cercopithecoides kimeui".

Homo habilis: Homo habilis was a species of the tribe Hominini, during the Gelasian and early Calabrian stages of the Pleistocene geological epoch, which lived between roughly 2.1 and 1.5 million years ago.

KNM ER 1805: KNM ER 1805 is the catalog number given to several pieces of a fossilized skull of the species "Homo habilis".  It was discovered in Koobi Fora, Kenya in 1974.  The designation indicates specimen 1805, collected from the east shore of Lake Rudolf (now Lake Turkana) for the Kenya National Museums.

KNM ER 1813: KNM ER 1813 is a skull of the species "Homo habilis".  It was discovered in Koobi Fora, Kenya by Kamoya Kimeu in 1973, and is estimated to be 1.9 million years old.

Question: How long ago did the the species associated with KNM ER 1805 live?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fossil_id": {
      "type": "string",
      "description": "The catalog number of the fossil."
    },
    "species_name": {
      "type": "string",
      "description": "The species associated with the fossil."
    },
    "time_period_lived": {
      "type": "object",
      "properties": {
        "start_million_years_ago": {
          "type": "number",
          "description": "The start of the period the species lived, in million years ago."
        },
        "end_million_years_ago": {
          "type": "number",
          "description": "The end of the period the species lived, in million years ago."
        }
      },
      "required": [
        "start_million_years_ago",
        "end_million_years_ago"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "fossil_id",
    "species_name",
    "time_period_lived"
  ],
  "additionalProperties": false
}
