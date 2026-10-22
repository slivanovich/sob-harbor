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
Rabin Ghosh: Rabin Ghosh (1932–2010), a 20th-century violin virtuoso of 'Seni-Maihar' Gharana (Seni-Maihar School of thoughts) of North Indian Classical Music, India, was a disciple of Baba Ustad Allauddin Khan Saheb.

Chatur Lal: Chatur Lal (1925 – October 1965) was a renowned Indian tabla player.  Lal toured with Ravi Shankar, Aashish Khan, Baba Allauddin Khan, Nikhil Banerjee and Ali Akbar Khan in the 1950s and early 1960s and helped popularize the tabla in Western countries and made the nuances of this Indian drum.  Chatur Lal was born 1925 in Udaipur, Rajasthan.  Lal died October 1965.  His legacy is maintained by the Pandit Chatur Lal Memorial Society and his elder son Charanjit Chaturlal, his daughter-in-law Meeta Lal, his granddaughter Shruti Lal, and his grandson Pranshu Lal.

Ali Akbar Khan: Ali Akbar Khan (14 April 192218 June 2009) was a Hindustani classical musician of the Maihar gharana, known for his virtuosity in playing the sarod.  Trained as a classical musician and instrumentalist by his father, Allauddin Khan, Khan also composed several classical "ragas" and film scores.  He established a music school in Calcutta in 1956, and the Ali Akbar College of Music in 1967, which moved with him to the USA and is now based in San Rafael, California, with a branch in Basel, Switzerland.

Debasis Chakroborty: Debasis Chakroborty (Bengali: দেবাশিস , Hindi: देबाशीष , born 9 June 1961) is an Indian classical slide guitar player who belongs to the Senia-Maihar Gharana.  Chakroborty was born in Calcutta, India, and was groomed in the atmosphere of music from his childhood.  He began learning guitar from his father Sh.  Madhusudan Chakroborty.  He then came under the tutelage of Pt.  Barun Kumar Pal, a renowned guitarist from Kolkata and Pandit Jotin Bhattacharya, an eminent Sarod player and senior disciple of Ustad Baba Allauddin Khan Sahib of Maihar Gharana.  Later on, Debasis became a disciple of the guitar maestro Pundit Brij Bhushan Kabra.

Vilayat Khan: Ustad Vilayat Khan (28 August 1928 – 13 March 2004) was one of India's well known sitar maestros.  Along with Ravi Shankar, Ali Akbar Khan, Nikhil Banerjee and his younger brother Imrat Khan, Vilayat Khan helped introduce Indian Classical Music to the West.

Hem Bihag: Hem-Behag is a late night (samay) raga in North Indian classical music that was composed by Ustad Baba Allauddin Khan.

Jotin Bhattacharya: Jotin Bhattacharya (Hindi: ज्योतिन भट्टाचार्य ), also known as Pandit Jotin Bhattacharya is an Indian classical musician and one of the most renowned sarod players and composers from Varanasi, India.  Jyotin Bhattacharya was a disciple of Baba Allauddin Khan and received his formal training from him.  Bhattacharya has created over 40 ragas, released Indian classical music albums and has written books about Baba Allauddin Khan.

Maihar Band: The Maihar Band is an instrumental musical group in the Indian city of Maihar that performs both Indian and western music.  After an epidemic orphaned many children, Ustad Allauddin Khan, a musician of the Maihar court who was moved by the tragedy, taught them how to play music and formed an orchestral group later known as the Maihar Band.  The ruling prince, Braj Nath Singh, cooperated and helped Allauddin Khan in procuring and preparing required instruments.

Nikhil Banerjee: Nikhil Ranjan Banerjee (Bengali: নিখিল রঞ্জন ব্যানার্জী ) (14 October 1931 – 27 January 1986) was an Indian classical sitarist of the Maihar Gharana.  A student of the legendary Baba Allauddin Khan, Pandit Nikhil Banerjee was known for his technical virtuosity and clinical execution.  Along with Pandit Ravi Shankar and Ustad Vilayat Khan, he emerged as one of the leading exponents of the sitar.  He was a recipient of the Indian civilian honour of the Padma Bhushan.

Allauddin Khan: Allauddin Khan, also known as Baba Allauddin Khan (c. 1862 – 6 September 1972) was a sarod player and multi-instrumentalist, composer and one of the most renowned music teachers of the 20th century in Indian classical music.

Question: Vilayat Khan helped introduce Indian Classical Music to the West, along with what other musician who was a student of Baba Allauddin Khan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_identified": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the musician who fits the criteria."
        },
        "relationship_to_allauddin_khan": {
          "type": "string",
          "description": "The relationship of the identified musician to Baba Allauddin Khan."
        }
      },
      "required": [
        "name",
        "relationship_to_allauddin_khan"
      ],
      "additionalProperties": false
    },
    "vilayat_khan_role": {
      "type": "string",
      "description": "The role of Vilayat Khan in introducing Indian Classical Music to the West."
    },
    "other_musicians_who_helped_introduce_to_west": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of other musicians, besides Vilayat Khan and the identified musician, who also helped introduce Indian Classical Music to the West."
    }
  },
  "required": [
    "musician_identified",
    "vilayat_khan_role",
    "other_musicians_who_helped_introduce_to_west"
  ],
  "additionalProperties": false
}
