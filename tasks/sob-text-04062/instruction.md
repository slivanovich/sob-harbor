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
Henry, Duke of Lower Lorraine: Henry I (  1059 – c. 1119) was the count of Limburg and Arlon from 1082 to his death and duke of Lower Lorraine between 1101 and 1106.  He was the son of Waleran I of Limburg and Jutta, daughter of Frederick, Duke of Lower Lorraine.

Lambert I, Count of Louvain: Lambert I of Louvain nicknamed "The Bearded" (born in Louvain, Duchy of Lotharingia, East Francia c. 950, died in Florennes, County of Namur, Duchy of Lower Lorraine, Holy Roman Empire on 12 September 1015) was the first Count of Louvain in 1003.  He was killed by Godfrey II, Duke of Lower Lorraine in battle for Godfrey's claim of Count of Verdun.

Godfrey III, Duke of Lower Lorraine: Godfrey III (  997 –1069), called the Bearded, was the eldest son of Gothelo I, Duke of Upper and Lower Lorraine.  By inheritance, he was Count of Verdun and he became Margrave of Antwerp as a vassal of the Duke of Lower Lorraine.  The Holy Roman Emperor Henry III authorized him to succeed his father as Duke of Upper Lorraine in 1044, but refused him the ducal title in Lower Lorraine, for he feared the power of a united duchy.  Instead Henry threatened to appoint a younger son, Gothelo, as Duke in Lower Lorraine.  At a much later date, Godfrey became Duke of Lower Lorraine, but he had lost the upper duchy by that point in time.

Gothelo I, Duke of Lorraine: Gothelo (or Gozelo) (  967 – 19 April 1044), called the Great, was the duke of Lower Lorraine from 1023 and of Upper Lorraine from 1033.  He was also the margrave of Antwerp from 1005 (or 1008) and count of Verdun.  Gothelo was the youngest son of Godfrey I, Count of Verdun, and Matilda Billung, daughter of Herman, Duke of Saxony.  On his father's death, he received the march of Antwerp and became a vassal of his brother, Godfrey II, who became duke of Lower Lorraine in 1012.  He succeeded his brother in 1023 with the support of the Emperor Henry II, but was opposed until Conrad II forced the rebels to submit in 1025.  When the House of Bar, which ruled in Upper Lorraine, became extinct in 1033, with the death of his cousin Frederick III, Conrad made him duke of both duchies, so that he could assist in the defence of the territory against Odo II, count of Blois, Meaux, Chartres, and Troyes (the later Champagne).

Conrad III of Germany: Conrad III (1093 – 15 February 1152) was the first King of Germany of the Hohenstaufen dynasty.  He was the son of Duke Frederick I of Swabia and Agnes, a daughter of the Salian Emperor Henry IV.

Henry II, Duke of Limburg: Henry II (  1111 – August 1167) was the duke of Limburg from 1139 and count of Arlon from 1147 to his death.  He was the son of Waleran, Duke of Lower Lorraine, and Jutta of Guelders, daughter of Gerard I of Guelders.  He succeeded his father in Limburg with the title of duke, but Conrad III refused to grant him Lower Lorraine.  He continued to style himself as duke nevertheless.

List of Dukes of Limburg: The counts of Limburg were the original rulers of the Duchy of Limburg and rose to prominence when one of their house was appointed Duke of Lower Lorraine.

Waleran, Duke of Lower Lorraine: Waleran II (or Walram II) ( 1085 – 1139), called "Paganus" meaning "the Pagan", probably due to a late baptism, was the Duke of Limburg and Count of Arlon () from his father's death in about 1119 until his own twenty years later.  He was given the Duchy of Lower Lorraine by Lothair of Supplinburg in 1128 after the latter's accession as King of Germany in 1125.

Frederick, Duke of Lower Lorraine: Frederick, Duke of Lower Lorraine, also known as "Frederick of Luxembourg" (  1003 – 18 May 1065) was the count of Malmedy from 1035 and Duke of Lower Lorraine from 1046.  He was a younger son of Frederick, Lord of Gleiberg.

Gerberga of Lower Lorraine: Gerberga of Lower Lorraine, Countess of Louvain, was the daughter of Charles, Duke of Lower Lorraine, himself the son of Louis IV of France and Gerberga of Saxony.  She married Lambert I, Count of Louvain and had three children with him:

Question: Who was the father of the man who refused to grant Lower Lorraine to Henry II, Duke of Limburg?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "refuser_of_grant": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who refused the grant."
        },
        "title": {
          "type": "string",
          "description": "The title of the person who refused the grant."
        },
        "father": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the father of the person who refused the grant."
            },
            "title": {
              "type": "string",
              "description": "The title of the father of the person who refused the grant."
            }
          },
          "required": [
            "name",
            "title"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "title",
        "father"
      ],
      "additionalProperties": false
    },
    "recipient_of_refusal": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person to whom the grant was refused."
        },
        "title": {
          "type": "string",
          "description": "The title of the person to whom the grant was refused."
        }
      },
      "required": [
        "name",
        "title"
      ],
      "additionalProperties": false
    },
    "refused_territory": {
      "type": "string",
      "description": "The territory that was refused to be granted."
    }
  },
  "required": [
    "refuser_of_grant",
    "recipient_of_refusal",
    "refused_territory"
  ],
  "additionalProperties": false
}
