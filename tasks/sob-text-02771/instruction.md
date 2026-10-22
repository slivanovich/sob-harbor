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
Ralph Wiggum: Ralph Wiggum is a recurring character on the animated series "The Simpsons", voiced by Nancy Cartwright.  The son of Police Chief Wiggum and a classmate of Lisa Simpson, Ralph is best known as the show's resident oddball, and is noted for his non sequiturs and erratic behavior.  His lines range from nonsensical, or bizarre interpretations of a current event, to surprisingly profound statements that go over people's heads; and his behavior varies between blissfully unaware, to dim-witted, to awkwardly spontaneous, even occasionally straightforward.  The very nature of the character has undergone seemingly differing interpretations over the years and within various media.

Corrado Balducci: Monsignor Corrado Balducci (born May 11, 1923, in Italy; died September 20, 2008 in Italy) was a Roman Catholic theologian of the Vatican Curia, a close friend of the pope, a long-time exorcist for the Archdiocese of Rome, and a Prelate of the Congregation for the Evangelization of Peoples and the Society for the Propagation of the Faith.  He has written several books about the subliminal messages in rock and metal music, diabolic possessions, and extraterrestrials.

Wild Barts Can't Be Broken: "Wild Barts Can't Be Broken" is the eleventh episode of "The Simpsons"' tenth season.  It originally aired on the Fox network in the United States on January 17, 1999.  When Homer, Barney, Lenny, and Carl drunkenly vandalize Springfield Elementary School, it is blamed on the children of Springfield, prompting Chief Wiggum to impose a curfew.  The children respond by setting up a pirate radio show in which they reveal the embarrassing secrets of Springfield's adults.  The episode was written by Larry Doyle and directed by Mark Ervin.  The concept behind the episode originates from show producer Mike Scully always wanting to do an episode where the children would be subject to a curfew.  The episode received an 8.9 Nielsen rating, and mostly positive reviews from critics.

New Kids on the Blecch: "New Kids on the Blecch" is the fourteenth episode of the twelfth season of "The Simpsons".  It first aired on the Fox network in the United States on February 25, 2001.  In the episode, a music producer selects Bart, Nelson, Milhouse and Ralph to be members of the next hit boy band, who record songs containing subliminal messages about joining the Navy.

Erick Morillo: Erick Morillo is a Colombian-American DJ, music producer and record label owner.  Having produced under a number of pseudonyms, including Ministers De la Funk, The Dronez, RAW, Smooth Touch, RBM, Deep Soul, Club Ultimate and Li'l Mo Ying Yang, Morillo is best known for his international work in house music, in particular for the label Strictly Rhythm, and the 1993 hit "I Like to Move It", which he produced under the pseudonym Reel 2 Real, and which was featured in commercials, movies and ringtones.  His label Subliminal Records has produced the #1 Billboard Hot Dance Music/Club Play hit "Fun" by Da Mob, and won the "Muzik" magazine "Remixer of the Year" award in 1999.  Subliminal also brought attention to artists like Eddie Thoneick, Carl Kennedy and DJ DLG.  He is a three-time winner of DJ Awards "Best House DJ" in 1998, 2001 and 2003 and a three-time winner of "Best International DJ" in 2002, 2006 and 2009 receiving a total of 15 nominations in all from 1998-2010.

The Great Louse Detective: "The Great Louse Detective" is the sixth episode of the fourteenth season of the American animated television sitcom "The Simpsons".  It originally aired on the Fox network in the United States on December 15, 2002.  In the episode, the Simpson family wins a free spa weekend, and Homer is nearly killed when a mysterious figure locks him in a sauna.  Chief Wiggum decides to hire someone who can think like a murderer in order to find the mystery assailant.  Bart's mortal enemy Sideshow Bob is sent to live with the Simpsons so he can help find Homer's attempted killer, who turns out to be the son of a man whom Homer drove to insanity.  Since airing, the episode has received generally positive reviews from critics, though it has been cited as not being as good as some other Sideshow Bob episodes.  The episode's title is a parody of the 1986 Disney animated feature "The Great Mouse Detective".

The Parent Rap: "The Parent Rap" is the second episode and official premiere of the thirteenth season of "The Simpsons".  It originally aired on the Fox network in the United States on November 11, 2001.  In the episode, Bart and his father, Homer, are sentenced by the cruel judge Constance Harm to be tethered to each other as a result of Bart stealing Police Chief Wiggum's car.  Eventually, Homer's wife, Marge, is fed up with the punishment and cuts the rope, which instead leads to Judge Harm sentencing them to have their heads and hands locked up in wooden stocks.

Judas Priest: Judas Priest are an English heavy metal band formed in Birmingham, England, in 1969.  The band have sold close to 50 million albums to date.  They are frequently ranked as one of the greatest metal bands of all time.  Despite an innovative and pioneering body of work in the latter half of the 1970s, the band struggled with indifferent record production, repeated changes of drummer and lack of major commercial success or attention until 1980, when they adopted a more simplified sound on the album "British Steel", which helped shoot them to rock superstar status.  In 1989, they were named as defendants in an unsuccessful lawsuit alleging that subliminal messages on the song "Better By You, Better Than Me" had caused the suicide attempts of two young men.

Subliminal messages in popular culture: While the effectiveness of subliminal messages is often overstated in popular culture, its history in television shows, movies, music and novels have long lead many cultural idioms that persist today.

Marge on the Lam: "Marge on the Lam" is the sixth episode of "The Simpsons"<nowiki>'</nowiki> fifth season.  It originally aired on the Fox network in the United States on November 4, 1993.  When Marge invites her neighbor Ruth Powers to attend the ballet with her, the two become friends and begin to go out, making Homer jealous as he wants Marge to spend time with him.  Ruth and Marge agree to remain friends but not go out together after a large police pursuit with Chief Wiggum.  It was written by Bill Canterbury and directed by Mark Kirkland.  Phil Hartman, Pamela Reed and George Fenneman guest star.

Question: The son of Police Chief Wiggum is chosen by a music producer to record songs containing subliminal messages about what? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character who is the son of Police Chief Wiggum."
    },
    "parent_name": {
      "type": "string",
      "description": "The name of the character's parent."
    },
    "episode_details": {
      "type": "object",
      "properties": {
        "episode_title": {
          "type": "string",
          "description": "The title of the episode where the event occurred."
        },
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "air_date": {
          "type": "string",
          "description": "The original air date of the episode."
        }
      },
      "required": [
        "episode_title",
        "season_number",
        "air_date"
      ],
      "additionalProperties": false
    },
    "activity_description": {
      "type": "string",
      "description": "Description of the activity the character was selected for by the music producer."
    },
    "subliminal_message_content": {
      "type": "string",
      "description": "The content of the subliminal messages in the recorded songs."
    }
  },
  "required": [
    "character_name",
    "parent_name",
    "episode_details",
    "activity_description",
    "subliminal_message_content"
  ],
  "additionalProperties": false
}
