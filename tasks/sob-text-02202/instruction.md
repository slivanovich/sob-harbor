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
Najam Sethi: Najam Aziz Sethi (Urdu/Punjabi: ; born c. 1948) is a Pakistani journalist and a left-leaning political commentator who serves as the editor-in-chief of The Friday Times, hosts the primetime current affairs show Aapas ki Baat on Geo News and serves as Chairman of Pakistan Super League.  Though he is an Ahmadi Muslim but he also served as the caretaker chief minister of Punjab during the 2013 election.

Priyamaanavale: Priyamaanavale (English: "The Girl I love" ) is a 2000 Tamil romance film written and directed by K. Selva Bharathy.  The film has Vijay and Simran playing the lead roles, with S. P. Balasubrahmanyam, Vivek and Radhika Chaudhari in supporting roles.  The film revolves around a working woman in a struggling family and portrays the sufferings she receives from her husband with negative shades in his role but later he realises his fault and he becomes a loving and caring husband.  The film released on 26 October 2000 to highly positive reviews and was declared a blockbuster.  This movie was a remake of 1996 Telugu movie "Pavitra Bandham" starring Daggubati Venkatesh  and Soundarya.  The movie was later dubbed in Hindi as "Dil Ki Baat".

Yeh Un Dinon Ki Baat Hai: Yeh Un Dinon Ki Baat Hain is a Hindi drama series on Sony TV & produced by Shashi Sumeet Productions, which airs at 10:30 pm from 5 September 2017 replacing Pehredaar Piya Ki from the same production house.

Ghar Ki Baat Hai: Ghar Ki Baat Hai is a Hindi television sitcom on NDTV Imagine in 2009.

Santosh Saroj: Santosh Saroj is a Bollywood screenwriter and dialogue writer mostly known for films like 'Agneepath','Major Saab'. His last film as writer was Sirf,released in 2008. He was also assistant director for films like 'Mausam','Raaste Ka Patthar' He has also directed two films "Waqt Waqt ki Baat" & "Pyar Mein Sauda Nahin" .

The Vagina Monologues: The Vagina Monologues is an episodic play written by Eve Ensler which began in 1996 at the Off-Broadway Westside Theatre after a limited run at HERE Arts Center.  The play delves into consensual and nonconsensual sexual experiences, body image, genital mutilation, direct and indirect encounters with reproduction, sex work, and several other topics through the eyes of women with various ages, races, sexualities, and other differences.  Charles Isherwood of "The New York Times" called the play "probably the most important piece of political theater of the last decade."  Ensler originally starred in the production which was produced by David Stone, Nina Essman, Dan Markley, The Araca Group, Willa Shalit and the West Side Theater.  When she left the play, it was recast with three celebrity monologists.  The play has been staged internationally, and a television version featuring Ensler was produced by cable TV channel HBO.  In 1998, Ensler and others, including Willa Shalit, a producer of the Westside Theatre production, launched V-Day, a global non-profit movement that has raised over US$ for groups working to end violence against women and girls anti-violence through benefits of "The Vagina Monologues".

Aapas ki Baat: Aapas ki Baat Najam Sethi Kay Sath (in Urdu:اپس کی بات نجم سیٹھی کے ساتھ) is an airing show on Geo News which airs from Monday to Wednesday at 11:00pm–12:00am.  The show gives political analysis on current affairs of Pakistan.  The show features to reveal the unknown in between talks of Country's establishment.  The show cast also predicts about future of political affairs in show under the given limits and code of conduct of channel.  This airing show is considered to be one of the most successful and popular airing show of country.  "Aapas ki Baat" is a discussion-based talk show which is different from usual format of Pakistani talk shows.  Najam Sethi expresses his views in clear and brief manner and draws attention to the happenings in the political area of Pakistan.

Sameer Iqbal Patel: Sameer Iqbal Patel, also referred to as Sammir I Patel and Sameer Patel, is a theatre personality from India.  Sameer, who started his career modeling for various brands, did TV shows, and wrote and directed a dozen commercial plays including 'Jo Khaya So Pachchtaye', 'Hawa Hawai', '3 Flights Down', and 'Baat Baat Mein Bigdey Haalaat'.  He has just completed his directorial debut Hotel Beautifool.  As an actor, he has featured in national television shows including "Ehsaas", "Mr. Aur Mrs. Verma Ki Rasoi", the "Noor Jehan" television show and others.  He is also the writer of the television show "Yeh Chanda Kanoon Hai", which airs on SAB TV.  Sameer's theatre production, a Hindi comedy play, named "Baat Baat Mein Bigdey Haalat," featured veteran actor Rakesh Bedi and Chetanya Adib.  Sameer has completed his debut film "Hotel Beautifool," which is due for release in 2017, adapted from his hit play Baat Baat Mein Bigdey Halaat.  After 'Hotel Beautifool', Sameer has started working on his next project, a Hindi feature film named Tata Goodbye, a black comedy.

Yoni Ki Baat: Yoni Ki Baat, roughly translated from Hindi as "Talks of the Vagina," is a live performance of monologues by women of South Asian origin.  The project was inspired by a production of Eve Ensler's "The Vagina Monologues" by the Kimaaya Theatre Company in Bangalore, India.  "Yoni Ki Baat" was conceptualized in 2003 by South Asian Sisters, a non-profit collective of South Asian women based in the San Francisco Bay Area.  At the time of its founding in 2003, the Bay Area was home to a critical mass of South Asian social justice organizations with which the South Asian Sisters collaborated.  This included Trikone, the oldest South Asian LGBTQ magazine in the world, Narika and Maitri, supporting survivors of domestic violence in the South Asian community, ASATA (The Alliance of South Asians Taking Action) and many other community groups.  The arts organization Yoni Ki Baat was co-founded by Sapna Shahani, Vandana Makker, and Maulie Dass in this climate of social justice organizing.  As of 2012, South Asian Sisters have had eight unique scripts assembled from separate calls for submissions.

Jolly Mukherjee: Jolly Mukherjee is an Indian singer/songwriter/producer.  Known as India's "King of Strings", Mukherjee specializes in the music of Bollywood, or the Indian film industry.  He started his career as a backup singer for commercials, then moving on to writing music for airline on-flight introductions, where he sometimes wrote for British Airways.  His Longtime friend and a great singer "HARIHARAN" has been a great influence.  His roots include a mixture of Hindustani classical music and Western music.It was Hariharan who actually gave him his first arrangement, HAZIR, which was an album with USTAD ZAKIR HUSSAIN.  Jolly Has been associated with Hariharans Ghazal arrangement, for the albums like Gulfam, Paigham, Jashn, Dil Ki Baat, Kaash, Waqt par Bolna, and HAZIR 2.  Also Reflection and Horizon to mention as associate .  He is known for working with the Madras Cinematic Orchestra, for his International Album, Fusebox, included remixes from State of Bengal and Badmarsh & Shri, from which the remixed version of "Bhatiyali" achieved success.  He has a series of hit songs from the Hindi movies DAYAVAN, CHANDNI, SAATHI, AAINA, SANGEET, AATISH, RAGHUVEER, AADMI, AAR YA PAAR, JUDGE MUJRIM, INDRAJEET, BHISHMA, RAAZ, JUNGLE , DHOOM 2 to name a few.  He is famous in Bangladesh for providing playback for veteran actor Dipjol.  One of his famous song in Dhallywood is "Ki batti lagaili (ore o mainka)".  He provided the string arrangements for the Icelandic performer Björk's song "Verandi".

Question: Who was the writer of an episodic play from which Yoni Ki Baat was inspired?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "inspired_project_name": {
      "type": "string",
      "description": "The name of the project that was inspired."
    },
    "inspiring_play": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the play that served as inspiration."
        },
        "writer": {
          "type": "string",
          "description": "The writer of the inspiring play."
        }
      },
      "required": [
        "title",
        "writer"
      ],
      "additionalProperties": false
    },
    "inspiration_source_details": {
      "type": "string",
      "description": "Details about the specific production or event that provided the inspiration."
    }
  },
  "required": [
    "inspired_project_name",
    "inspiring_play",
    "inspiration_source_details"
  ],
  "additionalProperties": false
}
