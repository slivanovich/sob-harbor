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
Grok Magazine: Grok Magazine is an Australian free student magazine.  The magazine is written and produced by Curtin University students and published by the Curtin Student Guild.  2009 would see 5 issues published, and approximately 10,000 copies distributed per issue.  These are distributed on the Curtin Bentley campus in Western Australia, as well as to many street location across the Perth metro area.

The Absynthe: Absynthe Magazine is a student magazine at Trent University.  Though commonly referred to as a newspaper, it is, according to its constitution, a magazine.  "Absynthe" does not have a stated political bias, because the articles are written and submitted by any members of the Trent community.  It was established in 1999 by Ken Giffen, Brad Harkness and Peter Read.  Matt Griem maintained the paper through its second edition.  In 2003, the organization formalized and created an executive board and a publication team.  The executive board consists of the president, editor, secretary, treasurer, and member representatives, while the publication team is made up of the editor, soliciting editor, production manager and production assistant.  It was in 2005 that the current editorial policy was written by Ted Cragg and Liz Zylstra and approved at the Annual General Meeting.  Absynthe Magazine receives funding via a $4.00 "(refundable)" levy from each full-time student.  ($2.00 from each nursing/part-time student).  Absynthe's website can be found at .

Motley Magazine: Motley Magazine is the award-winning student publication based in Ireland.  Originally set up in 2006 the magazine has evolved from a simple publication aimed at students around Ireland into the country's "Best Magazine" as awarded at the SMEDIA Awards in 2014, 2015 and 2016.  Motley has featured major names from the television, music and pop-culture industries.  To date, at the SMEDIA Awards, it is the most successful student magazine in Ireland.

Oxford Student Publications Limited: Oxford Student Publications Ltd (OSPL) is an independent student publishing house in Oxford that publishes the Cherwell student newspaper, ISIS student magazine, Bang Science Magazine, Keep Off the Grass freshers' magazine and Industry fashion magazine.

Future-Drama: "Future-Drama" is the fifteenth episode of "The Simpsons"<nowiki>'</nowiki> sixteenth season.  The 350th episode overall, it originally aired on the Fox network in the United States on April 17, 2005.  In the episode, Bart and Lisa stumble into Professor Frink's basement, and he gives them a look into their future as teenagers as they get ready for their high school graduation.  Matt Selman wrote the episode, and Mike B. Anderson served as director.  Amy Poehler and John DiMaggio guest-starred as the characters of Jenda and Bender respectively.

UPraw – UK Student Magazine: UPraw Magazine was a national UK student magazine distributed through various university-related sites, student unions and selected Blackwell bookstores from 2001 - 2002.  The magazine was based in Bournemouth.

A Star Is Born Again: "A Star Is Born Again" is the 13th episode from "The Simpsons"<nowiki>'</nowiki> fourteenth season.  It first aired on the Fox network in the United States on March 2, 2003.  The episode owes much of its plot to "Notting Hill" (1999).  While that film is about an actress (Julia Roberts) finding happiness with the owner of an independent bookstore, the Simpsons episode features Hollywood movie star Sara Sloane (Marisa Tomei) falling for Ned Flanders after visiting the Leftorium.

Matt Selman: Matthew "Matt" Selman (born September 9, 1971) is an American writer and producer.  Selman grew up in Massachusetts, attended the University of Pennsylvania and was editor-in-chief of student magazine "34th Street Magazine".  After considering a career in journalism, he decided to try to become a television writer.  After two years of failed spec scripts he was eventually hired to write an episode of "Seinfeld" in 1996.  Selman then joined the writing staff of "The Simpsons", where he has remained, rising to the position of executive producer.  He has written numerous episodes of the show, including "Natural Born Kissers", "Behind the Laughter", "Trilogy of Error", "Simpsons Bible Stories" (for which he won an Annie Award), "The Dad Who Knew Too Little" (for which he won a Writers Guild of America Award), and also "The Food Wife".  He also co-wrote the 2007 film adaptation of the show, as well as the video games "", "The Simpsons Hit and Run" and "The Simpsons Game".

Four Great Women and a Manicure: "Four Great Women and a Manicure" is the twentieth episode of the twentieth season of "The Simpsons".  First broadcast on the Fox network in the United States on May 10, 2009, it was the second Simpsons episode (after "Simpsons Bible Stories") to have four acts instead of the usual three.  The episode tells four tales of famous women featuring "Simpsons" characters in various roles: Selma as Queen Elizabeth I, Lisa as Snow White, Marge as Lady Macbeth and Maggie as Howard Roark from Ayn Rand's "The Fountainhead".

Impact (student magazine): Impact Magazine is the official student magazine of the University of Nottingham, it has been published in various forms and various names since 1939.  Run on a voluntary basis using funds from the Students' Union, the magazine is available free to students.  "Impact" also publishes a website, which has been online since 8 January 2006, and an app, which was launched in 2016.  In 2017, "Impact" won Best Magazine Design at the Student Publication Awards.

Question: The writer of the Simpsons episode "Future-Drama" was editor-in-chief of what student magazine?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "simpsons_episode_name": {
      "type": "string",
      "description": "The name of The Simpsons episode."
    },
    "episode_writer_name": {
      "type": "string",
      "description": "The name of the writer of the specified Simpsons episode."
    },
    "student_magazine_name": {
      "type": "string",
      "description": "The name of the student magazine where the writer served as editor-in-chief."
    }
  },
  "required": [
    "simpsons_episode_name",
    "episode_writer_name",
    "student_magazine_name"
  ],
  "additionalProperties": false
}
