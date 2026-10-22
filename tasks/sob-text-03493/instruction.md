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
Mary (1985 TV series): Mary is an American sitcom that aired on CBS from December 11, 1985, to April 8, 1986.  The series stars Mary Tyler Moore in her return to series television after an absence of over six years, during which time she appeared on Broadway in "Whose Life Is It Anyway? " and in the dramatic film "Ordinary People".  After "The Mary Tyler Moore Show", her subsequent ventures into series television on the variety shows "Mary" (1978) and "The Mary Tyler Moore Hour" (1979) had been short-running ratings disasters, and Moore decided to return to the sitcom format which had brought her the greatest television success; the sitcom nonetheless met the same fate as the variety shows.

Flirting with Disaster (film): Flirting with Disaster is a 1996 American black comedy film written and directed by David O. Russell about a young father's search for his biological parents.  The film stars Ben Stiller, Patricia Arquette, Téa Leoni, Mary Tyler Moore, George Segal, Glenn Fitzgerald, Alan Alda and Lily Tomlin.  It was screened out of competition in the Special Screenings section at the 1996 Cannes Film Festival.

Mary and Rhoda: Mary and Rhoda is a 2000 American made-for-television comedy-drama film starring Mary Tyler Moore and Valerie Harper reprising their roles as Mary Richards and Rhoda Morgenstern from the 1970–77 sitcom "The Mary Tyler Moore Show".

Mary Richards: Mary Richards, portrayed by Mary Tyler Moore, is the main character of the television sitcom "The Mary Tyler Moore Show".

Mary Tyler Moore: Mary Tyler Moore (December 29, 1936 – January 25, 2017) was an American actress, known for her roles in the television sitcoms "The Mary Tyler Moore Show" (1970–1977), in which she starred as Mary Richards, a single woman working as a local news producer in Minneapolis, and "The Dick Van Dyke Show" (1961–1966), in which she played Laura Petrie, a former dancer turned Westchester homemaker, wife and mother.  Her film work includes 1967's "Thoroughly Modern Millie" and 1980's "Ordinary People", in which she played a role that was very different from the television characters she had portrayed, and for which she was nominated for an Academy Award for Best Actress.

Nancy Walker: Nancy Walker (May 10, 1922 – March 25, 1992) was an American actress and comedian of stage, screen, and television.  She was also a film and television director (most notably of "The Mary Tyler Moore Show", on which she also made several guest appearances).  During her five-decade long career, she may be best remembered for her long-running roles as Mildred on "McMillan & Wife" and Ida Morgenstern, who first appeared on several episodes of "The Mary Tyler Moore Show" and later became a prominent recurring character on the spinoff series "Rhoda".

Phyllis (TV series): Phyllis is an American sitcom that aired on CBS from September 8, 1975, to March 13, 1977.  Created by Ed Weinberger and Stan Daniels, it was the second spin-off of "The Mary Tyler Moore Show" (the first being "Rhoda").  The show starred Cloris Leachman as Phyllis Lindstrom, who was previously Mary Richards' landlady on "The Mary Tyler Moore Show".

Lou Grant (TV series): Lou Grant is an American drama series starring Ed Asner in the title role as a newspaper editor that aired on CBS from September 20, 1977 to September 13, 1982.  The series was the third spin-off of the sitcom "The Mary Tyler Moore Show".  "Lou Grant" was created by "The Mary Tyler Moore Show" co-creators James L. Brooks and Allan Burns, along with Gene Reynolds.

Mary Tyler Moore filmography and awards: Mary Tyler Moore (December 29, 1936 – January 25, 2017) was an American actress, known for her roles in the television sitcoms "The Mary Tyler Moore Show" (1970–1977), in which she starred as Mary Richards, a thirtyish single woman who worked as a local news producer in Minneapolis, and "The Dick Van Dyke Show" (1961–1966), in which she played Laura Petrie, a former dancer turned Westchester homemaker, wife and mother.  Her notable film work includes 1967's "Thoroughly Modern Millie" and 1980's "Ordinary People", in which she played a role that was very different from the television characters she had portrayed, and for which she was nominated for an Academy Award for Best Actress.

The Mary Tyler Moore Show opening sequence: "The Mary Tyler Moore Show" opening sequence is an element of the American television series "The Mary Tyler Moore Show".  In 1999, "Entertainment Weekly" picked Mary Richards' hat toss at the end of the sequence as the 1970s' second-greatest television moment.  The theme song, "Love Is All Around", was written and performed by Sonny Curtis.

Question: Who is the actress known for her television sitcom "The Mary Tyler Moore Show" that appeared in Flirting with Disaster?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "known_for_tv_show": {
      "type": "string",
      "description": "The television show the actress is known for."
    },
    "appeared_in_film": {
      "type": "string",
      "description": "The film the actress appeared in."
    },
    "is_main_star_of_tv_show": {
      "type": "boolean",
      "description": "Indicates if the actress was the main star of the TV show."
    }
  },
  "required": [
    "actress_name",
    "known_for_tv_show",
    "appeared_in_film",
    "is_main_star_of_tv_show"
  ],
  "additionalProperties": false
}
