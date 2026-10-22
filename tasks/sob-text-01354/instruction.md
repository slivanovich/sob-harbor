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
Vaah! Life Ho Toh Aisi!: Vaah!  Life Ho Toh Aisi!  (English: "Wow!  That's what life should be like!" )  is a 2005 Indian Hindi fantasy drama film written and directed by Mahesh Manjrekar and produced by Sangeetha Ahir, starring Shahid Kapoor and Amrita Rao in the lead roles.  It was released on 23 December 2005.  It is the first Indian film to be shot in high definition (HD).  It was the 12th highest grossing hindi film of 2005 and was given the below average verdict at the box office.

Vivah: Vivah (English: "Marriage" ) is a 2006 Indian romantic drama film, written and directed by Sooraj R. Barjatya.  Starring Amrita Rao and Shahid Kapoor, it was produced and distributed by Rajshri Productions.  "Vivah" tells the story of two individuals, and relates their journey from engagement to marriage and aftermath.

Aditi Vasudev: Aditi Vasudev is an Indian film actress, known for her roles in the comedy-drama film "Do Dooni Chaar" (2010) and the comedy film "Sulemani Keeda" (2014).  She has made her TV debut in the serial "Meri Aawaaz Hi Pehchaan Hain" in February 2016 with her role as the young Ketaki along with Amrita Rao, who also made her TV debut in the same serial playing the role of Kalyani, the elder sister of Ketaki.  The TV serial is telecast in &TV channel.

Love U...Mr. Kalakaar!: Love U.. . Mr. Kalakaar!  (English: "Love you, Mr Artist") is a 2011 Bollywood film.  The film is directed by debutant S. Manasvi, who is an alumnus of Film and Television Institute of India.  It is the first film in which Tusshar Kapoor and Amrita Rao appear together.  It was released on 13 May 2011.

Masti (2004 film): Masti (English translation: "Fun") is a 2004 Indian adult comedy film directed by Indra Kumar, and starring Vivek Oberoi, Aftab Shivdasani and Ritesh Deshmukh in the lead roles with Lara Dutta, Amrita Rao, Tara Sharma and Genelia D'Souza as female leads and Ajay Devgan in a supporting role.  The film released IN 2004, and received positive response from critics, and also managed to do well at the box office, turning out to be a moderate success at the box office.  "Masti" was also amongst the low number of Bollywood adult comedy movies at the time of its release.

Amrita Rao: Amrita Rao (] , born 7 June 1981) is an Indian film actress and model.  She has appeared in Hindi films of Bollywood and a few films in Telugu.  Rao was born and raised in Mumbai; she made her screen debut in "Ab Ke Baras" (2002), for which she was nominated for the Filmfare Best Female Debut Award in 2003.  One of her most popular roles was in the romance film "Vivah" (2006).

Singh Saab the Great: Singh Saab the Great, sometimes called SSTG, is a 2013 Indian action drama film directed by Anil Sharma.  The film stars Sunny Deol, Amrita Rao, Urvashi Rautela and Prakash Raj as main characters.  The film marks the return of Sunny Deol to action genre after a long time.  Also, Deol and Sharma paired up once again after "".  The film narrates the story of a man who decides to teach a lesson to the man, who ruined his life, by reforming him.  The film's story and screenplay has been written by Shaktimaan Talwar, and the action sequences have been directed by Tinu Verna and Kanal Kannan.  The music has been provided by Anand Raj Anand and Sonu Nigam.  The film released officially on 22 November 2013.

Welcome to Sajjanpur: Welcome to Sajjanpur is a 2008 Indian Hindi comedy film directed by Shyam Benegal and starring Shreyas Talpade and Amrita Rao in the lead roles.  The film is by noted Parallel cinema director, Shyam Benegal, marking his return to comedy after filming "Charandas Chor" (1975).  Even though Benegal is responsible for other films in the parallel cinema genre, this film was one of his mainstream Bollywood films.  It was a remake of the 1977 film "Palkon Ki Chhaon Mein".

Athidhi (film): Athidhi or Atithi (English: Guest ) is a 2007 Telugu action thriller film starring Mahesh Babu and Amrita Rao, directed by Surender Reddy and produced by G. Ramesh Babu, brother of Mahesh Babu, under their banner Krishna Pictures Private Limited.  It was released on 18 October 2007.  It was dubbed into Tamil as "Thani Kaattu Raja", and into Hindi as "International Khiladi:The Iron Man".  "Athidi" was released with 500 prints in 820 theaters all over the world.  "Athidi" collected a share of () in its lifetime.

Shortkut: Shortkut (also known as Short Kut: The Con Is On) is a 2009 Bollywood comedy film directed by Neeraj Vora and produced by Anil Kapoor under Anil Kapoor Films Company.  The film stars Akshaye Khanna, Arshad Warsi and Amrita Rao in lead roles.  It released on 10 July 2009 worldwide to mostly negative reviews from critics.

Question: Who produced and distributed the film in which Amrita Rao was most popular for her role in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film where the actress had a popular role."
    },
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "role_popularity_description": {
      "type": "string",
      "description": "Description of the role's popularity from the context."
    },
    "producer_distributor": {
      "type": "string",
      "description": "The entity that produced and distributed the film."
    }
  },
  "required": [
    "film_title",
    "actress_name",
    "role_popularity_description",
    "producer_distributor"
  ],
  "additionalProperties": false
}
