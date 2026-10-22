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
Raat Bhar: "Raat Bhar" is a pop song from the 2014 Hit Bollywood film, "Heropanti".  Composed by Sajid-Wajid, the song is sung by Arijit Singh and Shreya Ghoshal, with lyrics penned by Kausar Munir.  The lively, peppy track, features Tiger Shroff and Kriti Sanon in the video.

Sabbir Khan: Sabbir Khan is an Indian film director and screenwriter.  In 2009 he made his directorial debut with the film "Kambakkht Ishq" (2009) that starred Akshay Kumar and Kareena Kapoor.  The film released on 3 July 2009 worldwide.  Sabbir's second movie, Heropanti starring Tiger Shroff & Kriti Sanon, released on 23 May 2014.

Munna Michael: Munna Michael is an Indian action dance film directed by Sabbir Khan and produced by Viki Rajani and Eros International.  The film features Tiger Shroff in a lead role alongside Nidhhi Agerwal and Nawazuddin Siddiqui.  Although it got mixed reviews, it failed to impress the audience.

Baaghi 2: Baaghi 2 is an upcoming Indian martial arts film directed by Ahmed Khan, written by Sanjeev Datta and produced by Sajid Nadiadwala under the banners Nadiadwala Grandson Entertainment and Fox Star Studios.  The film features Tiger Shroff and Disha Patani in lead roles.  It is a sequel to the 2016 film "Baaghi."

Ahmed Khan (choreographer): Ahmed Khan is an Indian choreographer, producer, actor, director and writer.  Khan began as a child actor playing small roles in films like "Raakh".  He played an orphan boy in his debut film, "Mr. India" and worked as choreographer's assistant in "Anjaam".  He choreographed for films such as "Rangeela", "Taal", "Ghajini" and "Kick".  He was a judge of Dance India Dance Lil Master season 3.  Khan made his directorial debut with the 2004 film "Lakeer – Forbidden Lines" starring John Abraham.  In 2007, he released "Fool n Final", a comedy with Sunny Deol and Shahid Kapoor.  He produced and wrote the script for "Paathshaala" and "Ek Paheli Leela".  Khan is currently set to direct "Baaghi 2" starring Tiger Shroff and Disha Patani.  It will be produced by Sajid Nadiadwala.

A Flying Jatt: A Flying Jatt is a 2016 Bollywood superhero film co-written and directed by Remo D'Souza and produced under the banner of Balaji Motion Pictures.  It features Tiger Shroff, Jacqueline Fernandez and Nathan Jones in the lead roles.  "A Flying Jatt" narrates the story of an ordinary man (Shroff) who gains superpowers.  The film released worldwide on 25 August 2016 on Janmashtami weekend.

Ayesha Dutt: Ayesha Shroff (born 5 June 1960) is an Indian model, actress and film producer.  She is the wife of Bollywood actor, Jackie Shroff and mother of Tiger Shroff and Krishna Shroff.

Baaghi (2016 film): Baaghi (English: "Rebel") is a 2016 Indian martial arts film directed by Sabbir Khan and produced by Sajid Nadiadwala under his banner of Nadiadwala Grandson Entertainment.  It features Tiger Shroff and Shraddha Kapoor in lead roles, with Sudheer Babu and Sunil Grover in supporting roles.  Journalists noted similarities between the film and the 2011 Indonesian film "" and the 2004 Telugu-language Indian film "Varsham".

Tiger Shroff: Tiger Shroff (born Jai Hemant Shroff; 2 March 1990) is an Indian film actor and martial artist who works in Hindi films.  Son of actor Jackie Shroff and producer Ayesha Dutt, he made his film debut with a leading role in the 2014 action comedy "Heropanti", which earned him a Filmfare Award for Best Male Debut nomination.  He next starred in the action drama "Baaghi" (2016), which earned over () worldwide, and received praise for the superhero thriller "A Flying Jatt" (2016).

Heropanti: Heropanti ("English: Heroic antics") is an Indian Hindi action film directed by Sabbir Khan and produced by Sajid Nadiadwala.  Actors Tiger Shroff and Kriti Sanon make their Hindi film debut with the film, alongside Prakash Raj as an important supporting role.  This is a remake of the Telugu film "Parugu", "Heropanti" released on 23 May 2014.  The film received mixed reviews from critics, but managed to become a box office super hit.  The satellite rights were bagged by Sony Entertainment Television.

Question: Tiger Shroff starred in a film directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor in question."
    },
    "films_starred_in": {
      "type": "array",
      "description": "A list of films the actor starred in, along with their directors.",
      "items": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the film."
          },
          "director_name": {
            "type": "string",
            "description": "The name of the director of the film."
          }
        },
        "required": [
          "film_title",
          "director_name"
        ],
        "additionalProperties": false
      }
    },
    "directors_of_tiger_shroff_films": {
      "type": "array",
      "description": "A list of unique directors who directed films starring Tiger Shroff.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "actor_name",
    "films_starred_in",
    "directors_of_tiger_shroff_films"
  ],
  "additionalProperties": false
}
