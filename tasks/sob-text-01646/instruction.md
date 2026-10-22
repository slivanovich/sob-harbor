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
Tera Kya Hoga Johnny: Tera Kya Hoga Johny (Hindi: तेरा क्या होगा जॉनी ; English: What's gonna happen to you, Johny ) is a 2008 Bollywood film directed by director Sudhir Mishra, starring child actor Sikander in the lead role.  Actors Karan Nath, Kay Kay Menon, Soha Ali Khan and Neil Nitin Mukesh are also part of the film.  It also stars two filmmakers, Anurag Kashyap and Aditya Bhattacharya.

Niharika Kareer: Niharika Kareer is an Indian Punjabi film actress born in Delhi.

Dheiraj Kapoor: Dheiraj Kapoor (born 25 October 1978) is an Indian film actor, model, director, producer and entrepreneur.  Kapoor is known for his modeling assignments with Honda Activa TVC, Byford T-shirts Campaign, Gurukul Campaign, BPL net.com Campaign, andIBM computers Campaigns.  Overall responsible for conceptualizing and organizing brand campaigns, events for the domestic/international markets for individuals, brands and Organizations.  He is also into the business of managing all communications and networking in support of extraordinary productions, campaign shoots, events including Indian & International Celebrities and Artists.

Kei Horie: Kei Horie (堀江 慶 , "Horie Kei" , born 4 October 1978 in Tokyo, Japan) is a Japanese former actor, writer, film producer and director.  He is known as Gaku Washio/GaoYellow in 2001's Super Sentai's series, Hyakujuu Sentai GaoRanger.  He reprised his role on one more occasion in the Super Sentai teamup, Hurricanger VS Gaoranger.  He also has an older brother, Kazuma Horie, who is a voice actor.

Tasneem Roc: Tasneem Roc (born 11 December 1978) is an Australian television and film actress born in Sydney.

Bhanumathi Ramakrishna: Paluvayi Bhanumathi (7 September 1925 – 24 December 2005) was a multilingual Indian film actress, director, music director, singer, producer, book writer and songwriter.  Widely known as the first female super star of Telugu cinema and South Indian film Industry, she is also known for her works in Tamil cinema.  She was awarded the Padma Bhushan in 2003 for her contribution in Indian cinema.  She was honored among "women in cinema" at the 30th International Film Festival of India.

List of awards and nominations received by Rekha: Rekha is an Indian film actress who primarily works in Hindi films. Hailed as one of India's finest actresses, she made her debut as a child artist in 1966 and went on to appear in lead roles in the early 1970s.  Since her debut as a leading actress she has acted in over 180 films.  Rekha has often portrayed strong female characters, while also acting in some arthouse films besides numerous mainstream cinema.  She has won four Filmfare Awards; two Best Actress Awards—resulting from seven nominations, one Best Supporting Actress Award—resulting from six nominations, and a Lifetime Achievement Award.  The first award came in 1981 for the Hrishikesh Mukherjee-directed "Khubsoorat" where she was cast in a comic role.  Her portrayal of a classical courtesan in "Umrao Jaan" (1981) fetched her the National Film Award for Best Actress in 1982.  Rekha received her second Filmfare award in 1989 for "Khoon Bhari Maang".  She portrayed the role of a widow who sets out to take revenge on her lover.  Her negative role in "Khiladiyon Ka Khiladi" was highly appreciated by the critics and earned her a Filmfare Award in the Best Supporting Actress category.  In 2003, she was presented with the Lifetime Achievement Award.  In 2010, Rekha was awarded the Padma Shri, the 4th highest civilian honour in India.  Other awards won by her include International Indian Film Academy Awards, Bengal Film Journalists' Association Awards, Star Screen Awards, Zee Cine Awards, Stardust Awards and Bollywood Movie Awards.

Swati Sen: Swati Sen is an Indian film actress born in Nagpur, Maharashtra, most known for her roles in "Udedh Bun", which won the Silver Bear for Best Short Film at the 2008 Berlin International Film Festival, and the National Film Award-winning "Antardwand" (2010), which won her critical acclaim as well as Best Actress MAMI.

Paoli Dam: Paoli Dam (born 4 October 1980) is an Indian film actress who started her career in 2004 with the Bengali television serial "Jibon Niye Khela".  She then worked in Bengali television serials such as "Tithir Atithi" and "Sonar Harin"; the former ran for six years on ETV Bangla.

Soha Ali Khan: Soha Ali Khan Khemu (born Soha Ali Khan , 4 October 1978) is an Indian film actress, known primarily for her work in the Hindi film industry, although she has also acted in Bengali and English-language films.

Question: Who is the director of the film in which an Indian film actress born on 4 October 1978 has a part?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "actress_name": {
          "type": "string",
          "description": "The name of the Indian film actress."
        },
        "date_of_birth": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the actress in YYYY-MM-DD format."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        }
      },
      "required": [
        "actress_name",
        "date_of_birth",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "director_name",
    "film_title",
    "actress_details"
  ],
  "additionalProperties": false
}
