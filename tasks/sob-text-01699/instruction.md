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
Eva Ingeborg Scholz: Eva Ingeborg Scholz (born 16 February 1928) is a German film and television actress.  She made her debut in the title role of the 1948 film "1-2-3 Corona" and appeared regularly in films over the following decade.  From the early 1960s she appeared increasingly in television.

Key Largo (film): Key Largo is a 1948 film noir directed by John Huston and starring Humphrey Bogart, Edward G. Robinson and Lauren Bacall.  The supporting cast features Lionel Barrymore and Claire Trevor.  The movie was adapted by Richard Brooks and Huston from Maxwell Anderson's 1939 play of the same name, which played on Broadway for 105 performances in 1939 and 1940.

Robin Chatterjee: Robin Chatterjee is an Indian music director who has scored music for more than a hundred films.  Starting from 1948 film 1948 film Samapika, he has composed music for evergreen soundtracks such as Godhuli, "Bipasha", Sagarika, Mayamrigo etc.

Neil North: Neil North (18 October 19327 March 2007) was a British actor, best known for his role in the 1948 film adaptation of Terence Rattigan's play "The Winslow Boy".  North appeared in four other films released between 1948 and 1951, but did not make acting a full-time career.  After a hiatus of over 40 years however, he did return to the screen with three further credits towards the end of his life, including a role in the 1999 remake of "The Winslow Boy".

Dorothea Kent: Dorothea Kent (June 21, 1916 – August 23, 1990) was an American film actress.  She appeared in 42 films between 1935 and 1948.  In addition to her credited roles, she also had roles in 6 other films, including her last role in the 1948 film "The Babe Ruth Story".  She was born in St. Joseph, Missouri in 1916, and died in 1990 from breast cancer.  She was buried at the San Fernando Mission Cemetery.

3 Godfathers: 3 Godfathers is a 1948 American Western film directed by John Ford and filmed (although not set) primarily in Death Valley, California.  The screenplay, written by Frank S. Nugent and Laurence Stallings, is based on the novelette of the same name written by Peter B. Kyne.  Ford had already adapted the film once before in 1919 as "Marked Men."  The original silent adaptation by Ford is thought to be lost today.  The story is something of a retelling of the story of The Three Wise Men in an American Western context.  Ford decided to remake the story in Technicolor and dedicate the film to the memory of long-time friend Harry Carey, who starred in the 1919 film "Marked Men".  Carey's son, Harry Carey, Jr., plays one of the title roles in this 1948 film.

Dan Seymour: Dan Seymour (February 22, 1915 – May 25, 1993) was an American character actor who frequently played villains in Warner Bros. films.  He appeared in several Humphrey Bogart films, including "Casablanca", "Key Largo", and "To Have and Have Not".

Black Bart (film): Black Bart is a 1948 film starring Dan Duryea as the real-life cowboy bandit Charles Bolles.  The 80 minute film was shot in Technicolor.  Also known as Black Bart, Highwayman.

Kamini Kaushal: Kamini Kaushal (born February 24, 1927) is a Hindi film and television actress, who is most noted for her roles in films like "Neecha Nagar" (1946) which won the 1946 Palme d'Or (Golden Palm) at Cannes Film Festival and "Biraj Bahu" (1955) which won her the Filmfare Best Actress Award in 1955.  She played lead heroine in films from 1946 to 1963 wherein her roles in Do Bhai (1947), Shaheed (1948 film), Ziddi (1948 film), Shabnam (1949 film), Nadiya Ke Paar (1948 film), Arzoo (1950 film), Paras(1949), Namoona(1949), Jhanjar (1953), Aabroo (1956 film), Night Club (1958 film), Jailor (1958 film), Bade Sarkar and Godaan (1963) are considered her career's best performances.  She played character roles since 1963 and was critically acclaimed for her performances in Shaheed (1965), in 3 films of Rajesh Khanna like Prem Nagar, Do Raaste, Maha Chor and with Sanjeev Kumar - "Anhonee" and 8 films with Manoj Kumar.

Dan Seymour (announcer): Dan Seymour (June 28, 1914 - July 27, 1982) was an announcer in the era of old-time radio and in the early years of television and later became an advertising executive.

Question: Dan Seymour appeared in a 1948 film by what director?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film the actor appeared in."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    }
  },
  "required": [
    "actor_name",
    "film_title",
    "film_year",
    "director_name"
  ],
  "additionalProperties": false
}
