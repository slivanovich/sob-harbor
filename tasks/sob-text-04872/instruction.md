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
The Experts (1989 film): The Experts is a 1989 American comedy film starring John Travolta, Arye Gross and Kelly Preston.  It was written by Steven Greene, Eric Alter, and Nick Thiel and directed by Dave Thomas.  During production there were several uncredited rewrites of the script performed by Thomas at the request of Paramount chief Ned Tannen.

Nicolas Rimsky: Nicolas Rimsky (Russian: Николай Алекса́ндрович Римский ; born Nikolai Alexandrovich Kurmashov; February 18, 1886 – September 5, 1941) was a Russian-born French film actor, director and writer.  He was born in Moscow, Russia.  In 1931, he directed and starred in "Pas sur la bouche" ("Not on the Mouth"), based on an operetta by André Barde.

Mark Ellis (actor): Mark Ellis is a Canadian actor and screenwriter.  He is the co-showrunner and executive producer of the CBC series X Company which premieres February 18, 2015 on CBC.  He also co-created and executive produced "Flashpoint" which aired on CBS, CTV, ION Television and networks around the world.  The series was awarded the Academy Board of Directors Tribute for Outstanding and Enduring Contribution to Canadian Television, in addition to a Canadian Screen Award (2013) and Gemini Award (2013) for Best Dramatic Series.  Ellis and his spouse Stephanie Morgenstern have received Gemini and Writers Guild awards for their writing in the series.  He has appeared in television, film and theatre, including the Emmy-award winning "Dark Oracle".  He co-wrote and starred in the Genie-nominated short film" Remembrance".

Maris Valainis: Maris Valainis (Latvian: Māris Valainis) (born on February 18, 1963) is an American construction consultant and a former actor, best known for his role in the 1986 film "Hoosiers", in which he played the character of Jimmy Chitwood, a basketball player who makes a last-second shot to win the Indiana state high school championship.  The character is based upon Bobby Plump, who actually accomplished that feat in 1954.

Chieko Honda: Chieko Honda (本多 知恵子 , Honda Chieko , March 28, 1963 – February 18, 2013) was a Japanese actress and voice actress.  During her life, she was attached to Tokyo Actor's Consumer's Cooperative Society and Mix Max; she was attached to Aoni Production at the time of her death.  On February 18, 2013, Honda died of multiple forms of colon cancer while undergoing treatment.

Colman Andrews: Colman Robert Hardy Andrews (born February 18, 1945) is an American writer and editor and authority on food and wine.  In culinary circles, he is best known for his association with "Saveur" magazine, which he founded with Dorothy Kalins, Michael Grossman, and Christopher Hirsheimer in 1994 and where he served as editor-in-chief from 2001 until 2006.  After resigning from the magazine in 2006, he became the restaurant columnist for "Gourmet".  In 2010, he helped launch a food and drink website, The Daily Meal, and serves as its editorial director.  He is considered one of the world's foremost experts on Spanish cuisine, particularly that of the Catalonia region.

John Travolta: John Joseph Travolta (born February 18, 1954) is an American actor, producer, dancer, and singer.  Travolta first became known in the 1970s, after appearing on the television series "Welcome Back, Kotter" (1975–1979) and starring in the box office successes "Saturday Night Fever" (1977) and "Grease" (1978).  His acting career declined through the 1980s, but enjoyed a resurgence in the 1990s with his role in "Pulp Fiction" (1994), and he has since starred in films such as "Face/Off" (1997), "Swordfish" (2001), "Wild Hogs", and "Hairspray" (both 2007).

Josephine Sophia White Griffing: Josephine Sophia White Griffing (December 18, 1814February 18, 1872) was an American reformer who campaigned against slavery and for women's rights.  She was born in Hebron, Connecticut on December 18, 1814 but later settled in Litchfield, Ohio.  There she worked as a lecturer for the Western Anti-Slavery Society and Ohio Women's Rights Association.  At the end of the American Civil War she moved to Washington, D.C., to help work with the unemployed freedmen.  Much of her work was done through the Freedmen's Bureau, where she worked as an assistant to the assistant commissioner and as an agent.  Griffing was also active in several women's rights organizations.  She died in Washington, D.C. on February 18, 1872.

Berlin Conference (1954): The Berlin Conference of 1954 was a meeting of the "Big Four" foreign ministers of the United States (John Foster Dulles), Britain (Anthony Eden), France (Georges Bidault), and the Soviet Union (Vyacheslav Molotov), on January 25-February 18, 1954.

Bonar Bain: Bonar Stewart Bain (February 4, 1923 – February 18, 2005) was a Canadian actor and the identical twin brother of actor Conrad Bain, who starred in the television sitcom "Diff'rent Strokes" as Phillip Drummond and "Maude" as Arthur Harmon.  He once played a fictional “evil” twin to Conrad (“Hank Bain”) in an episode of "SCTV", as well as Arthur (Conrad Bain)'s twin brother Arnold on "Maude".

Question: What actor who starred in the film "The Experts" was born on February 18, 1954?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "film_starred_in": {
      "type": "string",
      "description": "The title of the film the actor starred in."
    },
    "birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the actor in YYYY-MM-DD format."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the actor."
    },
    "matches_criteria": {
      "type": "boolean",
      "description": "True if the actor matches all criteria in the question."
    }
  },
  "required": [
    "actor_name",
    "film_starred_in",
    "birth_date",
    "birth_year",
    "matches_criteria"
  ],
  "additionalProperties": false
}
