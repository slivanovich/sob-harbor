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
Ennui (sonnet): "Ennui" is a sonnet by Sylvia Plath published for the first time in November 2006 in the online literary journal "Blackbird" .  Sylvia Plath wrote the Petrarchan sonnet “Ennui” during her undergraduate years at Smith College.

Otto Plath: Otto Emil Plath (April 13, 1885 – November 5, 1940) was a German American author, a professor of biology and German at Boston University, and an entomologist, with a specific expertise on bees.  He was the father of American poet Sylvia Plath, Warren Plath, and the husband of Aurelia Plath.  He wrote the 1934 book, "Bumblebees and Their Ways".  He is notable for being the probable subject of one of his daughter's most well-known poems, "Daddy".

David Malouf: David George Joseph Malouf (born 20 March 1934) is an Australian writer.  He was awarded the Neustadt International Prize for Literature in 2000, his 1993 novel "Remembering Babylon" won the International IMPAC Dublin Literary Award in 1996, he won the inaugural Australia-Asia Literary Award in 2008, and he was shortlisted for the Booker Prize.  In 2016, he received the Australia Council Award for Lifetime Achievement in Literature.

Sylvia Plath: Sylvia Plath ( ; October 27, 1932 – February 11, 1963) was an American poet, novelist, and short story writer.  Born in Boston, she studied at Smith College and Newnham College at the University of Cambridge before receiving acclaim as a poet and writer.  She married fellow poet Ted Hughes in 1956, and they lived together in the United States and then in England.  They had two children, Frieda and Nicholas, before separating in 1962.  Plath was clinically depressed for most of her adult life, and was treated multiple times with electroconvulsive therapy (ECT).  She committed suicide in 1963.

Sylvia (2003 film): Sylvia is a 2003 British biographical drama film directed by Christine Jeffs and starring Gwyneth Paltrow, Daniel Craig, Jared Harris, and Michael Gambon.  It tells the true story of the romance between prominent poets Sylvia Plath and Ted Hughes.  The film begins with their meeting at Cambridge in 1956 and ends with Sylvia Plath's suicide in 1963.

The Bell Jar: The Bell Jar is the only novel written by the American writer and poet Sylvia Plath.  Originally published under the pseudonym "Victoria Lucas" in 1963, the novel is semi-autobiographical, with the names of places and people changed.  The book is often regarded as a "roman à clef" since the protagonist's descent into mental illness parallels Plath's own experiences with what may have been clinical depression.  Plath died by suicide a month after its first UK publication.  The novel was published under Plath's name for the first time in 1967 and was not published in the United States until 1971, in accordance with the wishes of both Plath's husband, Ted Hughes, and her mother.  The novel has been translated into nearly a dozen languages.  The novel, though dark, is often read in high school English classes.

Sylvia Plath effect: The Sylvia Plath effect is the phenomenon that poets are more susceptible to mental illness than other creative writers.  The term was coined in 2001 by psychologist James C. Kaufman.  Although many studies (e.g., Andreasen, 1987; Jamison, 1989; Ludwig, 1995) have demonstrated that creative writers are prone to experience mental illness, this relationship has not been examined in depth.  This early finding has been dubbed "the Sylvia Plath effect", and implications and possibilities for future research are discussed.  Kaufman's work further demonstrated that female poets were more likely to experience mental illness than any other class of writers.  In addition, female poets were more likely to be mentally ill than other eminent women, such as politicians, actresses, and artists.

Winter Trees: Winter Trees is a 1971 posthumous collection of poetry by Sylvia Plath, published by her husband Ted Hughes.  Along with "Crossing the Water" it provides the remainder of the poems that Plath had written during her state of elevated creativity prior to her suicide.

Johnno: Johnno is a semi-autobiographical novel written by Australian author David Malouf and was first published in 1975.  It was Malouf's first novel.

Assia Wevill: Assia Wevill (15 May 1927 – 23 March 1969) was a German-born woman who escaped the Nazis at the beginning of World War II and emigrated to Mandate Palestine, then later the United Kingdom, where she had a relationship with the English poet Ted Hughes.  She killed herself and her four-year-old daughter Alexandra Tatiana Elise (nicknamed "Shura") in a fashion similar to that of Sylvia Plath, well-known writer and Hughes's first wife, who six years earlier had also committed suicide, by use of a gas oven.

Question: Who committed suicide in 1963, David Malouf or Sylvia Plath?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_who_committed_suicide": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who committed suicide."
        },
        "profession": {
          "type": "string",
          "description": "The primary profession of the person."
        },
        "suicide_year": {
          "type": "integer",
          "description": "The year the person committed suicide."
        }
      },
      "required": [
        "name",
        "profession",
        "suicide_year"
      ],
      "additionalProperties": false
    },
    "other_person_status": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the other person mentioned in the question."
        },
        "is_alive_in_context": {
          "type": "boolean",
          "description": "Indicates if the person is described as alive or no death date is provided in the context."
        },
        "death_details_available": {
          "type": "boolean",
          "description": "Indicates if death details (like year or cause) are available for this person in the context."
        }
      },
      "required": [
        "name",
        "is_alive_in_context",
        "death_details_available"
      ],
      "additionalProperties": false
    },
    "question_answered": {
      "type": "boolean",
      "description": "True if the question about who committed suicide has been answered."
    }
  },
  "required": [
    "person_who_committed_suicide",
    "other_person_status",
    "question_answered"
  ],
  "additionalProperties": false
}
