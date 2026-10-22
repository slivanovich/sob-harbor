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
Amy Sedaris: Amy Louise Sedaris ( ; born March 29, 1961) is an American actress, voice actress, singer, author, screenwriter and comedian.  She is known for playing Jerri Blank in the Comedy Central television series "Strangers with Candy".  She regularly collaborates with her older brother David, a humorist and author.  Since 2014, Sedaris has voiced the character Princess Carolyn in the Netflix animated series "BoJack Horseman".

Vermont Is for Lovers: Vermont is for Lovers is an independently produced docudrama released in 1992, starring George Thrush and Marya Cohn and shot on location Tunbridge, Vermont.  The film concerns a couple visiting Vermont in order to be married, and interviewing local residents on the subject of marriage.  Largely improvised and using non-professional actors, the film was shown at various film festivals including the Melbourne International Film Festival and the Hawaii International Film Festival.  The movie was not terribly well received by the national press, with the New York Times calling it, "vaguely amiable".  While the Washington Post review commented that the film was an "all-too-easy target for ridicule", it also mentioned one of the film's high points: "In one scene, a typically droll Vermont resident (playing himself) sums up his state's fabled coolness to strangers by suggesting that a sign be placed at the state line, reading "Welcome to Vermont.  Now Leave.""

When Lovers Become Strangers: "When Lovers Become Strangers" is the third US single release from American singer/actress Cher's 20th album "Love Hurts", released in US and Canada only in late May 1992.

Han Sun-hwa: Han Sun-hwa (born October 6, 1990), is a South Korean singer and actress.  She is a former member of the South Korean girl group Secret.  She made her television debut in 2004 while participating in SBS's "Superstar Survival" as a finalist, and in 2009, she was a regular cast on a variety show called "Invincible Youth".  Aside from music, she also ventured into acting and made her debut in the 2010 drama, "More Charming By The Day".  She also acted in several dramas with supporting roles in "Ad Genius Lee Tae-baek", "God's Gift - 14 Days", and "Marriage, Not Dating".  In 2014 she finally starred as a lead actress on MBC's weekend drama "Rosy Lovers" as Baek Jang Mi co-starring with actor Lee Jang Woo.  CNN International Seoul listed Sunhwa as one of the nine rising "It" stars in Korean entertainment citing her as a "multi-tasking" artist.  Her portrayal of Kang Se-Ah in the 2014 TVN drama, "Marriage, Not Dating" earned her a nomination for "Best Youth Actress" at the 16th Seoul International Youth Film Festival.  In 2014, her portrayal of Jang-Mi from "Rosy Lovers" and Jenny from "God's Gift 14 Day"s won her two best new actress awards from MBC and SBS Drama Awards.  It was confirmed on September 26, 2016 that Sunhwa had not renewed her contract with TS Entertainment and will officially part ways in October.  On October 14, 2016 Sunhwa joined Huayi Brothers as an actress.

Shin Bo-ra: Shin Bora (; born March 17, 1987) is a South Korean comedian, singer, and actress.  She made her entertainment debut as a comedian on the variety show "Gag Concert" in 2010.  Shin is also a member of the band , and has released several singles as a solo artist.  In 2014, she was cast in a supporting role in the television drama "Trot Lovers".

For All We Know (1970 song): "For All We Know" is a soft rock song written for the 1970 film "Lovers and Other Strangers", with music by Fred Karlin and lyrics by Robb Wilson (Robb Royer) and Arthur James (Jimmy Griffin).  Both Royer and Griffin were founding members of the soft-rock group Bread.  It was originally performed by Larry Meredith.  It is best known for a cover version by American pop duo Carpenters in 1971, which reached No. 3 on the "US Billboard Hot 100" singles chart and No. 1 on the "US Billboard Easy Listening" chart.  The song was also a hit for Shirley Bassey at the same time in the United Kingdom.  It has since been covered by a large number of artists.

Lovers &amp; Strangers: Lovers & Strangers, also translated as Only Love Strangers () is a 1999 album by Beijing-based C-pop singer Faye Wong.  It contains 10 tracks in Mandarin with bonus Cantonese versions of two of the songs.  The title is from a line of the refrain in track 4 (... 我只爱陌生人, "I only love strangers...").

David Zelag Goodman: David Zelag Goodman (January 15, 1930 – September 26, 2011) was a playwright and screenwriter for both TV and film.  His most prolific period was from the 1960s to the early 1980s.  He was nominated for an Academy Award for "Lovers and Other Strangers", though he did not win.  He co-wrote, with Sam Peckinpah, the screenplay for 1971's controversial "Straw Dogs".  He died less than two weeks after the remake was released.  Other films that he wrote or co-wrote included "Logan's Run", "Monte Walsh", and "Farewell, My Lovely".  He also wrote a number of the episodes of "The Untouchables" in the early 1960s.

Anne Meara: Anne Meara (September 20, 1929 – May 23, 2015) was an American actress and comedian.  Along with her husband, Jerry Stiller, she was one-half of a prominent 1960s comedy team, Stiller and Meara.  She was also featured on stage, television, in numerous films, and later became a playwright.

Lovers and Other Strangers: Lovers and Other Strangers is a 1970 comedy film based on the play by Renée Taylor and Joseph Bologna.  The cast includes Richard S. Castellano, Gig Young, Cloris Leachman, Anne Jackson, Beatrice Arthur, Bonnie Bedelia, Michael Brandon, Harry Guardino, Anne Meara, Bob Dishy, Marian Hailey, Joseph Hindy, and, in her film debut, Diane Keaton.  Sylvester Stallone was an extra in this movie.  The film was nominated for three Academy Awards (it won the Academy Award for Best Original Song), and was one of the top box office performers of 1970.  It established Richard S. Castellano as a star (receiving an Oscar nomination for his performance) and he, along with Diane Keaton, was subsequently cast in "The Godfather".  The song "For All We Know" was composed by Fred Karlin with lyrics by Robb Royer and Jimmy Griffin.

Question: Which actress that was also a comedian was in lovers and Other Strangers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who was also a comedian."
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of professional roles held by the person."
    },
    "film_appearances": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of films the person appeared in relevant to the question."
    },
    "comedy_team": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the comedy team the actress was part of."
        },
        "partner": {
          "type": "string",
          "description": "The name of the actress's comedy partner."
        }
      },
      "required": [
        "name",
        "partner"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "roles",
    "film_appearances"
  ],
  "additionalProperties": false
}
