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
Anil V. Kumar: Anil V Kumarr (born 4 June 1975) is a television and film director and producer in India.  He started his production house "Flying Turtle Films" with his partners Shabbir Ahluwalia and Sakett Sawhnney in 2010.  The shows he has directed include "Kahaani Ghar Ghar Kii" and "Kahin To Hoga", both on Star Plus.  In 2013, Flying Turtle Films co-produced the movie "Zanjeer" starring Priyanka Chopra and Ram Charan.

Arjan Bajwa: Arjan Bajwa (born 3 September 1979), is an Indian film actor known for his work in Bollywood and Telugu cinema.  Arjan initially started off with Telugu films, breaking the usual norm of being the first North Indian actor to have played leading roles in 8 films of which 5 were successful.  He then made his debut in Bollywood with director Mani Ratnam's critically acclaimed film, "Guru", playing the antagonist opposite Abhishek Bachchan and Aishwarya Rai.  Subsequently, he played the male lead in Madhur Bhandarkar’s "Fashion" with Priyanka Chopra.  The film won him the Stardust Award for Breakthrough Performance while "Fashion" won several awards such as Filmfare, IIFA, Star Screen and Stardust Awards along with two National Awards.  Bajwa also starred in the Telugu movie "King" along with Nagarjuna Akkineni and Trisha.  He then appeared in another Telugu film "Arundhati" starring Anushka Shetty and Sonu Sood, which became the highest grossing Telugu film at its time of release.

Omung Kumar: Omung Kumar is an Indian film director, and production designer, known for his works in Hindi cinema.  He made his directorial debut with the 2014 biographical sports drama "Mary Kom" starring Priyanka Chopra.  The film was a critical and commercial success.  He and the film received several awards and nominations, including the National Film Award for Best Popular Film Providing Wholesome Entertainment.  He came up with his second film Sarbjit which was a biopic based on the life of "Sarabjit Singh".  The film was commercially and critically success at the box office.  He is now coming up with another film 'Bhoomi', which will be Sanjay Dutt's comeback film which is a critical and commercial failure.

E. V. V. Satyanarayana: Eedara Veera Venkata Satyanarayana (Telugu: ఈదర వీర వెంకట సత్యనారాయణ ; 10 June 1956 – 21 January 2011), better known as E. V. V. Satyanarayana (Telugu: ఇ.వి.వి.సత్యనారాయణ ), was a Telugu Indian film director, screenwriter and producer.  He directed a total of 51 films in Telugu and Hindi and introduced many actors to Telugu cinema.  He was well known for making comedy films, most of which were very successful at the box office.  In 2000, he established his own production company called as E. V . V. Cinema.  He died in 2011 due to complications of throat cancer and cardiac arrest.

Zanjeer (2013 film): Zanjeer (English: "Shackles" ) in Hindi, Thoofan (English: Storm) in Telugu is a 2013 Indian bilingual action-drama film directed by Apoorva Lakhia, shot simultaneously in Hindi and Telugu.  It is a remake of the 1973 Hindi film of the same name.  The film marked the Bollywood debut of Tollywood actor Ram Charan in the lead role along with Priyanka Chopra.  Reliance BIG Entertainment bought worldwide distribution rights for () .

A. M. Rathnam: A. M. Rathnam is an Indian film producer from Andhra Pradesh, known for his works in Telugu cinema and Tamil cinema.  Under the gamut of Sri Surya Movies Entertainment, Hyderabad, a movie production house owned by him, he has produced blockbusters in Telugu such as "Karthavyam" (1990), "Peddarikam" (1992) and "Sneham Kosam" (1999) "Kushi" (2001).  He ventured into Tamil cinema in 1996 with the blockbuster, "Indian", which was India's Official Entry for the Best Foreign Language Film for the Academy Awards.  He then produced films like "Kushi", "Run", "Boys", "Enakku 20 Unakku 18", "Dhool", "Ghilli", "7G Rainbow Colony","Arrambam", Bangaram, "Yennai Arindhaal" and "Vedalam".

Telugu cinema: Telugu cinema, also known by its sobriquet Tollywood, is the segment of Indian cinema dedicated to the production of motion pictures in the Telugu language, based in Film Nagar, a neighbourhood of Hyderabad, Telangana.  It is one of the biggest film industries in India.  Since 1909, film maker Raghupathi Venkaiah Naidu was involved in producing short films and travelling to different regions in Asia to promote film work.  In 1921, he produced the first Telugu silent film, "Bhishma Pratigna".  He is cited as the father of Telugu cinema.  Telugu cinema is the second largest industry of Indian cinema after Hindi Bollywood cinema, accounting for the second largest global box office gross among all Indian film industries.  In 1933, East India Film Company has produced its first Indian film, "Savitri", in Telugu.  The film was based on a popular stage play by Mylavaram Bala Bharathi Samajam, directed by father of the "Telugu theatre Movement" Chittajallu Pullaiah and cast stage actors Vemuri Gaggaiah and Dasari Ramathilakam as "Yama" and "Savithri" respectively.  The film was shot with a budget of estimated in Calcutta.  The blockbuster film has received an honorary diploma at the 2nd Venice International Film Festival.

Ram Charan: Ram Charan is an Indian film actor, dancer, producer, businessman and entrepreneur, who works in Telugu cinema.  He won two Nandi Awards, two South Filmfare awards, two CineMAA Awards, and two Santosham Best Actor Awards. Charan is one of the highest paid actors in Tollywood.

Sunil Kumar Reddy: P. Sunil Kumar Reddy is an Indian director, Screenwriter, film producer who works primarily in Telugu cinema.  Well known for Directing low Budget film's like Sontha Ooru, Oka Romantic Crime Katha.  Sunil Kumar Reddy is associated with Sravya Films, a film production house in South.

Manchu Vishnu: Manchu Vishnu (Telugu: విష్ణు మంచు ;) is an Indian film actor, producer, and director known for his works exclusively in the Telugu cinema, and Television.  Vishnu had a brief stint as a child artist with the 1985 film "Ragile Gundelu".  Years later, He starred in the 2003 Telugu action film "Vishnu" for which he won the Filmfare Best Male Debut.  He is the co-owner of the film production house 24 Frames Factory and an educationalist through "Sree Vidyanikethan Educational Trust", founded by his father and veteran Telugu actor Mohan Babu.  In 2007, he starred in the comedy film, "Dhee", the film became a Super-Hit, and Vishnu established his career in Telugu cinema.  Vishnu is one of the sponsor's of the Celebrity Cricket League – "Telugu Warriors"

Question: Anil V. Kumar,  is a television and film director and producer in India, his production house, Flying Turtle Films co-produced the movie "Zanjeer" starring Priyanka Chopra and which actor, and entrepreneur, who works in Telugu cinema?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "production_house": {
      "type": "string",
      "description": "The production house that co-produced the movie."
    },
    "director_producer": {
      "type": "string",
      "description": "The director and producer associated with the production house."
    },
    "co_star_1": {
      "type": "string",
      "description": "The first co-star mentioned in the movie."
    },
    "co_star_2": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the second co-star."
        },
        "primary_cinema_industry": {
          "type": "string",
          "description": "The primary cinema industry the actor works in."
        },
        "is_entrepreneur": {
          "type": "boolean",
          "description": "Indicates if the actor is also an entrepreneur."
        }
      },
      "required": [
        "actor_name",
        "primary_cinema_industry",
        "is_entrepreneur"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movie_title",
    "production_house",
    "director_producer",
    "co_star_1",
    "co_star_2"
  ],
  "additionalProperties": false
}
