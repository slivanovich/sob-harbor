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
Under Capricorn: Under Capricorn is a 1949 British historical thriller film directed by Alfred Hitchcock about a couple in Australia who started out as lady and stable boy in Ireland, and who are now bound together by a horrible secret.  The film was based on the novel "Under Capricorn" (1937) by Helen Simpson, with a screenplay by James Bridie.  It was adapted to the screen by Hume Cronyn.  This was Hitchcock's second film in Technicolor, and like the preceding color film "Rope" (1948), it also featured 10-minute takes.

Alfred Hitchcock's Anthology – Volume 4: Alfred Hitchcock's Anthology – Volume 4 is the fourth installment of "Alfred Hitchcock's Anthology", one of the many Alfred Hitchcock story collection books; edited by Eleanor Sullivan.  Originally published in hardcover as "Alfred Hitchcock's Tales to Scare You Stiff" in 1978, the book includes 26 short stories and a short novel called "The Graveyard Shift" by William P. McGivern.  Also, within the 26 short stories is "The Green Heart" by Jack Ritchie which was made into the 1971 film "A New Leaf".

Charles Richman (actor): Charles J. Richman (January 12, 1865 – December 1, 1940) was an American stage and film actor who appeared in 66 films between 1914 and 1939.  Long before entering films Richman, in his youth one of the handsomest men on the stage, achieved a tremendous amount of stardom and success in the legitimate theatre.  Most certainly film acting was an afterthought in his long and distinguished stage career.  In Hollywood, he often played supporting roles as a dignified authoritarian figures like General Tufto in the first Technicolor film "Becky Sharp" (1935) and Judge Thatcher in "The Adventures of Tom Sawyer" (1938).

Alfred Hitchcock's Mystery Magazine: "AHMM" was founded in 1956 by HSD Publications, which licensed the use of the director's name.  Though there was no formal connection with the television show, stories published in the magazine were sometimes adapted by the producers of "Alfred Hitchcock Presents" (and later, "The Alfred Hitchcock Hour)".  A few writers, such as Henry Slesar, wrote for both.  Other contributors during the magazine’s early years included Evan Hunter/Ed McBain, Ed Lacy, Bill Pronzini, Jim Thompson, Donald E. Westlake and Charles Willeford (who briefly worked for the magazine, as did Patricia Hitchcock.  Alfred's daughter).

The Goldwyn Follies: The Goldwyn Follies is a 1938 Technicolor film written by Ben Hecht, Sid Kuller, Sam Perrin and Arthur Phillips, with music by George Gershwin, Vernon Duke, and Ray Golden, and lyrics by Ira Gershwin.  Some sources credit Kurt Weill as one of the composers, but this is apparently incorrect.  "The Goldwyn Follies" was the first Technicolor film produced by Samuel Goldwyn.

The Girl (2012 TV film): The Girl is a 2012 British television film directed by Julian Jarrold, written by Gwyneth Hughes and produced by the BBC and HBO Films.  The film stars Sienna Miller as Tippi Hedren and Toby Jones as Alfred Hitchcock.  It is based on Donald Spoto's 2009 book, "Spellbound by Beauty: Alfred Hitchcock and His Leading Ladies", which discusses British-born film director Hitchcock and the women who played leading roles in his films.  "The Girl"' s title was inspired by Hitchcock's alleged nickname for Hedren.

Alfred Hitchcock's Anthology – Volume 1: Alfred Hitchcock's Anthology – Volume 1 is the first installment of "Alfred Hitchcock's Anthology", one of the many Alfred Hitchcock story collection books; edited by Eleanor Sullivan.  Originally published in hardcover in 1976 as "Alfred Hitchcock's Tales to Keep You Spellbound", the book is a collection of 30 stories originally published in "Alfred Hitchcock's Mystery Magazine".

Jhansi Ki Rani (1953 film): Jhansi Ki Rani is a 1953 Hindi historical drama film produced and directed by Sohrab Modi for his Minerva Movietone production banner.  It is credited as the first Technicolor film made in India and starred Modi's wife, Mehtab in the title role, with Modi in the important role of her mentor Rajguru (royal adviser).  The film was dubbed in English as "The Tiger and the Flame" which released in 1956 with the same star cast.  The cast besides Mehtab and Sohrab Modi included Mubarak, Ulhas, Sapru, Ram Singh, Baby Shikha, Marconi, and Shakila.

Rope (film): Rope is a 1948 American psychological crime thriller film noir directed by Alfred Hitchcock, based on the 1929 play of the same name by Patrick Hamilton, adapted by Hume Cronyn and with a screenplay by Arthur Laurents.

Kangaroo (1952 film): Kangaroo is a 1952 American Technicolor film directed by Lewis Milestone.  It is also known as The Australian Story (American subtitle).  The first Technicolor movie filmed on-location in Australia.  Strong winds on location forced Milestone to re-dub much of the exterior dialogue.

Question: Who wrote the play on which Alfred Hitchcock's first Technicolor film was based ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of Alfred Hitchcock's first Technicolor film."
    },
    "film_director": {
      "type": "string",
      "description": "The director of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "is_hitchcocks_first_technicolor": {
      "type": "boolean",
      "description": "Indicates if this was Alfred Hitchcock's first Technicolor film."
    },
    "source_play": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the play the film was based on."
        },
        "author": {
          "type": "string",
          "description": "The author of the play."
        },
        "publication_year": {
          "type": "integer",
          "description": "The publication year of the play."
        }
      },
      "required": [
        "title",
        "author",
        "publication_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_director",
    "film_release_year",
    "is_hitchcocks_first_technicolor",
    "source_play"
  ],
  "additionalProperties": false
}
