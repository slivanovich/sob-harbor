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
Diff'rent Strokes: Diff'rent Strokes is an American sitcom that aired on NBC from November 3, 1978, to May 4, 1985, and on ABC from September 27, 1985, to March 7, 1986.  The series stars Gary Coleman and Todd Bridges as Arnold and Willis Jackson, two African American boys from Harlem who are taken in by a rich white Park Avenue businessman and widower named Phillip Drummond (Conrad Bain) and his daughter Kimberly (Dana Plato), for whom their deceased mother previously worked.  During the first season and first half of the second season, Charlotte Rae also starred as the Drummonds' housekeeper, Mrs. Garrett (who ultimately spun off into her own successful sitcom, "The Facts of Life").

The Facts of Life Reunion: The Facts of Life Reunion is a 2001 American made-for-television comedy film based on the 1979–1988 NBC sitcom "The Facts of Life" which reunited original cast members Charlotte Rae, Lisa Whelchel, Mindy Cohn and Kim Fields, with the exception of Nancy McKeon, who was unable to participate due to scheduling conflicts with her television series "The Division".

Molly Ringwald: Molly Kathleen Ringwald (born February 18, 1968) is an American actress, singer, dancer, and author.  She was cast in her first major role as Molly in "The Facts of Life" (1979–80) after a casting director saw her playing an orphan in a stage production of the musical "Annie".  She and several other members of the original Facts of Life cast were let go when the show was reworked by the network.  She made her motion picture debut in the independent film "Tempest" (1982), which earned her a Golden Globe nomination.

Facts of Life (band): Facts of Life was an American soul/disco group formed by producer Millie Jackson, whose members were Jean Davis (sister of Tyrone Davis), Keith Williams, and Chuck Carter.  They signed to independent label Kayvette Records, and a single, "Caught in the Middle", got airplay on Southern US radio stations but did not chart.  Their second single was "Sometimes", a remake of country singer Bill Anderson's smash hit; Facts of Life's version hit #3 on the US Black Singles chart and #31 on the pop charts in 1977.  As a result of the single's success, Kayvette rushed the album release, resulting in a bad pressing (the outer cover contained a number of spelling errors).  Nevertheless, RCA picked up the group in 1978, but their second album was not very successful, and the group fizzled.

The Facts of Life Goes to Paris: The Facts of Life Goes to Paris is a 1982 American made-for-television comedy film based on the sitcom "The Facts of Life" starring Charlotte Rae, Lisa Whelchel, Kim Fields, Mindy Cohn and Nancy McKeon.  The film originally aired September 25, 1982 on NBC, four days before the 1982–1983 premiere of "The Facts of Life".  When the series went into syndication, the film was split into four half-hour episodes and added to "The Facts of Life" syndication package.

Massacre of 3 March 1976 in Vitoria: The massacre of 3 March 1976 in Vitoria is the massacre that took place on March 3, 1976, in the Basque capital during the so-called Spanish Transition: in a day of strike, the Spanish armed police used tear gas to force the workers out of the parish where they were gathering in assembly.  As the workers left the Church of San Francisco de Asís, in the working-class neighbourhood of Zaramaga, they were shot by the police.  This resulted in 5 dead workers and 150 injured with gunshot wounds.  The same police described the facts as a massacre.  These facts inspired Lluís Llach celebrated song "Campanades a morts".

The Facts (Seattle): The Facts Newspaper /Seattle Facts is an African-American weekly newspaper that serves Seattle, Washington.  Headquartered in the Central District, it was founded in 1961 by Fitzgerald Redd Beaver.  His children, Marla, LaVonne Beaver are currently the publishers and editors "The Facts" is a member of the West Coast Black Publishers Association and bills itself as "The Voice of the Northwest African American Community."

The Facts of Life Down Under: The Facts of Life Down Under is a 1987 American made-for-television comedy film based on the sitcom "The Facts of Life" starring Cloris Leachman, Lisa Whelchel, Kim Fields, Mindy Cohn, Nancy McKeon and Mackenzie Astin.  The film originally aired February 15, 1987 on NBC between the 17th and 18th episode of the 1986–1987 of "The Facts of Life".  When the series went into syndication, the film was split into four half-hour episodes and added to "The Facts of Life" syndication package.

Seamen's strike of 1922: The Seamen's Strike of 1922 began on 12 January 1922, when Chinese seamen from Hong Kong and Canton (now Guangzhou) went on strike for higher wages.  Led by the Seamen’s Union after shipping companies refused to increase salaries by 40%, the strike quickly garnered over 30,000 participants, greatly disrupting everyday colonial life and food shipments to Hong Kong.  Though the strike was declared illegal by the Hong Kong government, negotiations eventually took place after 52 days, with employers capitulating on 5 March 1922 and agreeing to wage increases of 15-30%.

Strike It Rich (1990 film): Strike It Rich is a 1990 romantic comedy motion picture starring Robert Lindsay and Molly Ringwald.  Others in the cast include John Gielgud.

Question: Strike It Rich starred what member of "The Facts of Life"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in 'Strike It Rich' and was a member of 'The Facts of Life'."
    },
    "role_in_strike_it_rich": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film."
        },
        "role_type": {
          "type": "string",
          "description": "The type of role in the film (e.g., 'starring_role')."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "film_title",
        "role_type",
        "release_year"
      ],
      "additionalProperties": false
    },
    "role_in_the_facts_of_life": {
      "type": "object",
      "properties": {
        "series_title": {
          "type": "string",
          "description": "The title of the TV series."
        },
        "role_type": {
          "type": "string",
          "description": "The type of role in the series (e.g., 'cast_member')."
        },
        "character_name": {
          "type": "string",
          "description": "The name of the character played in the series."
        },
        "years_active": {
          "type": "string",
          "description": "The period the actor was active in the series."
        }
      },
      "required": [
        "series_title",
        "role_type",
        "character_name",
        "years_active"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "role_in_strike_it_rich",
    "role_in_the_facts_of_life"
  ],
  "additionalProperties": false
}
