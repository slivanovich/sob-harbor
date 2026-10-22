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
Kanave Kalaiyadhe: Kanave Kalayadhe (English: Oh My Dream, Do Not Fade ) is a 1999 Tamil film starring Murali, Simran, Shakti Kumar, Charle, Chinni Jayanth, Dhamu, Kovai Sarala and directed by V Gowthaman.  The score and soundtrack was composed by Deva.  It was produced by Sivasakthi Movie Makers.

Suriya Paarvai: Suriya Paarvai is a 1999 Tamil crime film directed by Jagan.  The film features Arjun and newcomer Pooja in lead roles.  The film, produced by Sreenivas Prasad, had musical score by S. A. Rajkumar and was released on 14 January 1999 to negative reviews.  The film is heavily inspired by the Luc Besson 1994 film "".

Suriya filmography: Suriya is an Indian actor and producer who works primarily in Tamil language films.  He made a commercially successful cinematic debut in Vasanth's "Nerrukku Ner" (1997).  This was followed by roles in a series of critical and commercial failures, including "Kaadhale Nimmadhi" (1998), "Sandhippoma" (1998) and "Periyanna" (1999).  Suriya collaborated with Vasanth again in "Poovellam Kettuppar" (1999), his first film with future wife Jyothika.

Vijay discography: Vijay is an Indian actor and playback singer who works mainly in Tamil language films.  He has sung for composers including Yuvan Shankar Raja, Harris Jayaraj, Deva, Anirudh Ravichander, G. V. Prakash Kumar, Santhosh Narayanan and Devi Sri Prasad.  He initially had sung songs for his own films, starting with "Bombay City" from "Rasigan", before also recording songs for other actors such as "Naa Dhum Adhikkura" for actor Suriya for the film "Periyanna".

Suriya: Saravanan Sivakumar, known by his stage name Suriya, is an Indian film actor, producer and television presenter, best known for his work in Tamil cinema.  After making his debut in "Nerukku Ner" (1997), Suriya landed his breakthrough role in "Nandha" (2001) and then had his first major commercial success with the thriller "Kaakha Kaakha" (2003).  Following award-winning performances of a conman in "Pithamagan" (2003) and a hunchback in "Perazhagan" (2004), Suriya played a patient suffering from anterograde amnesia in the 2005 blockbuster "Ghajini".  He rose to stardom with dual roles of a father and son in Gautham Menon's semi-autobiographical "Vaaranam Aayiram" (2008).  His status as an action star was established with roles of a smuggler in "Ayan" (2009), and an aggressive cop in the "Singam" trilogy ("Singam", "Singam II" and "S3").  Suriya has also found success with science fiction films like "7aum Arivu" (2011), "Maattrraan" (2014), and "24" (2016).  As of 2017, he has won three Tamil Nadu State Film Awards and four Filmfare Awards South.

Karthi: Karthik Sivakumar (born 25 May 1977), better known by his stage name Karthi, is an Indian film actor who works in the Tamil film industry.  The younger brother of actor Suriya, Karthi holds a Bachelor's degree in Mechanical Engineering and master of business administration in Industrial Engineering.  Since he had always wanted to become a film director, he returned to India and joined Mani Ratnam as an assistant director.  He was offered acting roles and made his acting debut in "Paruthiveeran" in 2007 as the title character, a careless village ruffian, winning critical acclaim and several accolades including the Filmfare Award for Best Actor and a Tamil Nadu State Film Award.  His next role was that of a coolie in "Aayirathil Oruvan" (2010), an adventure film directed by Selvaraghavan.  He achieved consecutive commercial successes with his subsequent releases – "Paiyaa" (2010), "Naan Mahaan Alla" (2010) and "Siruthai" (2011).  After appearing in a series of box office flops, he starred in successful films such as "Biriyani" (2013), "Madras" (2014) "Oopiri" (2016), and "Kaatru Veliyidai" (2017) which established him in Tamil cinema.

Sillunu Oru Kaadhal: Sillunu Oru Kaadhal (English: "A Breezy Love Story") is a 2006 Tamil romance film written and directed by N. Krishna.  It starred Suriya, Jyothika and Bhumika Chawla in pivotal roles, while Shriya Sharma, Sukanya, Vadivelu and Santhanam played other pivotal roles.  The film's score and soundtrack were composed by A. R. Rahman, with lyrics by the Indian poet Vaali; cinematography for the film was handled by R. D. Rajasekhar and editing was handled by Anthony.  The film was released on 8 September 2006, three days before the marriage of Suriya and Jyothika.  It grossed around 3 crore at box office.  The film was an average hit in spite of a decent opening.  The film was dubbed into Telugu as Nuvvu Nenu Prema (నువ్వు నేను ప్రేమ).  Vijay was first slated to do the film, but this was changed to Suriya.  Jyothika was nominated for Best Actress Category at Filmfare Awards for her portrayal of wife Character of Surya.  In 2015, this film was remade into Marathi as "Tu Hi Re", starring Swapnil Joshi, Sai Tamhankar, Tejaswini Pandit and directed by Sanjay Jadhav.  In 2017, the movie was dubbed into Hindi as "Mohabbat Ke Dushman" by Goldmines Telefilms Pvt. Ltd.

Periyanna: Periyanna is a 1999 Tamil film directed by S. A. Chandrasekhar featuring Vijayakanth and Suriya in the lead roles.  Meena and Manasa play other supporting roles, the soundtrack for this film composed by debutant music director Bharani.  The film released on 14 April 1999 to negative reviews and performed poor commercially.  Actor Vijay has lend his voice for three songs.

24 (soundtrack): 24 is the soundtrack album, composed by A. R. Rahman with song lyrics by Vairamuthu and Madhan Karky, to the 2016 Tamil film of the same name, produced by Suriya and directed by Vikram Kumar.  The film stars Suriya, Samantha Ruth Prabhu and Nithya Menen in lead roles.  The album features six tracks, and was released on April 11, 2016 by Eros Music.

Housefull (1999 film): Housefull is a 1999 Tamil film written and directed by R. Parthiepan.  The film stars Vikram, Parthiban and Suvalakshmi in the lead roles.  The film was produced by Parthiban's children under Bioscope Film Framers.  The film's score and soundtrack are composed by Ilaiyaraaja.  The film has won National Film Award for Best Feature Film in Tamil at 46th National Film Awards.

Question: Suriya, who starred in the 1999 Tamil film "Periyanna," made his debut in which movie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "debut_film": {
      "type": "string",
      "description": "The title of the film in which the actor made their debut."
    },
    "debut_year": {
      "type": "integer",
      "description": "The release year of the actor's debut film."
    },
    "film_mentioned_in_question": {
      "type": "string",
      "description": "The title of the film mentioned in the question for context."
    }
  },
  "required": [
    "actor_name",
    "debut_film",
    "debut_year",
    "film_mentioned_in_question"
  ],
  "additionalProperties": false
}
