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
Dangal (film): Dangal (English: "Wrestling competition" ) is a 2016 Indian Hindi-language biographical sports drama film loosely based on the story of Mahavir Singh Phogat, an amateur wrestler, who trains his daughters Geeta Phogat and Babita Kumari to be world-class wrestlers.  It was directed by Nitesh Tiwari.  Produced by Walt Disney Pictures, Aamir Khan Productions and UTV Motion Pictures, it stars Aamir Khan as the father.  Both daughters go on to win medals at the 2010 Commonwealth Games.  Babita won a silver medal at the Games, in the 51 kg class and gold at the 2014 Glasgow Games in the 55 kg class.  In 2012, Geeta became the first Indian female wrestler to qualify for the Olympics.  Mahavir's efforts inspired dozens of Indian women to take to wrestling.  Fatima Sana Shaikh and Sanya Malhotra play the older selves of the sisters while Sakshi Tanwar plays their mother and Aparshakti Khurana, their cousin.

Mirza Ghalib (film): Mirza Ghalib (1954) is an Indian Hindi and Urdu language biographical film, directed by Sohrab Modi.  Based on the life of well-known poet Mirza Ghalib, the film was acclaimed upon release.  It stars Bharat Bhushan as Ghalib and Suraiya as his courtesan lover.  The film won (1) the President's Gold Medal for the All India Best Feature Film and (2) the President's Silver Medal for Best Feature Film in Hindi in the 2nd National Film Awards for 1954.  Suraiya's singing (of Mirza Ghalib ghazal's) and her acting was specially applauded by the Prime Minister, Jawahar Lal Nehru, who remarked to her " You have brought back Ghalib to life",

Ekk Deewana Tha: Ekk Deewana Tha (English: "There Was a Crazy Lover" ) is a 2012 Indian Hindi romantic drama film, written and directed by Gautham Menon, featuring Prateik Babbar and Amy Jackson in her Bollywood debut, and in lead roles.  The film is a remake of Menon's own Tamil film "Vinnaithaandi Varuvaayaa" (2010) and features reused soundtrack and film score composed by A. R. Rahman, while the cinematography and editing are handled by M. S. Prabhu and Anthony Gonsalves, respectively.  Singer Chinmayi has provided the talking voice of the female lead, reprising her role from the Tamil version and the Telugu simultaneously made version where she dubbed for actresses Trisha Krishnan and Samantha Ruth Prabhu respectively.

Bollywood: Bollywood formally known as Hindi cinema is the Indian Hindi language film industry, based in the city of Mumbai, Maharashtra, India.  Bollywood is only a part of the larger cinema of India also known as Indywood, which includes other production centers producing blockbuster films in many other Indian languages.

Chand Sa Roshan Chehra: Chand Sa Roshan Chehra (English: "Glowing Face of Yours Is as Same as Moon") is a 2005 Indian Hindi language romance film directed by Shabah Shamsi and produced by Salim.  It stars Samir Aftab and Tamannaah Bhatia in pivotal roles.  This movie is the bollywood debut movie for the successful actress Tamannaah Bhatia.  The film received very positive reviews from critics and was praised for Tamannaah's performance.  However, the film was a commercial failure.

Pocket Gangsters: Pocket Gangsters (Hindi: पॉकेट गैंगस्टर्स) is a 2015 Indian Hindi language Bollywood comedy/drama film written and directed by Hemant Nilim Das, produced by V. M. Shah, and starring Madhur Mittal, Raghubir Yadav, and Mukesh Bhatt.  Though initially announced to release in July 2013 and then re-slated for September 2014, the film was finally released January 2015.

Jass Bhatia: Jass Bhatia (born Jaskaran Singh Bhatia on 29 June 1988) is an Indian actor and model.  He began his career by working in several television commercials and print ads.  He made his Bollywood debut with a supporting role in the Indian romantic drama film "Mausam" in 2011.  He followed it with a role in the less successful film "I Don't Luv U".  In 2013, the Indian biographical sports drama film "Bhaag Milkha Bhaag" directed by Rakeysh Omprakash Mehra proved to be his first commercially successful film in 5 years.  In 2014, Bhatia portrayed Parineeti Chopra's friend named "Chimsy" in Shaad Ali's Indian crime drama film "Kill Dil".  In the television circuit, Jass featured as Happy in "Rab Se Sona Ishq" and played the character Bakshish in "Firangi Bahu".

Sri Ramakrishna Darshanam: Sri Ramakrishna Darshanam is a 2012 Singaporean and Indian Tamil and Hindi language biographical film based on the life and philosophy of 19th century Bengali mystic saint Ramakrishna.  The film was directed by G N Dass produced by G.N.D. Vision International Private Limited.  The film had screened in Chennai before being shared 17 August as a part of the 150th anniversary of the birth of Swami Vivekananda.

Love Ke Chakkar Mein: Love Ke Chakkar Mein is a 2006 Hindi language comedy film written by Rajeev Kaul and Praful Parekh, and directed by B. H. Tharun Kumar.  The film stars Rishi Kapoor, Akshat Bhatia, Satish Shah, and Shoma Anand, and marks the debut of Akshat Bhatia.  The film was second movie for director B.H Tharunkumar.  He made Nayee Padosan in the year 2003.  The film was also a bollywood debut for south sensational actress Namitha who appeared only in this bollywood movie.

Aparshakti Khurana: Aparshakti Khurrana is an Indian RJ, Bollywood actor and TV anchor.  He is the younger brother of Ayushmann Khurrana who is a popular actor from Bollywood.  Khurana made his Bollywood debut with Aamir Khan's "Dangal".  He is currently hosting the show "You Have Been Warned" on Discovery Channel India.

Question: What is the name of this 2016 Indian Hindi language biographical sports drama film, in which Khurana made his Bollywood debut?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "film_language": {
      "type": "string",
      "description": "The primary language of the film."
    },
    "debut_actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor making their debut."
        },
        "debut_type": {
          "type": "string",
          "description": "The type of debut (e.g., Bollywood debut)."
        },
        "role_in_film": {
          "type": "string",
          "description": "The role played by the actor in the film."
        }
      },
      "required": [
        "actor_name",
        "debut_type",
        "role_in_film"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_genre",
    "film_language",
    "debut_actor_details"
  ],
  "additionalProperties": false
}
