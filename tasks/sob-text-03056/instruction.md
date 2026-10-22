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
Babylon 5: Final Reckoning – The Fate of Bester: Babylon 5: Final Reckoning – The Fate of Bester is a "Babylon 5" novel by J. Gregory Keyes.  It recounts the story of the final years of Alfred Bester, hiding, wanted for crimes committed during his time in Psi-Corp.

E. Howard Hunt: Everette Howard Hunt Jr. (October 9, 1918 – January 23, 2007), better known as E. Howard Hunt, was an American intelligence officer and writer.  From 1949 to 1970, Hunt served as an officer in the Central Intelligence Agency (CIA).  Along with G. Gordon Liddy and others, Hunt was one of the Nixon administration "plumbers", a secret team of operatives charged with fixing "leaks" – real or perceived causes of confidential administration information being leaked to outside parties.  Hunt and Liddy plotted the Watergate burglaries and other undercover operations for the Nixon administration.  In the ensuing Watergate scandal, Hunt was convicted of burglary, conspiracy, and wiretapping, eventually serving 33 months in prison.

Redemolished: Redemolished is a collection of short stories, interviews, and other articles and essays by science fiction author Alfred Bester.  Published in 2000 (thirteen years after Bester's death) by iBooks, inc, ISBN  , edited by Richard Raucci.

Golem100: Golem is science fiction novel by American writer Alfred Bester.  Currently out of print, it was published by Simon & Schuster in 1980.  It was based on Bester's short story "The Four-Hour Fugue".

Alfred Bester: Alfred Bester (December 18, 1913 – September 30, 1987) was an American science fiction author, TV and radio scriptwriter, magazine editor and scripter for comic strips and comic books.  Though successful in all these fields, he is best remembered for his science fiction, including "The Demolished Man", winner of the inaugural Hugo Award in 1953.

Tender Loving Rage: Tender Loving Rage is a novel by science fiction author Alfred Bester, published posthumously in 1991, four years after Bester's death in 1987.  In his 1991 article, "Alfred Bester's "Tender Loving Rage"" (reprinted in Platt's "Loose Canon" [2001]), his friend Charles Platt explains that Bester wrote the novel around 1959 using the title "Tender Loving Rape".  The book went unsold for many years, until Platt (who had read the manuscript much earlier while working at Avon in 1972) persuaded Bester to allow him to get the book published by a small press; Platt suggested the change of title and Bester agreed.

Time is the Traitor: "Time Is the Traitor" is a science fiction short story by American writer Alfred Bester, originally published in "The Magazine of Fantasy and Science Fiction" in September, 1953.  It is included in the Bester collections "The Dark Side of the Earth" (1964), "Star Light, Star Bright" (1976) and "Virtual Unrealities" (1997) and has been extensively anthologized.

The Space Opera Renaissance: The Space Opera Renaissance is an anthology of short science fiction that fits the definition of space opera: adventure stories of grand vision, where the majority of the action happens somewhere other than Earth.  Meant to be an overview from the pulp fiction era to modern times, it is chronologically-organized and very thick (944 pages) but lacks representation by noted pioneers of the genre such as E. E. "Doc" Smith, Jack Vance and Alfred Bester, focusing more on the next wave.  It was edited by David G. Hartwell and Kathryn Cramer.  A hardcover edition was published by Tor Books in July 2006 and a trade paperback edition in July 2007.

The Demolished Man: The Demolished Man is a science fiction novel by American writer Alfred Bester, which was the first Hugo Award winner in 1953.  An example of inverted detective story, it was first serialized in three parts, beginning with the January 1952 issue of "Galaxy Science Fiction", followed by publication of the novel in 1953.  The novel is dedicated to "Galaxy"'s editor, H. L. Gold, who made suggestions during its writing.  Bester's title was "Demolition!" , but Gold talked him out of it.

Alfred Bester (Babylon 5): Alfred Bester is a "Babylon 5" character played by Walter Koenig.  He is a senior Psi Cop and a recurring antagonist in the series.  J. Michael Straczynski named the character after the science fiction writer Alfred Bester, since telepathy is a recurring theme in his work (most notably "The Demolished Man", which partly may have inspired the Psi corps and the "death of personality" legal punishment in the Babylon 5 universe).

Question: Who spent more time in prison, E. Howard Hunt or Alfred Bester?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "individuals_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "prison_time_months": {
            "type": "integer",
            "description": "The duration of time spent in prison in months, if applicable."
          },
          "prison_status_note": {
            "type": "string",
            "description": "A note regarding prison status if no specific duration is mentioned."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Details of the individuals whose prison time is being compared."
    },
    "comparison_outcome": {
      "type": "string",
      "description": "A summary statement of who spent more time in prison."
    },
    "person_with_more_prison_time": {
      "type": "string",
      "description": "The name of the person who spent more time in prison."
    },
    "duration_of_more_prison_time_months": {
      "type": "integer",
      "description": "The duration in months for the person who spent more time in prison."
    }
  },
  "required": [
    "individuals_compared",
    "comparison_outcome",
    "person_with_more_prison_time",
    "duration_of_more_prison_time_months"
  ],
  "additionalProperties": false
}
