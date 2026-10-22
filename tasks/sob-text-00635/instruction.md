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
Anna Pavlova: Anna Pavlovna (Matveyevna) Pavlova (Russian: Анна Павловна (Матвеевна) Павлова ; February 12 [O.S. January 31] 1881 – January 23, 1931) was a Russian prima ballerina of the late 19th and the early 20th centuries.  She was a principal artist of the Imperial Russian Ballet and the Ballets Russes of Sergei Diaghilev.  Pavlova is most recognized for the creation of the role "The Dying Swan" and, with her own company, became the first ballerina to tour ballet around the world.

Avdotya Timofeyeva: Avdotia Timofeyeva (1739-?) , was a Russian ballerina.  She belonged to the first group of ballet dancers in the history of Russian ballet.  Timofejeva was a part of the first group of ballet students trained by the founder of the Russian ballet, Jean-Baptiste Landé, and was given a position in the ballet of the Imperial theatres in 1748.  She performed many parts in the ballets by Giovanni Battista Locatelli and Antonio Sacco.

Giselle: Giselle (French: "Giselle, ou les Wilis" ] ) is a romantic ballet in two acts.  It was first performed by the Ballet du Théâtre de l'Académie Royale de Musique at the Salle Le Peletier in Paris, France on Monday, 28 June 1841, with Italian ballerina Carlotta Grisi as Giselle.  The ballet was an unqualified triumph.  "Giselle" became hugely popular and was staged at once across Europe, Russia, and the United States.  The traditional choreography that has been passed down to the present day derives primarily from the revivals staged by Marius Petipa during the late 19th and early 20th centuries for the Imperial Ballet in St. Petersburg.

Theater des Westens: The Theater des Westens (Theatre of the West) is one of the most famous theatres for musicals and operettas in Berlin, Germany, located at 10–12 in Charlottenburg.  It was founded in 1895 for plays.  The present house was opened in 1896 and dedicated to opera and operetta.  Enrico Caruso made his debut in Berlin here, and the Ballets Russes appeared with Anna Pavlova.  In the 1930s it was run as the Volkstheater Berlin.  After World War II it served as the temporary opera house of Berlin, the Städtische Oper (Municipal Opera).  In 1961 it became the first theatre in Germany to show musicals.  Since then it has become the "German equivalent of Broadway extravaganzas", putting on plays and musical comedies.

Elena Smirnova: Elena Smirnova (Russian: Елена Александровна Смирнова , 6 May 1888 (O.S.)/18 May 1888 (N. S.) – 15 January 1934) was the last prima ballerina of the Mariinsky Theater in the Imperial period of Russia.  Starring in many leading roles, she often performed choreography created by Marius Petipa and .  Participating in early films of Germany and Russia, she made eight silent films and participated in the premiers of both the Ballets Russes in Paris and in the first performance of Russian ballet in Japan.

Alicia Markova: Dame Alicia Markova DBE (1 December 1910 – 2 December 2004) was an English ballerina and a choreographer, director and teacher of classical ballet.  Most noted for her career with Sergei Diaghilev's Ballets Russes and touring internationally, she was widely considered to be one of the greatest classical ballet dancers of the twentieth century.  She was the first British dancer to become the principal dancer of a ballet company and, with Dame Margot Fonteyn, is one of only two English dancers to be recognised as a prima ballerina assoluta.  Markova was a founder dancer of the Rambert Dance Company, The Royal Ballet and American Ballet Theatre, and was co-founder and director of the English National Ballet.

John Clifford (choreographer): John Clifford, born June 12th is the founder / artistic director of the original Los Angeles Ballet (1974–1985), and the chamber sized touring ensemble, Ballet of Los Angeles (1988–1991) and the creator of “CASABLANCA, THE DANCE” produced by Warner Bros.  Theatre Ventures, Inc. (which premiered in Beijing, China at the historic "Great Hall of the People" in 2005) and his Los Angeles Dance Theater.  Before that time,Clifford was a principal dancer and choreographer with George Balanchine’s New York City Ballet, (1966–1974) and guest artist from 1974–1980, and was widely considered to be Balanchine’s protégé (Saturday Review).  He choreographed his first (of 8) ballets for the NYC Ballet under Balanchine at age 20 thus making him the 2nd youngest choreographer in history ever to be attached to a major company.  The first was Balanchine himself who was 20 yrs-old when he choreographed his first ballet for Serge Diaghilev's "Ballets Russes."  During his time with Balanchine, in his early 20's, he also was a guest choreographer with co's ranging from the San Francisco Ballet, to the Royal Winnipeg Ballet, to the Deutsche Oper Ballet in Berlin.  Clifford's works were also featured in many TV shows and movies, such as "Flashdance," "The Man Who Loved Women," and TV series such as "Dynasty," "Glitter," and other shows produced by Blake Edwards and Aaron Spelling.

Russian Ballet (book): Russian Ballet is an artist's book by the English artist David Bomberg published in 1919.  The work describes the impact of seeing a performance of Diaghilev's "Ballets Russes", and is based on a series of drawings Bomberg had done around 1914, while associated with the Vorticist group of avant-garde artists in London.  Centred on Wyndham Lewis and Ezra Pound, the movement flourished briefly 1914–1915, before being dispersed by the impact of the First World War.  The only surviving example of a vorticist artist's book, the work can be seen as a parody of Marinetti's seminal futurist book "Zang Tumb Tumb", using similar language to the Italian's work glorifying war, ("Methodic discord startles ..."), but instead praising the impact of watching the decidedly less macho "Ballets Russes" in full flow.

Tamara Karsavina: Tamara Platonovna Karsavina (Russian: Тама́ра Плато́новна Карса́вина , 10 March 1885 – 26 May 1978) was a Russian prima ballerina, renowned for her beauty, who was a principal artist of the Imperial Russian Ballet and later of the Ballets Russes of Serge Diaghilev.  After settling in Britain at Hampstead in London, she began teaching ballet professionally and became recognised as one of the founders of modern British ballet.  She assisted in the establishment of The Royal Ballet and was a founder member of the Royal Academy of Dance, which is now the world's largest dance-teaching organisation.

Cesare Pugni: Cesare Pugni (Russian: Цезарь Пуни ) (] ; 31 May 1802–26 January [O.S. 14 January] 1870 ) born in Genoa, was an Italian composer of ballet music, a pianist and a violinist.  In his early career he composed operas, symphonies, and various other forms of orchestral music.  Pugni is most noted for the ballets he composed for Her Majesty's Theatre in London (1843–1850), and for the Imperial Theatres in St. Petersburg, Russia (1850–1870).  The majority of his ballet music was composed for the works of the ballet master Jules Perrot, who mounted nearly every one of his ballets to scores by Pugni.  In 1850 Perrot departed London for Russia, having accepted the position of "Premier maître de ballet" of the St. Petersburg Imperial Theatres at the behest of Carlotta Grisi, who was engaged as "Prima ballerina".  Cesare Pugni followed Perrot and Grisi to Russia, and remained in the imperial capital even after Grisi's departure in 1853 and Perrot's departure in 1858.  Pugni went on the compose for Perrot's successors Arthur Saint-Léon and Marius Petipa, serving as the Imperial Theatre's official composer of ballet music until his death in 1870.

Question: The Theater des Westens (Theatre of the West) is one of the most famous theatres for musicals and operettas in Berlin, Germany, here Ballets Russes appeared with which Russian prima ballerina of the late 19th and the early 20th centuries, and was  a principal artist of the Imperial Russian Ballet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ballerina_name": {
      "type": "string",
      "description": "The name of the prima ballerina."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the ballerina."
    },
    "title": {
      "type": "string",
      "description": "The professional title of the ballerina."
    },
    "theatre_of_performance": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the theatre where the performance took place."
        },
        "location": {
          "type": "string",
          "description": "The city and country of the theatre."
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "performing_company": {
      "type": "string",
      "description": "The name of the ballet company that performed at the theatre."
    },
    "imperial_ballet_role": {
      "type": "string",
      "description": "The role of the ballerina within the Imperial Russian Ballet."
    },
    "active_period": {
      "type": "string",
      "description": "The period during which the ballerina was active."
    }
  },
  "required": [
    "ballerina_name",
    "nationality",
    "title",
    "theatre_of_performance",
    "performing_company",
    "imperial_ballet_role",
    "active_period"
  ],
  "additionalProperties": false
}
