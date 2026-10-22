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
Philanthropy (magazine): Philanthropy is a quarterly magazine published by the Philanthropy Roundtable.  First published as a newsletter in 1987, "Philanthropy" became a glossy magazine in 1996.  The magazine's primary focus is philanthropy, with a special interest in donor intent and philanthropic freedom.  The magazine is headquartered in Washington, D.C.

Art &amp; Project: Art & Project (1968-2001) was a leading contemporary art gallery in Amsterdam and Slootdorp, the Netherlands, as well as an influential art magazine published by the gallery between 1968 and 1989.

GOSH!: GOSH!  magazine was a Los Angeles-based arts, entertainment, and fashion magazine published in eleven issues between October, 1978 and August, 1979.  In its short history it became notable enough to be recognized by the Smithsonian Institution and included in their archives.  In addition, GOSH!  articles written by Dennis Cooper have been archived as part of the Dennis Cooper Papers in the Fales Library and Special Collections of New York University.  It was distributed free of charge in art galleries, alternative bookstores and music shops in the Los Angeles area.  Articles ranged from interviews with experimental filmmakers like George Kuchar, Sara Kathryn Arledge, and Ted V. Mikels; influential radio announcers like Rodney Bingenheimer; to reviews of art exhibits, like Susan Greiger's (now Susan Singer) controversial show at Aarnun gallery featuring life-sized nude photos arranged in a flip book and an exhibit about how celebrities and common folk relate to their own noses.

Realms of Fantasy: Realms of Fantasy was a professional bimonthly fantasy speculative fiction magazine published by Damnation Books, which specialized in fantasy, nonfiction, and art.  The magazine published short stories by some of the genre's most popular and most prominent authors.  Its original publisher was Sovereign Media, and it first launched with the October 1994 issue.  It was headquartered in Herndon, Virginia.

Rock &amp; Ice: Rock & Ice is a magazine published by Big Stone Publishing focusing on rock and ice climbing.  The magazine got its start in early 1984 and the first issue was in late 1985.  The first publisher was Neal Kaptain, and it was bought out within the first year by George Bracksieck, who remained editor until 1997.  His company, North-South Publications, sold it to Primedia, a company led by Dougald MacDonald and others.  The magazine is published eight times a year.  It was headquartered in Boulder, Colorado until 2002 when it moved to Carbondale, Colorado.

Gutsoon! Entertainment: Gutsoon!  Entertainment, Inc. is a now defunct publisher of English translated manga.  The company, headquartered in Encino, Los Angeles, served as the US subsidiary of Coamix, which was founded by Nobuhiko Horie and manga artist Tsukasa Hojo.  The company published the English manga anthology "Raijin Comics", a U.S. equivalent to the Japanese "Weekly Comic Bunch" and published many of the same titles ("Fist of the Blue Sky" and "City Hunter"), as well titles from other magazines such as the Japanese "Weekly Shōnen Jump".  "Raijin Comics" began as a weekly magazine with its first issue (dated December 18, 2002), but switched to being a monthly publication beginning with its 36th issue (dated September 2003).  Gutsoon!  also published a companion magazine to "Raijin Comics", titled "Raijin Game & Anime" (originally called "Fujin Magazine"), which lasted only 20 issues before being merged into the pages of "Raijin Comics".  The collected volumes of "Raijin Comics" titles were published under the "Raijin Graphic Novels" imprint.  Raijin Comics also has a mascot called "Raijin Maru".  Before the company's fall they were also planning to make a shōjo manga magazine called "Smile Magazine".

Sickla Köpkvarter: Sickla Köpkvarter is a retail park and shopping district located on a redeveloped industrial estate in Nacka, Sweden.  It's wholly owned by Atrium Ljungberg — a real estate company headquartered in the area — and consists of several shopping malls in varying sizes, in addition to office buildings with shops at street level and a civic center housing a museum, art gallery, library and multiplex.  In 2013, the shopping center had 2,600 parking spaces, a total of 168 stores with a combined retail floor area of 78,700 m2 and annual turnover of SEK 3 billion.  The biggest stores are ICA, Elgiganten, Willys and Best of Brands, accounting for nearly a quarter of the annual rent payments.  It's one of the biggest shopping centers in Stockholm in terms of sales.

Magna Publishing Group: Magna Publishing Group, or Magna Publishing Group, Inc., is a publishing company headquartered in Paramus, New Jersey.  Founded in 1975, the company publishes a number of magazine titles and is one of the largest publishers of pornographic magazines in the United States with titles such as Club, Swank, Genesis, Gallery, Gent, as well as "nearly 60 total adult titles".  The Company has only 1 to 10 employees.  On December 22, 2015 Magna Publishing Group was purchased by 1-800-PHONESEX for an undisclosed amount.

291 (magazine): 291 was an arts and literary magazine that was published from 1915 to 1916 in New York City.  It was created and published by a group of four individuals: photographer/modern art promoter Alfred Stieglitz, artist Marius de Zayas, art collector/journalist/poet Agnes E. Meyer and photographer/critic/arts patron Paul Haviland.  Initially intended as a way to bring attention to Stieglitz's gallery of the same name (291), it soon became a work of art in itself.  The magazine published original art work, essays, poems and commentaries by Francis Picabia, John Marin, Max Jacob, Georges Ribemont-Dessaignes, de Zayas, Stieglitz and other avant-garde artists and writers of the time, and it is credited with being the publication that introduced visual poetry to the United States.

Gallery (magazine): Gallery is a men's magazine published by Magna Publishing Group.  It is one of the more popular "skin" magazines that arose on the "Playboy" magazine pattern in the 1970s.

Question: Gallery is a magazine published by a company headquartered in which city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine."
    },
    "publisher": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the publishing company."
        },
        "headquarters_city": {
          "type": "string",
          "description": "The city where the publishing company is headquartered."
        },
        "headquarters_state": {
          "type": "string",
          "description": "The state where the publishing company is headquartered."
        }
      },
      "required": [
        "name",
        "headquarters_city",
        "headquarters_state"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The city where the magazine's publisher is headquartered."
    }
  },
  "required": [
    "magazine_name",
    "publisher",
    "answer"
  ],
  "additionalProperties": false
}
