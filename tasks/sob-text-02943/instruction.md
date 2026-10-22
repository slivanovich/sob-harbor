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
Lost Man Booker Prize: The Lost Man Booker Prize was a special edition of the Man Booker Prize awarded by a public vote in 2010 to a novel from 1970 as the books published in 1970 were not eligible for the Man Booker Prize due to a rules alteration; until 1970 the prize was awarded to books published in the previous year, while from 1971 onwards it was awarded to books published the same year as the award.  The prize was won by J. G. Farrell for "Troubles".

The Creature of the Sunny Side Up Trailer Park: The Creature of the Sunnyside Up Trailer Park, originally titled "Bloodhead", is a 2004 comedy/horror film directed by Christopher Coppola.  The lead characters, one black and one white and both racists, are Donnie played by Andre Ware and Doug played by Steve Hedden.  They co-inherit a trailer park near Joshua Tree National Monument.  Despite their antagonism, they join forces to battle a monster created by retired cultists living in the park and stalking its other denizens.  Eventually they discover that they are fraternal twins whose Caucasian archeologist mother Shirley Jones was married to an African-American serviceman.  The film also stars Bernie Kopell, Lynda Carter, Fort Atkinson, Stephanie Dees, T'Keyah Crystal Keymáh and Frank Gorshin.

Russian Booker Prize: The Russian Booker Prize (Russian: Русский Букер , "Russian Booker") is a Russian literary award modelled after the Man Booker Prize.  It was inaugurated by English Chief Executive Sir Michael Harris Caine in 1992.  The country's premier literary prize, it is awarded to the best work of fiction written in the Russian language each year as decided by a panel of judges, irrespective of the writer's citizenship.  s of 2012 , the chair of the Russian Booker Prize Committee is British journalist George Walden.  The prize is the first Russian non-governmental literary award since the country's 1917 Revolution.

Adverse Childhood Experiences (ACEs) Movement: The Adverse Childhood Experiences (ACEs) Movement is a set of grassroots initiatives developing interventions and "tests of change" to reduce the incidence and societal effects of Adverse Childhood Experiences and to promote healing from these experiences.

Europa (novel): Europa is a stream of consciousness novel by Tim Parks, first published in 1997.  It was shortlisted for the Booker Prize in that year, losing out to Arundhati Roy's "The God of Small Things".

The God of Small Things: The God of Small Things (1997) is the debut novel of Indian writer Arundhati Roy.  It is a story about the childhood experiences of fraternal twins whose lives are destroyed by the "Love Laws" that lay down "who should be loved, and how.  And how much."  The book explores how the small things affect people's behavior and their lives.  It won the Booker Prize in 1997.

Twin: Twins are two offspring produced by the same pregnancy.  Twins can be either "monozygotic" ("identical"), meaning that they develop from one zygote, which splits and forms two embryos, or "dizygotic" ("fraternal"), meaning that they develop from two different eggs.  In fraternal twins, each twin is fertilized by its own sperm cell.

Adverse Childhood Experiences Study: The Adverse Childhood Experiences Study (ACE Study) is a research study conducted by the American health maintenance organization Kaiser Permanente and the Centers for Disease Control and Prevention.  Participants were recruited to the study between 1995 and 1997 and have been in long-term follow up for health outcomes.  The study has demonstrated an association of adverse childhood experiences (ACEs) with health and social problems as an adult.  The study is frequently cited as a notable landmark in epidemiological research, and has produced more than 50 scientific articles and more than 100 conference and workshop presentations that look at the prevalence and consequences of ACEs.

Booker Prize: The Man Booker Prize for Fiction (formerly known as the Booker-McConnell Prize and commonly known simply as the Booker Prize) is a literary prize awarded each year for the best original novel, written in the English language and published in the UK.  The winner of the Man Booker Prize is generally assured international renown and success; therefore, the prize is of great significance for the book trade.  From its inception, only Commonwealth, Irish, and South African (and later Zimbabwean) citizens were eligible to receive the prize; in 2014, however, this eligibility was widened to any English-language novel.

Russian Little Booker Prize: The Russian Little Booker Prize (Малая Букеровская премия or Малый Букер) was an annual prize awarded in 1992-2001 for a nominated genre of writing.  It was established in 1992 as part of the Russian Booker Prize.  In 2000 it separated from the Russian Booker and became independent.  The prize was founded by Francis Greene (son of Graham Greene), whose sponsorship was anonymous until 2000.  The nominations differed every year, to compliment the Russian Booker which is awarded for novels only.

Question: Europa lost the Booker Prize in 1997 to what novel that is a story about the childhood experiences of fraternal twins whose lives are destroyed by Love Laws?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "winning_novel_title": {
      "type": "string",
      "description": "The title of the novel that won the prize."
    },
    "winning_author": {
      "type": "string",
      "description": "The author of the winning novel."
    },
    "prize_name": {
      "type": "string",
      "description": "The name of the literary prize awarded."
    },
    "award_year": {
      "type": "integer",
      "description": "The year the prize was awarded."
    },
    "losing_novel_title": {
      "type": "string",
      "description": "The title of the novel that was shortlisted but did not win."
    },
    "novel_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key themes or plot points of the winning novel as described in the context."
    }
  },
  "required": [
    "winning_novel_title",
    "winning_author",
    "prize_name",
    "award_year",
    "losing_novel_title",
    "novel_themes"
  ],
  "additionalProperties": false
}
