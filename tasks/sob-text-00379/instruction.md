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
Homer's Triple Bypass: "Homer's Triple Bypass" is the eleventh episode in the fourth season of "The Simpsons".  It originally aired on the Fox network in the United States on December 17, 1992.  In the episode, Homer Simpson suffers a heart attack when Mr. Burns shouts at him at work.  Dr. Hibbert tells Homer that he needs a triple bypass, but the Simpson family resorts to a discount surgeon after learning how expensive the operation would be in a regular hospital.  The episode was written by Gary Apple and Michael Carrington and directed by David Silverman.

Dan Castellaneta: Daniel Louis Castellaneta ( ; born October 29, 1957) is an American actor, voice actor, comedian and screenwriter.  Noted for his long-running role as Homer Simpson on the animated television series "The Simpsons", he also voices many other characters for the show, including Abraham "Grampa" Simpson, Barney Gumble, Krusty the Clown, Sideshow Mel, Groundskeeper Willie, Mayor Quimby and Hans Moleman.

Clown in the Dumps: "Clown in the Dumps" is the season premiere of the twenty-sixth season of the American animated television series "The Simpsons", and the 553rd episode of the series overall.  It first aired in the United States on the Fox network on September 28, 2014, with "The Simpsons Guy", a crossover episode of "Family Guy" with "The Simpsons", airing afterwards.  This episode was dedicated in memory of Louis Castellaneta, the father of "The Simpsons" voice actor Dan Castellaneta.  It was written by Joel H. Cohen and directed by Steven Dean Moore, with Don Hertzfeldt directing a sequence in the opening titles.  Jeff Ross, Sarah Silverman and David Hyde Pierce guest starred as themselves, with Jackie Mason and Kelsey Grammer reprising their respective roles as Rabbi Krustofski and Sideshow Bob, while Maurice LaMarche voiced several minor characters.

Blame It on Lisa: "Blame It on Lisa" is the fifteenth episode of the thirteenth season of the American animated sitcom "The Simpsons".  In the episode, the Simpson family goes to Rio de Janeiro, Brazil in search of a Brazilian orphan named Ronaldo whom Lisa has been sponsoring.  Lisa used to receive a letter from Ronaldo every month, but that recently stopped and according to personnel at the orphanage, he is missing.  As the Simpsons search through Rio de Janeiro, Homer is kidnapped and in order to free him the family must pay a ransom of $50,000, which they do not have.  Lisa soon discovers that Ronaldo has been working in a flamingo costume on the children's television series "Teleboobies", which is the reason he left the orphanage.  Ronaldo finally meets up with the Simpsons and gives them the $50,000 they need to rescue Homer.

A Short Story About Love: "A Short Story About Love" is the fifteenth episode of the fourth season of the Fox science-fiction drama television series "Fringe", and the series' 80th episode overall.  The series follows members of a Federal Bureau of Investigation "Fringe Division" team based in Boston, Massachusetts that uses "fringe" science and FBI investigative techniques to investigate a series of unexplained, often ghastly occurrences, which are related to mysteries surrounding a parallel universe.  "A Short Story About Love" centered on a scientist extracting the pheromones of his victims, all male spouses, and using the resulting substances as a perfume to get close to their wives.  While the Fringe team investigates, Peter learns more about the Observer September.

Michael Carrington (voice actor): Michael Carrington is an American comic writer and voice actor best known for his work on the animated series "The Simpsons".  He co-wrote the episode "Homer's Triple Bypass" with Gary Apple and has provided occasional voicework, most notably as Sideshow Raheem (Krusty's militant black sideshow partner in the 1970s) in "I Love Lisa", the black comedian who does the joke about black drivers versus white drivers in "Homer and Apu", the drill sergeant in "Simpson Tide," and a sportscaster in "Million Dollar Abie".

Wedding for Disaster: "Wedding for Disaster" is the fifteenth episode of the twentieth season of "The Simpsons".  It originally aired on the Fox network in the United States on March 29, 2009.  In the episode, Marge and Homer's second marriage turns out to be invalid, so they decide to get married again.  Right before the remarriage, Homer goes missing, and Bart and Lisa suspect that he has been kidnapped by Sideshow Bob.  The episode was written by Joel H. Cohen and directed by Chuck Sheetz.  It features a guest appearance by Kelsey Grammer as Sideshow Bob.  Since airing, the episode has received mostly positive reviews from television critics.  It was viewed by 6.58 million viewers in its original American broadcast.

Project Runway Philippines: Project Runway Philippines is the Philippine adaptation of the American reality show "Project Runway".  This reality television series, which aims to find "the next big Filipino fashion designer," is produced by Solar Entertainment Corporation and Unitel Productions.  It is shown on ETC.  The series has an erratic airing schedule, as seasons 1 and 2 aired in 2008 and 2009, season 3 in 2012, and season 4 in 2105.  The show was hosted by model and actress Teresa Herrera during the first two seasons.  She was replaced by Filipina fashion legend Tweetie de Leon.  Fashion designer Jojie Lloren serves as mentor since the first season while Filipino top model and lifestyle feature writer Apples Aberin and fashion designer Rajo Laurel complete the judging panel.  The series fourth season ended on September 20, 2015.

Citizen Joe: "Citizen Joe" is the fifteenth episode for season eight of the Canadian-American military science fiction television series "Stargate SG-1".  The episode features known voice actor Dan Castellaneta, who voices Homer Simpson in "The Simpsons".  The episode was written by executive producer Robert C. Cooper, the episode was directed by Andy Mikita.  The episode received a below average Nielsen household rating and received no syndication rating to compare.  The episode got strong reviews from major media publishers worldwide.

I Love Lisa: "I Love Lisa" is the fifteenth episode of "The Simpsons"<nowiki>'</nowiki> fourth season.  It originally aired on the Fox network in the United States on February 11, 1993.  In the episode, Lisa gives Ralph Wiggum a Valentine's Day card when she sees that he has not received any.  Ralph reads too much into Lisa's gesture and, much to Lisa's dismay, relentlessly pursues her with affection.  Lisa snaps at Ralph and angrily tells him they are not together and that she never liked him.  Heartbroken, Ralph channels his feelings into his performance as George Washington in the school's President's Day pageant.  After a thunderous applause from the audience, he is able to accept Lisa as just a friend.

Question: Michael Carrington is an American comic writer and voice actor best known for his work on which animated series, he did voicework, most notably as Sideshow Raheem (Krusty's militant black sideshow partner in the 1970s) in "I Love Lisa", the fifteenth episode of the series fourth season?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "person_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Roles or professions of the person."
    },
    "animated_series_name": {
      "type": "string",
      "description": "The name of the animated series the person is best known for."
    },
    "episode_details": {
      "type": "object",
      "properties": {
        "episode_title": {
          "type": "string",
          "description": "The title of the specific episode mentioned."
        },
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "episode_number": {
          "type": "integer",
          "description": "The episode number within its season."
        },
        "character_voiced": {
          "type": "string",
          "description": "The name of the character voiced by the person in the episode."
        },
        "character_description": {
          "type": "string",
          "description": "A brief description of the character voiced."
        }
      },
      "required": [
        "episode_title",
        "season_number",
        "episode_number",
        "character_voiced",
        "character_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_roles",
    "animated_series_name",
    "episode_details"
  ],
  "additionalProperties": false
}
