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
Stranger Things (Yuck album): Stranger Things is the third studio album by UK-based indie rock band Yuck, released on Mamé Records on 26 February 2016.  The album was recorded over a period of several months in 2015 in frontman Max Bloom's parents' house in London.  "Stranger Things" was self-produced by the band.  The album's release was preceded by three singles: "Hold Me Closer"; "Hearts in Motion"; and "Cannonball".

Tony Anthony (actor): Tony Anthony (born Roger Pettito; October 16, 1937) is an American actor, producer, screenwriter and director best known for his starring roles in Spaghetti Westerns, most of which were produced with the aid of his friends and associates Allen Klein and Saul Swimmer.  These films consist of "The Stranger" series - "A Stranger in Town" (1967), "The Stranger Returns" (1967), "The Silent Stranger" (1968) and "Get Mean" (1975) - and the "Zatoichi"-inspired "Blindman" (1971).  Anthony also wrote, produced and starred in "Comin' at Ya! " (1981) and "Treasure of the Four Crowns" (1983), the first film being largely credited with beginning the 1980s revival of 3D films in Hollywood.

A Stranger Came Home: A Stranger Came Home, released in the United States under the title The Unholy Four, is a 1954 British film noir.  It was based on the novel "Stranger at Home", which was credited to film actor George Sanders but was actually ghostwritten by Leigh Brackett.  It was directed by Terence Fisher and starred American actress Paulette Goddard.

Stranger than Fiction (2006 film): Stranger than Fiction is a 2006 American fantasy comedy-drama film directed by Marc Forster, produced by Lindsay Doran, and written by Zach Helm.  The film stars Will Ferrell, Maggie Gyllenhaal, Dustin Hoffman, Queen Latifah, and Emma Thompson.  The main plot follows Harold Crick (portrayed by Ferrell), an IRS worker who begins hearing a disembodied voice narrating his life as it happens – seemingly the text of a novel in which it is stated that he will soon die – and he frantically seeks to somehow prevent that ending.  The film was shot on location in Chicago, and has been praised for its innovative, intelligent story and fine performances.  Ferrell, who came to prominence playing brash comedic parts, garnered particular attention for offering a restrained performance in his first starring dramatic role.

The Stranger Who Looks Like Me: The Stranger Who Looks Like Me is a 1974 ABC Movie of the Week that originally aired on March 6, 1974.  It stars Meredith Baxter (credited as Meredith Baxter-Birney) as a girl named Joanne Denver, who was adopted at birth and is searching for her birth parents.  She meets Chris Schroeder (Beau Bridges), who is also adopted and is searching for his birth parents.  The cast includes Whitney Blake, who was Meredith Baxter's real-life mother.  Bill Vint, who starred in the drive-in classic Macon County Line, is also in the cast, as well as future "Dallas" star Patrick Duffy, who has a small part.  The film was produced by Lillian Gallo.

Maggie Gyllenhaal: Margalit Ruth "Maggie" Gyllenhaal ( ; born November 16, 1977 in New York City) is an American actress.  Part of the Gyllenhaal family, she is the daughter of filmmakers Stephen Gyllenhaal and Naomi Achs, and the older sister of actor Jake Gyllenhaal.

The Perfect Stranger (film): The Perfect Stranger is a 2005 Independent Christian film based on the novel "Dinner With a Perfect Stranger" by David Gregory.  It was featured at the 2005 Western Film and Video Festival, and was released on October 28, 2005.  Directed by Jefferson Moore and Shane Sooter, the film starred Pamela Brumley and Jefferson Moore.

Sykes: Sykes is a British sitcom that aired on BBC 1 from 1972 to 1979.  Starring Eric Sykes and Hattie Jacques, it was written by Sykes, who had previously starred with Jacques in "Sykes and a.. . " (1960–1965) and "Sykes and a Big, Big Show" (1971).  Forty-three of the 1970s colour episodes were remakes of scripts for the 1960s black and white series, such as "Bus" based on 'Sykes and a Following' from 1964 and the episode "Stranger" with guest star Peter Sellers based on 'Sykes and a Stranger' from 1961.

Stranger than Fiction (soundtrack): Stranger than Fiction: Music From The Motion Picture is the soundtrack to the 2006 film "Stranger than Fiction" which was directed by Marc Forster and written by Zach Helm.  A fantasy comedy-drama film .

Kristina Paner: Kristina Paner (born August 1, 1971 in Manila, Philippines) is a Filipina actress and singer.  She is also an adoptive sister of Danita Paner, who is also a singer.  At a very young age, her parents noticed her interest in music.  Her adoptive parents were prominent celebrities as well.  Her father Manny Paner was a well known basketball player while her mother Daisy Romualdez was an actress way back in the 1960s.  It was her parents who convinced her to try singing at the age of nine and the song "Sana" was popularized by her.  She tried acting too at age of 10 when she starred in the movie "Sinasamba Kita" as the young Lorna Tolentino who played the character role of Nora.

Question: Who are the parents of the actress that starred in Stranger than Fiction?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who starred in the film."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film the actress starred in."
    },
    "parents": {
      "type": "array",
      "description": "A list of the actress's parents.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the parent."
          },
          "relationship": {
            "type": "string",
            "description": "The relationship to the actress (e.g., 'father', 'mother')."
          },
          "occupation": {
            "type": "string",
            "description": "The occupation of the parent, if mentioned."
          }
        },
        "required": [
          "name",
          "relationship"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "actress_name",
    "film_title",
    "parents"
  ],
  "additionalProperties": false
}
