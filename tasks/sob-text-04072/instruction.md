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
Classic X-Men: Classic X-Men, later retitled as X-Men Classic, is the Marvel Comics comic book series within the X-Men franchise that reprints classic X-Men stories.  The first issue was a partial reprint of "Giant-Size X-Men" #1 of the All-New All-Different X-Men era (originally published in 1975), and the other issues reprinted "Uncanny X-Men" #94-206, with the exceptions of #106, #110, and the "Days of Future Past" story from issues #141 and #142.  "Classic X-Men" initially printed additional back-up stories further delving into and explaining the original stories.  The series lasted 110 issues.

X-Men: Days of Future Past: X-Men: Days of Future Past is a 2014 American superhero film based on the fictional X-Men characters that appear in Marvel Comics.  Directed by Bryan Singer, it is the seventh installment of the "X-Men" film series and acts as a sequel to both 2006's "" and 2011's "".  The story, inspired by the 1981 "Uncanny X-Men" storyline "Days of Future Past" by Chris Claremont and John Byrne, focuses on two time periods, with Wolverine traveling back in time to 1973 to change history and prevent an event that results in doom for both humans and mutants.  The film features an ensemble cast, including Hugh Jackman, James McAvoy, Michael Fassbender, Jennifer Lawrence, Halle Berry, Anna Paquin, Ellen Page, Peter Dinklage, Ian McKellen and Patrick Stewart.  Simon Kinberg wrote the screenplay from a story conceived by Jane Goldman, himself, and Matthew Vaughn.

Days of Future Past (TV episodes): Days of Future Past is a two-part episodes from the animated TV series "X-Men Animated Series", based on the comic book story of the same name and Issue #8.  This episode has Bishop assuming Kitty Pryde's role from the comic version of this tale and his role from the comics to find a traitor within the ranks of the X-Men.  Storyboards from the episode have been published.

List of X-Men (TV series) episodes: The first "X-Men" animated series debuted on October 31, 1992 on the Fox Network as part of the "Fox Kids" Saturday morning lineup.  The plot was loosely adapted from famous storylines and events in the X-Men comics, such as the Dark Phoenix Saga, Days of Future Past, the Phalanx Covenant, and the Legacy Virus.  The show features a team line-up similar to that of the early 1990s X-Men comic books: the lineup largely resembles that of Cyclops' Blue Team, established in the early issues of .

Days of Future Present: "Days of Future Present" is a storyline published by Marvel Comics, appearing in the 1990 annuals of "Fantastic Four", "X-Factor", "New Mutants" and "Uncanny X-Men".  Centered on the appearance of an adult version of the powerful mutant Franklin Richards, it is a sequel to the popular "Days of Future Past" story arc from "Uncanny X-Men" #141–142 (January–February 1981).  The storyline unites the Fantastic Four, X-Factor, the New Mutants, and the remnants of a then-disbanded X-Men against a common foe from a dystopian alternate future.  It features the first appearance of Gambit, and the first encounter between Jean Grey and her alternate future daughter Rachel Summers.  Cyclops' baby son Nathan Christopher Charles Summers and the full-grown mutant antihero Cable are depicted in this story as two separate individuals, although they are subsequently revealed to be one and the same.

Days of Future Past: "Days of Future Past" is a storyline in the Marvel Comics comic book "The Uncanny X-Men" issues #141–142, published in 1981.  It deals with a dystopian future in which mutants are incarcerated in internment camps.  An adult Kate Pryde transfers her mind into her younger self, the present-day Kitty Pryde, who brings the X-Men to prevent a fatal moment in history that triggers anti-mutant hysteria.

Prime Sentinel: Prime Sentinels are an advanced type of Sentinel which exist in Marvel Comics.  They are a human/machine hybrid that uses nanotechnology from the "Days of Future Past" future.

Days of Future Past (disambiguation): Days of Future Past is an "X-Men" comic book storyline.

Bryan Singer: Bryan Jay Singer (born September 17, 1965) is an American film director, film producer, writer, and actor.  He is the founder of Bad Hat Harry Productions and he has produced or co-produced almost all of the films he has directed.

List of X-Men films cast members: The following is a list of cast members who have portrayed characters appearing in the "X-Men" film series, based upon the comic books of the same name.  Hugh Jackman appeared in the first seven films: he played James "Logan" Howlett / Wolverine in the original trilogy ("X-Men", "X2 - X-Men United", and "") and reprised his role in the prequel films "" and "", the latter in a cameo appearance.  He again starred in "The Wolverine" and "".  He appeared in photographic form in "Deadpool" and reprised his role as Wolverine in "" and one last stand-alone "Wolverine" film.  Patrick Stewart, Ian McKellen, Famke Janssen, Halle Berry, Anna Paquin, James Marsden and Shawn Ashmore have also appeared in the original trilogy and "Days of Future Past", with Stewart also making a cameo appearance in "Origins: Wolverine" and "The Wolverine", and Janssen and McKellen in "The Wolverine".  Rebecca Romijn also appeared in the original trilogy and made a cameo appearance in "First Class".

Question: In what month was the director of "X-Men: Days of Future Past" born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film in question."
    },
    "director_name": {
      "type": "string",
      "description": "The full name of the film's director."
    },
    "birth_month": {
      "type": "string",
      "description": "The month in which the director was born."
    }
  },
  "required": [
    "film_title",
    "director_name",
    "birth_month"
  ],
  "additionalProperties": false
}
